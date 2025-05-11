

#region Veri Seti Hikayesi
# Veri seti Flo’dan son alışverişlerini 2020 - 2021 yıllarında OmniChannel (hem online hem offline alışveriş yapan)
# olarak yapan müşterilerin geçmiş alışveriş davranışlarından elde edilen bilgilerden oluşmaktadır.

# master_id: Eşsiz müşteri numarası
# order_channel: Alışveriş yapılan platforma ait hangi kanalın kullanıldığı (Android, ios, Desktop, Mobile)
# last_order_channel: En son alışverişin yapıldığı kanal
# first_order_date: Müşterinin yaptığı ilk alışveriş tarihi
# last_order_date: Müşterinin yaptığı son alışveriş tarihi
# last_order_date_online: Müşterinin online platformda yaptığı son alışveriş tarihi
# last_order_date_offline: Müşterinin offline platformda yaptığı son alışveriş tarihi
# order_num_total_ever_online: Müşterinin online platformda yaptığı toplam alışveriş sayısı
# order_num_total_ever_offline: Müşterinin offline'da yaptığı toplam alışveriş sayısı
# customer_value_total_ever_offline: Müşterinin offline alışverişlerinde ödediği toplam ücret
# customer_value_total_ever_online: Müşterinin online alışverişlerinde ödediği toplam ücret
# interested_in_categories_12: Müşterinin son 12 ayda alışveriş yaptığı kategorilerin listesi

# 12 Değişken 19.945 Gözlem
#endregion

######################################################################################################

# Görev 1: Veriyi Anlama ve Hazırlama
######################################################################################################

#region imports
import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt
from lifetimes import BetaGeoFitter
from lifetimes import GammaGammaFitter
from lifetimes.plotting import plot_period_transactions

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
pd.set_option('display.float_format', lambda x: '%.4f' % x)
from sklearn.preprocessing import MinMaxScaler

#endregion

# Adım1: flo_data_20K.csv verisini okuyunuz.Dataframe’in kopyasını oluşturunuz.
df_ = pd.read_csv("D:\mert python\CSV Files/flo_data_20k.csv")
df = df_.copy()

# Adım2: Veri setinde
# a. İlk 10 gözlem,
# b. Değişken isimleri,
# c. Betimsel istatistik,
# d. Boş değer,
# e. Değişken tipleri, incelemesi yapınız.

df.head(10)
df.columns
df.describe().T
df.isnull().sum()
df.dtypes

# Adım3: Omnichannel müşterilerin hem online'dan hemde offline platformlardan alışveriş yaptığını ifade etmektedir. Her bir müşterinin toplam
# alışveriş sayısı ve harcaması için yeni değişkenler oluşturunuz.

df["TotalOrder"] = df["order_num_total_ever_online"] + df["order_num_total_ever_offline"]
df["TotalValue"] = df["customer_value_total_ever_offline"] + df["customer_value_total_ever_offline"]

# Adım4: Değişken tiplerini inceleyiniz. Tarih ifade eden değişkenlerin tipini date'e çeviriniz.
object_to_dates = ["first_order_date", "last_order_date", "last_order_date_online", "last_order_date_offline"]

for col in object_to_dates:
df[col] = pd.to_datetime(df[col])


# Adım5: Alışveriş kanallarındaki müşteri sayısının, toplam alınan ürün sayısının ve toplam harcamaların dağılımına bakınız.

df.groupby("order_channel").agg({"TotalOrder": ("count", "sum"),
                                 "TotalValue": "sum"})

df.groupby("order_channel").agg({"TotalOrder": "sum",
                                 "TotalValue": "sum",
                                 "master_id": "nunique"})




# Adım6: En fazla kazancı getiren ilk 10 müşteriyi sıralayınız.

df["TotalValue"].sort_values(ascending=False).head(10)

# Adım7: En fazla siparişi veren ilk 10 müşteriyi sıralayınız

df["TotalOrder"].sort_values(ascending=False).head(10)

def first_look(dataframe, head=5):
    print("########## shape ##########")
    print(dataframe.shape)
    print("########## type ##########")
    print(dataframe.dtypes)
    print("########## head ##########")
    print(dataframe.head(head))
    print("########## NA ##########")
    print(dataframe.isnull().sum())
    print("########## quantiles ##########")
    print(dataframe.describe().T)

    dataframe["TotalOrder"] = dataframe["order_num_total_ever_online"] + dataframe["order_num_total_ever_offline"]
    dataframe["TotalValue"] = dataframe["customer_value_total_ever_offline"] + dataframe["customer_value_total_ever_offline"]

    object_to_dates = ["first_order_date", "last_order_date", "last_order_date_online", "last_order_date_offline"]

    for col in object_to_dates:
        dataframe[col] = pd.to_datetime(dataframe[col])
    print("########## dağılımlar ##########")
    print(df.groupby("order_channel").agg({"TotalOrder": "sum",
                                     "TotalValue": "sum",
                                     "master_id": "nunique"}))
    print("########## TOP10 Value  ##########")
    print(df["TotalValue"].sort_values(ascending=False).head(head))
    print("########## TOP10 Order  ##########")
    print(df["TotalOrder"].sort_values(ascending=False).head(head))

first_look(df, 10)
df.head()
# Görev 2: RFM Metriklerinin Hesaplanması
# Adım 1: Recency, Frequency ve Monetary tanımlarını yapınız.
today_date = dt.datetime(2021, 6, 1)

# recency en son aldığı zaman aralığı

df["last_order_date"].max()

df["Recency"] = today_date - df["last_order_date"]

# frekans fatura kesilme yani alışvveriş yapılma sayısı/aralığı

rfm = df.groupby('master_id').agg({'last_order_date': lambda InvoiceDate: (today_date - InvoiceDate.max()).days,
                                     'TotalOrder': lambda Invoice: Invoice.sum(),
                                     'TotalValue': lambda TotalPrice: TotalPrice.sum()})
rfm.head()

rfm.columns = ['recency', 'frequency', 'monetary']

rfm.head()


rfm["recency_score"] = pd.qcut(rfm['recency'], 5, labels=[5, 4, 3, 2, 1])

rfm["frequency_score"] = pd.qcut(rfm['frequency'].rank(method="first"), 5, labels=[1, 2, 3, 4, 5])

rfm["monetary_score"] = pd.qcut(rfm['monetary'], 5, labels=[1, 2, 3, 4, 5])


rfm["RF_SCORE"] = (rfm['recency_score'].astype(str) + rfm['frequency_score'].astype(str))


seg_map = {
    r'[1-2][1-2]': 'hibernating',
    r'[1-2][3-4]': 'at_Risk',
    r'[1-2]5': 'cant_loose',
    r'3[1-2]': 'about_to_sleep',
    r'33': 'need_attention',
    r'[3-4][4-5]': 'loyal_customers',
    r'41': 'promising',
    r'51': 'new_customers',
    r'[4-5][2-3]': 'potential_loyalists',
    r'5[4-5]': 'champions'
}

rfm['segment'] = rfm['RF_SCORE'].replace(seg_map, regex=True)


# Adım1: Segmentlerin recency, frequnecy ve monetary ortalamalarını inceleyiniz.

rfm[["segment", "recency", "frequency", "monetary"]].groupby("segment").agg(["mean", "count"])

# Adım2: RFM analizi yardımıyla aşağıda verilen 2 case için ilgili profildeki müşterileri bulun ve müşteri id'lerini csv olarak kaydediniz.

# a. FLO bünyesine yeni bir kadın ayakkabı markası dahil ediyor. Dahil ettiği markanın ürün fiyatları genel müşteri
# tercihlerinin üstünde. Bu nedenle markanın tanıtımı ve ürün satışları için ilgilenecek profildeki müşterilerle özel olarak
# iletişime geçmek isteniliyor. Sadık müşterilerinden(champions, loyal_customers) ve kadın kategorisinden alışveriş (interested_in_categories_12)
# yapan kişiler özel olarak iletişim kurulacak müşteriler. Bu müşterilerin id numaralarını csv dosyasına kaydediniz.

champs_and_loyals = rfm[(rfm["segment"] == "champions") | (rfm["segment"] == "loyal_customers")]
champs_and_loyals.reset_index(inplace=True)

df.head()
id_and_categories = df[["master_id", "interested_in_categories_12"]]

id_and_categories_of_cl = id_and_categories.merge(right=champs_and_loyals, on="master_id",how="inner")

id_and_categories = id_and_categories_of_cl[["master_id", "interested_in_categories_12"]]

KADIN_master_id = id_and_categories[id_and_categories["interested_in_categories_12"].str.contains("KADIN")]["master_id"]

pd.set_option("display.max_rows",10 )


KADIN_master_id.to_csv("KADIN_master_id.csv")


# b. Erkek ve Çocuk ürünlerinde %40'a yakın indirim planlanmaktadır. Bu indirimle ilgili kategorilerle ilgilenen geçmişte
# iyi müşteri olan ama uzun süredir alışveriş yapmayan kaybedilmemesi gereken müşteriler, uykuda olanlar ve yeni
# gelen müşteriler özel olarak hedef alınmak isteniyor. Uygun profildeki müşterilerin id'lerini csv dosyasına kaydediniz.

id_and_categories = df[["master_id", "interested_in_categories_12"]]

# id_and_categories_of_cl = id_and_categories.merge(right=champs_and_loyals, on="master_id",how="inner")
#
# id_and_categories = id_and_categories_of_cl[["master_id", "interested_in_categories_12"]]


h_c_nc_df = rfm[rfm["segment"].str.contains("hibernating|cant_loose|new_customers")]

h_c_nc_merged = id_and_categories.merge(right=h_c_nc_df, on="master_id",how="inner")

h_c_nc_id = h_c_nc_merged[["master_id", "interested_in_categories_12"]]

# isim2 = pd.DataFrame()
# for i in ["ERKEK", "COCUK"]:
#     isim2 = pd.concat([isim2, isim[isim["interested_in_categories_12"].str.contains(i)]],ignore_index=True)
#
#
#
# isim2["master_id"].to_csv("ERKEK_COCUK_master_id.csv")

h_c_nc_id.to_csv("ERKEK_COCUK_master_id.csv")


#Hangi segmentten kaç adet bulunmakta ve %kaçını oluşturmakta.
#region import matplotlib 'Qt5Agg'
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Qt5Agg')
#endregion

segments_counts = rfm['segment'].value_counts().sort_values(ascending=True)

fig, ax = plt.subplots()

bars = ax.barh(range(len(segments_counts)),
              segments_counts,
              color='silver')
ax.set_frame_on(False)
ax.tick_params(left=False,
               bottom=False,
               labelbottom=False)
ax.set_yticks(range(len(segments_counts)))
ax.set_yticklabels(segments_counts.index)

for i, bar in enumerate(bars):
        value = bar.get_width()
        if segments_counts.index[i] in ['Can\'t loose']:
            bar.set_color('firebrick')
        ax.text(value,
                bar.get_y() + bar.get_height()/2,
                '{:,} ({:}%)'.format(int(value),
                                   int(value*100/segments_counts.sum())),
                va='center',
                ha='left'
               )

plt.show()




















ERKEKCOCUK = reyhan[reyhan["interested_in_categories_12"].str.contains("ERKEK|COCUK")]["master_id"]

ERKEKCOCUK.to_csv("KADIN_master_id.csv")













































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

#region Adım1: flo_data_20K.csv verisini okuyunuz.Dataframe’in kopyasını oluşturunuz.
df_ = pd.read_csv("D:\mert python\CSV Files/flo_data_20k.csv")
df = df_.copy()

#endregion


#region Adım 2: Aykırı değerleri baskılamak için gerekli olan outlier_thresholds ve replace_with_thresholds fonksiyonlarını tanımlayınız.
# Not: cltv hesaplanırken frequency değerleri integer olması gerekmektedir.Bu nedenle alt ve üst limitlerini round() ile yuvarlayınız.

def outlier_thresholds(dataframe, variable):
    quartile1 = dataframe[variable].quantile(0.01)
    quartile3 = dataframe[variable].quantile(0.99)
    interquantile_range = quartile3 - quartile1
    up_limit = round((quartile3 + 1.5 * interquantile_range))
    low_limit = round((quartile1 - 1.5 * interquantile_range))
    return low_limit, up_limit

def replace_with_thresholds(dataframe, variable):
    low_limit, up_limit = outlier_thresholds(dataframe, variable)
    dataframe.loc[(dataframe[variable] < low_limit), variable] = low_limit
    dataframe.loc[(dataframe[variable] > up_limit), variable] = up_limit

#endregion

#region Adım 3: "order_num_total_ever_online", "order_num_total_ever_offline", "customer_value_total_ever_offline",
# "customer_value_total_ever_online" değişkenlerinin aykırı değerleri varsa baskılayanız.
outlier_check_list = ["order_num_total_ever_online", "order_num_total_ever_offline", "customer_value_total_ever_offline", "customer_value_total_ever_online"]

outlier_thresholds(df, outlier_check_list)

for i in outlier_check_list:
    replace_with_thresholds(df, i)

#endregion

#region Adım 4: Omnichannel müşterilerin hem online'dan hem de offline platformlardan alışveriş yaptığını ifade etmektedir. Her bir müşterinin toplam
# alışveriş sayısı ve harcaması için yeni değişkenler oluşturunuz.

df["TotalOrder"] = df["order_num_total_ever_online"] + df["order_num_total_ever_offline"]
df["TotalValue"] = df["customer_value_total_ever_offline"] + df["customer_value_total_ever_offline"]

#endregion

#region Adım5: Değişken tiplerini inceleyiniz. Tarih ifade eden değişkenlerin tipini date'e çeviriniz.
object_to_dates = ["first_order_date", "last_order_date", "last_order_date_online", "last_order_date_offline"]

for col in object_to_dates:
    df[col] = pd.to_datetime(df[col])
df.dtypes

#endregion

# Görev 2: CLTV Veri Yapısının Oluşturulması

#region Adım 1: Veri setindeki en son alışverişin yapıldığı tarihten 2 gün sonrasını analiz tarihi olarak alınız.
today_date = dt.datetime(2021, 6, 1)

#endregion

#region Adım 2: customer_id, recency_cltv_weekly, T_weekly, frequency ve monetary_cltv_avg değerlerinin yer aldığı yeni bir cltv dataframe'i oluşturunuz.
# Monetary değeri satın alma başına ortalama değer olarak, recency ve tenure değerleri ise haftalık cinsten ifade edilecek.
cltv_df = pd.DataFrame()
df.head()
cltv_df["customer_id"] = df["master_id"]

cltv_df["recency_cltv_weekly"] = df["last_order_date"] - df["first_order_date"]
cltv_df["recency_cltv_weekly"] = cltv_df["recency_cltv_weekly"].astype("timedelta64[D]") / 7

cltv_df["T_weekly"] = today_date - df["first_order_date"]
cltv_df["T_weekly"] = cltv_df["T_weekly"].astype("timedelta64[D]")
cltv_df["T_weekly"] = cltv_df["T_weekly"] / 7

cltv_df["frequency"] = df["TotalOrder"]

cltv_df = cltv_df[(cltv_df["frequency"] > 1)]

cltv_df["monetary"] = df["TotalValue"]

cltv_df["monetary_cltv_avg"] = cltv_df["monetary"] / cltv_df["frequency"]

cltv_df.dtypes

cltv_df.head()
cltv_df.describe().T

#endregion

# region Görev 3: BG/NBD, Gamma-Gamma Modellerinin Kurulması ve CLTV’nin Hesaplanması
# region Adım1
bgf = BetaGeoFitter(penalizer_coef=0.001)

bgf.fit(cltv_df['frequency'],
        cltv_df['recency_cltv_weekly'],
        cltv_df['T_weekly'])

bgf.summary

# • 3 ay içerisinde müşterilerden beklenen satın almaları tahmin ediniz ve exp_sales_3_month olarak cltv
# dataframe'ine ekleyiniz.

cltv_df["exp_sales_3_month"] = bgf.conditional_expected_number_of_purchases_up_to_time(4 * 3,
                                                                                    cltv_df['frequency'],
                                                                                    cltv_df['recency_cltv_weekly'],
                                                                                    cltv_df['T_weekly'])

#• 6 ay içerisinde müşterilerden beklenen satın almaları tahmin ediniz ve exp_sales_6_month olarak cltv
# dataframe'ine ekleyiniz.

cltv_df["exp_sales_6_month"] = bgf.conditional_expected_number_of_purchases_up_to_time(4 * 6,
                                                                                    cltv_df['frequency'],
                                                                                    cltv_df['recency_cltv_weekly'],
                                                                                    cltv_df['T_weekly'])

cltv_df.head()

#endregion

#region Adım 2: Gamma-Gamma modelini fit ediniz. Müşterilerin ortalama bırakacakları değeri tahminleyip exp_average_value olarak cltv
# dataframe'ine ekleyiniz.
ggf = GammaGammaFitter(penalizer_coef=0.01)

ggf.fit(cltv_df['frequency'], cltv_df['monetary_cltv_avg'])

cltv_df['exp_average_value'] = ggf.conditional_expected_average_profit(cltv_df['frequency'],
                                                                       cltv_df['monetary_cltv_avg'])
cltv_df.head()

#endregion

#region Adım 3: 6 aylık CLTV hesaplayınız ve cltv ismiyle dataframe'e ekleyiniz.

cltv = ggf.customer_lifetime_value(bgf,
                                   cltv_df['frequency'],
                                   cltv_df['recency_cltv_weekly'],
                                   cltv_df['T_weekly'],
                                   cltv_df['monetary_cltv_avg'],
                                   time=6,
                                   freq="W",
                                   discount_rate=0.01)

cltv.index = cltv_df["customer_id"]

cltv_final = cltv_df.merge(cltv, on="customer_id", how="left")
cltv_final.sort_values(by="clv", ascending=False).head(20)

#endregion



#endregion

# region Görev 4: CLTV Değerine Göre Segmentlerin Oluşturulması
#region Adım 1: 6 aylık CLTV'ye göre tüm müşterilerinizi 4 gruba (segmente) ayırınız ve grup isimlerini veri setine ekleyiniz.

cltv_final["segment"] = pd.qcut(cltv_final["clv"], 4, labels=["D", "C", "B", "A"])
cltv_final["segment"].value_counts()
cltv_final.sort_values(by="clv", ascending=False).head(10)

cltv_final.groupby("segment").agg({"count", "mean", "sum"})
cltv_final.head()

# endregion


# Adım 2: 4 grup içerisinden seçeceğiniz 2 grup için yönetime kısa kısa 6 aylık aksiyon önerilerinde bulununuz.
cltv_final
cltv_final.head(50)

# iki tane birbirine yakın clv değerinde B ve C segmentlerindeki müşterilerin değerlerine baktığımızda (0. ve 2. index)
# birbirleriyle eşit frekanstalar fakat c segmentinin T_weekly ve monetary değeri daha yüksek olduğu ama recency_cltv_weekly değeri yüksek gözüküyor
# demekki bizim c ve b olarak ayrılan segmentlerimizde iki segmenti bir tutarak recency konusunda bir iyileştirme yapmamız gerekmekte

# D segmentimizin recency değeri çok fazla olanlarla (1. index) A segmentinden bile düşük olan (19943. index ) müşterimiz var gözüküyor.
# örneğin bu iki müşterimize çoklu alımlarda indirim tarzında bir kampanyayı ulaştırabilirsek A müşterisi değerini fark eder ve ya canı alışveriş yapmak isteyebilir.
# D müşterimiz de firmamızı unutmuşsa bile hatırlayıp daha aktif bir müşteriye dönüşebilir.

# 3. indexteki müşterimiz indirim kovalayan bir müşteri olabilir ve ya yeni müşteri olup az alışveriş yaptıysa elde tutmak için
# bu müşterimize çok fazla kampanya iletirsek kendi hesabından ailesine akrabalarına ve ya çevresindekilere önerdiğinde
# hem yeni müşteri kazanma olasılığımız olur hem de monetary değeri artar ve hatta belkide başka segmentlerdeki recency skoru yüksek olan müşterileri uykusundan uyandırabilir

# genel olarak iki grubu seçtiğimizde üzerinde durulması gereken c ve b yi birleştirip A ve BC segmentlerine odaklanmamız diye düşünüyorum
# zaten bu 3 segmente kampanyaları yaptığımız zaman D segmentindeki müşteriler de çoğunluğun ne yaptığına bakıp geri dönebilir

# endregion
















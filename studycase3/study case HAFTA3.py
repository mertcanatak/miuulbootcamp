
#############################################
# Kural Tabanlı Sınıflandırma ile Potansiyel Müşteri Getirisi Hesaplama
#############################################

#############################################
# İş Problemi
#############################################
# Bir oyun şirketi müşterilerinin bazı özelliklerini kullanarak seviye tabanlı (level based) yeni müşteri tanımları (persona)
# oluşturmak ve bu yeni müşteri tanımlarına göre segmentler oluşturup bu segmentlere göre yeni gelebilecek müşterilerin şirkete
# ortalama ne kadar kazandırabileceğini tahmin etmek istemektedir.

# Örneğin: Türkiye’den IOS kullanıcısı olan 25 yaşındaki bir erkek kullanıcının ortalama ne kadar kazandırabileceği belirlenmek isteniyor.



#region Veri Seti Hikayesi
#############################################
# Persona.csv veri seti uluslararası bir oyun şirketinin sattığı ürünlerin fiyatlarını ve bu ürünleri satın alan kullanıcıların bazı
# demografik bilgilerini barındırmaktadır. Veri seti her satış işleminde oluşan kayıtlardan meydana gelmektedir. Bunun anlamı tablo
# tekilleştirilmemiştir. Diğer bir ifade ile belirli demografik özelliklere sahip bir kullanıcı birden fazla alışveriş yapmış olabilir.

# Price: Müşterinin harcama tutarı
# Source: Müşterinin bağlandığı cihaz türü
# Sex: Müşterinin cinsiyeti
# Country: Müşterinin ülkesi
# Age: Müşterinin yaşı

#endregion
#region ################ Uygulama Öncesi #####################

#    PRICE   SOURCE   SEX COUNTRY  AGE
# 0     39  android  male     bra   17
# 1     39  android  male     bra   17
# 2     49  android  male     bra   17
# 3     29  android  male     tur   17
# 4     49  android  male     tur   17

#endregion
#region################ Uygulama Sonrası #####################

#       customers_level_based      PRICE SEGMENT
# 0     BRA_ANDROID_FEMALE_0_18  35.645303       B
# 1    BRA_ANDROID_FEMALE_19_23  34.077340       C
# 2    BRA_ANDROID_FEMALE_24_30  33.863946       C
# 3    BRA_ANDROID_FEMALE_31_40  34.898326       B
# 4    BRA_ANDROID_FEMALE_41_66  36.737179       A

#endregion

#############################################
# PROJE GÖREVLERİ
#############################################

#region IMPORTS
import seaborn as sns
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)

#endregion

#region GÖREV 1: Aşağıdaki soruları yanıtlayınız.
#############################################

# Soru 1: persona.csv dosyasını okutunuz ve veri seti ile ilgili genel bilgileri gösteriniz.

df = pd.read_csv("D:\mert python\CSV Files\persona.csv")

def check_df(dataframe, head=5):
    print("########## shape ##########")
    print(dataframe.shape)
    print("########## type ##########")
    print(dataframe.dtypes)
    print("########## head ##########")
    print(dataframe.head(head))
    print("########## tail ##########")
    print(dataframe.tail(head))
    print("########## NA ##########")
    print(dataframe.isnull().sum())
    print("########## quantiles ##########")
    print(dataframe.describe([0, 0.05, 0.50, 0.95, 0.99, 1]))

check_df(df)

# Soru 2: Kaç unique SOURCE vardır? Frekansları nedir?
df["SOURCE"].unique()
df["SOURCE"].describe()

# freq         2974

pd.DataFrame({"SOURCE": df["SOURCE"].value_counts(), "Ratio": 100 * df["SOURCE"].value_counts() / len(df)})

# Soru 3: Kaç unique PRICE vardır?
df["PRICE"].unique()

# Soru 4: Hangi PRICE'dan kaçar tane satış gerçekleşmiş?
df["PRICE"].value_counts()

# Soru 5: Hangi ülkeden kaçar tane satış olmuş?
df["COUNTRY"].value_counts()



# Soru 6: Ülkelere göre satışlardan toplam ne kadar kazanılmış?

df.groupby("COUNTRY").agg({"PRICE" : "sum"})


# Soru 7: SOURCE türlerine göre göre satış sayıları nedir?
df.groupby("SOURCE").agg({"PRICE" : "sum"})

# Soru 8: Ülkelere göre PRICE ortalamaları nedir?
df.groupby("COUNTRY").agg({"PRICE" : "mean"})

# Soru 9: SOURCE'lara göre PRICE ortalamaları nedir?
df.groupby("SOURCE").agg({"PRICE" : "mean"})

# Soru 10: COUNTRY-SOURCE kırılımında PRICE ortalamaları nedir?
df.groupby(["COUNTRY", "SOURCE"]).agg({"PRICE" : "mean"})
#endregion

#############################################

#region GÖREV 2: COUNTRY, SOURCE, SEX, AGE kırılımında ortalama kazançlar nedir?
#############################################
df.groupby(["COUNTRY", "SOURCE","SEX", "AGE"]).agg({"PRICE" : "mean"})

#endregion

#############################################

#region GÖREV 3: Çıktıyı PRICE'a göre sıralayınız.
#############################################
# Önceki sorudaki çıktıyı daha iyi görebilmek için sort_values metodunu azalan olacak şekilde PRICE'a uygulayınız.
# Çıktıyı agg_df olarak kaydediniz.
agg_df = df.groupby(["COUNTRY", "SOURCE", "SEX", "AGE"]).agg({"PRICE": "mean"}).sort_values("PRICE", ascending=False)

#endregion

#############################################

#region GÖREV 4: Indekste yer alan isimleri değişken ismine çeviriniz.
#############################################
# Üçüncü sorunun çıktısında yer alan PRICE dışındaki tüm değişkenler index isimleridir.
# Bu isimleri değişken isimlerine çeviriniz.
# İpucu: reset_index()
# agg_df.reset_index(inplace=True)
agg_df.reset_index(inplace=True)

#endregion

#############################################

#region GÖREV 5: AGE değişkenini kategorik değişkene çeviriniz ve agg_df'e ekleyiniz.
#############################################
# Age sayısal değişkenini kategorik değişkene çeviriniz.
# Aralıkları ikna edici olacağını düşündüğünüz şekilde oluşturunuz.
# Örneğin: '0_18', '19_23', '24_30', '31_40', '41_70' maximum 66 var

cut_bins = [0,18,23,30,40, agg_df["AGE"].max()]
cut_labels =['0_18', '19_23', '24_30', '31_40', f'41_{agg_df["AGE"].max()}']

agg_df["AGE_CAT"] = pd.cut(x=agg_df["AGE"], bins=cut_bins, labels=cut_labels)


#endregion

#############################################

#region GÖREV 6: Yeni level based müşterileri tanımlayınız ve veri setine değişken olarak ekleyiniz.
#############################################
# customers_level_based adında bir değişken tanımlayınız ve veri setine bu değişkeni ekleyiniz.
# Dikkat!
# list comp ile customers_level_based değerleri oluşturulduktan sonra bu değerlerin tekilleştirilmesi gerekmektedir.
# Örneğin birden fazla şu ifadeden olabilir: USA_ANDROID_MALE_0_18
# Bunları groupby'a alıp price ortalamalarını almak gerekmektedir.

agg_df["customers_level_based"] = [("_".join(col)).upper() for col in agg_df[["COUNTRY","SOURCE","SEX","AGE_CAT"]].values]

type(agg_df) # pandas.core.frame.DataFrame
type(agg_df["COUNTRY"]) #  pandas.core.series.Series
type(agg_df[["COUNTRY","SOURCE","SEX","AGE_CAT"]]) # pandas.core.frame.DataFrame
type(agg_df.values) # numpy.ndarray

agg_df = agg_df.groupby("customers_level_based").agg({"PRICE": "mean"})
agg_df.reset_index(inplace=True) # customers_level_based sütun ismi değil index ismi
agg_df["customers_level_based"].value_counts()

agg_df = agg_df[["customers_level_based", "PRICE", "SEGMENT"]] # gerekli kısımları alıoruz

agg_df["customers_level_based"].describe()
agg_df["customers_level_based"].value_counts()


#endregion

#############################################

#region GÖREV 7: Yeni müşterileri (USA_ANDROID_MALE_0_18) segmentlere ayırınız.
#############################################
# PRICE'a göre segmentlere ayırınız,
# segmentleri "SEGMENT" isimlendirmesi ile agg_df'e ekleyiniz,
# segmentleri betimleyiniz,
segments = ["D", "C", "B", "A"]
agg_df["SEGMENT"] = pd.qcut(x=agg_df["PRICE"], q=4, labels=segments)

#endregion

#############################################

#region GÖREV 8: Yeni gelen müşterileri sınıflandırınız ne kadar gelir getirebileceğini tahmin ediniz.
#############################################
# 33 yaşında ANDROID kullanan bir Türk kadını hangi segmente aittir ve ortalama ne kadar gelir kazandırması beklenir?
new_user = "TUR_ANDROID_FEMALE_31_40"
print(agg_df[agg_df["customers_level_based"] == new_user])

#       customers_level_based      PRICE SEGMENT
# 72  TUR_ANDROID_FEMALE_31_40  41.833333       A


# 35 yaşında IOS kullanan bir Fransız kadını hangi segmente ve ortalama ne kadar gelir kazandırması beklenir?

new_user2 = "FRA_IOS_FEMALE_31_40"
print(agg_df[agg_df["customers_level_based"] == new_user2])

# agg_df

#endregion




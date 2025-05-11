######################################################################################################
# Pandas Alıştırmalar
######################################################################################################


import seaborn as sns
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)

df = sns.load_dataset("car_crashes")
df.columns
df.info()


# df = sns.load_dataset("titanic")
# df.head()

#############################                 Görev 1


[("num_" + col).upper()  if df[col].dtype != "O" else col.upper() for col in df.columns]



# ###############################################
# # GÖREV 2: List Comprehension yapısı kullanarak car_crashes verisindeki isminde "no" barındırmayan değişkenlerin isimlerininin sonuna "FLAG" yazınız.
# ###############################################

df.head()

[col.upper() if "no_" in col else (col + "_flag").upper() for col in df.columns]


# ###############################################
# # Görev 3: List Comprehension yapısı kullanarak aşağıda verilen değişken isimlerinden FARKLI olan değişkenlerin isimlerini seçiniz ve yeni bir dataframe oluşturunuz.
# ###############################################

og_list = ["abbrev", "no_previous"]


new_cols = [col for col in df.columns if col not in df[og_list]]

new_df = df[new_cols]

new_df.head()

##################################################
# Pandas Alıştırmalar
##################################################

import numpy as np
import seaborn as sns
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

#########################################
# Görev 1: Seaborn kütüphanesi içerisinden Titanic veri setini tanımlayınız.
#########################################

df = sns.load_dataset("titanic")

#########################################
# Görev 2: Yukarıda tanımlanan Titanic veri setindeki kadın ve erkek yolcuların sayısını bulunuz.
#########################################

df.sex.value_counts()

df["sex"].value_counts()
df.count()


#########################################
# Görev 3: Her bir sutuna ait unique değerlerin sayısını bulunuz.
#########################################

df.nunique()


#########################################
# Görev 4: pclass değişkeninin unique değerleri bulunuz.
#########################################

df.pclass.unique()  # unique değerler
df.pclass.value_counts().unique() # sayısı

#########################################
# Görev 5:  pclass ve parch değişkenlerinin unique değerlerinin sayısını bulunuz.
#########################################
df[["pclass", "parch"]].nunique()


#########################################
# Görev 6: embarked değişkeninin tipini kontrol ediniz. Tipini category olarak değiştiriniz. Tekrar tipini kontrol ediniz.
#########################################

df["embarked"].dtype  # object

df.embarked = df.embarked.astype("category")

df["embarked"].dtype # category

#########################################
# Görev 7: embarked değeri C olanların tüm bilgelerini gösteriniz.
#########################################

df[df['embarked'] == 'C']



#########################################
# Görev 8: embarked değeri S olmayanların tüm bilgelerini gösteriniz.
#########################################

df[df['embarked'] != 'S']

#########################################
# Görev 9: Yaşı 30 dan küçük ve kadın olan yolcuların tüm bilgilerini gösteriniz.
#########################################


df[(df["age"] < 30) & (df["sex"] == "female")].head()
# aynısı
df.query('(age < 30) & (sex == "female")').head()

#########################################
# Görev 10: Fare'i 500'den büyük veya yaşı 70 den büyük yolcuların bilgilerini gösteriniz.
#########################################

df[(df["fare"] > 500) | (df["age"] > 70)].head()

#########################################
# Görev 11: Her bir değişkendeki boş değerlerin toplamını bulunuz.
#########################################

df.isnull().sum().sum()


#########################################
# Görev 12: who değişkenini dataframe'den düşürün.
#########################################

df.drop("who", axis=1).head()

df.columns

#########################################
# Görev 13: deck değikenindeki boş değerleri deck değişkenin en çok tekrar eden değeri (mode) ile doldurunuz.
#########################################

df['deck'].fillna(df['deck'].mode()[0], inplace=True)
df["deck"].isnull().sum()
df["deck"].head()


#########################################
# Görev 14: age değikenindeki boş değerleri age değişkenin medyanı ile doldurun.
#########################################

df['age'].fillna(df['age'].median(), inplace=True)
df["age"].head(10)

#########################################
# Görev 15: survived değişkeninin Pclass ve Cinsiyet değişkenleri kırılımınında sum, count, mean değerlerini bulunuz.
#########################################

df.groupby(["sex", "pclass"]).agg({"survived" : ["sum", "count", "mean"]})


#########################################
# Görev 16:  30 yaşın altında olanlar 1, 30'a eşit ve üstünde olanlara 0 vericek bir fonksiyon yazınız.
# Yazdığınız fonksiyonu kullanarak titanik veri setinde age_flag adında bir değişken oluşturunuz oluşturunuz. (apply ve lambda yapılarını kullanınız)
#########################################

df["age_flag"] = df.apply(lambda x: 1 if x["age"] < 30 else 0, axis=1)

#########################################
# Görev 17: Seaborn kütüphanesi içerisinden Tips veri setini tanımlayınız.
#########################################

df = sns.load_dataset("tips")


#########################################
# Görev 18: Time değişkeninin kategorilerine (Dinner, Lunch) göre total_bill  değerlerinin toplamını, min, max ve ortalamasını bulunuz.
#########################################

df.groupby(["time"]).agg({"total_bill" : ["min", "max", "mean"]})

#########################################
# Görev 19: Günlere ve time göre total_bill değerlerinin toplamını, min, max ve ortalamasını bulunuz.
#########################################

df.groupby(["time", "day"]).agg({"total_bill" : ["min", "max", "mean"]})

#########################################
# Görev 20:Lunch zamanına ve kadın müşterilere ait total_bill ve tip  değerlerinin day'e göre toplamını, min, max ve ortalamasını bulunuz.
#########################################

df.groupby((df["time"] == "Lunch") & (df["sex"] == "female")).agg({"total_bill" : ["min", "max", "mean"], "tip" : ["min", "max", "mean"]})

df[(df["time"] == "Lunch") & (df["sex"] == "Female")].groupby("day").agg({"total_bill" : ["sum", "min", "max", "mean"],
                                                                          "tip" : ["sum", "min", "max", "mean"]})

df[(df["time"] == "Lunch") & (df["sex"] == "Female")].groupby("day").agg({"total_bill": ["sum", "min", "max", "mean"],"tip": ["sum", "min", "max", "mean"]})


#########################################
# Görev 21: size'i 3'ten küçük, total_bill'i 10'dan büyük olan siparişlerin ortalaması nedir?
#########################################

df[(df["size"] < 3 ) & (df["total_bill"] >10 )][["total_bill", "tip"]].mean()


#########################################
# Görev 22: total_bill_tip_sum adında yeni bir değişken oluşturun. Her bir müşterinin ödediği totalbill ve tip in toplamını versin.
#########################################

df["total_bill_tip_sum"] = df["total_bill"] + df["tip"]
df["total_bill_tip_sum"].head()


#########################################
# Görev 23: total_bill_tip_sum değişkenine göre büyükten küçüğe sıralayınız ve ilk 30 kişiyi yeni bir dataframe'e atayınız.
#########################################

yeni_bir_df = df.sort_values("total_bill_tip_sum", ascending=False).head(30)


# mülakat HR
# Aşağıdaki fonksiyonun her satırında ne yapıldığını anlatınız.
# Bu fonksiyonu enumerate ile yazabilir miydik?
# Yazabiliyor olsaydık bu ne kazandırırdı?

def alternating(string):
    new_string = ""
    for string_index in range(len(string)):
        if string_index % 2 == 0:
            new_string += string[string_index].upper()

        else:
            new_string += string[string_index].lower()

    print(new_string)

A = ["sdfgshsh", "shjsfgjssd"]

alternating(A)

enumerate(A)


# alternating isimli bir fonksiyon yazıyoruz.
# bu fonksiyon ileride kullanılacak stringin her harfinde ikiye bölünebilen hanelerindeki harfi küçükse büyültüyor,
# bölünemeyen hanelerinde büyükse küçültüyor ve çıktı sağlıyor.
# eğer tuple bir new_string girilirse enumerate ile de yazardık.
# bu bize her elemanda kendine özel indexi olacağından her elemanın çift indexi büyürdü. yani listelerde kullanmamıza olanak sağlardı



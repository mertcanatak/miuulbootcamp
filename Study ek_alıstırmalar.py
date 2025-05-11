##############################################
#LIST COMPHRENSION
##############################################

#region ALIŞTIRMALAR

# Görev 1: 0-100 arasında değerler oluşturarak 2'ye ve 5'e kalansız bölünen sayıları list comprehension yapısı kullanarak oluşturunuz ve
# list_a adında bir değişkene atayınız.

list_a = [i for i in range(100) if i % 2 == 0 if i % 5 == 0]

# Görev 2: list comprehension yapısı kullanarak 0-20 arasında değerler üretip, çift olanlara 'ÇİFT' tek olanlara 'TEK' yazdırınız.

[(i, "ÇİFT") if i % 2 == 0 else (i, "TEK")  for i in range(20)]

# Görev 3: Aşağıdaki iç içe matrix listesinin transpozunu alınız.
matrix = [[1, 2], [3,4], [5,6], [7,8]]

[[row[i] for row in matrix] for i in range(2)]

import numpy as np
matrix = np.array(matrix)
matrix.transpose()


# Görev 4: Aşağıdaki list_name içerisindeki değerlerinin tüm değerlerini küçülterek x ile başlayanları gösteriniz.(list comp)
list_name = ['Xh','Dx','Xh','xb','Tb','Td']

[i for i in list_name if i.lower().startswith("x")]

#endregion

################################################################################################
#                           ILOC & LOC ALIŞTIRMALAR
###############################################################################################

#region Veri Seti Hakkında Bilgi

#Bu veriler, hayali Birleşik Krallık karakterleri için yapay adlar, adresler, şirketler ve telefon numaraları içerir.
#endregion


#region Kütüphaneler & Eklentiler
# Gerekli kütüphaneleri ve eklentileri tanımlayınız.

import random
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 500)



#endregion



#region Load Data
#Veri setini fonksiyon içinde oluşturunuz ve okutunuz.
df = pd.read_csv(r"D:\mert python\CSV Files\uk-500.csv")


#endregion


#region Veri Setini İnceleyiniz.

# Görev 1: Veri setinin ilk 5 gözlemini inceleyiniz.
df.head()

# Görev 2: Veri setinin boyut bilgisini inceleyiniz.

df.shape
# Görev 3: Veri setindeki eksik değerleri inceleyiniz.
df.isnull().sum()

# Görev 4: Veri setinin değişkenlerine bakınız.
df.columns

# Görev 5: Veri setinin index bilgisini inceleyiniz.
df.index

# Görev 6: Veri setindeki değişkenlerin tip bilgilerini inceleyiniz.
df.dtypes

#endregion


#region ALIŞTIRMA 1
# ID adında yeni bir değişken oluşturunuz ve list comprehension yapısı kullanarak, veri setinin boyutunu da göz önünde bulundurarak 0-1000 arasında random değerler üretip,
# oluşturmuş olduğunuz yeni ID değişkenine aktarınız ve ilk 5 gözlemi inceleyiniz.

df["ID"] = ["ID" + str(random.randint(0, 1000)) for col in df["first_name"]]
df.head()

#endregion


################
# ILOC
################

#df.iloc[<satır seçimi>, <sütun seçimi>]

# region Satır Seçimleri Alıştırmaları

# Görev 1: Veri setinin ilk satırını getiriniz.


# Görev 2: Veri setinin ikinci satırını getiriniz.


# Görev 3: Veri setinin son satırını getiriniz.


#endregion


#region Kolon Seçimi Alıştırmaları

# Görev 1: Veri setinin ilk kolonunu getiriniz.


# Görev 2: Veri setinin ikinci kolonunu getiriniz.


# Görev 3: Veri setinin son kolonunu getiriniz.

#endregion

#NOT : .iloc dizin oluşturucu kullanılarak birden çok sütun ve satır birlikte seçilebilir.

#region Birden çok Sütun ve Satır Seçimi Alıştırmaları

# Görev 1: Veri setinin 0'dan 5'e kadar olan elemanlarını seçiniz ve inceleyiniz.


# Görev 2: Veri setinde tüm satırları da alacak şekilde ilk iki sütununu inceleyiniz.


# Görev 3: Veri setinde satırlardan 0. 3. 6. ve 24. satırları, sütunlardan da 0. 5. ve 6. sütunları seçerek inceleyiniz.


# Görev 4: Veri setinin ilk 5 satırını ve 5. 6. 7. sütunlarını seçerek inceleyiniz.


#endregion

#NOT :ILOC da bir satır seçildiğinde Pandas Serisi. Birden çok satır veya bir sutün seçildiğinde Pandas Dataframe  dönüdürür.
#NOT : Seriden kurtulmak için bir liste alabiliriz.


type(df.iloc[20]) #pandas.core.series.Series

type(df.iloc[[20]]) #pandas.core.frame.DataFrame

df.iloc[[20]]
df.iloc[20]

type(df.iloc[2:4]) #pandas.core.frame.DataFrame


###################################
#LOC
###################################

#region LOC Alıştırmalar

# Görev 1: Veri setinin ilk 5 gözlemini inceleyiniz ve last_name değişkenini index değeri olarak atayınız.
# İndex değeri olarak atadıktan sonra tekrar ilk 5 gözlemi inceleyip, ardından veri setinin index bilgisini inceleyiniz.



# Görev 2: Veri setinde index değeri "Andrade" olan satırları getiriniz ve tipini sorgulayınız.



# Görev 3: Veri setinde index değeri "Andrade" ve "Veness" olan satırları getiriniz ve tipini sorgulayınız.



# Görev 4: Veri setinde index değeri "Andrade" ve "Veness" olan, 'first_name', 'address', 'city' kolonlarını getiriniz.


# Görev 5: city ve email kolonları arasında (email kolonu dahil) index değeri "Andrade" ve "Veness" olanları getiriniz.


# Görev 6: index değeri Andrade'den Veness'e kadar olan, 'first_name', 'adress' ve 'city' kolonlarını getiriniz.


#endregion

#region LOC Koşullu Seçme

# Görev 1: first_name'i 'Erasmo' olan kişinin/kişilerin 'company_name', 'email' ve 'phone1' bilgilerini getiriniz.


# Görev 2: first_name'i 'Antonio' olan kişinin/kişilerin 'email' bilgilerini getiriniz ve getirdikten sonra tip bilgisini inceleyiniz.


# Görev 3: first_name'i 'Antonio' olan kişinin/kişilerin 'email' değişkenini getiriniz ve getirdikten sonra tip bilgisini inceleyiniz.


#endregion

#region Alıştırmalar

# Görev 1: first_name'i 'Antonio' olan ve "city" ile "email" arasındaki tüm sütunları seçiniz.



##2. E-posta sütununun 'hotmail.com' ile bittiği satırları seçin, tüm sütunları dahil ederek getirin
# Görev 2: email sütununun 'hotmail.com' ile biten satırlarını seçin ve tüm sütunları dahil ederek getiriniz.



# Görev 3: first_name'i 'Antonio' olan ve email'i 'hotmail.com' ile biten satırları seçiniz.



# Görev 4: İlk başta oluşturmuş olduğunuz ID değişkeninde 100 ile 200 arasındaki (200 dahil) satırları seçerek
# 'postal' ve 'web' sütunlarını getiriniz.


# Görev 5: company_name içerisinde 4 kelime içeren satırları seçerek ilk 5 gözlemini getiriniz. (apply ve lambda kullanınız)



# Görev 6: ID'si 20'den büyük olan tüm satırların first_name'i "John" olarak değiştiriniz.


#endregion


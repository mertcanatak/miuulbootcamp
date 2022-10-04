# Değişken Türleri(Variable Types)
# ▪Sayısal Değişkenler

# ▪Kategorik Değişkenler(Nominal,Ordinal)
#   Kadın-Erkek Futbol Takımı Nominal (sırasız)
#   ilk okul orta okul lise Ordinal (sıralı)

# ▪Bağımsız Değişken(feature,independent,input,column,predictor,explanatory)

# Denetimli Öğrenme
# (Supervised Learning) bağımlı değişken ve target varsa
# şu şu varsa şu olmuş

# Denetimsiz Öğrenme bağımsız değişkenin target değişkeninin oladığı
# (Unsupervised Learning)

# Pekiştirmeli Öğrenme
# (Reinforcement Learning)

# Regresyon problemlerinde bağımlı değişken sayısal
# Sınıflandırma problemlerinde bağımlı değişken kategorik

#################################################
# Tahminlerim ne kadar başarılı?
#################################################
# MSE  - MinSquareError - gerçek değerler ile tahmin değerlerin arasınadki farkı
# RMSE  - RootMinSquareError -
# MAE mutlak ortak hata - MeanAbsoluteError -


# Accuracy= Doğru Sınıflandırma Sayısı / Toplam Sınıflandırılan Gözlem Sayısı

#################################################
# Model Doğrulama(Model Validation)Yöntemleri
#################################################

#[            ORJİNAL VERİ SETİ         ]
#[  EĞİTİM SETİ (TRAIN)  ][  TEST SETİ  ]
#[ 1 ][ 2 ][ 3 ][ 4 ][ 5 ]

# K-Katlı Capraz Doğrulama(KFold Cross Validation)
# beni, iki şekilde kullanabilirsiniz:
# orjinal veri setini 5 parçaya böl 4 farklı parçayla model kur biriyle test et
# sonra test kısmına tekrar git

# veri seti bol ise çaprazlamalar eğitim setinde bütün işlemler bittiğinde test setinde test etmek

#################################################
# Yanlılık-Varyans Değiş Tokuşu(Bias-Variance Tradeoff)
#################################################

# Underfitting (Az Öğrenme) Yüksek Yanlılık
# Doğru Model  Düşük Yanlılık, Düşük Varyans
# Overfitting (Veriyi Ezberlenme) Yüksek Varyans
# Eğitim seti ve test setinde birbirinden ayrılan hata değişimi incelenir
# ve bu hata değişimlerinde birbirinden ayrılma başladığında aşırı öğrenme başlamıştır
# Optimum Nokta denir
# Model Karmaşıklığını azaltırsak (modeli hassaslaştırmak)

##################################################################################################
# Doğrusal Regresyon(Linear Regression)
##################################################################################################

# Amaç, bağımlı ve bağımsız değişken(ler) arasındaki ilişkiyi doğrusal olarak modellemektir.

# Formul anlamı metrekare bilgisinin etkisini fiyata nasıl yansıtıcaz
#           ŷ₁=b+wxi x
#           i: evin metrekare bilgisinin
#           w: weight (etki oranı)
#           b: beta veya bias sabiti
#           ŷ₁: fiyat (bağımlı değişken)

# Ağırlıkların Bulunması
# Gerçek değerler ile tahmin edilen değerler arasındaki farkların karelerinin toplamını/ortalamasını
# minimum yapabilecek b ve w değerlerini bularak.

# tahmin fonksiyonu  MSE dir (gerçek değerlerle tahmin edilen değerlerin farkının karesi)
# Cost(b,w)= 1/2m Σ ((b + w*xi) - yi)^2

# fonksiyonda doğruyu sabit değeri(bias/beta) ve ağırlığı değiştirerek en iyi yere koymamız gerekir.

#################################################
# Regresyon Modellerinde Başarı Değerlendirme ( MSE, RMSE, MAE )
#################################################

# MSE, RMSE, MAE üçü de eş zamanlı denenir ama düşük olan alınmaz.
# ortalama hatamızdır

# MSE-RMSE-MAE.png

#################################################
# Parametrelerin Tahmin Edilmesi ( Ağırlıkların Bulunması ) b ve w
#################################################
# Nasıl tahmin ederiz?  : iki yöntemle

# Analitik Çözüm:Normal Denklemler Yöntemi(En Küçük Kareler Yöntemi)

# Optimizasyon Çözümü:Gradient Descent

# REGRESSIONS.png

##################################################################################################
# iki aşama var ilki hata değerlendirme ikincisi bu hata değerlendirmesini optimize etmek
##################################################################################################

#################################################
# Doğrusal Regresyon için Gradient Descent ( Gradient Descent for Linear Regression )
#################################################

# Gradient Descent Fonksiyonunun amacı : bir fonksiyonun minimum yapabilecek parametrelerini bulmaktır.

# repeat until convergence

# Gradyanın negatifi olarak tanımlanan'en dik iniş'yönünde
# iteratif olarak parametre değerlerini güncelleyerek
# ilgili fonksiyonun minimum değerini verebilecek parametreleri bulur.

# Cost fonksiyonunu minimize edebilecek parametreleri bulmak için kullanılır.

#######################
# OPTİMİZE ETME KISMI
#######################

# UPDATE RULE

# gradient descent ne diyordu türevlenebilir bir fonksiyonun türevini aldığında ben bu türevin
# tersine doğru giderek bu parametreleri güncellersem cost fonksiyonunu azaltıyor olurum


#################################################
# Basit Doğrusal Regresyon Modeli ( Linear Regression )
#################################################

# Sales Prediction with Linear Regression (advertising.csv)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.float_format',lambdax:'%.2f'%x)

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,mean_absolute_error
from sklearn.model_selection import train_test_split,cross_val_score

#################################################
# Simple Linear Regression with OLS Using Scikit-Learn
#################################################

df=pd.read_csv("datasets/advertising.csv")

X=df[["TV"]]
y=df[["sales"]]]

#################################################
#Model
#################################################

reg_model = LinearRegression().fit(x,y)


#y_hat=b+w*TV

#sabit (b-bias)

reg_model.intercept_[0]

#otv'nin katsayısı (w1)
reg_model.coef_[e][0]

#################################################
# Tahmin
#################################################

#150 birimlik TV harcaması olsa ne kadar satış olması beklenir?

reg_model.intercept_[0] + reg_model.coef_[0][0]*150


#Modelin Görselleştirilmesi
g=sns.regplot(x=X, y=y, scatter_kws={'color':'b','s':9},
              ci=False, color="r")
# ci güven aralığı

g.set_title(F"Model Denklemi: Sales = {round(reg_model.intercept_[0],2)} + TV*(round(reg_model.coef_[0][0],2)}")
g.set_ylabel("Satış Sayısı")
g.set_xlabel("TV Harcamaları")
plt.xlim(-10,310)
plt.ylim(bottom=0)
plt.show()

# kırmızı çizgi model dir.

###########################
# Tahmin Başarısı
###########################
# MSE
y_pred = reg_model.predict(x)
mean_squared_error(y, y_pred)
y.mean()
y.std()
#

# RMSE
np.sqrt(mean_squared_error(y, y_pred))
# 3.24

# MAE
mean_absolute_error(y, y_pred)
# 2.54

# R-KARE
reg_model.score(x, y)

######################################################
# Multiple Linear Regression
######################################################

df = pd.read_csv("datasets/advertising.csv", index_col=0)
X = df.drop('sales',axis=1)
y = df[["sales"]]

###########################
# Model
###########################

X_train, X_test, y_train, y_test = train_test_split(x,y,test_size=0.20,random_state=1)

reg_model = LinearRegression()
reg_model.fit(X_train,y_train)

reg_model = Linear Regression().fit(X_train,y_train)


#sabit(b- bias)
reg_model.intercept_

#coefficients(w-weights)
reg_model.coef_


#Aşağıdaki gözlem değerlerine göre satışın beklenen değeri nedir?

#TV:30
#radio:10
#newspaper:40

#2.98
#0.8468431,0.17854434,0.00258619

# Sales = 2.90 + TV * 0.8468431 + radio * 0.17854434 + newspaper * 0.00258619
2.90 + 30*0.8468431 + 18*0.17854434 + 40*0.00258619


yeni_veri[[30],[10],[40]]
yeni_veri = pd.DataFrame(yeni_veri).T

reg_model.predict(yeni_veri)

###########################
# Tahmin Başarısı
###########################

#Train RMSE
y_pred=reg_model.predict(X_train)
np.sqrt(mean_squared_error(y_train,y_pred))
#1.73


#TRAIN RKARE
reg_model.score(X_train,y_train)


#Test RMSE
y_pred=reg_model.predict(X_test)
np.sqrt(mean_squared_error(y_test,y_pred))
#1.41

#Test RKARE
reg_modelçscore(X_test, y_test)

# 10 katlı CV RMSE
np.mean(np.sqrt(-cross_val_score(reg_model,
                                 X,
                                 y,
                                 )))


# regresyon kurmamız gerektiğinde
# Veri setini okuma
# özellik mühendisliği
# modeli kurmadan önce 80/20 ayırmak
######################################################
#Simple Linear Regression with Gradient Descent from Scratch
######################################################
# TAMAMEN ÖRNEK

#Cost function. ->

# GRADIENT_DESCENT.png
# bu fonksiyonda minimum değere gitmeye çalışıyorduk

# MSE değerini hesaplama fonksiyonu
#cost function MSE
def cost_function(Y, b, w, X):
    m = len(Y)
    sse = 0
    for i in range(0, m):
        y_hat = b + w * X[i]
        y = Y[i]
        sse += (y_hat-y) ** 2
    mse = sse / m
    return mse

# UPDATE RULE
#update weights
def update_weights(Y, b, w, X, learning_rate):
    m = Len(Y)

    b_deriv_sum=0
    w_deriv_sum=0

    for i in range(0,m):
        y_hat=b+w*x[i]
        y= Y[i]
        b_deriv_sum += (y_hat - y)
        w_deriv_sum += (y_hat - y) * X[i]

    new_b = b - (learning_rate * 1 / m * b_deriv_sum)
    new_w = w - (learning_rate * 1 / m * w_deriv_sum)
    return new_b, new_w

#train fonksiyonu
def train(Y, initial_b, initial_w, X, learning_rate, num_iters):

   print("Starting gradient descent atb={0},w={1},mse={2}".format(initial_b,initial_w,
                                                                  cost_function(Y, initial_b, initial_w, X)))

   b = initial_b
   w = initial_w
   cost history = []

   for i in range(num_iters):|
       b, w = update_weights(Y, b, w, X, Learning_rate)
       mse = cost_function(Y,b,w,X)
       cost_history.append(mse)

        if i % 100 == 0:
             print("iter={:d}b={:. 2f}w={:. 4f}mse={:.4}".format(i,b,w,mse))


        print("After{0}iterations={1},w={2},mse={3}".format(num_iters,b,w,cost function(Y,b,w,x)))
         return cost history,b,w













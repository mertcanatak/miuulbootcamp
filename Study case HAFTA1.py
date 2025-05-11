#                                         GÖREV 1

x = 8  #int
y = 3.2  #float
z = 8j + 18 #complex
a = "Hello World" #str
b = True   #bool
c = 23 < 22   #bool
l = [1, 2, 3, 4]   #list
d = {"Name": "Jake",
     "Age": 27,
     "Adress": "Downtown"}   #dictionary
t = ("Machine learning", "Data Science")    #tuple
s = {"Pyth", "Machin Lear", "Data science"}   #set

type(s)


#####################               GÖREV 2

text = "The goal is to turn data into information, and information into insight."

dir(str)
text.upper().replace(",", " ").replace(".", " ").split()

#####################               GÖREV 3
dnm = "D A T A S C I E N C E"           #1

dnm3 = "DATASCIENCE"                    #3
                                        # NOT: 2 ve 3 farklı yöntemle harflerine ayırmak içindi
lst = dnm.split()

lst[0::10]

adim3 = lst[0:4]

lst.pop(10)

lst.append("Y")

lst.insert(8, "N")


#####################               GÖREV 4


dict = {"Christian": ["America", 18],
        "Daisy": ["England", 12],
        "Antonio": ["Spain", 22],
        "Dante": ["Italy", 25]}

dict.keys()
dict.values()

dict["Daisy"][1] = 13

dict["Ahmet"] = ["Turkey", 24]                   # ekledik

dict.pop("Antonio")


#####################               GÖREV 5

list = [2, 13, 18, 93, 22]

even_list = []
odd_list = []


def func(list_name):
    for l in list:
        if l % 2 == 0:
            even_list.append(l)
        else:
            odd_list.append(l)
    return

func(list)

print("even" + str(even_list), "odd " + str(odd_list))


# del odd_list
# del even_list

#####################               GÖREV 6

ogrenciler = ["Ali", "Veli", "Ayşe", "Talat", "Zeynep", "Ece"]

eng_students = []
med_students = []

def enum_students(list_name):
    for index, ogrenci in enumerate(ogrenciler, 1):
        if index <= 3:
            print("Mühendislik Fakültesi: " + str(index) + ", Öğrenci: " + ogrenci)
        else:
            print("Tıp Fakültesi: " + str(index - 3) + ", Öğrenci: " + ogrenci)
    return

enum_students(ogrenciler)

#####################               GÖREV 7


ders_kodu = ["CMP1005", "PSY1001", "HUK1005", "SEN2204"]
kredi = [3, 4, 2, 4]
kontenjan = [30, 75, 150, 25]

k = list(zip(ders_kodu, kredi, kontenjan))

for i in range(len(k)):
    print("Kredisi " + str(k[i][1]) + " olan "
          + str(k[i][0] + " kodlu dersin kontenjanı: " + str(k[i][2])))

# daha iyi hali

ders_kodu = ["CMP1005", "PSY1001", "HUK1005", "SEN2204"] ; kredi = [3, 4, 2, 4] ; kontenjan = [30, 75, 150, 25]

for ders_kodu, kredi, kontenjan in zip(ders_kodu, kredi, kontenjan):
    print(f"Kredisi  {kredi} olan {ders_kodu}  kodlu dersin kontenjanı: {kontenjan} ")



#####################               GÖREV 8


kume1 = set(["data", "python"])
kume2 = set(["data", "function", "qcut", "lambda", "python", "miuul"])

# kume1 kume2 'i kapsamıyor FALSE
kume1.issuperset(kume2)


if kume2.issuperset(kume1):
    print(kume2.difference(kume1))


















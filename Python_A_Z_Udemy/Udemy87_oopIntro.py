## OOP amacı kod tekrarı yapmamak, hızlı işlemler yapmak

## class isimleri büyük harfle başlar.

## class nitelikleri
"""
class Asker():
    saglik=100
    isim='Ahmet'
    silah='Tüfek'
print()
print(Asker.saglik)
Asker.mermiSayisi=100
print(Asker.mermiSayisi)
print()
"""
## class sınıf nitelikleri  , değişkene ilave edilince veya çıkarılınca aynı koşullar diğer sınıflara da işler
# string
"""
class Sipariş():
    firma=''  # Değiştirilemez veri tipleri
    miktar=0  # Değiştirilemez veri tipleri
    tarih=''  # Değiştirilemez veri tipleri

gofret=Sipariş()
gofret.firma="Ülker"
gofret.miktar=1000
gofret.tarih="20.02.2002"

print(gofret.firma)
print(gofret.miktar)
print(gofret.tarih)
print()

kitap=Sipariş()
kitap.firma="Can Yayınları"
kitap.miktar=1000
kitap.tarih="28.12.2020"
print(kitap.firma)
print(kitap.miktar)
print(kitap.tarih)
print()

"""
# list
"""
class Sipariş():
    firmalar=[]  # Değiştirilebilir veri tipleri
    miktar=0  # Değiştirilebilir veri tipleri
    tarih=''  # Değiştirilemez veri tipleri

gofret=Sipariş()
gofret.firmalar+=['Ülker']
gofret.miktar=1000
gofret.tarih="20.02.2002"

print(gofret.firmalar)
print(gofret.miktar)
print(gofret.tarih)
print()

kitap=Sipariş()
kitap.firmalar+=['Can Yayınları']
kitap.miktar=1000
kitap.tarih="28.12.2020"
print(kitap.firmalar)
print(kitap.miktar)
print(kitap.tarih)
print()
"""

## Örnek sınıf nitelikleri  , değişkene ilave edilince veya çıkarılınca aynı koşullar diğer sınıflara da İŞLEMEZ.
"""
class Asker():
    degisken="Bunu alır"
    def __init__(self): # Bir örnek oluşturulurken yapılacak işlemler burada yapılır.
        # self bu fonksiyonun örneğe ait olduğunu söyler.
        self.kabiliyetleri = []
        print("Burasını yazdırmaz sadece örneklerken çalışır birdaha çalışmaz")
ahmet=Asker()
mehmet=Asker()

ahmet.kabiliyetleri+=["128milyar"]
mehmet.kabiliyetleri+=["dolarNerde"]

print(ahmet.kabiliyetleri)
print(mehmet.kabiliyetleri)

print("Yazdırır",Asker.degisken)
a=Asker()
print("Bu şekilde yazıdır. Alttakinde erör verir",a.kabiliyetleri)
#print(Asker.kabiliyetleri)

class Deneme():
    print("Alfabe,burası sınıf tanımlanırken olduğu için çalışır")
    
"""
# Örneklere müdahale

class Asker():
    kabiliyetler=["ibneler"]
    def __init__(self,isim,güç): #parametre olan değğişkenler gönderilir
        self.isim=isim  # sınıfa ait olan  değişkenler
        self.gücü=güç
        self.kabiliyetler=[]
## Örneğe özgü nitelikler değişkene özgü olur. hepsine yazdırmaz.
## İstenirse sınıf şeklinde ikisinede yazdırabilir.
ahmet=Asker("Ahmet",80)
ahmet.kabiliyetler+=["Nişancı"]
print("Asker Adı : ",ahmet.isim)
print("Asker Gücü : ",ahmet.gücü)
print("Kabiliyeti : ",ahmet.kabiliyetler)

mehmet=Asker("Mehmet",60)
mehmet.kabiliyetler+=["Tankçı"]
print("Asker Adı : ",mehmet.isim)
print("Asker Gücü : ",mehmet.gücü)
print("Kabiliyeti : ",mehmet.kabiliyetler)

print(Asker.kabiliyetler) # böyle yapılır.
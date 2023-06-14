# STRING veri tipi:
print("STRING Veri Tipi")
print(30*"=")
string="Sadettin" 
print(string) ,print(string[3])

# DEMET veri tipi : Birden fazla veri depolanabiliyor ve listelerden daha hızlı çalışırlar.
# Listelerden farkı demetler değiştirilemiyor.
# Hiçbir zaman değiştirme ihtiyacı olmayacak durumlarda kullanımı tercih edilir.
print(30*"=")
print("DEMET Veri Tipi")
print(30*"=")
kitap=('Ahmet Ümit','İstanbul Hatırası',300)
print("Yazar : {}".format(kitap[0]))
print("Kitap Adı : {}".format(kitap[1]))
print("Kitap Sayfa Sayısı : {}".format(kitap[2]))

# LİSTE veri tipi:
print(30*"=")
print("LİSTE Veri Tipi")
print(30*"=")
kutuphane=[]
print("kutuphane : ",kutuphane)
kitap0=('Ahmet Ümit','İstanbul Hatırası',300)
kutuphane.append(kitap0)
print("kutuphane.append komutu : ",kutuphane)
kutuphane.remove(kitap0)
print("kutuphane.remove komutu : ",kutuphane)


# Kitap Ekleme/Çıkarma/Görüntüleme Fonksiyonu hazırlanışı
print(30*"=")
print("Kitap Çıkarma Fonksiyonu")
print(30*"=")
kitap1=('Ahmet Ümit','İstanbul Hatırası',300)
kitap2=('Paulo Coelho','Aldatmak ',300)
kutuphane.append(kitap1)
kutuphane.append(kitap2)
# Kitabın varlığı sorgulanıyor.
def kitapVarmi(hangi_Kitap:tuple):
    if hangi_Kitap in kutuphane:
        return True
    else:
        return False

def KitapCikar(hangi_Kitap:tuple):
    if kitapVarmi(hangi_Kitap):
        kutuphane.remove(hangi_Kitap)
        print(40*"-")
        print("Kitabınız çıkartıldı !\n",hangi_Kitap)
        print(40*"-")
        #print("Mevcut Kitaplar : \n",kutuphane)
    else:
        print("Kitap mevcut olmadığı için çıkarılamadı !")
        

def KitapEkle(hangi_Kitap):
    kutuphane.append(hangi_Kitap)
    print(40*"+")
    print("Eklenen Kitap : \n",hangi_Kitap)
    print(40*"+")
    

def MevcutKitap(kutuphane):
    print(50*"=")
    print("Mevcut Kitaplar : \n",kutuphane)
    print(50*"=")

MevcutKitap(kutuphane)
KitapCikar(kitap1)
KitapEkle(kitap2)
MevcutKitap(kutuphane)
import os

kitapListe=list()

menu="""
[1] Kitap Ekle
[2] Kitap Al
[3] Tümünü Listele
[Q] Çıkış

"""
def kitapEkle(kitap:tuple,liste:list):
    liste.append(kitap)
    print("Ekleme işlemi tamamlandı.")
    print("Ana menüye dönmek için 'enter' e basınız.")
    input()

def kitapKontrol(kitap:tuple,liste:list):
    if kitap in liste:
        return True
    else:
        return False

def kitapCikar(kitap:tuple,liste:list):
    if kitapKontrol(kitap,liste):
        liste.remove(kitap)         #Kitap Çıkartılıyor.
        print("Kitap çıkarma işlemi tamamlandı.")
        print("Ana menüye dönmek için 'enter' e basınız.")
        input()
    else:
        print("Arattığınız Kitap Mevcut değildir.")
        print("Ana menüye dönmek için 'enter' e basınız.")
        input()
        
def listele(liste:list):
    for i in liste:
        print("Kitap Adı: {}    =>>     Yazar Adı: {}".format(i[0],i[1]))
        print("Ana menüye dönmek için 'enter' e basınız.")
        input()
        
        
while True:
    os.system("cls")  # clear yerine cls yazılabilir
    print(menu)
    
    secim=input("İşleminizi Seçiniz: ")
    
    if secim=="1":
        kitap_adi=input("Kitabın Adı: ")
        kitap_yazar=input("Yazarın Adı: ")
        kitap=(kitap_adi,kitap_yazar)
        kitapEkle(kitap,kitapListe)  # Kitap Ekleniyor..
        
    elif secim=="2":
        kitap_adi=input("Kitabın Adı: ")
        kitap_yazar=input("Yazarın Adı: ")
        kitap=(kitap_adi,kitap_yazar)
        kitapCikar(kitap,kitapListe)  # Kitap Çıkarılıyor..
    
    elif secim=="3":
        listele(kitapListe)
        
    elif secim=="q" or secim=="Q":
        print("Keyifli Okumalar :) ")
        quit()
    else:
        print("Hatalı Giriş Yaptınız! ")
        
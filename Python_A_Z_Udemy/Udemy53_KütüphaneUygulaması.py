kitapListesi=list()

menü ="""
[1] Kitap Ekle
[2] Kitap Çıkar
[3] Kitapları Listele
[Q] Çıkış

"""
def kitapEkle(kitap,liste):
    liste+=[kitap]
    print("Kitap Eklendi'")
    input("Ana menüye dönmek için 'enter' e basınız.")

def kitapCikar():
    pass

def listele(liste):
    for i in liste:
        print("Kitap Adı ----->>>>>    {}".format(i))
    input("Ana menüye dönmek için 'enter' e basınız. ")

def cik():
    quit()

while True:
    print(menü)
    secim=input("Seçiminiz: ")
    
    if secim=="1":
        kitapAdi=input("Kitap Adi: ")
        kitapEkle(kitapAdi,kitapListesi)
        
    elif secim=="2":
        kitapCikar()
    
    elif secim=="3":
        listele(kitapListesi)
    
    elif secim=="q" or secim=="Q":
        cik()
    
    else:
        print("Hatalı Girdiniz !")
        print("Ana menüye dönmek için 'enter' e basınız!")
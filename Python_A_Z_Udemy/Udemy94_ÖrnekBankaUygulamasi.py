from os import system as komut
from re import S

class Musteri():
    def __init__(self,ID,PAROLA,ISIM):
        self.isim=ISIM
        self.id=ID
        self.parola=PAROLA
        self.bakiye=0

class Banka():
    def __init__(self):
        self.musteriler=list()
    
    def musteri_ol(self,ID:str,PAROLA:str,ISIM:str):
        self.musteriler.append(Musteri(ID,PAROLA,ISIM))
        print("Bankamıza Kayıt Oldunuz .")

# while kullanmak yerine modül modül yazmak daha güzel ve verimli olur.

def main(): # Her işlem buraya yazılacak.
    banka = Banka()
    while True:
        komut("cls") # ekranı temizlemek için
        print("""
              [1] Banka Müşterisiyim
              [2] Banka Müşterisi Olmak İstiyorum
              """)
        secim = input("Seçiminiz : ")
        
        if secim == "1":
            IDs=[i.id for i in banka.musteriler] # kısaca liste üretme yöntemi
            ID=input("ID :") # direkt IDler çekildi,kimin olduğu suanda bilinmiyor
            if ID in IDs: # Kullanıcının girdiği ID bankanın IDs ıd'lerinde varsa müşteri var 
                for musteri in banka.musteriler:
                    if ID==musteri.id: # Müşteri bulundu.
                        print("Hoşgeldiniz {}".format(musteri.isim))
                        parola=input("Parolanız : ")
                        if parola == musteri.parola:
                            print("Giriş Başarılı")
                            while True:
                                komut("cls") # ekran temizleme
                                print("""
                                    [1] Bakiye Sorgula
                                    [2] Kendi Hesabıma Para Yatırma
                                    [3] Başkasının Hesabına Para Yatırma
                                    [4] Para ÇEK
                                    [Q] Çıkış
                                    """)
                                secim2 = input("İşleminiz : ")
                                
                                if secim2=="1":
                                    print("Bakiyeniz : {}".format(musteri.bakiye))
                                    input("Ana menüye dönmek için 'enter'e basın.")
                                    
                                elif secim2=="2":
                                    miktar=int(input("Miktar : "))
                                    onay=input("Kendi Hesabınıza {} TL para yatırma işleminizi onaylıyor musunuz ? : E/H\n".format(miktar))
                                    input("Ana menüye dönmek için 'enter'e basın.")
                                    if onay =="E" or onay =="e":
                                        musteri.bakiye+=miktar
                                        print("Para yatırma işlemi BAŞARILI !")
                                        input("Ana menüye dönmek için 'enter'e basın.")
                                    elif onay=="h" or onay =="H":
                                        print("İşlem iptal edildi ! ")
                                        input("Ana menüye dönmek için 'enter'e basın.")
                                    else:
                                        print("Parola hatalı ! ")
                                        input("Ana menüye dönmek için 'enter'e basın.")
                                
                                elif secim2=="3":
                                    arananID=input("Müşteri ID : ")
                                    if arananID in IDs:
                                        for digerMusteri in banka.musteriler:
                                            if arananID == digerMusteri.id:
                                                miktar=int(input("Miktar : "))
                                                if miktar <= musteri.bakiye:
                                                    onay=input("{} adlı müşterimize {} TL para yatırma işlemini onaylıyor musunuz ? E/H\n".format(digerMusteri.isim,miktar))
                                                    if onay =="e" or onay=="E":
                                                        digerMusteri.bakiye+=miktar
                                                        musteri.bakiye-=miktar
                                                        print("Para yatırma işlemi BAŞARILI !")
                                                        input("Ana menüye dönmek için 'enter'e basın.")
                                                    elif onay =="h" or "H":
                                                        print("İşlem iptal edildi ! ")
                                                        input("Ana menüye dönmek için 'enter'e basın.")
                                                    else:
                                                        print("Hatalı giriş .")
                                                        input("Ana menüye dönmek için 'enter'e basın.")
                                                else:
                                                    print("Bakiyeniz işlem için Yetersiz.")
                                                    input("Ana menüye dönmek için 'enter'e basın.")
                                    else:
                                        print("Müşteri Bulunamadı !")
                                        input("Ana menüye dönmek için 'enter'e basın.")
                                    
                                elif secim2=="4":
                                    miktar=int(input("Miktar : "))
                                    if miktar<= musteri.bakiye:
                                        musteri.bakiye-=miktar
                                        print("Para çekme işlemi gerçekleşiyor.")
                                        input("Ana menüye dönmek için 'enter'e basın.")
                                    else:
                                        print("Bakiyeniz yetersiz. Para çekme işlemi iptal ediliyor.")
                                        input("Ana menüye dönmek için 'enter'e basın.")
                                elif secim2=="q" or secim2=="Q":
                                    break
        elif secim=="2":
            ID=input("ID : ")
            ISIM=input("İsmini : ")
            PAROLA=input("Parolanız : ")
            banka.musteri_ol(ID,PAROLA,ISIM)
                                            
if __name__=="__main__":
    main()
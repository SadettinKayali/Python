import os

masalar=dict()
for i in range(10):
    masalar[i]=0


def hesapEkle():
    masaNumarası=int(input("Masa Numarası : "))
    gecerliUcret=masalar[masaNumarası]
    ucretEkle=float(input("Eklenecek Ücret : "))
    toplamUcret=gecerliUcret+ucretEkle
    masalar[masaNumarası]=toplamUcret
    print("Hesap Ekleme işlemi tamamlandı. Ana menü için 'enter' !")
    
    
def hesapSil():
    masaNumarası=int(input("Masa Numarası : "))
    gecerliUcret=masalar[masaNumarası]
    ucretSil=float(input("Silinecek Ücret : "))
    toplamUcret=gecerliUcret-ucretSil
    if toplamUcret<0:
        print("Masa ücreti '-' olamaz. ! İşlemi kontrol edin ! Başa dönmek için 'enter'")
    else:
        masalar[masaNumarası]=toplamUcret
        print("Hesap Silme işlemi tamamlandı. Ana menü için 'enter' !")

def hesapKontrol(dosyaAdi):
    #hesapKontrol("Kayitlar.txt")
    try:
        dosya=open(dosyaAdi)
        veriler=dosya.read()
        veriler=veriler.split("\n") # listenin son öğesi boş olcak
        veriler.pop() # Bu komut ile o boşluğu siliyoruz.
        dosya.close()  # okunan dosyayı geri kapatmak lazım
        flag=True # Dosya varmış ve veriler adında liste bulunuyor
    except FileNotFoundError:
        dosya=open(dosyaAdi,"w") # dosya yoksa yazdıracak
        dosya.close()
        flag=False # Dosya yokmuş ve dosya oluşturuluyor.
        print("Dosya ilkkez açıldı. Kayıt Dosyası Oluşturuldu.")
    
    if flag: # Dosya varsa güncellenmiş oluyor
        for i in enumerate(veriler): # demet olarak veri gönderiyor. 0dan başlayarak kaç öğe varsa numara veriyor. 1. indisine aşağıdan çektiği değeri veriyor
            masalar[i[0]]=float(i[1]) # demetin 1. sayısı masaları okurken ilk öğe olacağı için 1.sine eşitlendi.
            
    else: # dosya yoksa bişey yapılmıyor yukarıda verilen 0 değerleri geçerli oluyor.
        pass
def kayitGuncelle():
    dosya=open("Kayitlar.txt","w")
    for i in range(10):
        ucret=masalar[i]
        ucret=str(ucret)
        dosya.write(ucret+"\n")
    dosya.close()

def main():
    hesapKontrol("Kayitlar.txt")
    while True:
        os.system("cls")   # windows için cls diğerlerinde clear
        print("""
            [1] Masaları Görüntüle
            [2] Hesap Ekle
            [3] Hesap Sil
            [Q] Çıkış
            
            """)
        
        secim=input("İşlemi seçiniz : ")

        if secim == "1":
            for i in range(10):
                print("Masa {} için hesap : {}".format(i,masalar[i]))
            print("İşlem tamamlandı. Ana menü için 'enter' !")
            input()
            
    #main()  # Programı çalıştırmak için (1.Kontrol)
        elif secim=="2":
            hesapEkle()
            #print("Hesap Ekleme işlemi tamamlandı. Ana menü için 'enter' !")
            input()
        elif secim=="3":
            hesapSil()
            #print("Hesap silme işlemi tamamlandı. Ana menü için 'enter' !")
            input()
        elif secim=="q" or secim=="Q":
            print("Çıkış Yapılıyor !")
            quit()

main()
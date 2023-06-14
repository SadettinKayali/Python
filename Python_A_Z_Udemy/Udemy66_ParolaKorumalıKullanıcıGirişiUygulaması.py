Kullanicilar={"Sadettin":"SadoRüm","KAYALI":"230416"}

isimler=Kullanicilar.keys()

KullaniciAdi=input("Kullanıcı Adı : ")

if KullaniciAdi in isimler:
    print("HOŞGELDİNİZ {}".format(KullaniciAdi))
    parola=input("Parolanız : ")
    if parola == Kullanicilar[KullaniciAdi]:
        print("Giriş Yapılıyor.")
    else:
        print("Parola Hatalı !")
else:
    print("Kullanıcı Bulunamadı ??")

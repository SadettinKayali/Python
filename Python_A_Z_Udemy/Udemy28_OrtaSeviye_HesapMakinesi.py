print("""
     \*=*=*=*=*=*=*=*=*=*=*/
      [1]   Toplama İşlemi
      [2]   Çıkarma İşlemi
      [3]   Çarpma İşlemi
      [4]   Bölme İşlemi
      [5]   Üs Alma
      [6]   Kök Alma
      [7]   Taban Bölme
      [8]   Mod Alma
      [Q]   ÇIKIŞ
     \*=*=*=*=*=*=*=*=*=*=*/
      """)

giris=input("Seciminiz: ")  #input fonksiyonu string tipinde giriş degeri alir. 

if giris == "1":
    x=input("1. Sayı : ")
    x=float(x)
    y=input("2. Sayı :")
    y=float(y)
    
    print("İşlemin Sonucu : ",x+y)
elif giris == "2":
    x=input("1. Sayı : ")
    x=float(x)
    y=input("2. Sayı :")
    y=float(y)
    
    print("İşlemin Sonucu : ",x-y)
elif giris == "3":
    x=input("1. Sayı : ")
    x=float(x)
    y=input("2. Sayı :")
    y=float(y)
    
    print("İşlemin Sonucu : ",x*y)
elif giris == "4":
    x=input("1. Sayı : ")
    x=float(x)
    y=input("2. Sayı :")
    y=float(y)
    
    print("İşlemin Sonucu : ",x/y)
elif giris == "5":
    x=input("Taban : ")
    x=float(x)
    y=input("Üs :")
    y=float(y)
    
    print("İşlemin Sonucu : ",x**y)
elif giris == "6":
    x=input("Taban : ")
    x=float(x)
    y=input("Kök :")
    y=float(y)
    
    print("İşlemin Sonucu : ",x**(1/y))
elif giris == "7":
    x=input("1.Sayı : ")
    x=float(x)
    y=input("2.Sayı :")
    y=float(y)
    
    print("İşlemin Sonucu : ",x//y)
elif giris == "8":
    x=input("1.Sayı : ")
    x=float(x)
    y=input("2.Sayı :")
    y=float(y)
    
    print("İşlemin Sonucu : ",x%y)
elif giris=="q" or giris=="Q":
    print("Çıkılıyor...")
    quit()
else:
    print("Hatalı Giriş Yapıldı.\n Çıkış yapılıyor.")
    
    
    
    
    
    
    
    
    
    """dsadsadsa
    dsadsadsa
    """
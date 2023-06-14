Bolunen=float(input("Bölünen : "))
Bolen=float(input("Bölen : "))
#Bolen=float(input("Bölen : "))

try: # Yapılmasını istenen işlemleri gerçekleştirir.
    print("Try bölümü ilk olarak her zaman çalıştırılır.")
    print("Sonuç : ",Bolunen/Bolen)
except ZeroDivisionError:
    print("Except içerisindekiler ön görülebilir hatalara alternatif çözümler \noluşturmak veya ayırt etmek için kullanılabilir.")
    print("0'a bölüm tanımsızdır !")
    print("Gerçek Hata Ayrıca Yazdırılabilir. => ",ZeroDivisionError)
except TypeError :
    print("Except içerisindekiler ön görülebilir hatalara alternatif çözümler \noluşturmak veya ayırt etmek için kullanılabilir.")
    print("Veri tipi desteklenemiyor !")
finally:
    print("Buradaki işlem her koşulda gerçekleştirilir.")
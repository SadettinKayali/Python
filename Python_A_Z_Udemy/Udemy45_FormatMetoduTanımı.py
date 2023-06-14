"""
karakterler = "abcdçedfghıijklmnoöprsştuüvyz"
for i in karakterler:
    print("Bastırılan karakter : {}".format(i))
"""
   
"""
Konumlarını Belirleme
Sözcük Atama
:> Sağa yaslama ve Alan Ayırma
:< Sola yaslama ve Alan Ayırma
:^ Merkezde Alan Ayırma
:s yalnızca string ifade
:d yalnızca sayısal ifade   (decimal)
:b ikili sistemde karşılık  (binary)
"""
degisken1="Sadettin"
degisken2="KAYALI"

#1
ifade1="{} {}".format(degisken1,degisken2)
ifade2="{} {}".format(degisken2,degisken1)
print("Kullanım 1:")
print(ifade1)
print(ifade2)
print("*_______________*")

#2 Sırası önemlidir, 0 dan başlar ilerler
ifade1="{1} {0}".format(degisken1,degisken2)
ifade2="{0} {1}".format(degisken2,degisken1)
print("Kullanım 2:")
print(ifade1)
print(ifade2)
print("*_______________*")

#3 Değişkene ne atanırsa onu yazdırır sırası önemli değildir.
ifade1="{ad} {soyad}".format(soyad=degisken1,ad=degisken2)
ifade2="{soyad} {ad}".format(ad=degisken2,soyad=degisken1)
ifade3="{ad} {soyad}".format(ad=degisken2,soyad=degisken1)
ifade4="{soyad} {ad}".format(soyad=degisken1,ad=degisken2)
print("Kullanım 3:")
print(ifade1)
print(ifade2)
print(ifade3)
print(ifade4)
print("*_______________*")

#4 Sağa ve Sola Yaslama  aradaki farka dikkat
ifade1="|{:<15}|".format(degisken1)
ifade2="|{:>15}|".format(degisken2)
ifade3="|{:<15}|".format(degisken1,degisken2)
ifade4="|{:>15}|".format(degisken2,degisken1)
print("Kullanım 4:")
print(ifade1)
print(ifade2)
print(ifade3)
print(ifade4)
print("*_______________*")

#5
ifade1="|{:^15}|".format(degisken1)
ifade2="|{:^15}|".format(degisken2)
print("Kullanım 5:")
print(ifade1)
print(ifade2)
print("*_______________*")

#6
ifade1="{:s}".format(degisken1)
ifade2="{:d}".format(126)
ifade3="{:b}".format(126)
print("Kullanım 6:")
print(ifade1)
print(ifade2)
print(ifade3)
print("*_______________*")

"""
format() Metodunun Kullanım Biçimleri
Herhangi bir yöne veya merkeze konumlandırmak ve alan ayırmak:
string = "|{:<15}|".format("Volkan")
print(string)
|Volkan         |
Yukarıda görüldüğü gibi string sola yaslanmış biçimde fakat string için ayrılan bölme 15 birim.

string = "|{:>15}|".format("Öğrenciler")
print(string)
|     Öğrenciler|
Yine yukarıda görüldüğü gibi string sağa yaslanmış biçimde fakat string için ayrılan bölme 15 birim.

Sıra belirleme:
string = "{} {}".format("isim","soyisim")
print(string)
isim soyisim
string = "{1} {0}".format("isim","soyisim")
print(string)
soyisim isim
Görüldüğü gibi değişkenlerin geleceği sıraları ayarlayabiliyoruz.

İsim Verme:
string = "{ad} {soyad}".format(soyad = "ATATÜRK",ad = "Mustafa Kemal")
print(string)
Mustafa Kemal ATATÜRK
Sıra ile yazmak mecburiyetinde değiliz, istersek değişken gibi isim verebiliyoruz.

String Zorunluluğu:
string = "bu bir string {:s}".format(str(12))
Bunda hata almazken şunda alırız:

string = "bu bir string {:s}".format(12)
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-11-c24a602ab5d9> in <module>()
----> 1 string = "bu bir string {:s}".format(12)

ValueError: Unknown format code 's' for object of type 'int'
Sayı Zorunluluğu:
string = "burada sayı var {:d}".format(25)
Tabi eğer şöyle yazarsak hata alırız:

string = "burada sayı var {:d}".format(str(25))
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-13-fb6a66e6a1fa> in <module>()
----> 1 string = "burada sayı var {:d}".format(str(25))

ValueError: Unknown format code 'd' for object of type 'str'
ASCII tablosundaki karşılıklar:
string = "--->>  {:c}".format(65)
print(string)
--->>  A
0 ile 256 arası sayıların ASCII tablosundaki karşılıklarını temsil eder.

Sekizlik sistemdeki karşılıklar:
string = "{:o}".format(16)
print(string)
20
Onaltılık sistemdeki karşılıklar:
string = "{:x}".format(42)
print(string)
2a
Eğer büyük 'X' harfi kullanırsak harfler büyük gösterilir:

string = "{:X}".format(42)
print(string)
2A
İkilik sistemdeki karşılıklar:
string = "26 sayısının ikilik karşılığı -->> {:b}".format(26)
print(string)
26 sayısının ikilik karşılığı -->> 11010
Sayıları basamaklarına ayırma:
string = "{:,}".format(2136238213621)
print(string)
2,136,238,213,621
"""

print("\a")
print("Bip Sesi")
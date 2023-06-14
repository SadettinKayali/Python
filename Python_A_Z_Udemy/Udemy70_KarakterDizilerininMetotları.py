string = "volkan"
string = string.replace("v","V")  #Bu metot sayesinde bir string içerisinde istediğimiz karakterler yerine yenilerini koyabiliyoruz.
print(string)

string = "İstanbul Büyükşehir Belediyesi"
bolunmus = string.split(" ") # String ifadeyi, parametre içerisinde verilen öğenin bulunduğu yerlerden böldü.
print(bolunmus)

bolunmus = string.split(" ",1) # İkinci parametrede kaç kez bölme işlemi uygulanacağını belirleyebiliyoruz. Fakat dikkat edilmesi gereken şey şudur: iki bölme işlemi uygulandığında ortaya üç adet öğe çıkacaktır.
print(bolunmus)
string = "bu bir denemedir bu bir denemedir"
bolunmus = string.split(" ",2) # İkinci parametrede kaç kez bölme işlemi uygulanacağını belirleyebiliyoruz. Fakat dikkat edilmesi gereken şey şudur: iki bölme işlemi uygulandığında ortaya üç adet öğe çıkacaktır.
print(bolunmus)

string = "İstanbul Büyükşehir Belediyesi"
bolunmus = string.rsplit(" ",1) # rsplit() Metodunun tek farkı string ifadeyi sağdan sola doğru okumasıdır.
print(bolunmus)

metin = """Python programlama dili Guido Van Rossum adlı Hollandalı bir programcı
tarafından 90'lı yılların başında geliştirilmeye başlanmıştır. Çoğu insan, isminin
Python olmasına bakarak, bu programlama dilinin, adını piton yılanından aldığını
düşünür. Ancak zannedildiğinin aksine bu programlama dilinin adı piton yılanından
gelmez. Guido Van Rossum bu programlama dilini, The Monty Python adlı bir İngiliz
komedi grubunun, Monty Python's Flying Circus adlı gösterisinden esinlenerek
adlandırmıştır. Ancak her ne kadar gerçek böyle olsa da, Python programlama
dilinin pek çok yerde bir yılan figürü ile temsil edilmesi neredeyse bir gelenek
halini almıştır diyebiliriz."""

print(metin.splitlines()) # splitlines() Metodu ile bir metinsel ifadeyi satırlarına bölebiliriz.

print("BUNLAR BÜYÜKTÜR".lower()) # Büyük harfleri küçük harflere dönüştürmek için kullandığımız bir metot.
print("küçük harfler".upper()) # Küçük harfleri büyük yazdırmak için kullanılır.

print("küçük harfler".islower()) # Karakter dizisi içerisinde hiç büyük harf yer almıyorsa True döndürür.
print("Küçük mü".islower()) # Karakter dizisi içerisinde hiç büyük harf yer almıyorsa True döndürür.

print("küçük harfler".isupper()) # islower() Metodunun tam tersi görev görür.
print("BÜYÜK HARFLER".isupper()) # islower() Metodunun tam tersi görev görür.
print("KaRIŞIK".isupper())

bolunmus = "İstanbul Büyükşehir Belediyesi".split() 
print(bolunmus)
birleştirme_karakteri = " "
string = birleştirme_karakteri.join(bolunmus) # Görüldüğü gibi split ile ayırdığımız veya zaten ayrık olan sözcükleri join() metodu ile birleştirebiliyoruz.
print(string)

print("deneme".count("n")) #bir ifadenin string içerisinde kaç kez geçtiğini sorgular.
print("deneme".index("n")) # Bir ifadenin, karakter dizisi içerisinde geçen ilk konumunu döndürür. 
print("deneme.".rindex("n")) # rindex() ise sağdan sola doğru okuyarak ilk karşılaşılan konumu döndürür.

string = "deneme"
print(string.index("a")) # index() metotlarıyla tamamen aynı işi yapar fakat index() metotları, eğer string içerisinde aranan ifadeyi bulamazsa hata verir, find() metotları ise hata vermez.

print(string.find("a")) #  find() metotları ise hata vermez. find() metotları bu gibi durumlarda hata yerine -1 değerini döndürür.

print("deneme".isalpha()) # Bir string yalnızca alfabe karakterlerinden oluşuyorsa True döndürür.
print("dene3me".isalpha())

print("1234565".isdigit()) # Bir string yalnızca sayısal ifade içeriyorsa True değeri döndürür.
print("12434223f".isdigit())

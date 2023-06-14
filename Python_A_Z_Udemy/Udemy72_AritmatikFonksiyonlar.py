# abs()     : Mutlak değer olarak döndürür.
# divmod()  : Bölüm işlemi yaptıktan sonra (bölünen,bölen) =>(bölüm,kalan) verir. Demet olarak sonucu verir.
# max()     : Maksimum değeri bulur.
# min()     : Minimum değeri bulur.
# sum()     : Dizi içindeki tüm sayıları toplar.

print(divmod(40,12))
isimler=["Ali","Ayşe","Süleyman","Sadettin","Eymen","Eyşan","Hatice","RümeysamKarağac"]
print(max(isimler,key=len))  # isimler listesinde anahtar kelime key=len (uzunluk) olacak şekilde maximum uzunluktaki ilk ismi ve indisi en düşük olanı bulur
print(min(isimler,key=len))  # isimler listesinde anahtar kelime key=len (uzunluk) olacak şekilde minimum uzunluktaki ismi bulur

sayılar=[1,2,3,4,5,6,7,8,9]
print(sum(sayılar))
print(sum(sayılar,5)) # ek parametre eklenebiliyor.

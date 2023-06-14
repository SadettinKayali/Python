"""
is işleci
id fonksiyonu
"""

a=5
b=5
print("ıd fonksiyonu sonucu")
print(id(a))
print(id(b))
print(id(5))
if a==b:
    print("----------------------")
    print("Aynı")
    print("İçeriğini kontrol eder")
    print("----------------------")
if a is b:
    print("**********************")
    print("Aynı")
    print("ID kontrol eder")
    print("**********************")   
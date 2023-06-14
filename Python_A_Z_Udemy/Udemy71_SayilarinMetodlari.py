# int 
# bit_length()          # : bit uzunluğu
sayi=5
print(sayi.bit_length())  # sonuç olarak binary sistemde yazılışını gösteriyor : 5 = 101

# float
# as_integer_ratio()    # : bölüm sonucu çıkması için gereken tam sayıları verir
# is_integer()          # : sayı tam sayı ise True döndürür

sayi=4.5
print(sayi.as_integer_ratio())  # bölüm sonucunu verecek sayıların oranını veriyor. 4.5 için (9,2)
sayi=4.0
print(type(sayi))  # veri tipi normalde float
print(sayi.is_integer()) # tam sayı olduğu için 4.0 , o yüzden True değeri veriyor

# Karmaşık sayılar
# imag                  # : Complex sayıların sanal kısmını verir
# real                  # : Complex sayıların reel kısmını verir.

karmaşık= 12+4j
print(type(karmaşık))
print(karmaşık.real)
print(karmaşık.imag)
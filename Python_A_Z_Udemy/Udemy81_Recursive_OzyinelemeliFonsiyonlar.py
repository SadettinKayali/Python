# Recursive - Özyinelemeli Fonksiyonlar, fonksiyonu kendi içerisinde döngüye almak.

def faktoriyel(sayi):
    if sayi==1:
        return 1
    else:
        return sayi*faktoriyel(sayi-1)
    
print(faktoriyel(6))
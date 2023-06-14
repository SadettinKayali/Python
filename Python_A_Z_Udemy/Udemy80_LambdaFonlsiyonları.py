## Fonksiyon oluşturma 1 standart 
def ucgenmi(a,b,c):
    if a**2+b**2==c**2:
        return True
    else:
        return False
    
## Fonksiyon oluşturma 2 İdeal
fonksiyon=lambda a,b,c : a**2+b**2==c**2
print(fonksiyon(2,3,4))

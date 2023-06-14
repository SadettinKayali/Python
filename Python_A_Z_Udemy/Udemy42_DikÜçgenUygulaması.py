def dikücgen(Taban,Yükseklik,Hipotenüs):
    if Taban**2+Yükseklik**2==Hipotenüs**2:
        return "Bu bir dik üçgendir."
    else:
        return "Bu bir dik üçgen değildir."
    
print("3,5,7 dik üçgen mi ?\n",dikücgen(3,5,7))
print("3,4,5 dik üçgen mi ?\n",dikücgen(3,4,5))
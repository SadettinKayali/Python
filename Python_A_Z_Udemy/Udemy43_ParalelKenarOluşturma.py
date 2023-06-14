def sagSlas(adet):
    for i in range(int(adet)):
        print("/",end="")


def solSlas(adet):
    for i in range(int(adet)):
        print("\\",end="")

def satirAtla(adet):
    for i in range(int(adet)):
        print()

def bosluk(adet):
    for i in range(int(adet)):
        print(" ",end="")

def ustKisim(cap):
    UstBaslangicBosluk=cap/2-1
    for i in range(int(cap/2)):
        bosluk(UstBaslangicBosluk-i)
        sagSlas(1)
        bosluk(i*2)
        solSlas(1)
        satirAtla(1)

ustKisim(10)

def altKisim(cap):
    AltBaslangicBosluk=cap-2
    for i in range(int(cap/2)):
        bosluk(i)
        solSlas(1)
        bosluk(AltBaslangicBosluk-i*2)
        sagSlas(1)
        satirAtla(1)

altKisim(10)

def paralelkenar(cap):
    ustKisim(cap)
    altKisim(cap)

paralelkenar(20)
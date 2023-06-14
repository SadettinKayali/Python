# birbirlerine bağlı yeni classlar oluşturulabilir. Inheritance, parent child ilişkisi
class Tasit():
    def __init__(self,tekerSayisi,kapiSayisi):
        self.tekerSayisi=tekerSayisi
        self.kapiSayisi=kapiSayisi
    
    def kapiAc():
        print("Kapı Açıldı ")

class Tir(Tasit):
    def __init__(self,tekerSayisi,kapiSayisi,turboSayisi):
        super().__init__(tekerSayisi,kapiSayisi)
        self.turboSayisi=turboSayisi
    
    
    def dorseBirak():
        print("Dorse Bırakıldı.")
tir=Tir(4,2,1)
print("Araç Tipi Tır : Kapı Sayısı : {} -- Teker Sayısı : {} -- Turbo Sayısı : {} ".format(tir.kapiSayisi,tir.tekerSayisi,tir.turboSayisi))

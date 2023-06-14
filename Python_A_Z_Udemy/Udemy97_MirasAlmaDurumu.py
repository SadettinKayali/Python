class Tasit():
    def __init__(self,tekerSayisi,kapiSayisi):
        self.tekerSayisi=tekerSayisi
        self.kapiSayisi=kapiSayisi

class Araba(Tasit):
    pass

araba=Araba(4,4)
print("Araçtaki Teker Sayısı : ",araba.tekerSayisi)
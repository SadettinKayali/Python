"""
sozluk={
    "home":"ev",
    "book":"kitap",
    "pen" :"kalem"
}
print(sozluk)
print(sozluk["book"])
print(sozluk["home"])
print(sozluk["pen"])

"""
karakter1 ={
    "Adı"   : "Sadettin",
    "Görevi": "Savaşçı" ,
    "Güç"  : 100        ,
    "Silah" : "Kılıç"   ,
    "Can"   : 100       ,
        }
karakter2 ={
    "Adı"   : "KAYALI",
    "Görevi": "OKÇU"  ,
    "Güç"  : 60       ,
    "Silah" : "OK"    ,
    "Can"   : 100     ,
        }
def hasar(alınan:dict,verilen:dict):
    eksilen=alınan["Güç"]
    verilen["Can"]=verilen["Can"] - eksilen

hasar(karakter1,karakter2)
hasar(karakter2,karakter1)

print("Karakter1 Canı: ",karakter1["Can"])
print("Karakter2 Canı: ",karakter2["Can"])
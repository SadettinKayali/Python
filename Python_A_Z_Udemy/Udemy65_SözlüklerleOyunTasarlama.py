Zırhlar={"Demir":10,"Çelik":20}
Karakterler={
    "Savasci" : {"Silah":"Kılıç","Güç":30,"Sağlık":100,"Zırh":Zırhlar["Çelik"]},
    "Okcu" : {"Silah":"OK","Güç":30,"Sağlık":100,"Zırh":Zırhlar["Demir"]},
}

def Saldırı(Saldıran,SaldırıyaUgrayan):
    Guc=Saldıran["Güç"]
    Saglık=SaldırıyaUgrayan["Sağlık"]
    Zırh=SaldırıyaUgrayan["Zırh"]
    Hasar=Guc-Zırh
    Saglık-=Hasar
    SaldırıyaUgrayan["Sağlık"]=Saglık

print("Okçu Sağlığı :",Karakterler["Okcu"]["Sağlık"])
Saldırı(Karakterler["Savasci"],Karakterler["Okcu"])
print("Okçu Sağlığı :",Karakterler["Okcu"]["Sağlık"])
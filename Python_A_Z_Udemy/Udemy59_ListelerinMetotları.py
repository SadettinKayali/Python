"""
liste=["İnce Memed","Simyacı","Otomatik Portakal","Cemo"]
liste.append("Ruby")
liste.append("C++")
liste.remove("Simyacı")
liste.append("C++")
def listele(liste):
    for i in liste:
        print(i)
        

listele(liste)
print(liste.count("Simyacı"))
print(liste.count("C++"))

"""
def listele(liste):
    for i in liste:
        print(i)
"""
liste1=["İnce Memed","Simyacı","Otomatik Portakal","Cemo"]
liste2=liste1
print("Durum 1 :")
print(liste1)
print(liste2)
print(20*"=*")

liste1.remove("İnce Memed")
liste1.remove("Simyacı")
liste1.append("Bla Bla")
liste2.append("sadettin")

print("Durum 2 :")
print(liste1)
print(liste2)
print(20*"*=")


liste1=["İnce Memed","Simyacı","Otomatik Portakal","Cemo"]
liste2=liste1.copy()
        
print("Durum 3 :")
print(liste1)
print(liste2)
print(20*"=*")

liste1.remove("İnce Memed")
liste1.remove("Simyacı")
liste1.append("Bla Bla")
liste2.append("sadettin")

print("Durum 4 :")
print(liste1)
print(liste2)
print(20*"*=")
"""
liste=["İnce Memed","Simyacı","Otomatik Portakal","Cemo","Simyacı"]
sıra=liste.index("Otomatik Portakal")
print(sıra+1,". Sıradaki")

Numaralar=[5,4,8,9,6,3,2,55,7,7,88,1,1,1,444,6,5,55,588,566,52]
print(Numaralar)

Numaralar.sort()
print(Numaralar)

Sayılar=set(Numaralar)
print(Sayılar)
"""
Liste=[]
Liste=list()

string= ""
string= str()

"""
"""
kitapListe=["abc",12,10.5]
for i in kitapListe:
    print(type(i))

kitapListe=["İnce Memed","ENDGAME","Efendi","Cemo","Python","C++"]
for i in kitapListe:
    print("Kitabın Adı: {}".format(i))

eklenecek=input("Kitap adı: ")
kitapListe+=[eklenecek]
print(kitapListe)

"""

# Sözlük metodları
"""
for i in dir(dict()):
    if "__"not in i:
        print(i)
        
clear
copy
fromkeys
get
items
keys
pop
popitem
setdefault
update
values

"""
sozluk={"book":"kitap",
        "computer":"bilgisayar",
        "phone":"telefon",
        "pen":"kalem"}

#s=input("Sorgu: ") 
#print(sozluk.get(s,"Aratılan Kelime Bulunamadı !"))

for i in sozluk.items():
    print(i)
    
# [print(i) for i in sozluk.items()]

for i in sozluk.values():
    print(i)

[print(i) for i in sozluk.values()]

sozluk2=sozluk.copy()
print(sozluk2)
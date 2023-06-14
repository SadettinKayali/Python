"""
[] : liste
{} : sözlük
() : demet
"" : string
12 : sayı
set() :  küme     kümenin belirteci yok
Her elemandan sadece bir tane olabilir 
"""
"""
string="wdasdwadsadwdaw"
kume=set(string)
print(kume)
print(type(kume))
for i in dir(kume):
    if "__" not in i:
        print(i)

ans:
{'w', 's', 'a', 'd'}
<class 'set'>
add                     EKLEMEK
clear                   TEMİZLEMEK/BOŞALTMAK
copy                    KOPYALAMAK
difference              FARK
difference_update       
discard                 ÇIKARTMAK
intersection            KESİŞİM
intersection_update
isdisjoint
issubset
issuperset
pop
remove                  KALDIRMAK
symmetric_difference
symmetric_difference_update
union
update

kume=set([1,2,3,4,5])
kume.add("deneme")
print(kume)
kume.discard(5)
print(kume)
kume.discard(5)
print("Normalde hata vermeli ama vermiyor",kume)
kume.remove(2)
print(kume)

kume.remove("2")
print("Hata vericek",kume)
"""
a=set([1,2,4,5])
b=set([2,4,5,6,7,8])
print("A Kümesi : ",a)
print("B kümesi : ",b)
print(25*"=")

print("A nın B den farkı : ",a.difference(b))
print("B nin A dan farkı : ",b.difference(a))

b.difference_update(a)
print("Güncellenmiş B Kümesi :",b)

a=set([1,2,4,5])
b=set([2,4,5,6,7,8])
c=b.intersection(a)
print("C Kümesi A ve B nin Kesişim Kümesi : ",c)
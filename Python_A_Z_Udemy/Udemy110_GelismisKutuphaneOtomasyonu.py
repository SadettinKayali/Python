import sqlite3

VeriTabani=sqlite3.connect("kitaplar.sqlite")
imlec=VeriTabani.cursor()

menu="""
    [1] Kitap Ara
    [2] Yazar Ara
"""
print(menu)

islem=input("İşleminiz : ")

if islem=="1":
    isim=input("Kitap Adı : ")
    sorgu="SELECT  * FROM 'kitaplik tablosu' WHERE kitap='{}'".format(isim)
    imlec.execute(sorgu)
    veriler=imlec.fetchall()
    for i in veriler:
        print(i)
if islem=="2":
    isim=input("Yazar Adı : ")
    sorgu="SELECT  * FROM 'kitaplik tablosu' WHERE yazar='{}'".format(isim)
    imlec.execute(sorgu)
    veriler=imlec.fetchall()
    for i in veriler:
        print(i)

VeriTabani.close()
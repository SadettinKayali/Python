import sqlite3

VeriTabani=sqlite3.connect("kitaplar.sqlite")
imlec=VeriTabani.cursor()

imlec.execute("SELECT * FROM 'kitaplik tablosu' WHERE yazar='Paulo Coelho'") # Kitaplık tablosundan bütün(*) verileri çek

veriler=imlec.fetchall() # hepsini seçer
#print(veriler)
for i in veriler:
    print(i)



VeriTabani.close()
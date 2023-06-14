import sqlite3

VeriTabani=sqlite3.connect("kitaplar.sqlite")
imlec=VeriTabani.cursor()

imlec.execute("SELECT * FROM 'kitaplik tablosu'") # Kitaplık tablosundan bütün(*) verileri çek

#veriler=imlec.fetchall() # hepsini seçer
#print(veriler)
#for veri in veriler:
    #print(veri)

print(imlec.fetchone()) 
print(imlec.fetchone())
print(imlec.fetchone()) # tek tek seçilebilir
print(imlec.fetchone())

print(imlec.fetchmany(5)) # kaç tane istenirse çekilebilir


VeriTabani.close()
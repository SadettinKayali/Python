import sqlite3
## VERİ TABANI OLUŞTURMA
#Dosya varsa bağlanıyor, yoksa oluşturuyor.
VeriTabani=sqlite3.connect("kitaplar.sqlite") # .sqlite uzantısı değiştirilebilir. belli olsun diye sqlite kullanıldı.

## İMLEÇ OLUŞTURMA
imlec=VeriTabani.cursor()



#VeriTabani.close()
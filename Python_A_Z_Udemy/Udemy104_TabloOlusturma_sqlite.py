import sqlite3

VeriTabani=sqlite3.connect("kitaplar.sqlite")

imlec=VeriTabani.cursor()
imlec.execute("CREATE TABLE kitaplik (yazar,kitap)")
# Eğer tablo birkere oluşturulduysa birdaha oluşturmaz hata verir.
# rm *sqlite  # terminale yazılarak sqlite ile oluşturulmuş olanlar kaldırılır (remain)
# SQLite uygulamasına girilerek tablo görüntülenebiliyor.

VeriTabani.close()
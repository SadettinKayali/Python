import sqlite3

VeriTabani=sqlite3.connect("kitaplar.sqlite")

imlec=VeriTabani.cursor()
imlec.execute("CREATE TABLE IF NOT EXISTS kitaplik (yazar,kitap)") 
# Eğer tablo birkere oluşturulduysa birdaha oluşturmaz hata verir.
# IF NOT EXIST ifadesini yazarsak hatadan kurtuluruz.
# Başlıklar tablo başlığı sütun başlığı birden fazla kelime içeriyorsa birleşik yazılmalı veya 'içerisine' yazılmalıdır.
# SQLite uygulamasına girilerek tablo görüntülenebiliyor.

VeriTabani.close()
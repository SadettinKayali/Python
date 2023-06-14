import sqlite3
from ssl import VerifyFlags

VeriTabani=sqlite3.connect("kitaplar.sqlite")

imlec=VeriTabani.cursor()
imlec.execute("CREATE TABLE IF NOT EXISTS 'kitaplik tablosu' (yazar,kitap)") 
# Eğer tablo birkere oluşturulduysa birdaha oluşturmaz hata verir.
# IF NOT EXIST ifadesini yazarsak hatadan kurtuluruz.
# Başlıklar tablo başlığı sütun başlığı birden fazla kelime içeriyorsa birleşik yazılmalı veya 'içerisine' yazılmalıdır.
# SQLite uygulamasına girilerek tablo görüntülenebiliyor.

imlec.execute("INSERT INTO 'kitaplik tablosu' VALUES ('Yaşar KEMAL','Fırat Suyu Kan Akıyor')") # Her çalıştırmada tekrar kaydetmeye devam ediyor. Üzerine yazmıyor kaldığı yerden devam ediyor.
VeriTabani.commit() # tabloya işlenmesini sağlıyor.

VeriTabani.close()
"""
# Dosya Okuma:
## dosya=open("Dosya Konumu","r") (read)
dosya=open("Dosya Konumu") # Dosya mevcut konumundan açılıyor.
veri=dosya.read() # Dosya okunuyor ve bir değişkene atanıyor.
dosya.close()   # Dosyayı kapatmak şart değil lakin büyük programlarla uğraşırken RAM tasarrufu için güzel olabilir.
print(veri)  # açılan dosyada okunuyor ve veri yazdırılıyor.

# Dosya Oluşturma:

dosya=open("deneme.txt,"w") (write)
dosya.close()

# eğer dosya mevcut ise o dosya siliniyor ve baştan kaydediliyor.

"""

"""
# Dosyaya Yazma:
dosya=open("deneme.txt,"w") (write)
yazılacaklar="Yazılması istenenler"
dosya.write(yazılacaklar)
dosya.close()

"""

"""
# Dosya Okuma2:
dosya=open("OKUNACAKLAR.txt","r")
okunan=dosya.readlines() # her satırı tek tek okur ve \n şeklinde ayırır. Düzenlemek için ayrıca işlem gerekir.
print(okunan)
dosya.close

"""
"""
# Dosyaya erişim ve işlem

'r' : OKUMA

'w' : YAZMA ( dosydaki siler ve istenileni yazar)
'a' : YAZMA ( dosyada silme işlemi yapmaz, üzerine yazmaya devam eder.)
'x' : YAZMA ( dosya bulunmuyorsa yazdırır,dosya bulunuyorsa hata verir dosyayı silmez)

'r+' : OKUMA ve YAZMA (dosyanın varolması lazım,okuma yazma yapar)
'w+' : OKUMA ve YAZMA (dosyayı yaratabilir, varsa siler ve baştan yazar,okuma yapar)
'a+' : OKUMA ve YAZMA (dosyayı okur ve yazdırır, dosya içeriğini silmez)
'x+' : OKUMA ve YAZMA (dosyayı okur ve yazar, dosya varsa hata verir.)



"""
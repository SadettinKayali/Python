rehber= { 
    "Karakter1" :{
        "Ev Adresi"   :"Kütahya"        ,
        "İş Adresi"   :"İzmir"          ,
        "Ev Telefonu" :"0546759431"     ,
        "İş Telefonu" :"054697523132"   ,
        "Cep Telefonu":"0254632979"      }}

# Rehberdeki isimleri .key() yardımıyla isimler değişkenine topluyor
isimler=rehber.keys()
# Aranan kişi ismi kullanıcıdan input olarak alınıyor.
arananKisi=input("Aranan İsim : ")
#Eğerki aranan kişi isimler değişkeninde bulunuyorsa işleme devam ediliyor.
if arananKisi in isimler:
    flag = True
else:
    flag = False
# Yukarıdaki if else bloğunda flag True ise rehberde arananKisi inputunua arananOzellik inputu ile giriş yapılıyor
# Bu işlemin sebebi üst üste get kullanılabildiğinden ve .get() komutu kendinden önceki ifadeyi str tipinde kabul ettiği için olası hataların önüne geçmek
arananOzellik=input("Aranan Bilgisi : ")
if flag:
    print(rehber.get(arananKisi).get(arananOzellik,"Bilgi BUlunamadı"))
else:
    print("Aranan Kişi Rehberde Bulunamadı !")



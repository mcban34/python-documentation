
#!python sitesinden
#!3.8.2 versiyonunu indiriyoruz
#!executable versiyonu!

# !mesaj vermek
# print("hello world")

# print("hello","world") #?ayrı değişkenler

# print("hello" + "world") #?birleştirme işlemi

# print("hello    " + "world") #?boşluğa duyarlı

# print("""selam

#       ben mehmet""")#?3 tırnak ise alt satırlara geçmek için duyarlıdır

# mesaj="selam python derslerine hoşgeldin!"
# print(mesaj)

# print("front-end","backend" , sep="--") #?sep iki farklı değişken arasına hangi işaretin koyulcağını belirler

# print("selamlar burası",end=" cümle sonu") #?end cümle sonuny belirler

# isim = "mehmet"
# print("selamlar ben"," " ,end=isim)

#! f ile değer çekmek
# isim = "mehmet"
# print(f'Selam {isim}, Hoşgeldin!')


# !yorum satırları
# ? yorum satırları # işareti ile verilir
# selam burası yorum satırı
# """3 tırnak ilede yorum satırı kullanılabilir"""


# !format metodu
# ?format metodu yer tutucu anlamına gelir ve değişkenleri yerlerine yerleştirir
# print("Selam benim adım {ad}".format(ad="mehmet"))

# marka="BMW"
# print("Benim arabamın markası : {}".format(marka))

# meslek="web dev."
# yil=2016;
# print("Benim mesleğim {}. Ben {} yılından beri yazılımla uğraşmaktayım".format(meslek,yil))


# isim="mehmet"
# soyisim="coban"
# print("selamlar ben {1} ve soyadım {0}".format(isim,soyisim)) #?değişkenlerin index numaralarıyla oynayıp yerlerini değiştirirebiliriz.


# print("{1} {3} {2} {0}".format("ben","python","öğrenmek","istiyorum"));

# print("selam benim adım: {ad}. Soyadım : {soyad}, ve ben {yas} yaşındayım".format(ad="mehmet",soyad="coban",yas=23))


#!değişken oluşturma
#?DEĞİŞKEN OLUŞTURMA KURALLARI

#? 1)Değişkenler sayı ile başlamaz!
# 1sayi = 20 #!hata

#? 2)DEĞİŞKENLER ARASINDA BOŞLUK BIRAKILMAZ
# girilen kullanici adi = "mehmet" #!hata

#? 3) DEĞİŞKENLER İÇERESİNDE ÖZEL KARAKTER KONULMAZ
# degisken$adi="mehmet" #!hata

#!doğru değişken oluşturma yöntemleri

# girilenIsim="mehmet"
# print(girilenIsim)

# girilen_yas = 23
# print(girilen_yas)

#!değişken atama işlemleri
# sayi = 20 #?int
# print(sayi)

# isim = "mehmet" #?string
# print(isim)

# sayi = 20
# sayi2 = 30
# print(sayi+sayi2)

# sayi = 20
# say2 = 10 + sayi
# print(say2)

# sayi = 20
# sayi = sayi + 1
# print(sayi)

# sayi = 20
# sayi = sayi + 10

# sayi = 20
# sayi = sayi - 20
# print(sayi)

# sayi = 5
# sayi +=10
# print(sayi)

# sayi = 5
  # sayi -= 3
# print(sayi)

#!ÇOKLU DEĞİŞKEN OLUŞTURMA
# x,y,z= 5,10,15 #?python ile çoklu bir şekilde değişken oluşturabilirsiniz!

# sinav1,sinav2,sinav3 = 50,70,90
# print(sinav1,sinav2,sinav3)

# sinav1,sinav2,sinav3 = 50,50,50
# print((sinav1+sinav2+sinav3) / 3)

#?alternatif olarak birden fazla değişkene aynı değeri verebiliriz
# a=b=c=d="kırmızı"
# print(a)


# a=b=c=d="kırmızı"
# print(a,b,c,d)


#!değişkenlerde type çeşitleri
#?int (sayısal)
#?string (sözel)
#?float (ondalıklı sayı)
#?tuple (string ifadelerin toplamı) #!arrayden farklı bir yapıdır içerisindeki değerleri değiştirmeden kullanırız
#?list (array mantığındaki yapılardır)
#?set (obje mantığındaki yapılardır {12,"python",23,"django"} key değerleri almazlar)
#?*Set öğeleri değiştirilemez, ancak öğeleri kaldırabilir ve yeni öğeler ekleyebilirsiniz.
#?dict (objelerdir {"ad":"mehmet","soyad":"coban"})


#?İNT
# sayi = 20
# print(type(sayi))

#?STRİNG
# metin = "selam burada metin yazıyor"
# print(type(metin))

#?örnek
#*değişken adına print veriniz ve içerine bir değer atınızö
#*ardından bu printi ekrana yazınız


#?FLOAT
# sayi = 1.25
# print(type(sayi))

#?tuple
# renkler = "sarı","mavi","pembe","yeşil","turuncu"
# print(type(renkler))

#*tupledan eleman çağırmak
# renkler = "sarı","mavi","pembe","yeşil","turuncu"
# print(renkler[0])

# ?list
# karisikList = ["a","b",23,44,"x","y",76]
# print(type(karisikList))

#?listedeki elemana ulaşma
# karisikList = ["a","b",23,44,"x","y",76]
# print(karisikList[0])

# karisikList = ["a","b",23,44,"x","y",76]
# elemanAl = karisikList[0]
# print(elemanAl)

#?set
# degerler = {"renkler","arabalar",23,44,55}
# print(type(degerler))

#?set değerleri değiştirilemez elemanlar olduğu için python
#?elemanlara tek tek ulaşmayı garanti etmez bunun için for yapısı kullanılabilir

# degerler = {"renkler","arabalar",23,44,55}
# for i in degerler:
#   print(i)

#?dict
# calisanlar = {
#   "isim":"mehmet",
#   "soyisim":"coban",
#   "yas":23
# }
# print(type(calisanlar))

#?dict(obje) içerisindeki veriye ulaşma
# calisanlar = {
#   "isim":"mehmet",
#   "soyisim":"coban",
#   "yas":23
# }

# print(calisanlar["isim"])

#?dict ve list yapısının iç içe kullanımı
# calisanlar = [
#   {
#     "isim":"mehmet",
#     "soyisim":"coban",
#     "yas":23
#   },
#   {
#     "isim":"burak",
#     "soyisim":"yalcin",
#     "yas":25
#   },
# ]

# print(calisanlar[1]["yas"])



#!OPERATÖR İŞLERMLERİ
#? +++++ (toplama)
#? ----- (çıkartma)
#? ***** (çarpma)
#? ///// (bölme)
#? %%%%% (mod alma)
#? ** (üs alma)

# print(5%2)

# print(10%5)

#!metinsel ve sayısal ifadelerde toplama

# sayi1=20
# sayi2=40
# toplam = sayi1 + sayi2
# print(toplam)

# sayi1="20"
# sayi2="40"
# toplam = sayi1 + sayi2

# print(toplam)
# isim="mehmet"
# soyisim="coban"
# toplam = isim+soyisim
# print(toplam)

# sayi1="20"
# sayi2=40
# toplam = sayi1 + sayi2
# print(toplam) #?int ve stirng bir değer toplamanamaz! typlerın aynı olması gerekmektedir

#? üs alma 
# sayi = 10
# sayi = sayi**3
# print(sayi)


#!değişkenlerde type  tipini değiştirmek
#?int()
# sayi = int("23")
# sayi2 = int("24")
# topla = sayi + sayi2
# print(topla)

# isim = int("mehmet")
# soyisim = int("coban")
# topla = isim + soyisim
# print(topla) #!HATA

# sayi =  int(45.65) #?ondalıklı sayıyı tam sayıya çevirdik
# print(sayi)

#?str()
# sayi = str(23)
# print(type(sayi))

# sayi1= str(10)
# sayi2 = str(20)
# print(sayi1+sayi2)

#!len
#?uzunluk kontrolü anlamına gelir (lenght)

# myList = [1,2,3,4,5,6,7,8,9]
# print(len(myList))

# myList = [1,2,3,4,5,6,7,8,9]
# myListLen = len(myList)
# print(myListLen)

# mesaj = "selam ben mehmet"
# print(len(mesaj))
 
# person = {
#   "ad":"mehmet",
#   "soyad":"coban"
# }
# length = len(person)
# print(length)

#!eval  
# x = "print(25)"
# eval(x) #?eval straing ifade içerisinde python kodu varsa derleyip çalıştırır

# y = "print(len('mehmet coban'))"
# eval(y)

# result = eval("2 + 3")
# print(result)

# result = eval("max(1,2,3)")
# print(result)


#!input
# test = input("testi giriniz")
# print(type(test)) #?inputdan gelen değerler stringdir

# isim = input("adınızı giriniz ")
# print("Hoşgeldin" + isim)

# kullaniciAdi = input("Kullanici Adiniz : ")
# sifreniz = input("Şifreniz : ")
# print("Hoşgeldin! Kullanıcı Adın : " + kullaniciAdi + "Şifren : " + sifreniz)

#?inputdan gelen değeri int çevirme
# x = input("bir sayı giriniz")
# x = int(x)
# print(type(x))

# x = int(input("bir sayi giriniz"))
# print(type(x))

#?örnekler
#*dışardan girilen ad soyad ve doğum tarihini print ile ekrana yazdır

# isim = input("adınızı giriniz : ")
# soyisim = input("soyadınızı giriniz : ")
# dogumTarihi = input("Doğum tarihinizi giriniz : ")
# print(isim,soyisim,dogumTarihi)

#*kullanıcın girdiği sayının 3 katını yazdırın
# sayi = input("bir sayı giriniz")
# sonuc = int(sayi) * 3
# print(sonuc)

#*kullanıcının girdiği sayının karesini alan program
# girilenSayi = int(input("Bir sayi giriniz :"))
# girilenSayi  = girilenSayi ** 2;
# print(girilenSayi)

#*girilen 3 sınavın ortalamasını alan uygulamayı yazını
# sın1 = int(input("1. Sınavı Giriniz : "))
# sın2 = int(input("2. Sınavı Giriniz : "))
# sın3 = int(input("3. Sınavı Giriniz : "))
# ort = (sın1 + sın2 + sın3) / 3
# print("Ortalamanız : " , ort)

#*kenar uzunluğu ve yüksekliği girilen üçgenin alanını hesaplayan programı yazınız ((k*h) / 2)
# kenarUzunlugu = int(input("Kenar uzunluğunu giriniz : "))
# yukseklik = int(input("Yüksekliği Giriniz : "))
# alan = (kenarUzunlugu * yukseklik) / 2
# print("Üçgenin Alanı : " , alan)

#*kısakenarın ve uzun kenarın girildiği dikdörtgenin çevresini hesaplayan programı yazınız ((kk+uk) * 2)
# kısaKenar = int(input("Kısa Kenarı Giriniz : "))
# uzunKenar = int(input("Uzun Kenarı Giriniz : "))
# cevre = (kısaKenar+uzunKenar) * 2
# print("Dikdörtgenin Çevresi : " , cevre)


#* vizenin %40 finalin %60 alınarak ortalamayı ekrana yazdıran program
# vize = int(input("Vize notunuzu giriniz : "))
# final = int(input("Final notunuzu giriniz : "))
# ortlama = (vize*0.4) + (final*0.6)
# print("Ortalamanız : " , int(ortlama))

#*kullanıcıdan alınan kullanıcı adının karakter uzunluğunu bulunuz
# kullaniciAdi  = input("Lütfen Kullanıcı Adınızı Giriniz : ")
# print(len(kullaniciAdi))

#* kullanıcıdan alınan kilo ve boy ile vücut kitle indeksini hesaplayını/// kilo=50 boy=1.55 (kilo / (boy*boy))
# girilenBoy = float(input("Lütfen Boyunuzu Giriniz (1.83) : "))
# girilenKilo = int(input("Lütfen Kilonuzu Giriniz (78) : "))

# vucutIndex = girilenKilo / (girilenBoy * girilenBoy)
# print(vucutIndex)

#* kullanıcıdan alınan bir python kodunu çalıştırınız
# girilenDeger = input("Lütfen Py komutu giriniz: ")
# eval(girilenDeger) 

#* kullanıcıdan maaşını ve zam oranını alınız. hesaplama yaparak yeni zamlı maaşı verin
#* maas * zam / 100 (zam oranı hesaplama)

# girilenMaas = int(input("Lütfen Maaşınızı Giriniz"))
# girilenZam = int(input("Zam Oranını Giriniz : "))
# zamlıMaas =   girilenMaas+(girilenMaas * girilenZam / 100)
# print(f"Zamlı Maaşınız {zamlıMaas}")

#*kullanıcıdan 3 farklı değer alınız bu değerleri ekrana yazdırırken aralarına *** işareti koyunuz
  #*mesela ahmet***mehmet***rojin

# deger1 = input("1. Değeri Giriniz : ")
# deger2 = input("1. Değeri Giriniz : ")
# deger3 = input("1. Değeri Giriniz : ")
# print(deger1,deger2,deger3,sep="**")

#*klavyeden yarıçapı girilen dairenin alanını ve çevresini hesaplayınız.
  #*kullanıcıya alanı ve çevreyi verini 
  #* cevre = 2 * pi * yarıcap
  #* alan = pi * yaricap * yaricap

# yaricap = int(input("Yarı çapı giriniz : "))
# cevre = 2 * 3 * yaricap
# alan = 3 * yaricap * yaricap
# print(f"Dairenin Alanı : {alan}\nDairenin cevresi : {cevre}")

#*kullanıcın girdiği isimi 10 kere alt alta ekrana yazdırınız (for kullanmadan)
# girilenIsim = input("Lütfen Adınızı Giriniz")
# print(f"{girilenIsim}\n"*10)


#!zor örnek
#* kullanıcın girdiği meyve isimlerini (virgülle ayrılmış) bir array içerisinde toplayın
# bosArray = []
# meyveler = input("Meyvereli giriniz (arasında virgüller olarak) : ")
# meyveler = meyveler.split(",")
# print(meyveler)



#!STRİNG ELEMAN AYIRMA
# text = "selam ben mehmet"
# print(text[:5]) #?ilk 5 elemanı alır
# print(text[:-3]) #?sondan elemanları çıkarır
# print(text[6:9]) #?aralık belirtmek
# print(text[-6:]) #*tersten eleman ayırma
# print(text[::3]) #?3er 3er atlayarak eleman seçer


#!STRİNG METHOD

#?lower() (girilen metini küçük harflere dönüştürür)
# text = "SELAM BEN MEHMET COBAN"
# text = text.lower()
# print(text)

#?casefold() (girilen metini küçük harflere dönüştürür)
#* casefold lower ile aynı işlemi yapar fakar casefol daha güçlüdür ve daha fazla kelimeyi küçük harfe dönüştürür
# text = "SELAM BEN MEHMET COBAN"
# print(text.casefold())

#?upper() (girilen metini büyük harfe dönüştürür)
# text = "selam ben mehmet coban"
# print(text.upper())

#?strip() (metin başındaki ve sonundaki boşlukları siler)
# text = "     selam ben mehmet coban       "
# print(text.strip())

#*strip örnek (strip ile aynı zamanda silmek istediğiniz karakterleride belirtebeilirsiniz)
# text = ",,,....**MEHMET COBAN,,,....**"
# print(text.strip(",.*"))


#?istitle() (is title kelimelerin baş harflerine bakar)
#*baş harfler küçük ise bize false döndürür
#*baş harfler büyük ise true

# text = "selam ben mehmet coban"
# text = text.istitle()
# print(text)

# text = "Selam Ben Mehmet Çoban"
# text = text.istitle()
# print(text)

#*örnek
#*kullanıcıdan bir kkuallnıcı adı alınız!
#*eğer kullanıcı adının baş harhfi büyükse hoşgeldiniz değilse hatalı kullanım yazdırınız
# girilenKullanici = input("Adınızı Giriniz (baş harfi büyük şekilde) : ")
# kullaniciKontrol = girilenKullanici.istitle()
# if(kullaniciKontrol==True):
#   print("Teşekkürler",girilenKullanici)

# else:
#   print("Hatalı Kullanım! Tekrar dene")

#?count() (metin içerisinde belirttiğimiz kelimenin kaç adet olduğunu döndürür)
# yazi = "Selam ben yazılım çok severim. Çünkü benim işim yazılım"
# yazi = yazi.count("yazılım")
# print(yazi) #2

#* countda berlirilen aralıklar cümle içerisinde nereden başlayıp nerede biteceğini belirtir
# yazi = "Selam ben yazılım çok severim. Çünkü benim işim yazılım"
# yazi = yazi.count("yazılım",19,55) #*19-55 indexleri arasında yazılım ifadesini arar
# print(yazi)

#?index() (girilen metin yada karakterin index numarasını bize döndürür)
# text = "selam ben mehmet coban"
# print(text.index("m"))

# text = "selam ben mehmet coban"
# print(text.index("ben"))

# text = "selam ben mehmet coban"
# print(text.index("e",5,10)) #*5.index ile 10.indexdeki ilk "e" karakterin indexini döndürür


#?center() (metinde alınan değere göre bir ortalama işlemi yapar)
#* yazılan metinin karakter sayısından daha küçük bir ortalam girilemez
# metin = "Neos Yazılım"
# metin = metin.center(20)
# print(metin)

#*boşluk bırakılan yerleri doldurmak için ikinci bir değer girilebilir
# metin = "Neos Yazılım"
# metin = metin.center(50,"*")
# print(metin)


#*kullanıcıdan bir metin alınız 
#*alınan metinin başına ve sonuna kaç adet tıldınız kulannıcı belirlesin




# girilenMetin = input("lütfen bir metin giriniz : ")
# girilenBosluk = int(input("Lütfen Boşluk Sayısını Giriniz : "))
# girilenKarakter = input("lütfen karakter giriniz : ")

# metin = girilenMetin.center(girilenBosluk,girilenKarakter)
# print(metin)



#?split (verilen metini bize dizi olarak döndürür)
# metin = "selam ben mehmet coban"
# print(metin.split())

# aylar = ("ocak,şubat,mart,nisan,mayıs,haziran,")
# aylar = aylar.split(",") #*virgülden sonra bir ayrıştırma yapar
# print(aylar[1])

#*örnek
# isimler = input("Ayları arasına virgül koyarak yazınız")
# isimler = isimler.split(",")
# for i in isimler:
#   print(i)

#?lstrip() 
#*metin içerisinde verilen ifadede ilk karakteri siler
# text  = "05453054354"
# text = text.lstrip("0")
# print(text)


#?endswith() (metin içerisinde metin sonunun ne ile bittiğine bakmak için)
#*true yada false döndürür
# text = "selam, ben mehmet coban!"
# text = text.endswith(".") #?true
# print(text)

#?startswith() (metin içerisinde metin başının ne ile başladığına bakmak için)
# text = "neos akademide yazılım dersleri alıyorum!"
# text = text.startswith("n")  #?true
# print(text)

#?replace() (metin içerisindeki değiştirmek istediğimiz karakterlerde uygulanır)
# text = "selam ben mehmet coban"
# x = text.replace("selam","merhaba") #?selam yerine merhaba yazdırır
# print(x)


#*telefon numarasının başında 0 girildiğini silinmesini sağlayan yapı hazırlayalım
# tel = input("telefon numaranızı giriniz!")
# telKontrol = tel.startswith("0")
# if telKontrol==True:
#   tel = tel.replace("0","",1) #? buradaki 1 ilk elemanı değiştir anlamında kullanılır (briden fazla sıfır olabilr ilk sıfırı sil)
#   print(tel)
# else:
#   print(tel)


#?isnumeric() (girilen metinsel değerlerin rakam olup olmadığına bakar)
# text = "5538462904"
# text = text.isnumeric()
# print(text)

#*örnek
#*kullancııdan string olarak bir telefon numarası alınız 
#*telefon numarası içerisinde harf var ise hatalı giriş yapıldı şekilinde bir mesaj yazdırınız!
# tel = input("lütfen telefon numaranızı giriniz (bitişik şekilde) : ")
# tel = tel.isnumeric()

# if(tel==True):
#   print("Teşekkürler")

# else:
#   print("Hatalı Giriş Yapıldı!")


#?find() (metinsel değerin index numarasını verir)
#*değer bulunmazsa -1 döndürür
#*find ile index arasındaki fark index bulmazsa hata döndürür find ise -1

# text = "selam ben mehmet coban"
# text = text.find("ş") #? -1 döndürür
# print(text)

# text2 = "selam naber?"
# text2 = text2.index("k") #? hata dönderir
# print(text2)

#!listeleri toplama birleştirme
# list1 = [1,2,3,4,5]
# list2 = ["a","b","c","d","e"]

# listeToplamı = list1 + list2
# print(listeToplamı)


#!LİSTE METOTLARI
#?append (dizi sonuna bir eleman ekler)
# arabalar = ["audi","bmw","mercedes"]
# arabalar.append("renault")
# print(arabalar)

#*kullanıcıdan alınan bilgileri listeye ekleyin
# meyveler=["elma","armut","kivi","ananas"]
# alınanBilgi = input("Sevdiğiniz Meyveler : ")
# meyveler.append(alınanBilgi)
# print(meyveler)

#*var olan diziye kullanıcıdan aldığınız farklı bir diziyi ekleyin
# diller = ["html","css","js"]
# girilenDil = input("Yazılım Dillerini Sıralayınız : ")
# girilenDil = girilenDil.split()
# diller.append(girilenDil)
# print(diller)


#?insert() (ilk degeri nereye ekleneceği, ikinci değeri ne ekleneceği)
# mylist = ["html","css","js","python"]
# mylist.insert(1,"DJANGO") #*sıfırıncı elemana django ekler
# print(mylist)

# mylist = ["html","css","js","python"]
# mylist.insert(1,"react") #*birinci elemana react ekledi
# print(mylist)


#?remove() (listedeki elemanı siler)
# mylist = ["html","css","js","python"]
# mylist.remove("html")
# print(mylist)

#?del()
#*index numarasına göre silme işlemi yapar

# myList = ["test1","test2","test3","test4"]
# del myList[0]
# print(myList)


#?count() (listedeki o elemandan kaç adet varsa sayısal olarak döndürür)
# mylist = ["html","css","js","python","html","react","html"]
# x = mylist.count("html") #3
# print(x)

#?reverse() (listeyi tersine çevirip yazdırır)
# mylist = ["html","css","js","python"]
# mylist.reverse()
# print(mylist)

#?extend (dizideki bütün elemanları diğer diziye atar)
# front = ["html","css","js"]
# back = ["django","c#","php"]
# front.extend(back)
# print(front)

#*diziler hem rakamsal hemde sözel ifade tutabilir
# dizi1 = ["a","b","c"]
# dizi2 = [1,2,3]
# dizi1.extend(dizi2)
# print(dizi1)

#?sum() (dizi içerisinde rakamsal değerlerin toplamını döner)
# myList = [1,2,3,4,5,6]
# myListTop = sum(myList)
# print(myListTop)

#?clear() (dizideki bütün elemanları siler)
# mylist = ["html","css","js","python"]
# mylist.clear()
# print(mylist)

#?pop() (dizide pop içerisinde verilen index numaralı elemanı siler)
# mylist = ["html","css","js","python"]
# mylist.pop(1)
# print(mylist)

#*pop() değer alınmadığında son elemanı silmiş olur
# mylist = ["html","css","js","python"]
# mylist.pop()
# print(mylist)

#?sort() (listeyi küçükten büyüğe sıralar)
#*string olan diziyi alfabedik olarak A-Z'ye şekilde
# mylist = ["html","css","js","python"]
# mylist.sort()
# print(mylist)

#*numeric olan diziyi küçükten büyüğe doğru sıralar
# myList = [11,99,22,42,12,67,32,78,23,1,4,77,99]
# myList.sort()
# print(myList)

# myList = [11,99,22,42,12,67,32,78,23,1,4,77,99]
# sorted_list = sorted(myList, reverse=True)
# print(sorted_list)

#?alternatif
# sayisalDizi = [1,20,40,23,11,190,2334,23,54,324,123,67]
# sayisalDizi.sort()
# sayisalDizi.reverse()
# print(sayisalDizi)



#?ÖRNEKLER
#*boş list1 içerisine 4 meyve tanımla ve 3. indextekini patates ile değiştir

# list1 = []
# list1.append("muz")
# list1.append("kivi")
# list1.append("elma")
# list1.append("karpuz")
# list1.pop(3)
# list1.insert(3,"patates")
# print(list1)

#*list2 3 yazılım dili girilsin sonuna "python" ekle ve 2.indexteki listeden çıkar

# list2 = ["javascript", "c#", "java"]
# list2.append("python")
# list2.pop(2)
# print(list2)

#!İF ELSE (KARŞILAŞTIRMA OPERATÖRLERİ)
# karşılaştırma operatörü == (eşittir)
# karşılaştırma operatörü < (küçüktür)
# karşılaştırma operatörü > (büyüktür)
# karşılaştırma operatörü <= (küçük eşittir)
# karşılaştırma operatörü >= (büyük eşittir)
# karşılaştırma operatörü != (eşit değil)



#* if 3==3 => (eğer 3 3'e eşitse)
#* if 3<4 => (eğer 3 küçüktür 4'den ise)
#* if 10>5 => (eğer 10 büyük 5'den ise)
#* if 10<=5 => (eğer 10 küçük eşittir 5'den ise)
#* if 10>=5 => (eğer 10 büyük eşittir 5'den ise)
#* if 10!=5 => (eğer 10 eşit değil 5 ise)

#?Aşağıdaki değerler print olarak basıldığında
#?ekrana hangisi basılır (true-false)
# print(44==44)
#print(44==55)
#print(44<55)
#print(44>55)
#print(44>=55)
#print(44<=55)
#print(44!=55)
# print(44!=44)

# if kosul :
#   #?işlenecek kodlar
# else:
#   #?işlenecek kodlar



#?ÖRNEKLER
#*sayı eşitmi?
# if 44==44:
#   print("sayılar eşittir")

# else:
#   print("sayılar eşit değildir")

#*yaşın 18'den büyük olduğunda "reşitsiniz" yazan program
# yas = 18

# if yas>=18:
#   print("reşitsiniz!")

# else:
#   print("reşit değilsiniz!")

#*kullanıcı yaşını kendisi girdiğinde reşit olup olmadığını bulalım
# isim = input("Adınız : ")
# yas = int(input("yaşınızı giriniz : "))
# if yas>=18:
#   print(f"Selam {isim},Reşitsiniz!")

# else:
#   print(f"Selam {isim},Reşit Değilsiniz!")

#*kullanıcıdan alınan 2 sayının eşit olup olmadığı kontrol edilsin
# sayi1 = int(input("1. Sayıyı Giriniz"))
# sayi2 = int(input("2. Sayıyı Giriniz"))

# if sayi1==sayi2:
#   print("Girilen İki Sayı Eşit")

# else:
#   print("sayılar eşit değil")

  #*ortalamasını giren öğrencinin geçip geçmediği kontrol edilsin
# ortalama = int(input("Ortalamanızı Giriniz : "))
# if ortalama>=50 :
#   print("Tebrikler Geçtiniz!")
# else :
#   print("Maalsef Kaldınız!")

#*girilen iki sayının hangisinin büyük olduğunu bulunuz
# say1 = int(input("1. Sayıyı Giriniz : "))
# say2 = int(input("2. Sayıyı Giriniz : "))

# if say1>say2:
#   print(f"{say1} sayısı {say2} sayısından büyüktür")
# else:
#   print(f"{say1} sayısı {say2} sayısından Küçüktür")

#*girilen sayının tekmi çiftmi olduğunu bulun
# print("Girilen Sayının Tekmi Çiftmi Olduğunu Bul \n")
# girilenSayi = int(input("Lütfen Sayıyı Giriniz : "))
# if girilenSayi%2==0:
#   print(f"{girilenSayi} sayısı çifttir")

# else:
#   print(f"{girilenSayi} sayısı tektir")

#*kullanıcıdan yaptığı alışveriş fiyatını alınız.
#*alışveriş fiyatı 100 lira altındaysa 15 TL kargo ücreti fiyata dahil edilsin
#*100 lira üstündeyse kargo ücreti alınmasın

# alisverisFiyati = int(input("Lütfen alışveriş fiyatınızı giriniz! : "))

# if alisverisFiyati<100:
#   alisverisFiyati += 15;
#   print("Kargo Ücreti 15TL. Toplam Ödenecek Tutar : " , alisverisFiyati)

# else:
#   print("Kargo Ücretsiz! Ücretiniz : ",alisverisFiyati)

#*üç sınav noturunu giren öğrencinin
#*ortalaması alındıktan sonra geçme durumu kontrol edilecektir

# sinav1 = int(input("1. Sınavı Giriniz : "))
# sinav2 = int(input("2. Sınavı Giriniz : "))
# sinav3 = int(input("3. Sınavı Giriniz : "))

# ortalama = (sinav1+sinav2+sinav3) / 3
# ortalama = int(ortalama)

# if ortalama>=50:
#   print(f"Tebrikler Geçtiniz! Ortalamanız : {ortalama}")

# else:
#   print(f"Maalesef Kaldınız! Ortalamanız : {ortalama}")

#*kullanıcın girdiği vize ve final notlarının ortalamanı alınız
#*vize=40% final=60%
#*vize ve final ortalaması sonucu kalan öğrencilerden büt notunuz sorunuz
#*büt notu sonucu yeniden ortalama alıp geçip kaldığını mesaj olarak veriniz!
#* vize=40% büt=60%

# vize = int(input("Vize Notunuzu Giriniz : "))
# final = int(input("Final Notunuzu Giriniz : "))

# ortalama = (vize*0.4) + (final*0.6)

# if ortalama>=50:
#   print("Tebrikler Geçtiniz, Ortalamanız : ",ortalama)

# else:
#   print("Maalesef Kaldınız, Ortalamanız : ",ortalama)
#   but = int(input("Büt Notunuzu Giriniz : "))
#   ortalama = (vize *0.4) + (but*0.6)
#   if ortalama>=50:
#     print("Tebrikler Geçtiniz! Ortalamanız : ", ortalama)

#   else:
#     print("Maalesef Kaldınız, Ortalamanız : ",ortalama)

#!ELİF()
#* else if anlamına gelir
#* birden fazla şartınız var ise elif şartını kullanabilirsiniz

#if şart:
  #*işlenecek kodlar

#elif şart:
  #*işlenecek kodlar

#elif şart:
  #*işlenecek kodlar

#else:
  #*işlenecek kodlar

#?ÖRNEKLER
#*verilen rengi elif ile karşılaştır

# renk="kırmızı"
# if renk=="mavi":
#   print("Girilen Renk Mavi")

# elif renk=="yeşil":
#   print("Girilen Renk Yeşil")

# elif renk=="kırmızı":
#   print("Girilen Renk Kırmızı")

# else:
#   print("Hatalı Giriş!")

#*girilen iki sayının hangisinin büyük olduğunu bulunuz
# sayi1 = int(input("1. Sayıyı Giriniz : "))
# sayi2 = int(input("2. Sayıyı Giriniz : "))

# if sayi1>sayi2:
#   print(f"{sayi1} sayısı {sayi2} sayısından büyüktür!")

# elif sayi2>sayi1:
#   print(f"{sayi2} sayısı {sayi1 } sayısından büyüktür!")

# else:
#   print(f"{sayi1} sayısı {sayi2} sayısına eşittir")


#*girilen sayının kaç basamaklı olduğunu bulun
# sayi = int(input("Sayıyı Giriniz : "))

# if sayi<10:
#   print("Sayı 1 Basamaklıdır")

# elif sayi<100:
#   print("Sayı 2 Basamaklıdır")

# elif sayi<1000:
#   print("Sayı 3 Basamaklıdır")

# elif sayi<10000:
#   print("Sayı 4 Basamaklıdır")

# else:
#   print("Sayı Çok Basamaklıdır :)")

#*alternatif
# sayi=int(input("1 sayi giriniz"))
# print(len(str(sayi)))


#*100lük sistemde girilen notu 5lik sisteme çevirin (87 => 5)
# sinavNotu = int(input("Notounuzu Giriniz : "))

# if sinavNotu < 45:
#   print("Notunuz 1")

# elif sinavNotu < 55:
#    print("Notunuz 2")

# elif sinavNotu<69:
#   print("Notunuz : 3")

# elif sinavNotu<84:
#   print("Notunuz : 4")

# elif sinavNotu<=100:
#   print("Notunuz : 5")

# else:
#   print("Hatalı Not!")

#*aslınan iki sayının girilen harfe göre dört işlem yapan uygulamayı yazınız
#* örn =  toplama = t

# sayi1 = int(input("1. Sayıyı Giriniz : "))
# sayi2 = int(input("1. Sayıyı Giriniz : "))

# print("""Toplama : T
# Çıkart : Ç
# Çarp : X
# Böl : B
#       """)
# secilenislem = input("Yapacağınız İşlemin Baş Harfini Yazını : ")

# if secilenislem=="T":
#   sonuc = sayi1 + sayi2
#   print(f"Toplama İşleminin Sonucu : {sonuc}")

# elif secilenislem=="Ç":
#    sonuc = sayi1 - sayi2
#    print(f"Çıkartma İşleminin Sonucu : {sonuc}")

# elif secilenislem=="X":
#    sonuc = sayi1 * sayi2
#    print(f"Çarpma İşleminin Sonucu : {sonuc}")

# elif secilenislem=="B":
#    sonuc = sayi1 / sayi2
#    print(f"Bölme İşleminin Sonucu : {sonuc}")

# else:
#   print("Hatalı bir işlem yaptınız!")


#*Kullanıcıya sinema ya da tiyatro tercihi sorulsun.
#*Sinema izlemek için 50 TL,
#*tiyatro için 100 TL ödenmesi gerekmedir.
#*Öğrencilere % 50 indirim yapıldığı düşünülerek
#*öğrenci ise indirim yapılan
#*öğrenci değilse indirimsiz tutarı
#*hesaplayarak ekrana yazdıran kodu yazınız.

# tiyatro,sinema=100,50

# secim = input("Sinema yada Tiyato! Lütfen Seçiminizi Yapınız.. : ")

# if secim=="sinema":
#   ogrenci = input("Öğrencimisiniz : e/h ")
#   if ogrenci=="e":
#     sinemaIndırım = sinema *0.5;
#     print("Öğrenci İndirimi Uygulandı! Ödenecek Tutar : ",sinemaIndırım)
#   else:
#     print("Tam Bilet Fiyatı : ",sinema)

# elif secim=="tiyatro":
#   ogrenci = input("Öğrencimisiniz : e/h ")
#   if ogrenci=="e":
#     tiyatroIndırım = tiyatro * 0.5
#     print("Öğrenci İndirimi Uygulandı! Ödenecek Tutar : ",tiyatroIndırım)
#   else:
#     print("Tam Bilet Fiyatı : ",tiyatro)

# else:
#   print("HATALI SEÇİM!")



#!and / or (&& - ||) (VE - VEYA)
#?ve veya anlamına gelmektedir

#*sisteme giriş örneği
# kadi ="mehmet"
# sifre = "1a2b3c"

# if kadi=="mehmet" and sifre=="1a2b3c":
#   print("Sisteme Hoşgeldiniz!")
# else:
#   print("Hatalı Giriş Yaptınız!")

#*bir sisteme girişte or kullanarak kullanıcı adı veya şifre yanlışsa
#*ekrana "kullanıcı adı veya şifre yanlış" yazdırınız
# kadi ="mehmet"
# sifre = "1a2b3c"

# if kadi=="mehmet" and sifre=="1a2b3c":
#   print("Sisteme Hoşgeldiniz!")

# elif kadi!="mehmet" or sifre!="1a2b3c":
#   print("Kullanıcı adı veya şifre yanlış!")

# else:
#   print("Lütfen bilgilerinizi giriniz!")

#*Kullanıcının girdiği 3 sayının en büyük sayısını bulun
# say1 = int(input("1. Sayıyı Giriniz"))
# say2 = int(input("1. Sayıyı Giriniz"))
# say3 = int(input("1. Sayıyı Giriniz"))

# if say1>say2 and say1>say3:
#   print(say1," En Büyüktür")

# elif say2>say1 and say2>say3:
#   print(say2," En Büyüktür")

# else:
#   print(say3," En Büyüktür")



#*kullanıcıdan bir şifre ve kullanıcı adı oluşturmasını isteyiniz
#*eğer kullanıcı adı veya şifre en az 8 karakterden oluşuyorsa
#*"hatalı kullanım" yazdırınız değilse "kayıdınınız oluşturuldu" yazınız

# print("Kayıt Ekranına Hoşgeldiniz \n")
# kadi = input("Lütfen Kullanıcı Adınızı Giriniz : ")
# sifre = input("Lütfen Şifrenizi Giriniz : ")

# kadilen,sifrelen = len(kadi),len(sifre)

# if kadilen<8 or sifrelen<8:
#   print("8 Karakterden fazla bir kullanıcı adı veya şifre oluşturunuz")
# else:
#   print("Kayıdınız Başarı İle Oluşturuldu! ",kadi)


#*Bir kişi mağazadan 100 TL ve üzeri alışveriş yaparsa %10 indirim, 200 TL ve üzeri alışveriş
#*yaparsa *%15 indirim, 300 TL ve üzeri alışveriş yaparsa %20
#*indirim kazandığını ve ödeyeceği miktarı ekrana yazınız

# fiyatTutar = int(input("Ne kadarlık alışveriş yaptınız : "))

# if fiyatTutar>=100 and fiyatTutar<200:
#   fiyatTutarIndırım = fiyatTutar * 0.10
#   fiyatTutar-=fiyatTutarIndırım
#   print("%10'luk bir indirim Kazandınız! Ödenecek Tutar : ",fiyatTutar)

# elif fiyatTutar>=200 and fiyatTutar<300:
#    fiyatTutarIndırım = fiyatTutar * 0.15
#    fiyatTutar-=fiyatTutarIndırım
#    print("%15'lik bir indirim Kazandınız! Ödenecek Tutar : ",fiyatTutar)

# elif fiyatTutar>=300:
#   fiyatTutarIndırım = fiyatTutar * 0.20
#   fiyatTutar-=fiyatTutarIndırım
#   print("%20'lik bir indirim Kazandınız! Ödenecek Tutar : ",fiyatTutar)

# else:
#   print("Hatalı Giriş!")

#*basit bir bankamatik uygulaması oluşturunuz
#*kullanıcıdan bir şifre alınız şifre doğru olduğu taktirde işlemler alanlarına yöneltilsin
#*para çekme ve para yatırma işlemleri yapılsın
# sifre = "123"
# bakiye = 2500
# islemler = ["para çek","para yatır"]
# girilenSifre = input("Zırt Bankasına Hoşgeldiniz! \nLütfen Şifrenizi Giriniz : ")
# if(girilenSifre==sifre):
#   print("Hoşgeldiniz!")
#   yapilacakIslem = input("Lütfen Yapmak İstediğiniz İşlemi Yazınız : ")
#   if yapilacakIslem==islemler[0]:
#     print("Para çekilme işlemi seçildi")
#     girilenTutar = int(input("Lütfen Bir Tutar Giriniz : "))
#     if girilenTutar<bakiye:
#       bakiye = bakiye-girilenTutar
#       print("Para Çekilme İşlemi Tamamlandı!")
#       print(f"Kalan Tutar {bakiye}")
#     else:
#       print("Yetersiz Bakiye")
#   elif yapilacakIslem==islemler[1]:
#     print("Para Yatırma İşlemi Seçildi!")
#     girilenTutar = int(input("Lütfen Bir Tutar Giriniz : "))
#     bakiye = bakiye + girilenTutar
#     print("Para Çekme İşlemi Tamamlandı!")
#     print(f"Toplam Tutar : {bakiye}")
# else:
#   print("Girilen Parola Hatalı")



#!date time
#* zaman dilimini kullanırken pythona import datetime ile zamanı eklemeniz gerekir

# import datetime
# zaman = datetime.datetime.now() #?şuanki zamanı döner
# print(zaman)

# y = datetime.datetime.now()
# print(y.year) #*yıl
# print(y.month) #*ay
# print(y.day) #*gün


# z = datetime.datetime.now()
# print(z.hour) #*saat
# print(z.minute) #*dakika
# print(z.second) #*saniye

#!random()
#?randomu kullanmak içinc randomu importlamamız gerekmektedir
# import random

# print(random.randrange(1,10)) #*random.randrange ile başlangıç ve bitiş değerini belirtir

# myList = ["elma","armut","karpuz","kavun","kivi"]
# secilenEleman = random.choice(myList) #*choice liste içerisinde random değer alır
# print(secilenEleman)

#*choices kullanarak birden fazla veriyi dizi içerisinden alabiliriz
# renkler = ["kırmızı","mavi","sarı","turuncu","yeşil"]
# rstRenk = random.choices(renkler, k=3)
# print(rstRenk)


#*basit bir sayı tahmin oyunu yapınız 1 ile 50 arasında
#*kullanıcı sayıyı bildiğinde "bildiniz" bilemediğinde "bilemediniz"
#*gibi bir mesaj gönderiniz

# import random

# rndSayi = random.randint(1,50)
# print(rndSayi)

# girilenSayi = int(input("Lütfen Bir Sayı Giriniz : "))

# if girilenSayi==rndSayi:
#   print("Sayıyı Bildiniz!")
# else:
#   print("Sayıyı Bildiniz!")

#*hava durumlarının olduğu bir liste tutununuz
#* örnek =   havaDurumu = [yağışlı,karlı,güneşli]
#*rastgele değer alıp değer karşılığında if else kullanarak mesajlar bastırınız

# havaDurumu = ["yağışlı","karlı","güneşli"]
# rndHavaDurumu = random.choice(havaDurumu)

# if rndHavaDurumu=="yağışlı":
#   print("Bugün Hava Yağışlı! Şemsiyenizi Alınız")
# elif rndHavaDurumu=="karlı":
#   print("Bugün Hava Kar Yağışlı! Lütfen Sıkı Giyininiz")
# elif rndHavaDurumu=="güneşli":
#   print("Bugün Hava Güneşli! Parkta çekirdek kola yapabilirsiniz")

#*bir çekliliş uygulaması yapınız
#* kazanan sayısı ve yedek sayısı sorulsun

# kisiler = input("Kişilerin İsimlerini Giriniz (isimler arasına virgül koyunuz) : ")
# kisiler = kisiler.split(",")
# kazananlar = []
# yedekler = []
# print(kisiler)

# kazananSayisi = int(input("Kazanan sayisini giriniz : "))
# yedekSayisi = int(input("Yedek sayisini giriniz : "))

# while(True):
#   if len(kisiler) < (kazananSayisi + yedekSayisi):
#     kazananSayisi = int(input("Kazanan sayisini giriniz : "))
#     yedekSayisi = int(input("Yedek sayisini giriniz : "))
#   else:
#     break

# import random
# for i in range(kazananSayisi):
#   rnd = random.choice(kisiler)
#   kazananlar.append(rnd)
#   kisiler.remove(rnd)

# for i in range(yedekSayisi):
#   rnd = random.choice(kisiler)
#   yedekler.append(rnd)
#   kisiler.remove(rnd)

# print(kazananlar)
# print(yedekler)










#!PYTHON LOOPS
#!for yapısı

# for i in range(10): #?1 ile 9 arasında değerler girilir
#   print(i)

#*20 kere adınızı ekrana yazınız
# for i in range(20):
#   print("mehmet")

#?başlangıç ve bitiş değerlerini belirleyelim
# for i in range(5,10): #? çıktı olarak 5-9 verilir
#   print(i)

#?artış değerini belirleyelim
# for i in range(0,20,2): #?başlangıç;bitiş;artış
#   print(i)

#?liste içerisindeki elemanları yazdırmak
# havaDurumu = ["yağışlı","karlı","güneşli"]
# for i in havaDurumu:
#   print(i)



#*myList = [1,2,3,4,5,6] listesini ekrana => 123456 olarak yazdırınız

# myList = [1,2,3,4,5,6]

# text =""
# for i in myList:
#   text += str(i)
# print(text)

#*bir sayısal loto oyunu yapınız!
#*rastgele 3 adet rakam oluşturunuz ve kullanıcıdanda 3 adet tahmin rakamı isteyiniz
#*kullanıcıdan bahis miktarınıda giriniz
#*rastgele oluşturulan 3 rakam ile girilen rakamları karşılaştırınız
#*3 rakamıda bilen kullanıcın bahisini 3e katlayınız
#*2 rakam bilen kullanıcın bahisini 2ye katlayınız
#*1 rakam bilen kullanıcının bahisini amorti olarak geri iade ediniz!
#*örnek olarak 
#*rasgelesayılar = 1,4,7 kulllanıcınTahmini 1,9,1
#*bu durumda amorti kazanılır ve bahis iade edilir

# import random
# tutulansayilar= []
# tutulansayilar.append(random.randint(1,10))
# tutulansayilar.append(random.randint(1,10))
# tutulansayilar.append(random.randint(1,10))

# girilenBakiye = int(input("Ne Kadarlık Oynamak İstersin!"))
# say1 = int(input("Lütfen 1. Sayıyı Giriniz : "))
# say2 = int(input("Lütfen 1. Sayıyı Giriniz : "))
# say3 = int(input("Lütfen 1. Sayıyı Giriniz : "))

# sayac=0
# for i in tutulansayilar:
#   if say1==i or say2==i or say3==i:
#     sayac+=1
# if sayac==3:
#   girilenBakiye *=3
#   print(f"Tebrikler! {sayac} adet rakam bildiniz! Kazancınız : {girilenBakiye}")
# elif sayac==2:
#   girilenBakiye *=2
#   print(f"Tebrikler! {sayac} adet rakam bildiniz! Kazancınız : {girilenBakiye}")
# elif sayac==1:
#   print(f"Amorti! Kazancınız : {girilenBakiye}")
# else:
#   print("Kasa Kazandı :)")

# import random
# rastgele = []
# for i in range(3):
#   rastgele.append(random.randint(1,10))

# rastgele.append(random.randint(1,10))
# rastgele.append(random.randint(1,10))

# print(rastgele)

# tahmin1 = int(input("1. Sayıyı Tahmin Ediniz :"))
# tahmin2 = int(input("2. Sayıyı Tahmin Ediniz :"))
# tahmin3 = int(input("3. Sayıyı Tahmin Ediniz :"))


# sayac = 0


# if rastgele[0]==tahmin1:
#   sayac+=1
# if rastgele[1]==tahmin2:
#   sayac+=1
# if rastgele[2]==tahmin3:
#   sayac+=1
  
# print(sayac)


# print(rastgele)

#?break komutu ile for döngüsünü kırmak
# renkler = ["kırmızı","mavi","turuncu","yeşil","gri","siyah"]
# for i in renkler:
#   if i=="turuncu":
#     print(i)
#     break

#?continue ile döngüyü başa almak
# for i in range(10):
#   if i==3:
#     continue
#   print(i)

#? else ile for kullanımı
#*else döngü bittiğinde devreye girer ve genelde döngünün bittiğini gösterir
# for i in range(5):
#   print(i)
# else:
#   print("Sayımlar Bitti!")

#?örnekler
#*1'den 100e kadar olan tek sayıları yazınız
# for i in range(1,100,2):
#   print(i)

#*0'den 100e kadar olan çift sayıları yazını
# for i in range(0,100,2):
#   print(i)

#* 0'dan 100 yanlızca 5'e bölünebilen rakamları yazdırınız!
# for i in range(0,101):
#   if i%5==0:
#     print(i)


#* 1'dan 100 e kadar 3 ve 7 ye tam bölünenler
# for i in range(1,101):
#   if i%3==0 and i%7==0:
#     print(i)


#*1den 100e kadar olan tek ve çift sayıları ayrı
#*arraylere append ile ekleyiniz daha sonra bu iki arrayi
#*ekrana yazıdırınız
# tekSayilar = []
# ciftSayilar = []

# for i in range(0,101):
#   if i%2==0:
#     ciftSayilar.append(i)
#   else:
#     tekSayilar.append(i)

# print(f"Tek Sayılar : {tekSayilar}")
# print("\n \n \n")
# print(f"Çift Sayılar : {ciftSayilar}")

#*meyveler listesinde her eleman sırasıyla gelsin ve karşılığında fiyatları yazılsın
# meyveler = ["elma","armut","kavun","kivi"]

# for i in meyveler:
#   if i=="elma":
#     print(f"{i} 10 TL")
#   elif i=="kivi":
#     print(f"{i} 20 TL")
#   elif i=="kavun":
#     print(f"{i} 30 TL")
#   elif i=="armut":
#     print(f"{i} 40 TL")


#*renkler listesinden yeşil olaan değerlere kadar değerleri yazdırınız
# renkler = ["kırmızı","mavi","turuncu","yeşil","gri","siyah"]
# for i in renkler:
#   if i=="yeşil":
#     break
#   print(i)

#*renkler listesinde mavi hariç bütün elemanları yazdırınız
# renkler = ["kırmızı","mavi","turuncu","yeşil","gri","siyah"]
# for i in renkler:
#   if i=="mavi":
#     continue
#   print(i)

#*dict işlemleri
#?veri almak
# kullanici = {
#   "isim":"mehmet",
#   "soyisim":"coban",
#   "yas":23,
#   "numara":34535  
# }

# print(kullanici["isim"])

#?veri güncellemek
# kullanici = {
#   "isim":"mehmet",
#   "soyisim":"coban",
#   "yas":23,
#   "numara":34535  
# }
# kullanici["isim"]="rojin"
# print(kullanici)

#*update()
# kullanici = {
#   "isim":"mehmet",
#   "soyisim":"coban",
#   "yas":23,
#   "numara":34535  
# }

# kullanici.update({"yas":30})
# print(kullanici)

#?veri eklemek
# kullanici = {
#   "isim":"mehmet",
#   "soyisim":"coban",
#   "yas":23,
#   "numara":34535  
# }
# kullanici["maas"]=12345
# print(kullanici)

#*update()
# kullanici = {
#   "isim":"mehmet",
#   "soyisim":"coban",
#   "yas":23,
#   "numara":34535  
# }

# kullanici.update({"test":"test"})
# print(kullanici)

#?veri silmek
#* pop("") içerisine key girilen veriyi siler
# kullanici = {
#   "isim":"mehmet",
#   "soyisim":"coban",
#   "yas":23,
#   "numara":34535  
# }

# kullanici.pop("isim")
# print(kullanici)

#* popitem() dict içerisindeki son veriyi siler
# kullanici = {
#   "isim":"mehmet",
#   "soyisim":"coban",
#   "yas":23,
#   "numara":34535  
# }
# kullanici.popitem()
# print(kullanici)

#*tek bir dict içerisinde kullanıcıadı,şifre,meslek,yas bilgileri barındırın
#*kullanıcıdan alınan kullanıcı adı ve şifreyi dict içerisindeki yapıyla karşılaştırın
#*giriş yapmasını sağlayıp girilen kullanıcının bilgilerini paylaşın 

# kullanici = {
#   "kadi":"mehmet",
#   "sifre":"1234",
#   "yas":23,
#   "meslek":"web dev."
# }

# girilenKullaniciAdi = input("Lütfen Kullanıcı Adınızı Giriniz : ")
# girilenSifre = input("Lütfen Şifrenizi Giriniz : ")

# if girilenKullaniciAdi==kullanici["kadi"] and girilenSifre==kullanici["sifre"]:
#   print(f"Hoşgeldin! {kullanici['kadi']}\nYaşın : {kullanici['yas']}\nMeslek : {kullanici['meslek']}")

# else:
#   print("Bilgiler Hatalı")

#?keys ile verilere ulaşmak
# kuallanici = {
#   "isim":"mehmet",
#   "soyisim":"coban",
#   "yas":23,
#   "numara":34535  
# }

# for i in kuallanici.keys():
#   print(i)

#?value ile verilere ulaşmak
# kuallanici = {
#   "isim":"mehmet",
#   "soyisim":"coban",
#   "yas":23,
#   "numara":34535  
# }

# for i in kuallanici.values():
#   print(i)

#?items ile verilere ulaşmak
# kuallanici = {
#   "isim":"mehmet",
#   "soyisim":"coban",
#   "yas":23,
#   "numara":34535  
# }

# for k,v in kuallanici.items():
#   print(k,v)

#*bir dict içerisinde ürünler olsun ve karşılığında fiyat listesi olsun
#*dict içerisindeki ürünlerin fiyatlarını toplamını ekrana yazınız

# urunFiyatlari = []
# urunler={
#   "çikolata":3,
#   "ekmek":5,
#   "cips":4,
#   "meyvesuyu":2
# }

# for k,v in urunler.items():
#   urunFiyatlari.append(v)

# urunFiyatlariToplami = sum(urunFiyatlari) #?sum() dizi içerisindeki rakamları toplar
# print(f"Toplam Ürün Fiyatı : {urunFiyatlariToplami}")

#*kullanıcıdan 0'ın üstünde bir sayı isteyiniz!
#* 0'dan girilen sayıya kadar olan sayıların toplamını ekrana yazınız

# girilenSayi  = int(input("Bir Sayı Giriniz : "))
# toplam=0
# if girilenSayi>0:
#   for i in range(girilenSayi+1):
#     toplam = toplam + i
#   print(toplam)
# else:
#   print("0'dan büyük bir sayı giriniz!")


#*kullanıcıdan 0'ın üstünde bir sayı isteyiniz!
#* 0'dan girilen sayıya kadar olan tek sayıların toplamını bir değişkene
#* çift sayıların toplamını bir değişkene atınız

# tekToplam = 0
# ciftToplam = 0
# girilenSayi = int(input("Bir Sayı Giriniz : "))

# for i in range(girilenSayi+1):
#   if i%2==0:
#     ciftToplam = ciftToplam + i
#   else:
#     tekToplam = tekToplam + i

# print(f"Tek Sayıların Toplamı : {tekToplam} \n Çift Sayıların Toplamı : {ciftToplam}")


#*rastgele üretilen 1-50 arası bir sayıyı kullanıcı 5 hakta bulmaya çalışacak
#*kaçıncı defada sayıyı tahmin ettiği hakkında veri tutulacak
#*örnek "tebrikler 3. tahmininde sayıyı bildin!"
# import random
# rndSayi = random.randint(1,50)
# print(rndSayi)

# bilinmeSayısı=1

# for i in range(5):
#   girilenSayi = int(input("Sayıyı Tahmin Ediniz : "))
#   if girilenSayi==rndSayi:
#     print(f"Tebrikler {bilinmeSayısı}. defada Bildiniz!")
#     break
#   else:
#     bilinmeSayısı+=1
#     if i==4:
#       print("Hakkınız Doldu!")
#     print("Bilemedin la")


#*kullanıcıdan şifresiniz isteyiniz
#*3 kere yanlış girme hakkı olsun
#* her yanlış girdiğinde kaç hakkı olduğunu mesaj olarak versin
#* "şiferyi yanlış girdiniz kalan hakkınız 2" gibi
#*şifre doğru girildiğinde "sisteme hoşgeldiniz" mesajı veriniz
# sifre="123"
# hak=3
# for i in range(3):
#   girilenSifre = input("Lütfen şifre giriniz : ")
#   if girilenSifre==sifre:
#     print("Hoşgeldiniz!")
#     break
#   else:
#     hak-=1
#     if hak==0:
#       print("Hakkınız Bitti!")
#       break
#     print(f"Hatalı Şifre! Kalan Hakkınız : {hak}")


"""
  #*boş bir dizi oluşturun
  #*kullanıcıdan kaç adet user eklemek istediğini sorun
  #*kullanıcı adı ve şifrenizi giriniz
  #*kullanıcı adı ve şifrenizi dizi içerisinde ayrı ayrı obje olarak oluşturun
"""

# kullanicilar = []

# girilenKullaniciSayisi = int(input("Kaç Ader Kullanıcı Eklemek İsteriniz ?"))

# for i in range(girilenKullaniciSayisi):
#   girilenKullaniciAdi = input("Kullanıcı Adı Giriniz : ")
#   girilenSifre = input("Şifre Giriniz : ")
#   kullanicilar.append({"kadi":girilenKullaniciAdi,"sifre":girilenSifre})

# print(kullanicilar)



"""
  #*dizi içerisinde objelerle birden fazla kullanıcı oluşturunuz
  #*döngü kullanarak kullanıcıların kadi ve sifresini alıp giriş yaptırın 
"""

# kullanicilar = [
#   {
#     "kadi":"mehmet",
#     "sifre":"1234"
#   },
#   {
#     "kadi":"rojin",
#     "sifre":"4567"
#   }
# ]

# girilenKullanici = input("Lütfen Kullanıcı Adınızı Giriniz : ")
# girilenSifre = input("Lütfen Kullanıcı Adınızı Giriniz : ")

# for i in range(len(kullanicilar)):
#     if girilenKullanici==kullanicilar[i]["kadi"] and girilenSifre==kullanicilar[i]["sifre"]:
#       kontrol = True
#       break
#     else:
#       kontrol = False

# if kontrol==True:
#   print("hg")
# else:
#   print("yanlış şifre")


"""
  *Şifre doğrulama yapan bir sistem yazınız toplamda 3 hakda bulunması gerekiyor şifrenin
  *eğer şifre yanlış girilirse parolayı unuttunmu diye sorulsun
  *hayır derse direkt olarak sistemden çıkılsın evet derse kayıt olunurken girilen mail adresi
  *ve gizli cevabı cevaplasın doğru bildiği zaman yeni şifre belirlensin ve yeni şifre ile giriş yapılsın
"""

# sifre = "123"
# mail="test@test.com"
# gizliSoru="mehmet"

# for i in range(3):
#   girilenSifre = input("Şifrenizi Giriniz : ")
#   if girilenSifre!=sifre:
#     parolaUnuttunMu = input("Parolayı Unuttunuz Mu ? e/h")
#     if parolaUnuttunMu=="e":
#       girilenGizliSoru = input("Gizli Sorunun cevabını giriniz! : ")
#       girilenMail = input("Maili giriniz! : ")
#       if girilenGizliSoru==gizliSoru and girilenMail==mail:
#         sifre = input("Yeni Şifreinizi giriniz : ")
#         continue
#       else:
#         print("Bilgiler Hatalı!")
#     elif parolaUnuttunMu=="h":
#       continue
#   else:
#     print("Girilen Şifre Doğru")
#     break

#*sezar şifreleme algoritması!
#?ilk şifreleme algoritmalarından birisidir!
#?hashing (özetleme) veritabanına şifrelerken kullanılma yapısına benzer


# plainText = "omer mehmet"
# mytest = ""

# for i in range(len(plainText)):
#   test =  int(ord(plainText[i])) + 3 #?String ascii karsiliğini verir
#   mytest += chr(test) #?asciye karaktere çevirir

# print(mytest)




#*for yapısını kullanarak aşşağıdaki yapıyı ekrana çıkartınız
"""
  *
  **
  ***
  ****
  *****
  ******
  *******
  ********
  *********
"""
# for i in range(10):
#   print(i*"*")



#!iç içe for yapısı kullanımı
# for i in range(5):
#   for j in range(2):
#     print(i)

#*0'dan 10a kadar olan sayıları 3 kere yazdırın
# for i in range(11):
#   for j in range(3):
#     print(i)

#*0'dan 10a kadar olan sayıları 2 kere yazdırın ama 5 sayısını yazdırmayın
# for i in range(11):
#   if i==5:
#     continue
#   for j in range(3):
#     print(i)

#*0'dan 10a kadar olan sayıları 2 kere yazdırın ama 3 ve 7 sayısını yazdırmayın
# for i in range(11):
#   if i==3 or i==7:
#     continue
#   for j in range(2):
#     print(i)

#*for yapısını kullanarak aşşağıdaki yapıyı ekrana çıkartınız
"""
  *
  **
  ***
  ****
  *****
  ****
  ***
  **
  *
"""

# for i in range(5):
#   print(i*"*")
#   if i==4:
#     for j in range(5,0,-1):
#       print(j*"*")

#!ileri seviye if sorguları
#?ileri seviye if sorguları for şeklindede çalışabilir

# mylist = ["a","b","c","d","e","f"]
# if "a" in mylist:
#   print("Bu liste içerisinde a elementi bulunuyor")
# else:
#   print("bu liste içerisinde bu element yok")



#*Bir metin içerisinde bir kelimeyi arayan bir kod:
# text = "Merhaba dünya!"
# word = "dünya"
# if word in text:
#     print("Kelime metin içerisinde bulundu.")
# else:
#     print("Kelime metin içerisinde bulunamadı.")


#*meyveler ve renkler adında iki farklı array oluşturunuz
#*iki arraydede if ile elma ve yeşilin varlığını kontrol ettirip
#*varsa "Her iki arraydede değerler mevcut" yazdırırn

# meyveler = ["elma","armut","karpuz","kivi"]
# renkler = ["kırmızı","mavi","yeşil","turuncu"]

# if "elma" in meyveler and "yeşil" in renkler:
#   print("Her iki arraydede değerler mevcut")
# else:
#   print("değerler bulunmuyor!")



#*kullanıcıdan bir harf alınız
#*sesli har girildiğinde sesli harf girildi şeklinde mesaj veriniz

# b = input("Bir harf giriniz: ")
# if b in "aeiouAEIOU":
#     print("Girdiğiniz harf bir sesli harftir.")
# else:
#     print("Girdiğiniz harf bir sessiz harftir.")

#*bir dict yapısı oluşturunuz
#* if sorgusu ile dict key sorgusu ile dict içerisinde o keyin var olup olmadığını sorgulayınız

# test =[]
# kullanicilar = {
#   "ad":"mehmet",
#   "soyad":"coban",
#   "yas":23
# } 

# for k,v in kullanicilar.items():
#   test.append(v)

# if "mehmet" in test:
#   print("mehmet var")
# else:
#   print("yok")
  
  
  
  
# if "ad" in kullanicilar:
#   print(f"{kullanicilar['ad']}")





#!while yapısı
#* dögülerde alternatif olarak kullanılır (genelde sonsuz döngüler yaratılabilir)

# i=1
# while i<=5:
#   print(i)
#   i += 1


#* döngü sayınız 3 e ulaştığınızda döngüden çıkınız

# i=1
# while i<=10:
#   print(i)
#   if i==3:
#     break
#   i += 1

#* 1'den 10 kadar olan sayıları yazınız 3 rakamı hariç

# i=0
# while i<=10:
#   i += 1 
#   if i==3:
#     continue
#   print(i)
  
#*0dan 5e kadar olan rakamları while döngüsü ile ekrana yazdırınız
#*while döngüsü bittiğinde else ile mesaj verdiniz

# i=0
# while i<=5:
#   print(i)
#   i +=1
# else:
#   print("Sona erdi")


#*while ile sonsuz bir döngü oluştma
#*sayıyı sıfırtan başlatın ve sonsuza doğru ilerleyin
#*sayı ona ulaştığında döngüyü durdurun

# i=0
# while True:
#   print(i)
#   if i==10:
#     break
#   i+=1

#*while döngüsü ile 1-100 arasındaki sayıların tek ve çiflerini yazdırınız
# i=1
# while i<=100:
#   if i%2==0:
#     print(f"{i} Sayısı Çifttir")
#   else:
#     print(f"{i} Sayısı Tektir")
#   i+=1
 

#*1- 100 e kadar tek sayıları üzerine ekleyerek toplamını hesaplayalım.
# i=1
# toplam=0

# while i<=100:
#   if i%2==1:
#     toplam = i + toplam
#     print(toplam)
#   i+=1


#*kullanıcı adını sonsuz döngüde kullanıcıya sorunuz
#*kullanıcı adını doğru girdiğinde sisteme hoşgeldiniz uyazın
#*yanlış girdiği sürece sürekli yeniden kullanıcı adını sorunuz

# kadi = "mehmet"
# i=0
# while True:
#   girilenKadi = input("Kullanıcı Adınızı Giriniz!")
#   if girilenKadi==kadi:
#     print("Hoşgeldiniz!")
#     break
#   else:
#     continue

#*varolan bir listedeki elemanları ekrana yazdırınız

# myList = ["a","b",3,4,5,6,7,8,9,0]

# i=0
# while i < len(myList):
#   print(myList[i])
#   i+=1

  

#*başlangıcı , bitiş ve artış değerlerini kullanıcının belirlediği bir döngü oluşturun
# baslangic = int(input("Başlangıç Değerini Giriniz : "))
# bitis = int(input("Bitiş Değerini Giriniz : "))
# artis = int(input("Artış Değeri Giriniz : "))
# i=baslangic
# while i<=bitis:
#   print(i)
#   i+=artis

#*girilen metinsel ifadeyi harf harf alt alta yazdırınız 
# girilenDeger = input("Lütfen Değer Giriniz")

# i=0
# while i<len(girilenDeger):
#   print(girilenDeger[i])
#   i+=1



#*başlangıcı , bitiş kullanıcının belirlediği bir döngü oluşturun
#* 3e ve 5e bölünen sayıları ekrana yazdırınız

# baslangic = int(input("Başlangıç Değerini Giriniz : "))
# bitis = int(input("Bitiş Değerini Giriniz : "))

# i=baslangic
# while i<=bitis:
#   if i%3==0 and i%5==0:
#     print(i)
#   i+=1
  
#* 100'den 1e kadar olan sayıları azalan şekilde yazınız

# i=100
# while i>1:
#   print(i)
#   i-=1

#*Kullanıcıdan alacağınız 5 sayıyı küçükten büyüğe ve büyükten küçüğe yazdırınız
# i=0
# dizi = []
# while i<5:
#   girilenDeger = int(input("Deger giriniz:  "))
#   dizi.append(girilenDeger)
#   i+=1

# dizi.sort()
# print(f"Küçükten Büyüğe : {dizi}")

# test = sorted(dizi,reverse=True)
# print(f"Büyükten Küçüğe : {test}")


#*kullanıcıya kaç ürün ekleyeceğinizi sorunuz
#*eklenecek ürünlerim adını ve fiyatını isteyiniz (obje olarak verileri tutunuz)
#*ürünler eklendikten sonra ürünleri döngü ile listeleyiniz

# urunler = []
# urunMiktari = int(input("Kaç Adet Ürün Eklemek isteriniz : "))

# i=1
# while i<=urunMiktari:
#   urunIsim = input("Ürün İsimi : ") 
#   urunFiyatı = int(input("Ürün Fiyatı : "))
#   urunler.append({
#     'isim':urunIsim,
#     'fiyat':urunFiyatı
#   }) 
#   i+=1

# for i in urunler:
#   print(f"Ürün İsimleri : {i['isim']} Ürün Fiyatları : {i['fiyat']}")


#!TRY EXCEPT  (TRY -CATCH)
#*hata ayıklayıcı
# try:
#   print(x)
# except:
#   print("BÖyle Bir Değer Yok!")

# *excepte error tipini verip o şekilde bir yönlendirme yapabibiliriz
# try:
#   print(x)
# except NameError:
#   print("NameError Verdi! x değişkenini göremiyorum")
# except:
#   print("Birşeyler Ters Gitti")


#*else herahangi bir hata çıkmadığıdna devreye girecek kod blogğunu temsil eder
#?try ile birlikte (aynı anda çalışırlar)
# try:
#   print("selam!")
# except:
#   print("hatalı bir işlem!")
# else:
#   print("Hata Yok Devam Et")  


#*open ile bir .txt dosyası açmaya çalışınız
#*dosyanın dizinde var olup olmadığını kontrol ediniz

# try:
#   dosya = open("test.txt","r")
# except:
#   print("Böyle bir dosya yoktur")



#!txt belgesi veri okuma/yazma
#*dosya seçmek
#? r(read) olarak geçer ve hazırda bulunan dosyayı çeker
#? dosya yoksa hata bastırır
# dosya = open("test.txt","r")

#*tüm dosyayı ekrana yazdırmak
# dosya = open("test.txt","r")
# oku = dosya.read()
# print(oku)


#*satır satır ekrana yazdırmak
# dosya = open("test.txt","r")
# oku = dosya.readline() #?readline sadece ilk satırı ekrana yazdırır
# print(oku)

#*birden fazla satırı ekrana yazdırmak için  her seferinde reanline() arttırılır
# dosya = open("test.txt","r")
# print(dosya.readline())
# print(dosya.readline())
# print(dosya.readline()) #?3 satır okuduk
 
# dosya = open("test.txt","r")
# for satir in dosya:
#   print(satir)


#*dosyanın her satırını bir dizide toplamak
#?readlines metodu dosyanın tüm satırlarını bir dizide toplar

# dosya = open("test.txt","r")
# dosyaDizi = dosya.readlines()
# print(dosyaDizi)



#!dosyadaki her dizi içerisinde "\n" olarak gelir, burada \n temizlememiz gerekmektedir
#?strip ile "\n" leri silelim
# dosya = open("test.txt","r")
# dosyaDizi = dosya.read().splitlines()
# print(dosyaDizi)

#!dosya açma yöntemleri
"""
  *r	Mevcut dosyayı okumak için açar, yoksa hata verir
  *w	Dosya yoksa oluşturur, varsa içeriği silerek sıfır dosya açar
  *a	Dosya yoksa oluşturur, varsa dosyanın sonunda imleçten başlayarak ekleme yapar
"""


#? W modu
# dosya = open("test.txt","w")
#? A modu
# dosya = open("test.txt","a")

#?dosyaya veri yazdırmak
# dosya = open("test.txt","a")
# dosya.write("selam naber?")


#*kodlamayla yeni bir dosya oluşturunuz
#*içerisine "selam naber yazınız"
#*ardından bu dosyayı okuyup yazdılan mesajı print ile ekrana bastırınız



# dosya = open("test.txt","a")
# dosya.write("selam naber")

# dosya.close()

# dosya = open("test.txt","r")
# oku = dosya.read()
# print(oku)


#*kullanıcıdan virgüllerle ayrılarak kullanicilar isteyiniz!
#* ardından bu kullanıcıları bir dizi haline getirin
#* oluşturulan bu diziyi .txt dosyası içerisine tek tek yazdırınız
#* son olarak dosyayı okuyup verileri print ile yazdırınız

# kullanicilar = input("Kullanıcıları Girinziz : ")
# kullanicilar = kullanicilar.split(",")

# dosya = open("test.txt","a")
# for x in kullanicilar:
#   dosya.write(x+"\n")

# dosya.close()

# dosya = open("test.txt","r")
# dosyaOku = dosya.read()
# print(dosyaOku)

#!MATEMATİKSEL İŞLEMLER
#?min,max
# degeriBul = min(1,2,3,4,5) #?min en küçük değeri bulur
# print(degeriBul)

# degeribul2 = max(10,20,30,40,50) #?max en büyük değeri bulur
# print(degeribul2)


#*kullanıcıdan kaç adet değer gireceğini sorunuz
#*mesela 3 değeri girilirse 3 kere "Lütfen Sayı Belirleyiniz" deyiniz
#*belirlenen her sayıyı bir array içerisinde toplayınız 
#*dizi içerisine alınan değerlerin en büyüğünü bulunuz

# girilenDegerKat = int(input("Kaç Adet Değer Gireceksin ? "))
# test = []
# for i in range(girilenDegerKat):
#   girilenDeger = int(input("Lütfen Deger Giriniz : "))
#   test.append(girilenDeger)

# buyuk = min(test)
# print(buyuk)

#?abs
# sayi = abs(-20) #?abs negatif değeri hızlı bir şekilde pozitife çevirir
# print(sayi)

# sayi  =50
# sayi2 = 60
# sonuc = sayi - sayi2
# print(abs(sonuc))


#?pow
# sayi = pow(2,3) #?pow üssü almamıza yarar
# print(sayi)

# sayi =1
# sayi2 = 2
# toplamSonuc = sayi + sayi2
# genel = pow(toplamSonuc,sayi2)
# print(genel)

#*kullanıcıdan iki farklı değer alınız
#*ilk değer alt değer ikinci değer ise üssü olacak şekilde ayarlayıp sonucu alınız

# altDeger = int(input("Alt Değeri Giriniz : "))
# üssüDeger = int(input("Üssü Değeri Giriniz : "))
# sonuc = pow(altDeger,üssüDeger)
# print(sonuc)

#?round()
#*en yakın yakın tam sayıya yuvarlar 2.3=>2  2.8=>3
# sayi = round(2.8)
# print(sayi)

#!PYTHON MATH
#?pythonun matematik fonksiyonlarını kullanmak için math  modülünü içeriye aktarmamaız gerekir
# import math

#?math.sqrt
# karekok = math.sqrt(16) #?sqrt karekök işlemi yapar
# print(karekok)

#?math.ceil
# sayi = math.ceil(2.2) #?bir üst sayıya yuvarlama yapar
# print(sayi)

# sayi =  1.2
# sayi = math.ceil(sayi)
# print(sayi)

#?math.floor
#*bir alt sayıya yuvarlar
# sayi = math.floor(2.8)
# print(sayi)


#!fonksiyonlar
# def yazdir():
#   print("selamlar ben mehmet")
# yazdir()

#*def fonksiyonunda inputtan adımız alıncak ve eğer adımız doğruysa ekrana doğrudur yazdırsın
# def isim():
#   name = input("lütfen adınızı giriniz : ")
#   if name=="mehmet":
#     print("TRUE")
#   else:
#     print("FALSE")
# isim()


#?parametre örnekleri
# def toplam(say1,say2):
#   sonuc = say1 + say2
#   return sonuc

# print(toplam(5,10))


# def carpma(say1,say2,say3):
#   sonuc = say1*say2*say3
#   return sonuc

# x = carpma(1,1,1)
# print(x)

#*girilen Metinin uzunluğunu hesaplamak için bir foksiyon yazınız

# def uzunlukHesapla(sonuc):
#   return len(sonuc)

# girilenDeger = input("Lütfen Bir Değer Giriniz : ")
# yazdir =  uzunlukHesapla(girilenDeger)
# print(yazdir)


#*3 sınavın ortalamasını alan fonksiyonu yazınız
# def ortalama(say1,say2,say3):
#   sonuc  = (say1+say2+say3) / 3
#   return sonuc

# print(ortalama(50,50,50))


#*kullanıcıdan alınan 3 sınvın ortalamasını alan fonksiyonu yazınız
# def ortalama():
#   sin1 = int(input("1. Sınavı Giriniz : "))  
#   sin2 = int(input("2. Sınavı Giriniz : "))  
#   sin3 = int(input("3. Sınavı Giriniz : "))  
#   sonuc = (sin1+sin2+sin3) / 3
#   print(f"Ortalamanız : {sonuc}")
# ortalama()

#*aynı ortalama fonksiyonunu parametrelerle kullanıcıdan alarak yazınız
# def ortalama(say1,say2):
#   sonuc = (say1 + say2) / 2
#   return sonuc

# girilenSinav1 = int(input("1.Sınavı Giriniz : "))
# girilenSinav2 = int(input("2.Sınavı Giriniz : "))
# newSonuc = ortalama(girilenSinav1,girilenSinav2)
# print(newSonuc)


#*bir fonksiyon içerisinde rastgele 6 karakterli bir hex kodu oluşturmalısınız
#*örneğin fonksiyon çalıştığında çıktı şu olmalı => #E7736C
#*kullanıcıya soru sorarak "random renk oluşturulsun mu?" denilsin
#*evet dediği taktirde fonksiyonum devreye girsin ve 6 haneli hexim oluşsun
#*hayır dediğinde ise fonksiyonu çalıştırmayacağız 
# import random
# def colorPalette():
#   colorHex = "0123456789ABCDEF"
#   newColor="#"
#   for i in range(0,6,1):
#     rndHex = random.choice(colorHex)
#     newColor+=rndHex
#   print(newColor)

# soruCevap = input("Random olarak Color Oluşturmak İster Misiniz?")
# if soruCevap=="e":
#   colorPalette()
# else:
#   print("Color Oluşmadı")


#*islem adında bir def oluşturunuz ve içerisinde parametre olarak tutar giriniz
#*def içerisinde bakiye tanımlayıp bakiyeden tutarı çıkarıp return ile değeri döndürünüz
#*kullanıcıdan şifre isteyiniz ve şifre doğru olduğunda girilen tutarı alıp
#*fonksiyonu çalıştırarak bakiyeden girilen tutarı çıkartınız

# def islem(tutar):
#   bakiye=1000
#   kalanTutar = bakiye-tutar  
#   return kalanTutar

# sifre = "1234"
# girilenSifre = input("Lütfen Şifre Giriniz : ")

# if (girilenSifre==sifre):
#   girilenTutar = int(input("Lütfen Tutar Giriniz : "))
#   sonuc = islem(girilenTutar)
#   print(sonuc)
# else:
#   print("hatalı sifre")


#*bir çarpma fonksiyonu oluturunuz parametre olarak say1 ve say2 dönsün
#*bir cikartma fonksiyonu oluşturun parametre dönmeden cikartma fonksiyonu içerisinde
#*çarpma fanksiyonunu kullarak iki adet farklı değerler üretiniz 
#*ve ekrana cikartma fonksiyonunu yazdırınız

# def carpma(say1,say2):
#   carpim = say1 *say2
#   return carpim

# def cikartma():
#   x1 = carpma(2,2)
#   x2 = carpma(3,3)
#   cikar = x1 - x2
#   return cikar

# print(cikartma())


#*bir diziniz olsun => yemek = ["pilav","çorba","köfe","bulgur","patates"]
#* def ile dizi içerisinden random bir yemek seçiniz
#* sonsuz döngüde yemek seçmej için 1'e çıkmak için 2'ye basınız yazdırın
#* defden random seçilen yemek kullanıcıya verilir ve sorulur beğendin mi?
#* beğenmezse def ile yeniden random bir yemek sunulur

# import random
# yemek = ["pilav","çorba","köfe","bulgur","patates"]

# def rndYemek():
#   gelenYemek = random.choice(yemek)
#   return gelenYemek

# while True:
#   soru = input("Rastgele Yemek Seçmek İçin 1'e basınız! Uygulamadan Çıkmak İçin 2'ye basınız")
#   if soru=="1":
#     gelenYemek = rndYemek()
#     print(gelenYemek)
#     begeni = input("beğendin mi?")
#     if begeni=="evet":
#       break
#     else:
#       continue
#   elif soru=="2":
#     break
    



#!class
# class ClassOlustur:
#   x = 5
# print(ClassOlustur)


#*classları ayakta tutan nesnelerdir
# class ClassOlustur:
#   x = 5
# test = ClassOlustur()
# print(test.x)

#*nesneyi tek başına oluşturmak sağlıksızdır
#*init yardımıyla nesneler oluşturulmalıdır
#?init kullanımı
# class Kullanici:
#   def __init__(self,isim,sifre):
#     self.isim = isim
#     self.sifre = sifre

# elemanYaz = Kullanici("mehmet","123")
# print(elemanYaz.isim)



#?örnek
# class Kisi:
#   def __init__(self,isim,yas):
#     self.isim=isim 
#     self.yas=yas
# k1 = Kisi("mehmet",23)
# print(k1.yas)

#?örnek2 
# class Kisi:
#   def __init__(self,isim,yas):
#     self.isim = isim
#     self.yas= yas
#   def yazdir(self):
#     print("Selamlar! Adım : ",self.isim, "yaşım",self.yas)

# p1 = Kisi("mehmet",23)
# p1.yazdir()


#!python bitirme ödevleri
# hak= int(input("Kaç Hakkım Olsun knk ? : "))
# belirlenenRandom = int(input("0 ile Kaç Arası Bir Sayı Tutayım ? : "))
# tutulanSayilar = []
# while True:
#   import random
#   uretilenSayi = random.randint(1,belirlenenRandom) 
#   print("Ürettiğim sayı",uretilenSayi)
#   karar = input("Doğru bildimmi ?  e/h : ")
#   if karar=="e":
#     print("heheeyyt ne sandın yav")
#     break
#   else:
#     hak-=1
#     if hak==0:
#       print("Hakkım Bitti knk")
#       break
#     print("Bir Şans daha ver bana!\n")
#     continue


#*zor ödev sorusu
"""
  *bir obje içerisinde ürünler ve karşılığında fiyatları bulunan bir liste yapısı hazırlayınız
  * sonsuz bir döngüde sürekli olarak almak istediği ürünü sorunuz
  * bir sonraki sorusu ise alışverişe devam etmek istermisiniz gibi soru yöneltin
  * evet dediği sürece alışveriş yapmaya devam edecek müşteri
  * hayır dediğinde seçtiği ürünleri bir liste içerisine gönderip toplamlarını alınız!
"""
# urunlerAdi = list(urunler.keys())
# toplamFiyat = []
# while True:
#   girilenUrun = input("Lütfen İstediğiniz Ürünü Giriniz : ")
#   for i in range(len(urunlerAdi)):
#     if girilenUrun==urunlerAdi[i]:
#       for j, (key,value) in enumerate(urunler.items()):
#         if i==j:
#           toplamFiyat.append(value)
#           baskaUrun = input("Başka Ürün İstermisiniz ? : E / H ")
#           if baskaUrun=="E" or baskaUrun=="H":
#             break
#       continue
#   if baskaUrun=="E":
#     continue
#   else:
#     break
# print(toplamFiyat)
# toplamFiyat = sum(toplamFiyat)
# print(f"Toplam Market Alışverişiniz : {toplamFiyat} TL")

#*girilen şifreyi while ile kıran bir algoritma yazınız

# import random

# password = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k', 
#             'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u','v', 
#             'w', 'x', 'y', 'z', '0','1','2','3','4','5','6','7','8','9',]

# girilenSifre = input("Lütfen Şifre Giriniz : ")

# while True:
#   rastgeleSifre=""
#   for i in range(len(girilenSifre)):
#     test = random.choice(password)
#     rastgeleSifre+=test 
#   if girilenSifre==rastgeleSifre:
#     break
#   print(rastgeleSifre)
# print(f"Şifre Kırıldı! Şifreniz : {rastgeleSifre}")


# ?alternatif (daha güçlü ve hızlı)
# import random

# password = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k', 
#             'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u','v', 
#             'w', 'x', 'y', 'z', '0','1','2','3','4','5','6','7','8','9',]

# girilenSifre = input("Lütfen Şifre Giriniz : ")
# deneme = []
# tahmin = []
# for i in girilenSifre:
#   deneme.append(i)

# while True:
#   for test in range(len(girilenSifre)):
#     for j in password:
#       if j in deneme:
#         tahmin.append(j)
#     if test==0:
#       break
#   break

# while True:
#   yeniSifre = ""
#   for z in range(len(girilenSifre)):
#     zaa = random.choice(tahmin)
#     yeniSifre += zaa
#   if yeniSifre==girilenSifre:
#     break
#   print(yeniSifre)
# print(f"Şifreniz Kırıldı! Kırılan Şifre : {yeniSifre}")

#!-------------------

# import urllib.request
# import json

# url = 'https://randomuser.me/api/'
# response = urllib.request.urlopen(url)
# data = json.loads(response.read())

# # Burada "https://api.example.com/data" API endpoint'inizin URL'sini temsil ediyor
# # response.read() metodu, API yanıtını byte formatında döndürür
# # json.loads() metodu, byte veriyi Python sözlükleri ve listeleri gibi veri tiplerine dönüştürür

# print(data['results'])



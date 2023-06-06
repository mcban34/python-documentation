
#*kullanici adında bir dict oluşturunuz
#*dict içerisinde kullanıcıadı ve şifre adında keyler oluşturup value karşılığında değerleri oluşturunuz
#*klavyeden girilen kullanıcıadı ve şifreyi dict içerisindeki verilerle karşılaştırın
#*"hoşgeldiniz kullanici" veya "hatalı kullanıcı adı veya şifre yazdırınız"


# kullanici = {
#   "isim":"mehmet",
#   "sifre":"123"
# }
# girilenKadi = input("Lütfen Kullanıcı Adınızı Giriniz : ")
# girilenSifre = input("Lütfen Şifrenizi Giriniz : ")

# if girilenKadi==kullanici["isim"] and girilenSifre==kullanici["sifre"]:
#   print("Hoşgeldiniz! " , kullanici["isim"])
# else:
#   print("Kullanıcı Adı veya Şifre Yanlış")




#*şifresini unutmuş bir kullanıcı olduğunu varsayalım
#*dışarıdan gizlisoru,mailadres adında değişkenler oluşturunuz
#*kullanıcıya gizisorunun cevabını ve mail adresini sorunuz
#*bu iki veriyi karşılaştırınız ve yeni şifre oluşturması için yeni şifrenizi giriniz yazınız
#*kullanıcı yeni şifresini doğrulamak için 2 defa girilmesini isteyin
#*girilen bu iki yeni şifreleri karşılaştırıp eğer aynı şifreler girildiyse "şifreniz değiştirildi yazınız"
#*değilse hatalı giriş yazınız
# gizliSoru = "mehmet"
# mailAdres = "ccobanmehmet@gmail.com"
# gizliSoruCevap = input("Gizli Soru Cevabınızı Giriniz : ")
# girilenMailAdres = input("Gizli Soru Cevabınızı Giriniz : ")

# if gizliSoru==gizliSoruCevap and girilenMailAdres==mailAdres:
#   yeniSifre = input("Lütfen Şifrenizi Giriniz : ")
#   yeniSifre2 = input("Lütfen Şifrenizi Tekrar Giriniz : ")
  
#   if yeniSifre==yeniSifre2:
#     print("Tebrikler Şifreniz Oluşturuldu!")
#   else:
#     print("Girilen Şifreler Uyuşmuyor Lütfen Tekrar Deneyiniz")
# else:
#   print("Hatalı Giriş!")





#*bilet satış uygulaması
#*kullanıcıya tiyatro / sinema / gezi mi diye sorulursun
#*kaç adet bilet istediklerinizi sorunuz
#*öğrenci olup olmadığı sorulsun
#*öğrencilere 50% indirim yapınız
#* tam biletler için fiyat listesi::::
    #*sinema:5TL
    #*tiyatro:10TL
    #*gezi:20TL

# secim = input("Tiyatro/Sinema/Gezi : ")
# biletSayisi = int(input("Kaç Adet Bilet Almak İstersiniz? : "))
# ogrenciKont = input("Öğrenci Misiniz ?")

# if secim=="tiyatro" and ogrenciKont=="hayır":
#   biletSayisi *= 5
#   print(biletSayisi)

# elif secim=="sinema" and ogrenciKont=="hayır":
#   biletSayisi *=10
#   print(biletSayisi)

# elif secim=="gezi" and ogrenciKont=="hayır":
#   biletSayisi *=20
#   print(biletSayisi)
  
# elif secim=="tiyatro" and ogrenciKont=="evet":
#   biletSayisi *= 5
#   biletSayisi /= 2
#   print(biletSayisi)
  
# elif secim=="sinema" and ogrenciKont=="evet":
#   biletSayisi *= 10
#   biletSayisi /= 2
#   print(biletSayisi)

# elif secim=="gezi" and ogrenciKont=="evet":
#   biletSayisi *= 20
#   biletSayisi /= 2
#   print(biletSayisi)

# else:
#   print("hatalı seçim")
  


#*basit bir bankamatik uygulaması oluşturunuz
#*kullanıcıdan bir şifre alınız şifre doğru olduğu taktirde işlemler alanlarına yöneltilsin
#*para çekme ve para yatırma işlemleri yapılsın




#*kullanıcıdan girilen 2 veri alıyruz eğer sayılardan oluşuyorsa ikisini
#*toplasın değilse ekrana "yalnızca sayı girilsin"

# say1 = input("1. Sayıyı Giriniz : ")
# say2 = input("2. Sayıyı Giriniz : ")

# if say1.isnumeric() and say2.isnumeric():
#   say1,say2 = int(say1),int(say2)
#   print(say1+say2)
# else:
#   print("Lütfen Sadece Rakam Giriniz!")


        


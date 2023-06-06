import sqlite3
import json
db = sqlite3.connect("test.db")
cs = db.cursor()

girilenIsim = input("Lütfen Bir Kullanıcı Giriniz : ")
girilenSoyisim = input("Lütfen soyisim : ")

#!tablo oluştur
# cs.execute("create table Users (username,password)")

#!veri yükle
cs.execute(f"INSERT INTO people VALUES('{girilenIsim}','{girilenSoyisim}')")
db.commit()
# db.close()

#!veriyi çek
cs.execute("""SELECT * FROM people""")
people = cs.fetchall()
db.close()

#!json dosya haline getirir

data = []
for i in people:
  d = {
    "isim":i[0],
    "soyisim":i[1]
  }
  data.append(d)
print(data)
import sqlite3 as sql
import time


class Kitap:  # parantexe gerek yok class tanımında
    def __init__(self, isim, yazar, yayınevi, tür, baskı):
        self.isim = isim
        self.yazar = yazar
        self.yayınevi = yayınevi
        self.tür = tür
        self.baskı = baskı

    def __str__(self):
        print("Kitap özellikleri : ")
        print("Kitap ismi : {}\nYazarı : {}\nYayınevi : {}\nTürü : {}\nBaskı : {}\n".format(self.isim, self.yazar,
                                                                                            self.yayınevi, self.tür,
                                                                                            self.baskı))


class Kütüphane:  # DB oluştur, bağlantıları sağla, DB işlemlerini metod olarak yaz
    def __init__(self):
        self.baglantı_olustur()

    def baglantı_olustur(self):
        self.con = sql.connect("kütüphane.db")  # self dedğimiz için kütüphane sınıfın bir özelliği oldu 'con'
        self.cursor = self.con.cursor()
        sorgu = "Create table if not exists kitaplar (isim TEXT, yazar TEXT, yayınevi TEXT, tür TEXT, baskı INT)"
        self.cursor.execute(sorgu)
        self.con.commit()

    def baglantı_kapat(self):
        self.con.close()

    def kitapları_göster(self):
        sorgu = "Select * from kitaplar"

        self.cursor.execute(sorgu)
        kitaplar = self.cursor.fetchall()

        if len(kitaplar) == 0:
            print("Kitap yok...")
        else:
            for i in kitaplar:
                kitap = Kitap(i[0], i[1], i[2], i[3])
                print(kitap)

    def kitap_sorgula(self, isim):
        sorgu = "Select * from kitaplar Where isim = ?"

        self.cursor.execute(sorgu, (isim,))
        liste = self.cursor.fetchall()

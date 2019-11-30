from kütüphaneDNM import *
import time

print("""***********************************

Kütüphane Programına Hoşgeldiniz.

İşlemler;

1. Kitapları Göster

2. Kitap Sorgulama

3. Kitap Ekle

4. Kitap Sil 

5. Baskı Yükselt

Çıkmak için 'q' ya basın.
***********************************""")

kütüphane = Kütüphane()  # kütüphaneDNM modülünün içindeki Kütüphane class'ından bir obje oluşturduk = 'kütüphane'
# Burada Kütüphane sınıfınıı çağırdığımız için içindeki baglantı_oluştur metodu direkt çalışacaktır. COnstructor ında bu metodu çağırıyoruz çünkü.

while True:
    seçim = input("Yapacağınız işlemi seçiniz : ")

    if seçim == "q":
        print("Çıkış yapılıyor...")
        break
    elif seçim == "1":
        kütüphane.kitapları_göster()
    elif seçim == "2":
        kitapİsmi = input("Aradığınız kitabın adını giriniz : ")
        kütüphane.kitap_sorgula(kitapİsmi)
    elif seçim == "3":
        isim = input("İsim: ")
        yazar = input("Yazar: ")
        yayınevi = input("Yayınevi: ")
        tür = input("Tür: ")
        baskı = int(input("Baskı: "))

        kütüphane.kitap_ekle(isim, yazar, yayınevi, tür, baskı)
    elif seçim == "4":
        kitapİsmi = input("Silinecek kitabın adını giriniz : ")
        kütüphane.kitap_sil(kitapİsmi)
    elif seçim == "5":
        kitapİsmi = input("Kitabın adını giriniz : ")
        kütüphane.baskı_yükselt(kitapİsmi)
    else:
        print("Geçersiz İşlem...")

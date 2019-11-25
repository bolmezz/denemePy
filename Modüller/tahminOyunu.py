import random
import time

rastgele_sayi = random.randint(1, 40)
tahminHakki = 7

while True:
    tahmin = int(input("Tahmininiz : "))

    if tahmin < rastgele_sayi:
        print("Sorgulanıyor..")
        time.sleep(1)
        print(" İpucu : Daha yüksek bir sayı söyleyin !")
        tahminHakki -= 1
    elif tahmin > rastgele_sayi:
        print("Sorgulanıyor..")
        time.sleep(1)
        print("İpucu : Daha düşük bir sayı söyleyin !")
        tahminHakki -= 1
    else:
        print("Sorgulanıyor..")
        time.sleep(1)
        print("Doğru Tahmin Ettiniz !!", rastgele_sayi)
        break
    if tahminHakki == 0:
        print("Tahmin hakkınız bitti!\nSayı : ", rastgele_sayi)
        break

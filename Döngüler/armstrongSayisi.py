while True:
    sayi = input("Bir sayı girin : ")

    basamakSayisi = len(sayi)

    basamaklar = list()
    for i in sayi:
        basamaklar.append(int(i))

    toplam = 0
    for k in basamaklar:
        toplam += k ** basamakSayisi

    if toplam == int(sayi):
        print(sayi, " Armstrong sayısıdır.")
    else:
        print(sayi, "Armstrong sayısı DEĞİLDİR.")

    s = input("Devam etmek için d'ye çıkmak için q'ya basın : ")
    if s == "d":
        continue
    elif s == "q":
        print("Çıkış yapılıyor...")
        break
    else:
        break

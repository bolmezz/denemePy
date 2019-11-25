while True:
    sayi = int(input("Bir sayı girin : "))

    bolenler = list()  # girilen sayıyı tam bölen sayıların listesi
    for i in range(1, sayi):
        if sayi % i == 0:
            bolenler.append(i)
    toplam = 0
    for x in bolenler:
        toplam = toplam + x
    if toplam == sayi:
        print(sayi, "mükemmel sayıdır.")
    else:
        print(sayi, "mükemmel sayı DEĞİLDİR.")

    s = input("Devam etmek için d'ye çıkmak için q'ya basın : ")
    if s == "d":
        continue
    elif s == "q":
        print("Çıkış yapılıyor..")
        break
    else:
        break

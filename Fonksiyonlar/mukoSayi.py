def muko_mu(sayi):
    toplam = 0
    for i in range(1, sayi):
        if sayi % i == 0:
            toplam += i
    return toplam == sayi


for s in range(1, 1000):
    if muko_mu(s):
        print("Mükemmel sayı : ", s)

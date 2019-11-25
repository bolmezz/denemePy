def asal_mi(sayi):
    if sayi == 1:
        return False
    elif sayi == 2:
        return True

    for i in range(2, sayi):
        if sayi % i == 0:
            return False
    return True

while True:
    s = input("Bir sayı girin : ")
    if s == "q":
        print("Çıkış yapılıyor..")
        break
    if asal_mi(int(s)):
        print(s, "asaldır.")
    else:
        print(s, "asal değildir.")

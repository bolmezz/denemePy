def sayi_oku(sayi):
    birler = {"1": "bir", "2": "iki", "3": "üç", "4": "dört", "5": "beş", "6": "altı", "7": "yedi", "8": "sekiz",
              "9": "dokuz"}
    onlar = {"1": "on", "2": "yirmi", "3": "otuz", "4": "kırk", "5": "elli", "6": "altmış", "7": "yetmiş",
             "8": "seksen", "9": "doksan"}

    okunus = onlar[sayi[0]] + " " + birler[sayi[1]]
    return okunus


while True:
    s = input("Sayi : ")
    if s == "q":
        print("Çıkış yapılıyor..")
        break
    else:
        print("{}'nin okunuşu : {}".format(s, sayi_oku(s)))

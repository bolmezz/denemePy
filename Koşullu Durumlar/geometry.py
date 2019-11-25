sekil = int(input("Geometrik şekil seçin:\nDİkdörtgen için 1\nÜçgen için 2 seçiniz : \n"))

if sekil == 1:
    a = int(input("Kenar uzunluğu girin: "))
    b = int(input("Kenar uzunluğu girin: "))
    c = int(input("Kenar uzunluğu girin: "))
    d = int(input("Kenar uzunluğu girin: "))

    if a == b and a == c and a == d:
        print("Kare")
    elif (a == b and d == c) or (a == c and b == d) or (b == c and a == d):
        print("Dikdörtgen")
    else:
        print("Dörtgen")

else:
    a = int(input("Kenar uzunluğu girin: "))
    b = int(input("Kenar uzunluğu girin: "))
    c = int(input("Kenar uzunluğu girin: "))

    if (abs(a - b) < c < abs(a + b)) or (abs(a - c) < b < abs(a + c)) or (abs(b - c) < a < abs(b + c)):
        if a == b and a == c:
            print("Eşkenar üçgen")
        elif a == b or a == c or b == c:
            print("İkizkenar üçgen")
        else:
            print("Çeşitkenar üçgen")
    else:
        print("Üçgen değildir")

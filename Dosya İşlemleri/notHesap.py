def harfNotu(ortalama):
    if ortalama >= 90:
        return "AA"
    elif ortalama >= 85:
        return "BA"
    elif ortalama >= 80:
        return "BB"
    elif ortalama >= 75:
        return "CB"
    elif ortalama >= 70:
        return "CC"
    elif ortalama >= 65:
        return "DC"
    elif ortalama >= 60:
        return "DD"
    else:
        return "FF"


def hesap(satir, gecenler, kalanlar):
    isim = satir[0]
    vize1 = int(satir[1])
    vize2 = int(satir[2])
    final = int(satir[3])

    ort = (vize1 * 0.3) + (vize2 * 0.3) + (final * 0.4)
    harf = harfNotu(ort)

    if harf != "FF":
        bilgi = isim + "-----> " + harf + "\n"
        gecenler.append(bilgi)
    else:
        bilgi2 = isim + "-----> " + harf + "\n"
        kalanlar.append(bilgi2)


with open("dosya.txt", "r", encoding="utf-8") as dosya:
    gecenler = list()
    kalanlar = list()
    liste = dosya.readlines()

    for i in liste:
        i = i[:-1]  # her satırın sonundaki "\n" ifadesi silinir
        line = i.split(",")  # her satırdaki eleman "," ile ayrılıp listeye eleman olarak atılır
        hesap(line, gecenler, kalanlar)

    with open("gecenler.txt", "w", encoding="utf-8") as file:
        for i in gecenler:
            file.write(i)
    with open("kalanlarr.txt", "w", encoding="utf-8") as file2:
        for j in kalanlar:
            file2.write(j)
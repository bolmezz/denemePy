from functools import reduce


def ekstra(func):
    def wrapper(sayılar):
        çiftler = list()
        tekler = list()
        for i in sayılar:
            if i % 2 == 0:
                çiftler.append(i)
            else:
                tekler.append(i)
        func(sayılar) # asıl fonksiyonu çalıştırır (ort(sayılar))
        print("Çift sayıların ortalaması : ", (reduce(lambda x, y: x + y, çiftler) / len(çiftler)))
        print("Tek sayıların ortalaması : ", (reduce(lambda x, y: x + y, tekler) / len(tekler)))

    return wrapper


@ekstra
def ort(sayılar):
    toplam = 0

    for i in sayılar:
        toplam += i
    ortalama = toplam / len(sayılar)
    print("Genel ortalama : ", ortalama)


ort([1, 2, 3, 5, 6, 8, 9])

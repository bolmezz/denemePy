class Hayvanlar:
    def __init__(self, isim="İsimsiz", yas=0, tur="", durum="vahşi"):
        self.isim = isim
        self.yas = yas
        self.tur = tur
        self.durum = durum

    def sahiplenildi(self):
        self.durum = "evcil"

    def dogum_günü(self):
        self.yas += 1


class Kopek(Hayvanlar):
    def __init__(self, cins, isim, yas, ası=False, tur="köpek"):
        super().__init__(isim, yas, tur)
        self.cins = cins
        self.ası = ası

    def __str__(self):
        return "Adı {}\nCinsi {}\nYaşı {}\nDurumu {}\nAşılı mı {}".format(self.isim, self.cins, self.yas, self.durum,
                                                                         self.ası)

    def sahiplen(self):
        self.durum = "evcil"


kopek = Kopek("Golden Retriever", "Gold", 3, True)
print(kopek)


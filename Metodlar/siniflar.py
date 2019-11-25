class yazilimci():
    def __init__(self, isim, soyisim, numara, diller):
        self.isim = isim
        self.soyisim = soyisim
        self.numara = numara
        self.diller = diller

    def bilgiler(self):
        print("Yazılımcı Bilgileri :\n")
        print("İsim : {}\nSoyisim : {}\nNumara : {}\nDiller : {}".format(self.isim, self.soyisim, self.numara,
                                                                         self.diller))

    def dilEkle(self, yeniDil):
        self.diller.append(yeniDil)


yazilimciA = yazilimci("beyza", "ölmez", 1234, ["python", "java"])

yazilimciA.bilgiler()

yazilimciA.dilEkle("C++")
yazilimciA.bilgiler()

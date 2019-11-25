import random
import time


class Kumanda:

    def __init__(self, kanal="Trt", sesSeviyesi=5, durum="Kapalı", kanalListesi=["Trt", "Fox", "Show"]):
        self.durum = durum
        self.sesSeviyesi = sesSeviyesi
        self.kanal = kanal
        self.kanalListesi = kanalListesi

    def ses_gorsel(self):
        ses = self.sesSeviyesi
        seviye = ["|"]
        while True:
            if ses != 0:
                seviye.append("|")
                ses -= 1
            else:
                print("Ses seviyesi : ")
                for i in seviye:
                    print(i, end="")
                break

    def ses_ac(self):
        self.sesSeviyesi += 2
        self.ses_gorsel()

    def ses_dusur(self):
        self.sesSeviyesi -= 2
        self.ses_gorsel()

    def kanal_degistir(self):
        rand = random.randint(0, len(self.kanalListesi) - 1)
        self.kanal = self.kanalListesi[rand]
        print("  ...  ")
        time.sleep(1)
        print("Kanal : ", self.kanal)

    def tv_ac(self):
        if self.durum != "açık":
            self.durum = "açık"
            print("TV açık")
        else:
            print("TV zaten açık")

    def tv_kapat(self):
        if self.durum != "kapalı":
            self.durum = "kapalı"
            print("TV kapalı")
        else:
            print("TV zaten kapalı")

    def __str__(self):
        return "TV Durum {}\nTV Kanal {}\nTV Ses {}\nTV Kanal Listesi {}\n".format(self.durum, self.kanal,
                                                                                   self.sesSeviyesi, self.kanalListesi)

    def tv_bilgisi(self):
        print("TV Durum {}\nTV Kanal {}\nTV Ses {}\nTV Kanal Listesi {}\n".format(self.durum, self.kanal,
                                                                                  self.sesSeviyesi, self.kanalListesi))


kumanda = Kumanda()
print(kumanda)
print("""*******************

    Televizyon Uygulaması

    İşlemler ;

    1. Televizyonu Aç

    2. Televizyonu Kapat

    3. Televizyon Bilgileri

    4. Kanal Değiştir

    5. Sesi Azalt
     
    6. Sesi Arttır
    
    Çıkmak için 'q' ya basın.
    *******************""")

while True:
    s = input("\n\nİşlem seçin : \n")

    if s == "1":
        kumanda.tv_ac()
    elif s == "2":
        kumanda.tv_kapat()
    elif s == "3":
        kumanda.tv_bilgisi()
    elif s == "4":
        kumanda.kanal_degistir()
    elif s == "5":
        kumanda.ses_dusur()
    elif s == "6":
        kumanda.ses_ac()
    elif s == "q":
        print(" Çıkış yapılıyor...")
        break
    else:
        print("Geçersiz işlem..")

class Kuvvet4:
    def __init__(self, max=0):
        self.max = max
        self.kuvvet = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.kuvvet <= self.max:
            sonuc = 4 ** self.kuvvet

            self.kuvvet += 1

            return sonuc
        else:
            self.kuvvet = 0
            raise StopIteration


kuvvet = Kuvvet4(4)

iterator = iter(kuvvet)

# print(next(iterator))
# print(next(iterator))

for i in kuvvet:
    print(i)

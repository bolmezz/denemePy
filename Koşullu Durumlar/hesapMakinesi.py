print("1. Toplama işlemi\n2. Çıkarma işlemi\n3. Çarpma işlemi\n4. Bölme işlemi\n")

a = int(input("İlk sayıyı girin : "))
b = int(input("İkinci sayıyı girin : "))

islem = input("Yapılacak işlem no'sunu girin : ")

if islem == "1":
    print("{} ile {} toplamı {} ".format(a, b, a + b))
elif islem == "2":
    print("{} ile {} farkı {} ".format(a, b, a - b))
elif islem == "3":
    print("{} ile {} çarpımı {} ".format(a, b, a * b))
elif islem == "4":
    print("{} ile {} bölümü {} ".format(a, b, a / b))
else:
    print("İşlem geçersiz")

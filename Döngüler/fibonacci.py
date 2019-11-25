while True:
    a = int(input("sayı girin : "))

    k = 1
    m = 1
    fib = [1, 1]
    for i in range(1, a - 1):
        k, m = m, k + m
        fib.append(m)
    print(fib)
    s = input("Çıkmak için q'ya, devam etmek için d'ye basın\n")
    if s == "q":
        print("Çıkış yapılıyor...")
        break
    elif s == "d":
        continue
    else:
        continue

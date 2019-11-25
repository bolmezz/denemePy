def EBOB(x, y):
    i = 1
    ebob = 1
    while (x >= i) and (y >= i):
        if (x % i == 0) and (y % i == 0):
            ebob = i
        i += 1
    return ebob


sayi1 = int(input("sayi1 : "))
sayi2 = int(input("sayi2 : "))

print("{} ve {} EBOB'u : ".format(sayi1, sayi2), EBOB(sayi1, sayi2))

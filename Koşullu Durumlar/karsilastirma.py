a = float(input("sayı girin : "))
b = float(input("sayı girin : "))
c = float(input("sayı girin : "))

if a >= b and a >= c:
    print("en büyük sayı {}".format(a))
elif b >= a and b >= c:
    print("en büyük sayı {}".format(b))
elif c >= a and c >= b:
    print("en büyük sayı {}".format(c))

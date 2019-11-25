print("Vize1 harf notuna %30 etki edecek\nVize2 harf notuna %30 etki edecek\nFİnal harf notuna %40 etki edecek")

vize1 = float(input("Vize1 notunuz : "))
vize2 = float(input("Vize2 notunuz : "))
final = float(input("Final notunuz : "))

ortalama = (vize1 * 0.3) + (vize2 * 0.3) + (final * 0.4)

if ortalama >= 90:
    print("AA")
elif ortalama >= 85:
    print("BA")
elif ortalama >= 80:
    print("BB")
elif ortalama >= 75:
    print("CB")
elif ortalama >= 70:
    print("CC")
elif ortalama >= 65:
    print("DC")
elif ortalama >= 60:
    print("DD")
else:
    print("FF")

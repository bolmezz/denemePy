a = int(input("a : "))
b = int(input("b : "))

print("Değiştirilmeden önce ;\na: {} \nb: {}".format(a,b))

a,b = b,a

print("Değiştirildikten sonra ;\na: {} \nb: {}".format(a,b))


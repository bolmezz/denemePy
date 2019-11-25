def pisagor():
    pisagorlar = list()
    for x in range(1, 101):
        for y in range(1, 101):
            z = ((x ** 2) + (y ** 2)) ** 0.5
            if z == int(z):
                ucgen = [x, y, int(z)]
                pisagorlar.append(ucgen)

    return pisagorlar


for i in pisagor():
    print(i)

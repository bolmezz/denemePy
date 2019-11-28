with open("cumle", "r", encoding="utf-8") as file:
    x = dict()
    cumle = file.read()
    for harf in cumle:
        if harf in x:
            x[harf] += 1
        else:
            x[harf] = 1

for i, j in x.items():
    print(i," -> ",j)
    print("********")

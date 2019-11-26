def alan(x):
    return x[0] * x[1]


liste = [(3, 4), (10, 3), (5, 6), (1, 9)]

print(list(map(alan, liste)))

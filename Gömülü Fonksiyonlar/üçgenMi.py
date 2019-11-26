def ucgen(x):
    a = x[0]
    b = x[1]
    c = x[2]

    if (abs(a - b) < c < abs(a + b)) or (abs(a - c) < b < abs(a + c)) or (abs(b - c) < a < abs(b + c)):
        if a == b and a == c:
            return True
        elif a == b or a == c or b == c:
            return True
        else:
            return True
    else:
        return False

liste = [(3,4,5),(6,8,10),(3,10,7)]

print(list(filter(ucgen, liste)))

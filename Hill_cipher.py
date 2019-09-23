def EEA(a,b):
    if b == 0:
        return a, 1, 0
    else:
        q = int(a/b)
        P = EEA(b,a%b)
        return P[0], P[2], P[1] - q*P[2]


print(EEA(372, 321))

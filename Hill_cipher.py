def EEA(a,b):
    if b == 0:
        return a, 1, 0
    else:
        q = int(a/b)
        P = EEA(b,a%b)
        return P[0], P[2], P[1] - q*P[2]


def make_pairs(txt):
    array = []
    for i in range(1, len(txt), 2):
        array.append((ord(txt[i-1])-65, ord(txt[i])-65))
    if len(txt)%2 != 0:
        array.append((ord(txt[len(txt)-1])-65,ord("X")-65))
    return array


while True:
    print("ingrese 1 si desea encriptar y otra cosa si desea desencriptar")
    n = input()
    if n == "1":
        message = []
        print("ingrese la clave en siguiente formato \n|A  B| \n|C  D|\nA B C D")
        key = input()
        key = key.split(" ")
        print("ingrese el texto a cifrar en mayusculas")
        text = input()
        text = make_pairs(text)
        for i in text:
            message.append(chr((i[0] * int(key[0]) + i[1] * int(key[2])) % 26 + 65))
            message.append(chr((i[0] * int(key[1]) + i[1] * int(key[3])) % 26 + 65))
        print("El mensaje cifrado es :",end=" ")
        print("".join(message))

    else:
        message = []
        print("ingrese la clave en siguiente formato \n|A  B| \n|C  D|\nA B C D")
        key = input()
        key = key.split(" ")
        det = (int(key[0]) * int(key[3]) - int(key[1]) * int(key[2])) % 26
        data = EEA(det,26)
        newDet = data[1]
        print(det)
        print(data[0])
        if det != 0 and data[0] == 1:
            newKey = [(int(key[3]) * newDet) % 26, (-int(key[1]) * newDet) % 26,
                      (-int(key[2]) * newDet) % 26, (int(key[0]) * newDet) % 26]
            print("ingrese el texto a decifrar en mayusculas")
            text = input()
            text = make_pairs(text)
            for i in text:
                message.append(chr((i[0] * int(newKey[0]) + i[1] * int(newKey[2])) % 26 + 65))
                message.append(chr((i[0] * int(newKey[1]) + i[1] * int(newKey[3])) % 26 + 65))
            print("El mensaje decifrado es :",end=" ")
            print("".join(message))
        else:
            print("No es invertible")
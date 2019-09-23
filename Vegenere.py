matrix = []
for i in range(26):
    temp = []
    for j in range(26):
        temp.append(chr((j+i)%26+65))
        #temp.append(((j+i)%26))
    matrix.append(temp)
#for i in matrix:
#    print(i)

while True:
    print("ingrese 1 si desea encriptar y otra cosa si desea desencriptar")
    n = input()
    if n == "1":
        code = []
        print("ingrese la clave")
        key = input()
        print("ingrese el texto a cifrar en mayusculas")
        originalText = input()
        k = 0
        for i in originalText:
            code.append(matrix[ord(i)-65][ord(key[k%len(key)])-65])
            k += 1
            if k % 5 == 0:
                code.append(" ")
        print("".join(code))
    else:
        originalText = []
        print("ingrese la clave")
        key = input()
        print("ingrese el texto a decifrar en mayusculas")
        code = input()
        k = 0
        for i in code:
            originalText.append(chr(((ord(i)-65) - (ord(key[k%len(key)])-65))%26 + 65))
            k += 1
            if k % 5 == 0:
                originalText.append(" ")
        print("".join(originalText))

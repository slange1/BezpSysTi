print (chr(65))
tab = [[0 for x in range(0,26)] for y in range(0,26)]
for x in range(0, 26):
    z = -x
    for y in range(65, 91):
        if(x+y<91):
            tab[x][y-65] = chr(y+x)
        else:
            tab[x][y-65] = chr(y+x-26)
    print(tab[x][:])
while(True):
    text = input("Plain Text: (If you want to decipher - leave blank)").upper()
    text = text.replace(" ","")
    key  = input("Key: ").upper()
    keypadded = ''
    if(len(text)>0):
        ciphertext = ''
        if(len(key)<len(text)):
            z = 0
            for x in range(0,len(text)):
                if(z>=len(key)):
                    z=0
                keypadded +=key[z]
                z+=1
        else:
            keypadded = key;
        for x in range(0, len(text)):
            ciphertext += tab[ord(text[x])-65][ord(keypadded[x])-65]
        print(ciphertext)
    else:
        ciphertext = input("Ciphertext: ").upper()
        if(len(key)<len(ciphertext)):
            z = 0
            for x in range(0,len(ciphertext)):
                if(z>=len(key)):
                    z=0
                keypadded += key[z]
                z += 1
        else:
            keypadded = key;
        for y in range(0, len(ciphertext)):
            x = tab[ord(keypadded[y])-65][:].index(ciphertext[y])
            text += tab[0][x]
        print(text)

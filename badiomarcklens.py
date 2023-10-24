import random
import os
import time

taille = 15
# y itilize pou jwet la pa janm kanpe
y = 0
while y < 5:
# ti a itilize pou fe obje a desann
    ti = 0
    posac = 1
# posac la itilize pou pran pozisyon aktyel obje a
    pos = random.randint(0, taille - 1)
# pos la itilize pou pran o aza yon pozisyon
    while ti < taille - 1:
        i = 0
        os.system('cls' if os.name == 'nt' else 'clear')
        while i < taille:
            j = 0
            if i == 0 or i == taille - 1:
                while j < taille:
                    print("* ", end="")
                    j += 1
            if (i != 0 or i != taille - 1):
                while j < taille:
                    if j != pos and i != posac:
                        print("  ", end="")
                    if j == pos or i == posac:
                        if (i != posac or j != pos):
                            print("  ", end="")
                        else:
                            print("0 ", end="")
                    j += 1
                print()
            i += 1
        posac += 1
        time.sleep(1/3)
        ti += 1

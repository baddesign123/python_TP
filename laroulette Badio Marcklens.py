
import random
import pickle
import os

rekomanse=True
while(rekomanse):
    nbre = random.randint(0, 100)
    nom = input("Entre votre nom: ")
    while (nom.count(' ') > 0 or nom.islower() == False):
        nom = input("Nom an pa sipoze gen espas ak gen let majiskil.\nAntre nomw svp: ")

    chans = 1
    sko = 0
    print(nbre)
    while chans <= 5:
        print(chans)
        nbre1 = input("Antre nimewo ou chwazi a: ")
        nbre1 = int(nbre1)
        while(nbre1 < 0 or nbre1 > 100):
            nbre1 = input("Nonb lan pa sipoze pi piti ke 0, ni pi gwo ke 100\nAntre nimewo ou chwazi a: ")
            nbre1 = int(nbre1)
        if(nbre1 == nbre):
            print("🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉 Bravo 🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉")
            sko += (6 - chans) * 30
            break
        else:
            if(nbre1 > nbre):
                print("😒😒😒😒😒😒😒😒😒 Nonb ou chwazi a pigwo ke nonb odinate a chwazi a 😒😒😒😒😒😒😒😒😒")
            else:
                print("😒😒😒😒😒😒😒😒😒 Nonb ou chwazi a pipiti ke nonb odinate a chwazi a 😒😒😒😒😒😒😒😒😒")
            if(chans == 5):
                print("🤬🤬🤬🤬🤬🤬🤬🤬🤬🤬🤬🤬🤬🤬🤬🤬 Ou pedi 🤬🤬🤬🤬🤬🤬🤬🤬🤬🤬🤬🤬🤬🤬🤬🤬")
            else:
                print("---------------Ou rete ", 5 - (int(chans)), " chans-----------------")
                print("Chwazi on lot nonb: ")
        chans += 1

    print(f"Score ou fe nan pati sa se {sko}")


    bazla = {}
    if os.path.exists('fichye.pkl'):
        bazdone = open('fichye.pkl', 'rb')
        bazla = pickle.load(bazdone)
        bazdone.close()

    if nom in bazla:
        bazla[nom] += sko
    else:
        bazla[nom] = sko


    bazdone = open('fichye.pkl', 'wb')
    pickle.dump(bazla, bazdone)
    bazdone.close()


    print(f"Sko total : {bazla[nom]}")
    print("\n\n Ou vle kite jwet la??")
    k=input("Si ou vle kite jwet la peze K sinon peze nenpot lot bouton")
    if k=="K" or k=="k":
        rekomanse=False
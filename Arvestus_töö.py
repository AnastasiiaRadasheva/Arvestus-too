from random import randint
from module1 import *
from module2 import *
print("Võistlused algavad!!!")
sportlased = []
tulemused = []

i = randint(3, 10)


for b in range(i):
    while True:
        sportlane = input(f"Sisesta sportlase nimi ({i} osalejat): ").capitalize()
        if sportlane.isalpha():
            break
        else:
            print("Nimi peab sisaldama ainult tähti!")

    arv1, arv2, arv3 = randint(1, 100), randint(1, 100), randint(1, 100)
    tulemus = max(arv1, arv2, arv3)

    sportlased.append(sportlane)
    tulemused.append(tulemus)



print("\nMENÜÜ\n"
      "1. Vaadata n parimat tulemust;\n"
      "2. Sortida tulemused kasvavas järjekorras;\n"
      "3. Sisestada sportlase nimi ja näha tema tulemust;\n"
      "4. Diskvalifitseerida sportlased, kelle tulemus on alla 40;\n"
      "5. Vaadata n halvimat tulemust.")

try:
    while True:
        valik = int(input("Sisesta oma valik: "))
        if valik == 1:
            valik1(sportlased, tulemused)
        elif valik == 2:
            valik2(sportlased, tulemused)
        elif valik == 3:
            valik3(sportlased, tulemused)
        elif valik == 4:
            valik4(sportlased, tulemused)
        elif valik == 5:
            valik5(sportlased, tulemused)
        else:
            print("Vale valik, proovi uuesti.")
except ValueError:
    print("Viga! Sisesta arv vahemikus 1 kuni 5.")
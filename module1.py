import random

sportlased = []
tulemused = []
hüpped = []

def lists() -> None:
    """Genereerib sportlaste tulemused"""
    while True:
        inim = input("Sisesta sportlase nimi (või 'stopp' lõpetamiseks): ")
        if inim.lower() == "stopp":
            break
        
        score = [random.randint(1, 100) for _ in range(3)]
        jumps = [random.randint(100, 500) for _ in range(3)]
        best1 = max(score)
        best2 = max(jumps)
        
        sportlased.append(inim)
        sportlased.sort()

        tulemused.append(best1)
        tulemused.sort()

        hüpped.append(best2)
        hüpped.sort()

        print(f"{inim} tulemus on {best1} ja hüppab {best2} sentimeetrit")

def best() -> None:
    """Väljasta parima sportlase nimi ja tulemus"""
    if tulemused:
        max_index = tulemused.index(max(tulemused))
        print(f"Parim sportlane on {sportlased[max_index]} tulemusega {tulemused[max_index]} ja hüppe pikkusega {hüpped[max_index]} sentimeetrit")
    else:
        print("Tulemusi ei ole!")

def main() -> None:
    """Käivita programm"""
    lists()
    print("Kõik sportlased:", sportlased)
    print("Kõik tulemused:", tulemused)
    print("Kõik hüpped:", hüpped)
    best()


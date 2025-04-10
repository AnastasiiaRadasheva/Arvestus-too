from random import randint

def tabel(sportlased, tulemused):
    print("Osalejad : Tulemused")
    for n in range(len(sportlased)):
        print(f"{sportlased[n]} : {tulemused[n]}")


def valik1(sportlased, tulemused):
    kogus = int(input("Sisesta parimate tulemuste arv: "))
    sorted_results = sorted(zip(tulemused, sportlased), reverse=True)
    
    print(f"Top {kogus} parimat tulemust:")
    for tulemus, nimi in sorted_results[:kogus]:
        print(f"{nimi} : {tulemus}")


def valik2(sportlased, tulemused):
    sorted_results = sorted(zip(tulemused, sportlased))
    
    print("\nTulemused kasvavas järjekorras:")
    for i, (tulemus, nimi) in enumerate(sorted_results, 1):
        print(f"{i}. {nimi} : {tulemus}")


def valik3(sportlased, tulemused):
    name = input("Sisesta sportlase nimi: ").capitalize()
    if name in sportlased:
        index = sportlased.index(name)
        print(f"{name} : {tulemused[index]}")
    else:
        print("Sportlast ei leitud.")


def valik4(sportlased, tulemused):
    """Eemaldab sportlased, kelle tulemus on alla 40."""
    for i in range(len(tulemused) - 1, -1, -1):  # Проходим список с конца, чтобы удалять элементы
        if tulemused[i] < 40:
            del sportlased[i]
            del tulemused[i]

    print("\nUuendatud nimekiri pärast diskvalifitseerimist:")
    tabel(sportlased, tulemused)

# Funktsioon halvimate n tulemuste kuvamiseks
def valik5(sportlased, tulemused):
    kogus = int(input("Sisesta halvimate tulemuste arv: "))
    sorted_results = sorted(zip(tulemused, sportlased))
    
    print(f"Top {kogus} halvimat tulemust:")
    for tulemus, nimi in sorted_results[:kogus]:
        print(f"{nimi} : {tulemus}")


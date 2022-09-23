
from random import randint

teisingas = randint(-100, 100)
print(teisingas)
spejimu_kiekis = 0
skirtumas =0
while True:
    try:
        vartotojo_ivestis = int(input("Iveskite spejama skaiciu: \n"))
    except ValueError as e:
        print(f"Ivestas ne skaicius: {e}")
    else:
        spejimu_kiekis += 1
        if vartotojo_ivestis == teisingas:
            print(f"Atspejai skaiciu {teisingas}!! Tau pavyko is {spejimu_kiekis}-o karto")
            break
        elif abs(teisingas-vartotojo_ivestis) < skirtumas:
            print(f"Spejimas {vartotojo_ivestis}  - silta")
        else:
            print(f"Spejimas {vartotojo_ivestis}  - salta")
        skirtumas = abs(teisingas-vartotojo_ivestis)

        


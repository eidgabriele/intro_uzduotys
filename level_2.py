
from random import randint

teisingas = 11
skirtumas =0
while True:
    try:
        vartotojo_ivestis = int(input("Iveskite spejama skaiciu: \n"))
    except ValueError as e:
        print(f"Ivestas ne skaicius: {e}")
    else:
        if vartotojo_ivestis == teisingas:
            print("Atspejai skaiciu!!")
            break
        elif abs(teisingas-vartotojo_ivestis) < skirtumas:
            print(f"Spejimas {vartotojo_ivestis}  - silta")
        else:
            print(f"Spejimas {vartotojo_ivestis}  - salta")
        skirtumas = abs(teisingas-vartotojo_ivestis)

        


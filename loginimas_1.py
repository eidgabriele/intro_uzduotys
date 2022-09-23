# Sukurti funkcijas, kurios:

#     Gražintų visų paduotų skaičių sumą (su *args argumentu)
#     Gražintų paduoto skaičiaus šaknį (panaudoti math.sqrt())
#     Gražintų paduoto sakinio simbolių kiekį (su len())
#     Gražintų rezultatą, skaičių x padalinus iš y

# Nustatyti standartinį logerį (logging) taip, kad jis:

#     Saugotų pranešimus į norimą failą
#     Saugotų INFO lygio žinutes
#     Pranešimai turi būti tokiu formatu: data/laikas, lygis, žinutė

# Kiekviena funkcija turi sukurti INFO lygio log pranešimą apie tai, ką atliko, pvz.:

# logging.info(f"Skaiciu {args} suma lygi: {sum(args)}")

# Paleisti kiekvieną funkciją su norimais argumentais

import math
import logging

logging.basicConfig(level=logging.DEBUG, filename="loginimas_1.log", format="%(asctime)s:%(levelname)s:%(message)s")

def skaiciu_suma(*args):
    rez = sum(args)
    logging.info(f"Skaiciu {args} suma lygi: {rez}")
    return rez

def skaiciaus_saknis(skaicius):
    rez = math.sqrt(skaicius)
    logging.info(f"Skaiciaus {skaicius} saknis lygi: {rez}")
    return rez

def sakinio_ilgis(sakinys):
    rez = len(sakinys)
    logging.info(f"Sakinio {sakinys} ilgis yra: {rez}")
    return 

def dalyba(skaicius1, skaicius2):
    rez = skaicius1/skaicius2
    logging.info(f"Padalinus {skaicius1} is {skaicius2} yra lygu: {rez}")
    return rez

skaiciu_suma(20, 50, 20, 10, -5, 15, 40)
skaiciaus_saknis(9)
sakinio_ilgis("o labas!")
dalyba(30,6)
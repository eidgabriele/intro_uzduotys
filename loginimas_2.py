# Perdaryti 1 užduoties programą, kad:

#     Į šaknies funkciją padavus string tipo argumetrą, į log failą būtų išsaugoma išimties klaida su norimu tekstu
#     Į dalybos funkciją antrą argumentą padavus 0, į log failą būtų išsaugoma išimties klaida su norimu tekstu

# Patarimas: panaudoti try/except/else, logging.exception()

import math
import logging

logging.basicConfig(level=logging.DEBUG, filename="loginimas_2.log", format="%(asctime)s:%(levelname)s:%(message)s")

def skaiciu_suma(*args):
    rez = sum(args)
    logging.info(f"Skaiciu {args} suma lygi: {rez}")
    return rez

def skaiciaus_saknis(skaicius):
    try:
        rez = math.sqrt(skaicius)
    except Exception as e:
        logging.exception(f"Ivestas ne skaicius: {e}")

    else:
        logging.info(f"Skaiciaus {skaicius} saknis lygi: {rez}")
        return rez

def sakinio_ilgis(sakinys):
    rez = len(sakinys)
    logging.info(f"Sakinio {sakinys} ilgis yra: {rez}")
    return 

def dalyba(skaicius1, skaicius2):
    try:
        rez = skaicius1/skaicius2
    except ZeroDivisionError:
        logging.exception("Dalyba is nulio nera galima")
    else:
        logging.info(f"Padalinus {skaicius1} is {skaicius2} yra lygu: {rez}")
        return rez

skaiciu_suma(20, 50, 20, 10, -5, 15, 40)
skaiciaus_saknis(9)
skaiciaus_saknis("ee")
sakinio_ilgis("o labas!")
dalyba(30, 6)
dalyba(4, 0)
# Perdaryti 2 užduoties programą, kad:

#     Būtų sukurtas savo logeris, kuris fiksuotų visus anksčiau aprašytus pranešimus
#     Sukurtas logeris ne tik išsaugotų pranešimus faile, bet ir atvaizduotų juos konsolėje


import math
import logging

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("loginimas_3.log")
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(message)s")
file_handler.setFormatter(formatter)
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)



def skaiciu_suma(*args):
    rez = sum(args)
    logger.info(f"Skaiciu {args} suma lygi: {rez}")
    return rez

def skaiciaus_saknis(skaicius):
    try:
        rez = math.sqrt(skaicius)
    except Exception as e:
        logger.exception(f"Ivestas ne skaicius: {e}")

    else:
        logger.info(f"Skaiciaus {skaicius} saknis lygi: {rez}")
        return rez

def sakinio_ilgis(sakinys):
    rez = len(sakinys)
    logger.info(f"Sakinio {sakinys} ilgis yra: {rez}")
    return 

def dalyba(skaicius1, skaicius2):
    try:
        rez = skaicius1/skaicius2
    except ZeroDivisionError:
        logger.exception("Dalyba is nulio nera galima")
    else:
        logger.info(f"Padalinus {skaicius1} is {skaicius2} yra lygu: {rez}")
        return rez

skaiciu_suma(20, 50, 20, 10, -5, 15, 40)
skaiciaus_saknis(9)
skaiciaus_saknis("ee")
sakinio_ilgis("o labas!")
dalyba(30, 6)
dalyba(4, 0)
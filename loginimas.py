import logging

from modules.aritmetika import daugyba


logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('aritmetika.log')
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(module)s:%(lineno)s:%(funcName)s:%(message)s")
file_handler.setFormatter(formatter)

# logging.basicConfig(
#     level=logging.DEBUG, 
#     filename = "problemos.log", 
#     format="%(asctime)s:%(levelname)s:%(module)s:%(message)s"
# )



def dalyba(a,b):
    try:
        res = a/b
    except Exception as e:
       logger.error(f"Vykstant funkcija {dalyba.__name__}, ivyko klaida {e.__class__.__name__}: {e}")
       return None
    else:
        logger.info(f"Paleista funkcija {dalyba.__name__}: {a} / {b} = {res}")
        return res

print(dalyba(7, 0))
print(dalyba(7, 3))
print(daugyba(3, 5))

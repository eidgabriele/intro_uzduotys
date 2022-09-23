import logging
logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('aritmetika.log')
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s:%(name)s:%(levelname)s:%(module)s:%(message)s")
file_handler.setFormatter(formatter)

def daugyba(a,b):
    try:
        res = a*b
    except Exception as e:
       logger.exception(f"Vykstant funkcija {daugyba.__name__}, ivyko klaida {e.__class__.__name__}: {e}")
       return None
    else:
        logger.info(f"Paleista funkcija {daugyba.__name__}: {a} * {b} = {res}")
        return res

print(daugyba(2, 2))
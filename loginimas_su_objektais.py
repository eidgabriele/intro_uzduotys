import logging
import loginimas

# logging.basicConfig(
#     filename="asmenys.log",
#     level=logging.INFO,
#     format="%(asctime)s:%(levelname)s:%(module)s:%(lineno)s:%(message)s"
# )
# sukuriamaas loggeris su paleistos progrmaos pavadinimu
logger = logging.getLogger(__name__)
#  sukuriamas file handleris kuris rasys zinutes i nurodyta faila
file_handler = logging.FileHandler('asmenys.log')
#  priskiriamas logeriui file handleris
logger.addHandler(file_handler)
#  nurodoma kokio lygio zinutes bus apdorojamos logerio
logger.setLevel(logging.DEBUG)
#  nurodomas zinuciu formatas
formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(module)s:%(lineno)s:%(funcName)s:%(message)s")
# file handleriui priskiriamas formatas
file_handler.setFormatter(formatter)
#  stream handleris spausdinis zinutes i terminala
stream_handler = logging.StreamHandler()
# priskiriamas formatas stream handleriui (tas pats kaip ir file handleriui)
stream_handler.setFormatter(formatter)
# logeriui priskiriamas stream handleris (kaip pries tai file handleriui)
logger.addHandler(stream_handler)

class Asmuo:
    def __init__(self, vardas, pavarde):
        self.vardas = vardas
        self.pavarde = pavarde
        logger.info(f"sukurtas asmuo {self.__class__.__name__} {vardas} {pavarde}")


ingrida = Asmuo("ingrida", "vaitkuviene")
darius = Asmuo("darius", "vasionis")

print(loginimas.dalyba(10,2))
print(loginimas.daugyba(3,4))
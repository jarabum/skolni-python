import os
from random import randint
from time import sleep

cena_penez = 1

while True:
    os.system("cls")
    print("Cena bitcoinu:", cena_penez)
    random = randint(1,2)
    if random == 1:
        cena_penez += randint(1,50)
    elif random == 2:
        cena_penez -= randint(1,35)
    sleep(0.1)

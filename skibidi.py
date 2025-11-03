import os
from turtle import *

cyklus = 0
speed(10)

os.system("cls")
print("zaciname :)")

while True:
    if cyklus < 1:
        cyklus += 1
        home();clear()
        for i in range(600):
            if i % 5 == 0:
                left(3)
            forward(200)
            left(360/5)
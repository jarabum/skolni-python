from turtle import *
import random

cykly = 0
rovne = 1
leva = 1
rychlost = 0

while True:
    forward(rovne)
    left(leva)
    rovne += 1
    leva += 1
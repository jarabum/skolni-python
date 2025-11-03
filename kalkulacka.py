import os
from time import sleep

os.system("cls")
print("Vítejte ve vaší kalkulačce")
print()
print("1) Sčítání")
print("2) Odčítání")
print("3) Násobení")
print("4) Dělení")
print()

print("Vyberte možnost (1, 2, 3, 4):")
volba = int(input())

if volba == 1:
    os.system("cls")
    print("Napište 1. číslo:")
    a = int(input())
    print("Napište 2. číslo:")
    b = int(input())
    os.system("cls")
    print("Výsledek je:")
    print(a + b)
elif volba == 2:
    os.system("cls")
    print("Napište 1. číslo:")
    a = int(input())
    print("Napište 2. číslo:")
    b = int(input())
    os.system("cls")
    print("Výsledek je:")
    print(a - b)
elif volba == 3:
    os.system("cls")
    print("Napište 1. číslo:")
    a = int(input())
    print("Napište 2. číslo:")
    b = int(input())
    os.system("cls")
    print("Výsledek je:")
    print(a * b)
elif volba == 4:
    os.system("cls")
    print("Napište 1. číslo:")
    a = int(input())
    print("Napište 2. číslo:")
    b = int(input())
    if b == 0:
        os.system("cls")
        print("Jdi domů ty vtipálku")
        sleep(2)
        exit(1)
    os.system("cls")
    print("Výsledek je:")
    print(a / b)
else:
    os.system("cls")
    print("ERROR 128")
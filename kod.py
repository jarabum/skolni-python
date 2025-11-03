print("kalkulačka")

#prikald
cislo1 = int(input("napis 1. cislo: "))
znamenko = input("napis znamenko: ")
cislo2 = int(input("napis 2. cislo: "))

#vypocert
print("vysledek je:")
if znamenko == "+":
    if cislo1 + cislo2 == 67:
        print("hahahaah six seveeeeen 🙌🙌")
    else:
        print(cislo1 + cislo2)
elif znamenko == "-":
    if cislo1 - cislo2 == 67:
        print("hahahaah six seveeeeen 🙌🙌")
    else:
        print(cislo1 - cislo2)
elif znamenko == "*":
    if cislo1 * cislo2 == 67:
        print("hahahaah six seveeeeen 🙌🙌")
    else:
        print(cislo1 * cislo2)
elif znamenko == "/":
    if cislo1 / cislo2 == 67:
        print("hahahaah six seveeeeen 🙌🙌")
    elif cislo2 == 0:
        print("di do pekla a umri kretene")
    else:
        print(cislo1 / cislo2)
else:
    print("zab se vole")
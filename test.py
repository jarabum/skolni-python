import os

print("co chces zapsat do souboru")
text = input()
os.system("cls")
print("jak chces aby se soubor jmenoval (jmeno.txt)")
jmeno = input()
f = open(jmeno,"w")
f.write(text)
f.close()
os.system("cls")
print("hotovo")
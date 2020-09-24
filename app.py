import time
import os

local = time.localtime()
soubor = "test.txt"
kodovani = "utf-8"

def zapis_cas():
    return f.write(f"{local[2]}.{local[1]}.{local[0]}. Je {local[7]}.den v roce. Čas je {local[3]}:{local[4]}:{local[5]}\n")

try:
    if os.path.exists('test.txt'):
        odp = input("Soubor již existuje, chcete do něj přidat data? a/n ")
        if odp.lower() == "a":
            with open(soubor, "a", encoding=kodovani) as f:
                zapis_cas()
                print("Zápis byl úspěšně dokončen")
        else:
            print("Zápis neproběhl")
    else:
        with open(soubor, "w", encoding=kodovani) as f:
            zapis_cas()
            print("Vytvoření souboru bylo úspěšně dokončeno")
except:
    print("Chyba")
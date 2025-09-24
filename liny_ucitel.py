import json
import random

def uloz_data(data):
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)

def vypocet_prumer(znamky):
    return sum(znamky) / len(znamky) if znamky else 0

def pridat_znacku(jmeno):
    try:
        with open('data.json', 'r') as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}

    if jmeno not in data:
        print(f"Student {jmeno} nebyl nalezen.")
        odpoved = input("Chcete ho přidat? (ano/ne): ").strip().lower()
        if odpoved == "ano":
            while True:
                znamka_input = input("Zadejte první známku studenta (1-5): ").strip()
                if znamka_input.isdigit() and 1 <= int(znamka_input) <= 5:
                    znamka = int(znamka_input)
                    break
                else:
                    print("Neplatná známka, zadejte číslo od 1 do 5.")
            data[jmeno] = [znamka]
            print(f"Student {jmeno} byl přidán s první známkou: {znamka}")
            uloz_data(data)
        else:
            print(f"Student {jmeno} nebyl přidán.")
    else:
        nova_znamka = random.randint(1, 5)
        data[jmeno].append(nova_znamka)
        print(f"Student {jmeno} má novou známku: {nova_znamka}")

        prumer = vypocet_prumer(data[jmeno])
        print(f"Průměr známek studenta {jmeno} je {prumer:.2f}")

        if prumer > 4.0:
            print("Bohužel, průměr je nízký. Snad se to zlepší... 😢")

        uloz_data(data)

def hlavni_program():
    jmeno = input("Zadejte jméno studenta: ").strip()
    pridat_znacku(jmeno)

hlavni_program()

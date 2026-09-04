import json
import os
import yfinance

portfolio= []

def speichern(portfolio):
    with open("portfolio.json", "w", encoding="utf-8") as datei:
        json.dump(portfolio, datei)
    print("Gespeichert!")

def laden():
    global portfolio
    if os.path.exists("portfolio.json"):
          with open("portfolio.json", encoding="utf-8") as datei:
                portfolio = json.load(datei)
          print(str(len(portfolio)) + " Aktien geladen.")
    else: print("Keine Gespeicherte Datei gefunden.")

def aktie_hinzufuegen(portfolio):
    name = input("Unternehmensname: ")
    kuerzel = input("Kürzel der Aktie: ")
    kurs = float(input("Kaufkurs in $: "))
    stueck = float(input("Stückzahl: "))
    aktie= { "Name": name,
                "Kürzel": kuerzel.upper(),
                "Kurs": kurs,
                "Stück": stueck
            }
    portfolio.append(aktie)
    print("Aktie: ", name, "wurde hinzugefuegt!")

def gesamtwert_berechnen(portfolio):
    summe = 0.0
    for aktie in portfolio:
            wert = aktie["Stück"] * aktie["Kurs"]
            summe += wert
    print("Gesamtwert beträgt: ", summe),

def aktueller_depotwert():
    print("Aktueller Depotwert wird abgerufen...")
    gesamt = 0.0

    for aktie in portfolio:
        kuerzel = aktie["Kürzel"]
        stueck = aktie["Stück"]

        try:
             daten = yfinance.Ticker(kuerzel)
             kurs_aktuell = daten.fast_info["last_price"]
             wert = kurs_aktuell * stueck
             gesamt = gesamt + wert
             print(kuerzel + " " + str(stueck) + " Stück x " + str(round(kurs_aktuell, 2)) + " $ = " + str(round(wert, 2)) + " $")

        except Exception:
             print(kuerzel + ": Kurs konnte nicht abgerufen werden.")

    print("Gesamtwert (aktuell): " + str(round(gesamt, 2)) + " $")

def depot_loeschen():
     global portfolio
     portfolio = []
     print("Portfolio wurde gelöscht")

def differenz_berechnen():
    print("Differenz wird berechnet...")
    einstand = 0.0
    aktuell = 0.0
    fehlende = []

    for aktie in portfolio:
        kuerzel = aktie["Kürzel"]
        stueck = aktie["Stück"]
        kurs = aktie["Kurs"]

        try:
            daten = yfinance.Ticker(kuerzel)
            kurs_aktuell = daten.fast_info["last_price"]
        except Exception:
            fehlende.append(kuerzel)
            continue

        einstand = einstand + kurs * stueck
        aktuell = aktuell + kurs_aktuell * stueck

        veraenderung = (kurs_aktuell - kurs) / kurs * 100
        print(kuerzel + ": " + str(round(veraenderung, 2)) + " %")

    if fehlende:
        print("Kein Kurs abrufbar für: " + ", ".join(fehlende))

    if einstand == 0:
        print("Kein Gewinn berechenbar (Depot leer oder keine Kurse).")
        return
    
    gewinn = aktuell - einstand
    prozent = gewinn / einstand * 100

    print("Gesamt: " + str(round(gewinn, 2)) + " $ (" + str(round(prozent, 2)) + " %)")

laden()

while True:
    # 1. Menüstruktur anzeigen
    print(" Hauptmenü ")
    print("1. Aktie hinzufügen")
    print("2. Depot anzeigen")
    print("3. Momentaner Depotwert")
    print("4. Gesamtwert berechnen")
    print("5. Gewinn berechnen")
    print("6. Depot löschen")
    print("9. Speichern")
    print("0. Beenden")

    wahl = input("Bitte wählen sie eine Option: ")

    if wahl== '1':
        aktie_hinzufuegen(portfolio),
    elif wahl == '2':
        if portfolio == []: print("Portfolio ist leer")
        else: print(portfolio),
    elif wahl == '3':
        aktueller_depotwert(),
    elif wahl == '4':
        gesamtwert_berechnen(portfolio),
    elif wahl == '5':
        differenz_berechnen(),
    elif wahl == '6':
        depot_loeschen(),
    elif wahl == '9':
        speichern(portfolio),
    elif wahl == '0':
        speichern(portfolio)
        print("Das Programm wird beendet ")
        break
    else: print("Ungültige Eingabe.")

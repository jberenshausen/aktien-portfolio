"""
Aktien-Portfolio-Manager
========================
Funktionen:
  1. Aktien hinzufügen (Name, Kürzel, Stückzahl, Kaufkurs)
  2. Portfolio anzeigen
  3. Gesamtwert berechnen
  4. Daten speichern & laden (JSON oder CSV)
  5. Portfolio sortieren (nach Name, Kürzel, Wert oder Kaufdatum)
"""

import json
import csv
import os
from datetime import date

SPEICHERDATEI_JSON = "portfolio.json"
SPEICHERDATEI_CSV  = "portfolio.csv"


# ──────────────────────────────────────────────
#  Datenstruktur
# ──────────────────────────────────────────────

def neue_aktie(name: str, kuerzel: str, stueckzahl: float, kaufkurs: float) -> dict:
    return {
        "name":       name,
        "kuerzel":    kuerzel.upper(),
        "stueckzahl": stueckzahl,
        "kaufkurs":   kaufkurs,
        "kaufdatum":  str(date.today()),
    }


# ──────────────────────────────────────────────
#  Kern-Funktionen
# ──────────────────────────────────────────────

def aktie_hinzufuegen(portfolio: list) -> None:
    print("\n── Neue Aktie hinzufügen ──")
    name       = input("  Unternehmensname       : ").strip()
    kuerzel    = input("  Börsenkürzel (z. B. AAPL): ").strip()

    while True:
        try:
            stueckzahl = float(input("  Stückzahl              : ").replace(",", "."))
            kaufkurs   = float(input("  Kaufkurs (€ pro Stück) : ").replace(",", "."))
            break
        except ValueError:
            print("  ⚠ Bitte eine gültige Zahl eingeben.")

    aktie = neue_aktie(name, kuerzel, stueckzahl, kaufkurs)
    portfolio.append(aktie)
    print(f"\n  ✓ {aktie['name']} ({aktie['kuerzel']}) wurde hinzugefügt.")


def portfolio_anzeigen(portfolio: list) -> None:
    print("\n── Portfolio-Übersicht ──")
    if not portfolio:
        print("  (Noch keine Aktien vorhanden)")
        return

    # Spaltenbreiten
    breite_name = max(len(a["name"]) for a in portfolio)
    breite_name = max(breite_name, 20)

    kopf = (
        f"  {'Nr.':>4}  "
        f"{'Kürzel':<8}  "
        f"{'Name':<{breite_name}}  "
        f"{'Stück':>8}  "
        f"{'Kaufkurs':>10}  "
        f"{'Wert (€)':>12}  "
        f"{'Kaufdatum':<12}"
    )
    trennlinie = "  " + "─" * (len(kopf) - 2)

    print(trennlinie)
    print(kopf)
    print(trennlinie)

    for i, a in enumerate(portfolio, 1):
        wert = a["stueckzahl"] * a["kaufkurs"]
        print(
            f"  {i:>4}  "
            f"{a['kuerzel']:<8}  "
            f"{a['name']:<{breite_name}}  "
            f"{a['stueckzahl']:>8.2f}  "
            f"{a['kaufkurs']:>10.2f}  "
            f"{wert:>12.2f}  "
            f"{a['kaufdatum']:<12}"
        )

    print(trennlinie)


def gesamtwert_berechnen(portfolio: list) -> None:
    print("\n── Gesamtwert des Portfolios ──")
    if not portfolio:
        print("  (Keine Aktien vorhanden)")
        return

    gesamt = 0.0
    for a in portfolio:
        wert   = a["stueckzahl"] * a["kaufkurs"]
        gesamt += wert
        print(f"  {a['kuerzel']:<8}  {a['name']:<30}  {wert:>12.2f} €")

    print("  " + "─" * 58)
    print(f"  {'GESAMT':<40}  {gesamt:>12.2f} €")


def aktie_loeschen(portfolio: list) -> None:
    portfolio_anzeigen(portfolio)
    if not portfolio:
        return
    while True:
        try:
            nr = int(input("\n  Nummer der zu löschenden Aktie (0 = Abbrechen): "))
            if nr == 0:
                return
            if 1 <= nr <= len(portfolio):
                entfernt = portfolio.pop(nr - 1)
                print(f"  ✓ {entfernt['name']} ({entfernt['kuerzel']}) wurde entfernt.")
                return
            print(f"  ⚠ Bitte eine Zahl zwischen 1 und {len(portfolio)} eingeben.")
        except ValueError:
            print("  ⚠ Ungültige Eingabe.")


def portfolio_sortieren(portfolio: list) -> None:
    if not portfolio:
        print("\n  (Keine Aktien vorhanden)")
        return

    print("\n── Portfolio sortieren ──")
    print("  [1] Nach Name         (A → Z)")
    print("  [2] Nach Kürzel       (A → Z)")
    print("  [3] Nach Wert         (höchster zuerst)")
    print("  [4] Nach Wert         (niedrigster zuerst)")
    print("  [5] Nach Kaufdatum    (neueste zuerst)")
    print("  [6] Nach Kaufdatum    (älteste zuerst)")
    print("  [0] Abbrechen")

    wahl = input("  Auswahl: ").strip()

    if wahl == "0":
        return
    elif wahl == "1":
        portfolio.sort(key=lambda a: a["name"].lower())
        hinweis = "Name (A → Z)"
    elif wahl == "2":
        portfolio.sort(key=lambda a: a["kuerzel"])
        hinweis = "Kürzel (A → Z)"
    elif wahl == "3":
        portfolio.sort(key=lambda a: a["stueckzahl"] * a["kaufkurs"], reverse=True)
        hinweis = "Wert (höchster zuerst)"
    elif wahl == "4":
        portfolio.sort(key=lambda a: a["stueckzahl"] * a["kaufkurs"])
        hinweis = "Wert (niedrigster zuerst)"
    elif wahl == "5":
        portfolio.sort(key=lambda a: a["kaufdatum"], reverse=True)
        hinweis = "Kaufdatum (neueste zuerst)"
    elif wahl == "6":
        portfolio.sort(key=lambda a: a["kaufdatum"])
        hinweis = "Kaufdatum (älteste zuerst)"
    else:
        print("  ⚠ Ungültige Auswahl – Sortierung abgebrochen.")
        return

    print(f"\n  ✓ Sortiert nach: {hinweis}")
    portfolio_anzeigen(portfolio)


# ──────────────────────────────────────────────
#  Speichern & Laden
# ──────────────────────────────────────────────

def speichern_json(portfolio: list, datei: str = SPEICHERDATEI_JSON) -> None:
    with open(datei, "w", encoding="utf-8") as f:
        json.dump(portfolio, f, ensure_ascii=False, indent=2)
    print(f"  ✓ Portfolio als JSON gespeichert → {datei}")


def laden_json(datei: str = SPEICHERDATEI_JSON) -> list:
    if not os.path.exists(datei):
        return []
    with open(datei, encoding="utf-8") as f:
        return json.load(f)


def speichern_csv(portfolio: list, datei: str = SPEICHERDATEI_CSV) -> None:
    felder = ["name", "kuerzel", "stueckzahl", "kaufkurs", "kaufdatum"]
    with open(datei, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=felder)
        writer.writeheader()
        writer.writerows(portfolio)
    print(f"  ✓ Portfolio als CSV gespeichert → {datei}")


def laden_csv(datei: str = SPEICHERDATEI_CSV) -> list:
    if not os.path.exists(datei):
        return []
    portfolio = []
    with open(datei, newline="", encoding="utf-8") as f:
        for zeile in csv.DictReader(f):
            zeile["stueckzahl"] = float(zeile["stueckzahl"])
            zeile["kaufkurs"]   = float(zeile["kaufkurs"])
            portfolio.append(zeile)
    return portfolio


def speichern_menue(portfolio: list) -> None:
    print("\n── Speichern ──")
    print("  [1] Als JSON speichern")
    print("  [2] Als CSV speichern")
    print("  [3] Beide Formate")
    wahl = input("  Auswahl: ").strip()
    if wahl == "1":
        speichern_json(portfolio)
    elif wahl == "2":
        speichern_csv(portfolio)
    elif wahl == "3":
        speichern_json(portfolio)
        speichern_csv(portfolio)
    else:
        print("  Ungültige Auswahl – nichts gespeichert.")


def laden_menue() -> list:
    print("\n── Laden ──")
    print("  [1] Aus JSON laden")
    print("  [2] Aus CSV laden")
    wahl = input("  Auswahl: ").strip()
    if wahl == "1":
        p = laden_json()
        print(f"  ✓ {len(p)} Einträge aus JSON geladen.")
        return p
    elif wahl == "2":
        p = laden_csv()
        print(f"  ✓ {len(p)} Einträge aus CSV geladen.")
        return p
    else:
        print("  Ungültige Auswahl – nichts geladen.")
        return []


# ──────────────────────────────────────────────
#  Hauptmenü
# ──────────────────────────────────────────────

MENU = """
╔══════════════════════════════════════╗
║      Aktien-Portfolio-Manager        ║
╠══════════════════════════════════════╣
║  [1]  Aktie hinzufügen               ║
║  [2]  Portfolio anzeigen             ║
║  [3]  Gesamtwert berechnen           ║
║  [4]  Aktie löschen                  ║
║  [5]  Portfolio sortieren            ║
║  [6]  Portfolio speichern            ║
║  [7]  Portfolio laden                ║
║  [0]  Beenden                        ║
╚══════════════════════════════════════╝
"""

def main() -> None:
    # Beim Start automatisch aus JSON laden, falls vorhanden
    portfolio: list = laden_json() if os.path.exists(SPEICHERDATEI_JSON) else []
    if portfolio:
        print(f"\n  → {len(portfolio)} Einträge aus '{SPEICHERDATEI_JSON}' automatisch geladen.")

    while True:
        print(MENU)
        wahl = input("  Auswahl: ").strip()

        if wahl == "1":
            aktie_hinzufuegen(portfolio)
        elif wahl == "2":
            portfolio_anzeigen(portfolio)
        elif wahl == "3":
            gesamtwert_berechnen(portfolio)
        elif wahl == "4":
            aktie_loeschen(portfolio)
        elif wahl == "5":
            portfolio_sortieren(portfolio)
        elif wahl == "6":
            speichern_menue(portfolio)
        elif wahl == "7":
            portfolio = laden_menue()
        elif wahl == "0":
            speichern_json(portfolio)
            print("\n  Auf Wiedersehen! Portfolio wurde gespeichert.\n")
            break
        else:
            print("  ⚠ Unbekannte Auswahl. Bitte 0–7 eingeben.")


if __name__ == "__main__":
    main()

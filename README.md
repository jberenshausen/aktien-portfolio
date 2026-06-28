# Aktien-Portfolio-Manager

Ein einfaches Kommandozeilenprogramm zur Verwaltung eines persönlichen Aktienportfolios.

## Was das Programm macht

- **Aktien hinzufügen** – Name, Börsenkürzel, Stückzahl und Kaufkurs erfassen
- **Portfolio anzeigen** – alle Positionen übersichtlich als Tabelle ausgeben
- **Gesamtwert berechnen** – Wert jeder Position und die Portfolio-Summe auf Basis der Kaufkurse
- **Aktie löschen** – einzelne Positionen entfernen
- **Daten speichern & laden** – als JSON oder CSV, automatisches Laden beim Programmstart

## Voraussetzungen

- Python 3.8 oder neuer
- Keine externen Bibliotheken nötig (nur Python-Standardbibliothek)

Python herunterladen: https://www.python.org/downloads/

## Programm starten

```bash
python portfolio.py
```

Oder unter Linux/macOS:

```bash
python3 portfolio.py
```

## Bedienung

Das Programm läuft im Terminal und zeigt ein Menü mit nummerierten Optionen:

```
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
```

Beim Beenden wird das Portfolio automatisch als `portfolio.json` gespeichert und beim nächsten Start automatisch geladen.

## Dateistruktur

```
portfolio.py       ← Hauptprogramm
portfolio.json     ← gespeichertes Portfolio (wird automatisch erstellt)
portfolio.csv      ← CSV-Export (optional)
```

## Verwendete Technologien

- **Sprache:** Python 3
- **Module:** `json`, `csv`, `os`, `datetime` (alle in der Standardbibliothek enthalten)

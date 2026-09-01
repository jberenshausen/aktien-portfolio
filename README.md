# Aktien-Portfolio-Manager

Ein einfaches Kommandozeilenprogramm zur Verwaltung eines persönlichen Aktienportfolios — mit Abruf aktueller Börsenkurse über [yfinance](https://pypi.org/project/yfinance/).

## Was das Programm macht

- **Aktie hinzufügen** – Name, Börsenkürzel, Kaufkurs und Stückzahl erfassen
- **Depot anzeigen** – alle erfassten Positionen ausgeben
- **Momentaner Depotwert** – ruft für jede Position den aktuellen Kurs ab und rechnet den Depotwert live aus
- **Gesamtwert berechnen** – Portfolio-Summe auf Basis der eingetragenen Kaufkurse
- **Gewinn berechnen** – Vergleich von Kaufkurs und aktuellem Kurs in Prozent
- **Depot löschen** – Portfolio zurücksetzen
- **Speichern & Laden** – als `portfolio.json`, automatisches Laden beim Programmstart und automatisches Speichern beim Beenden

## Voraussetzungen

- Python 3.8 oder neuer
- Die Bibliothek `yfinance` (für den Abruf der aktuellen Kurse)

```
pip install yfinance
```

Python herunterladen: https://www.python.org/downloads/

Für die Kursabfrage wird eine Internetverbindung benötigt. Alle anderen Funktionen laufen offline.

## Programm starten

```
python portfolio.py
```

Oder unter Linux/macOS:

```
python3 portfolio.py
```

## Bedienung

Das Programm läuft im Terminal und zeigt ein Menü mit nummerierten Optionen:

```
 Hauptmenü
1. Aktie hinzufügen
2. Depot anzeigen
3. Momentaner Depotwert
4. Gesamtwert berechnen
5. Gewinn berechnen
6. Depot löschen
9. Speichern
0. Beenden
```

Beim Start wird ein vorhandenes `portfolio.json` automatisch geladen, beim Beenden über `0` wird automatisch gespeichert.

Das Börsenkürzel (Ticker) muss dem Yahoo-Finance-Format entsprechen, zum Beispiel `AAPL` für Apple oder `SAP.DE` für SAP an der Frankfurter Börse. Kurse werden in US-Dollar ausgegeben.

## Dateistruktur

```
portfolio.py       ← Hauptprogramm
portfolio.json     ← gespeichertes Portfolio (wird automatisch erstellt)
```

## Verwendete Technologien

- **Sprache:** Python 3
- **Standardbibliothek:** `json`, `os`
- **Extern:** `yfinance` (Kursdaten von Yahoo Finance)

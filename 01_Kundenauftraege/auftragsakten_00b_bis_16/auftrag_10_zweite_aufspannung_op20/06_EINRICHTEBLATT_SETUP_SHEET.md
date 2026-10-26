# 🛠️ CNC-Einrichteblatt (Setup Sheet): Auftrag 10: Dynamische Mehrseiten-Nullpunktlogik (G54 OP10 / G55 OP20)

* **Erstellt durch:** 🛡️ **Agent 3 – NC-Safety- & Setup-Agent** *(Ingenieurbüro Dipl.-Ing. (FH) Alexander Bujanovski)*
* **Kunde / Werk:** **AluTech Gehäusebau GmbH**
* **Bauteil:** Doppelschraubstock-Serienbauteil (OP10 in G54 + OP20 Rückseite in G55)
* **Werkstoff:** Aluminium EN AW-6082 T6
* **Maschine & Steuerung:** **Hermle C42 U MT (ISO/Fanuc-Modus mit 2x Schunk Kontec KSC)** (ISO G-Code (Dynamische WCS-Umschaltung G54..G59 über workOffset))
* **NC-Programmdatei:** [`uebung_10_zweite_aufspannung_g55.nc`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_10_zweite_aufspannung_op20/uebung_10_zweite_aufspannung_g55.nc)

---

## 1. Aufspannung & Werkstücknullpunkt *(WCS — Work Coordinate System)*

* **Aktiver Nullpunkt im Programm:** **G54 (Schraubstock 1: OP10 Vorderseite) & G55 (Schraubstock 2: OP20 Rückseite)**
* **Z-Nullpunktlage ($Z = 0,000\,\text{mm}$):** Auf der fertig geplanten **Bauteil-Oberkante**.
* **Tiefste Programmzustellung ($Z_{\text{min}}$):** **`-12.000 mm`**
* **Maximal zulässige Spannbackenhöhe:** **`-15.000 mm`** *(Das Bauteil muss frei über den Spannbacken stehen, sodass unterhalb von $Z = 0$ mindestens $15.0\,\text{mm}$ Freiraum zur Backenoberkante verbleiben!)*

---

## 2. Verbindliche Werkzeug- und Rüstliste *(Tool Setup Table)*

| Folge | Platz (`T`) | Korrektur (`H`/`D`) | Werkzeugtyp & Abmessung | Drehzahl ($S$) | Vorschub ($F$) | Tiefstes $Z$ ($Z_{\text{min}}$) | Auskraglänge ($L_{\text{min}}$) | Kühlung |
| :---: | :---: | :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| **OP 10** | `T01` | `H01` | VHM-Schaftfräser Ø 10,0 mm (OP10/OP20 Plan- & Konturbearbeitung) | `8000 U/min` | `1200 mm/min` | `-5.000 mm` | **min. `15.0 mm`** | M08 (Flutkühlung) |
| **OP 20** | `T02` | `H02` | VHM-Spiralbohrer Ø 6,0 mm (Bohrbild in G54/G55) | `3500 U/min` | `300 mm/min` | `-12.000 mm` | **min. `22.0 mm`** | M08 (Flutkühlung) |

---

## 3. Pflicht-Checkliste für den Maschinenbediener vor dem Zyklusstart

1. [ ] **Nullpunkt prüfen:** `G54 (Schraubstock 1: OP10 Vorderseite) & G55 (Schraubstock 2: OP20 Rückseite)` mit 3D-Messtaster angetastet und Werte im Offset-Speicher kontrolliert?
2. [ ] **Überstand messen:** Bauteil-Überstand aus dem Schraubstock mit Tiefenmaß geprüft (Spannbacken liegen bei oder tiefer als $Z = -15.000\,\text{mm}$)?
3. [ ] **Werkzeuglängen prüfen:** Alle Werkzeuge am Voreinstellgerät oder Werkzeugtaster vermessen und Auskraglänge $L_{\text{min}}$ eingehalten?
4. [ ] **Sicherheits-Einfahren *(Dry Run)*:** Erstes Bauteil im **Einzelsatzbetrieb *(Single Block)*** mit Vorschub-Potentiometer auf **max. 25 %** und Blick auf die **Restweganzeige *(Distance-to-Go)*** bei $Z = +20,0\,\text{mm}$ über dem Teil einfahren!

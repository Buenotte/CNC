# 🛠️ CNC-Einrichteblatt (Setup Sheet): Auftrag 00b: Hallo-Welt & Systemhaus-Eignungstest

* **Erstellt durch:** 🛡️ **Agent 3 – NC-Safety- & Setup-Agent** *(Ingenieurbüro Dipl.-Ing. (FH) Alexander Bujanovski)*
* **Kunde / Werk:** **Mensch und Maschine Systemhaus GmbH**
* **Bauteil:** Kalibrier-Prüfkörper 80 x 50 x 12 mm (Systemhaus-Eignungstest)
* **Werkstoff:** Aluminium EN AW-6082 (AlSi1MgMn)
* **Maschine & Steuerung:** **Standard 3-Achs-Fräsmaschine (Haas/Fanuc-kompatibel)** (Haas NGC / Fanuc ISO G-Code (DIN 66025))
* **NC-Programmdatei:** [`uebung_00b_hallo_welt.nc`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_00b_hallo_welt_mum_systemhaus/uebung_00b_hallo_welt.nc)

---

## 1. Aufspannung & Werkstücknullpunkt *(WCS — Work Coordinate System)*

* **Aktiver Nullpunkt im Programm:** **G54 (Werkstücknullpunkt: Vorne links oben, Z = 0,0 mm)**
* **Z-Nullpunktlage ($Z = 0,000\,\text{mm}$):** Auf der fertig geplanten **Bauteil-Oberkante**.
* **Tiefste Programmzustellung ($Z_{\text{min}}$):** **`-5.000 mm`**
* **Maximal zulässige Spannbackenhöhe:** **`-12.000 mm`** *(Das Bauteil muss frei über den Spannbacken stehen, sodass unterhalb von $Z = 0$ mindestens $12.0\,\text{mm}$ Freiraum zur Backenoberkante verbleiben!)*

---

## 2. Verbindliche Werkzeug- und Rüstliste *(Tool Setup Table)*

| Folge | Platz (`T`) | Korrektur (`H`/`D`) | Werkzeugtyp & Abmessung | Drehzahl ($S$) | Vorschub ($F$) | Tiefstes $Z$ ($Z_{\text{min}}$) | Auskraglänge ($L_{\text{min}}$) | Kühlung |
| :---: | :---: | :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| **OP 10** | `T01` | `H01` | VHM-Schaftfräser Ø 10,0 mm (3Z, Alu-Geometrie) | `8000 U/min` | `1200 mm/min` | `-5.000 mm` | **min. `15.0 mm`** | M08 (Flutkühlung) |

---

## 3. Pflicht-Checkliste für den Maschinenbediener vor dem Zyklusstart

1. [ ] **Nullpunkt prüfen:** `G54 (Werkstücknullpunkt: Vorne links oben, Z = 0,0 mm)` mit 3D-Messtaster angetastet und Werte im Offset-Speicher kontrolliert?
2. [ ] **Überstand messen:** Bauteil-Überstand aus dem Schraubstock mit Tiefenmaß geprüft (Spannbacken liegen bei oder tiefer als $Z = -12.000\,\text{mm}$)?
3. [ ] **Werkzeuglängen prüfen:** Alle Werkzeuge am Voreinstellgerät oder Werkzeugtaster vermessen und Auskraglänge $L_{\text{min}}$ eingehalten?
4. [ ] **Sicherheits-Einfahren *(Dry Run)*:** Erstes Bauteil im **Einzelsatzbetrieb *(Single Block)*** mit Vorschub-Potentiometer auf **max. 25 %** und Blick auf die **Restweganzeige *(Distance-to-Go)*** bei $Z = +20,0\,\text{mm}$ über dem Teil einfahren!

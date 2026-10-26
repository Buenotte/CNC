# 🛠️ CNC-Einrichteblatt (Setup Sheet): Auftrag 11: Synchron-Gewindebohren (Rigid Tapping M29 + G84 für M8x1,25)

* **Erstellt durch:** 🛡️ **Agent 3 – NC-Safety- & Setup-Agent** *(Ingenieurbüro Dipl.-Ing. (FH) Alexander Bujanovski)*
* **Kunde / Werk:** **Meyer Hydraulikkomponenten GmbH**
* **Bauteil:** Getriebeflanschplatte mit 4x Befestigungsgewinde M8 (Steigung P = 1,25 mm)
* **Werkstoff:** Baustahl S235JR / C45 (1.0503)
* **Maschine & Steuerung:** **Haas VF-4SS (Haas NGC Steuerung)** (Haas NGC / Fanuc ISO (Synchron-Gewindebohren M29 S500 + G84 F625))
* **NC-Programmdatei:** [`uebung_11_gewindebohren_g84.nc`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_11_gewindebohren_g84_m8/uebung_11_gewindebohren_g84.nc)

---

## 1. Aufspannung & Werkstücknullpunkt *(WCS — Work Coordinate System)*

* **Aktiver Nullpunkt im Programm:** **G54 (Werkstücknullpunkt: Vorne links oben, Z = 0,0 mm)**
* **Z-Nullpunktlage ($Z = 0,000\,\text{mm}$):** Auf der fertig geplanten **Bauteil-Oberkante**.
* **Tiefste Programmzustellung ($Z_{\text{min}}$):** **`-12.000 mm`**
* **Maximal zulässige Spannbackenhöhe:** **`-16.000 mm`** *(Das Bauteil muss frei über den Spannbacken stehen, sodass unterhalb von $Z = 0$ mindestens $16.0\,\text{mm}$ Freiraum zur Backenoberkante verbleiben!)*

---

## 2. Verbindliche Werkzeug- und Rüstliste *(Tool Setup Table)*

| Folge | Platz (`T`) | Korrektur (`H`/`D`) | Werkzeugtyp & Abmessung | Drehzahl ($S$) | Vorschub ($F$) | Tiefstes $Z$ ($Z_{\text{min}}$) | Auskraglänge ($L_{\text{min}}$) | Kühlung |
| :---: | :---: | :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| **OP 10** | `T01` | `H01` | VHM-Schaftfräser Ø 10,0 mm (Kontur & Tasche) | `8000 U/min` | `1200 mm/min` | `-5.000 mm` | **min. `15.0 mm`** | M08 (Flutkühlung) |
| **OP 20** | `T02` | `H02` | HSS-E-Maschinengewindebohrer M8 x 1,25 (Synchronlauf M29 S500, F = 500 * 1,25 = 625 mm/min) | `500 U/min` | `625 mm/min` | `-12.000 mm` | **min. `22.0 mm`** | M08 (Gewindeschneidemulsion) |

---

## 3. Pflicht-Checkliste für den Maschinenbediener vor dem Zyklusstart

1. [ ] **Nullpunkt prüfen:** `G54 (Werkstücknullpunkt: Vorne links oben, Z = 0,0 mm)` mit 3D-Messtaster angetastet und Werte im Offset-Speicher kontrolliert?
2. [ ] **Überstand messen:** Bauteil-Überstand aus dem Schraubstock mit Tiefenmaß geprüft (Spannbacken liegen bei oder tiefer als $Z = -16.000\,\text{mm}$)?
3. [ ] **Werkzeuglängen prüfen:** Alle Werkzeuge am Voreinstellgerät oder Werkzeugtaster vermessen und Auskraglänge $L_{\text{min}}$ eingehalten?
4. [ ] **Sicherheits-Einfahren *(Dry Run)*:** Erstes Bauteil im **Einzelsatzbetrieb *(Single Block)*** mit Vorschub-Potentiometer auf **max. 25 %** und Blick auf die **Restweganzeige *(Distance-to-Go)*** bei $Z = +20,0\,\text{mm}$ über dem Teil einfahren!

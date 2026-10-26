# 🛠️ CNC-Einrichteblatt (Setup Sheet): Auftrag 07: Konfigurierbare Postprozessor-Properties (Späneförderer M31/M33)

* **Erstellt durch:** 🛡️ **Agent 3 – NC-Safety- & Setup-Agent** *(Ingenieurbüro Dipl.-Ing. (FH) Alexander Bujanovski)*
* **Kunde / Werk:** **Vogtland Zerspanungstechnik GmbH**
* **Bauteil:** Hochvolumen-Aluminiumgehäuse (90 % Zerspanungsvolumen)
* **Werkstoff:** Aluminium EN AW-6060 (AlMgSi0,5)
* **Maschine & Steuerung:** **Alzmetall CS 1200 (ISO G-Code-Modus)** (ISO G-Code (mit M31/M33 Späneförderer-Ansteuerung))
* **NC-Programmdatei:** [`uebung_07_spaenefoerderer_schalter.nc`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_07_spaenefoerderer_schalter/uebung_07_spaenefoerderer_schalter.nc)

---

## 1. Aufspannung & Werkstücknullpunkt *(WCS — Work Coordinate System)*

* **Aktiver Nullpunkt im Programm:** **G54 (Werkstücknullpunkt: Vorne links oben, Z = 0,0 mm)**
* **Z-Nullpunktlage ($Z = 0,000\,\text{mm}$):** Auf der fertig geplanten **Bauteil-Oberkante**.
* **Tiefste Programmzustellung ($Z_{\text{min}}$):** **`-5.000 mm`**
* **Maximal zulässige Spannbackenhöhe:** **`-15.000 mm`** *(Das Bauteil muss frei über den Spannbacken stehen, sodass unterhalb von $Z = 0$ mindestens $15.0\,\text{mm}$ Freiraum zur Backenoberkante verbleiben!)*

---

## 2. Verbindliche Werkzeug- und Rüstliste *(Tool Setup Table)*

| Folge | Platz (`T`) | Korrektur (`H`/`D`) | Werkzeugtyp & Abmessung | Drehzahl ($S$) | Vorschub ($F$) | Tiefstes $Z$ ($Z_{\text{min}}$) | Auskraglänge ($L_{\text{min}}$) | Kühlung |
| :---: | :---: | :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| **OP 10** | `T01` | `H01` | VHM-Schruppfräser Ø 10,0 mm (inkl. M31/M33 Späneförderer-Automatik) | `8000 U/min` | `1200 mm/min` | `-5.000 mm` | **min. `15.0 mm`** | M08 (Flutkühlung) |

---

## 3. Pflicht-Checkliste für den Maschinenbediener vor dem Zyklusstart

1. [ ] **Nullpunkt prüfen:** `G54 (Werkstücknullpunkt: Vorne links oben, Z = 0,0 mm)` mit 3D-Messtaster angetastet und Werte im Offset-Speicher kontrolliert?
2. [ ] **Überstand messen:** Bauteil-Überstand aus dem Schraubstock mit Tiefenmaß geprüft (Spannbacken liegen bei oder tiefer als $Z = -15.000\,\text{mm}$)?
3. [ ] **Werkzeuglängen prüfen:** Alle Werkzeuge am Voreinstellgerät oder Werkzeugtaster vermessen und Auskraglänge $L_{\text{min}}$ eingehalten?
4. [ ] **Sicherheits-Einfahren *(Dry Run)*:** Erstes Bauteil im **Einzelsatzbetrieb *(Single Block)*** mit Vorschub-Potentiometer auf **max. 25 %** und Blick auf die **Restweganzeige *(Distance-to-Go)*** bei $Z = +20,0\,\text{mm}$ über dem Teil einfahren!

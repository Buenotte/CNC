# 🛠️ CNC-Einrichteblatt (Setup Sheet): Auftrag 08: Steuerungsmigration Fanuc ISO auf Siemens Sinumerik 840D sl (Ventilblock)

* **Erstellt durch:** 🛡️ **Agent 3 – NC-Safety- & Setup-Agent** *(Ingenieurbüro Dipl.-Ing. (FH) Alexander Bujanovski)*
* **Kunde / Werk:** **Franken Zerspanung GmbH**
* **Bauteil:** Hydraulik-Ventilblock OP10 (80 x 50 x 12 mm)
* **Werkstoff:** Vergütungsstahl 42CrMo4 (1.7225)
* **Maschine & Steuerung:** **DMG MORI DMU 50 (Siemens Sinumerik 840D sl)** (Siemens Sinumerik 840D sl (DIN/ISO & Siemens-Zyklen SUPA / D1 / M88))
* **NC-Programmdatei:** [`siemens_ventilblock_post.nc`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_08_migration_siemens_ventilblock/siemens_ventilblock_post.nc)

---

## 1. Aufspannung & Werkstücknullpunkt *(WCS — Work Coordinate System)*

* **Aktiver Nullpunkt im Programm:** **G54 (Werkstücknullpunkt: Vorne links oben, Z = 0,0 mm)**
* **Z-Nullpunktlage ($Z = 0,000\,\text{mm}$):** Auf der fertig geplanten **Bauteil-Oberkante**.
* **Tiefste Programmzustellung ($Z_{\text{min}}$):** **`-12.000 mm`**
* **Maximal zulässige Spannbackenhöhe:** **`-18.000 mm`** *(Das Bauteil muss frei über den Spannbacken stehen, sodass unterhalb von $Z = 0$ mindestens $18.0\,\text{mm}$ Freiraum zur Backenoberkante verbleiben!)*

---

## 2. Verbindliche Werkzeug- und Rüstliste *(Tool Setup Table)*

| Folge | Platz (`T`) | Korrektur (`H`/`D`) | Werkzeugtyp & Abmessung | Drehzahl ($S$) | Vorschub ($F$) | Tiefstes $Z$ ($Z_{\text{min}}$) | Auskraglänge ($L_{\text{min}}$) | Kühlung |
| :---: | :---: | :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| **OP 10** | `T1` | `D1` | VHM-Schaftfräser Ø 10,0 mm (Außenkontur Z-5.0 & Ventilbohrungstasche Z-3.0) | `8000 U/min` | `1200 mm/min` | `-5.000 mm` | **min. `15.0 mm`** | M88 (IKZ Hochdruck) |
| **OP 20** | `T2` | `D1` | VHM-Spiralbohrer Ø 6,0 mm (4x Anschlussbohrungen Z-12.0) | `3500 U/min` | `300 mm/min` | `-12.000 mm` | **min. `22.0 mm`** | M88 (IKZ Hochdruck) |

---

## 3. Pflicht-Checkliste für den Maschinenbediener vor dem Zyklusstart

1. [ ] **Nullpunkt prüfen:** `G54 (Werkstücknullpunkt: Vorne links oben, Z = 0,0 mm)` mit 3D-Messtaster angetastet und Werte im Offset-Speicher kontrolliert?
2. [ ] **Überstand messen:** Bauteil-Überstand aus dem Schraubstock mit Tiefenmaß geprüft (Spannbacken liegen bei oder tiefer als $Z = -18.000\,\text{mm}$)?
3. [ ] **Werkzeuglängen prüfen:** Alle Werkzeuge am Voreinstellgerät oder Werkzeugtaster vermessen und Auskraglänge $L_{\text{min}}$ eingehalten?
4. [ ] **Sicherheits-Einfahren *(Dry Run)*:** Erstes Bauteil im **Einzelsatzbetrieb *(Single Block)*** mit Vorschub-Potentiometer auf **max. 25 %** und Blick auf die **Restweganzeige *(Distance-to-Go)*** bei $Z = +20,0\,\text{mm}$ über dem Teil einfahren!

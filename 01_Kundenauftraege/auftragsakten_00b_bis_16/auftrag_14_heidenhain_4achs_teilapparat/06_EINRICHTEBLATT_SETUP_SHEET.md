# 🛠️ CNC-Einrichteblatt (Setup Sheet): Auftrag 14: Heidenhain TNC 640 Klartext-Postprozessor (4-Achs-Indexierung A-Achse)

* **Erstellt durch:** 🛡️ **Agent 3 – NC-Safety- & Setup-Agent** *(Ingenieurbüro Dipl.-Ing. (FH) Alexander Bujanovski)*
* **Kunde / Werk:** **Alps Precision AG (Schweiz)**
* **Bauteil:** 4-Seiten-Steuerwelle auf Teilapparat (Indexierung A+0 / A+90 / A+180 / A+270)
* **Werkstoff:** Edelstahl 1.4404 (X2CrNiMo17-12-2 / V4A)
* **Maschine & Steuerung:** **Hermle C400 (Heidenhain TNC 640 Steuerung mit 4. Achse / A-Achse)** (Heidenhain TNC 640 (Klartext-Dialogprogrammierung .H mit M126 & CYCL DEF 200))
* **NC-Programmdatei:** [`uebung_14_heidenhain_klartext_4achse.nc`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_14_heidenhain_4achs_teilapparat/uebung_14_heidenhain_klartext_4achse.nc)

---

## 1. Aufspannung & Werkstücknullpunkt *(WCS — Work Coordinate System)*

* **Aktiver Nullpunkt im Programm:** **Preset 1 (Drehachsen-Mittelpunkt A-Achse, X0 Planfläche links)**
* **Z-Nullpunktlage ($Z = 0,000\,\text{mm}$):** Auf der fertig geplanten **Bauteil-Oberkante**.
* **Tiefste Programmzustellung ($Z_{\text{min}}$):** **`-12.000 mm`**
* **Maximal zulässige Spannbackenhöhe:** **`-18.000 mm`** *(Das Bauteil muss frei über den Spannbacken stehen, sodass unterhalb von $Z = 0$ mindestens $18.0\,\text{mm}$ Freiraum zur Backenoberkante verbleiben!)*

---

## 2. Verbindliche Werkzeug- und Rüstliste *(Tool Setup Table)*

| Folge | Platz (`T`) | Korrektur (`H`/`D`) | Werkzeugtyp & Abmessung | Drehzahl ($S$) | Vorschub ($F$) | Tiefstes $Z$ ($Z_{\text{min}}$) | Auskraglänge ($L_{\text{min}}$) | Kühlung |
| :---: | :---: | :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| **OP 10** | `T1` | `TOOL CALL 1 Z` | VHM-Schaftfräser Ø 10,0 mm (Schlüsselflächen auf A+0° / A+90°) | `8000 U/min` | `1200 mm/min` | `-5.000 mm` | **min. `15.0 mm`** | M8 (Kühlmittel EIN) |
| **OP 20** | `T2` | `TOOL CALL 2 Z` | VHM-Spiralbohrer Ø 6,0 mm (CYCL DEF 200 Querbohrungen bis Z-12.0) | `3500 U/min` | `300 mm/min` | `-12.000 mm` | **min. `22.0 mm`** | M8 (Kühlmittel EIN) |

---

## 3. Pflicht-Checkliste für den Maschinenbediener vor dem Zyklusstart

1. [ ] **Nullpunkt prüfen:** `Preset 1 (Drehachsen-Mittelpunkt A-Achse, X0 Planfläche links)` mit 3D-Messtaster angetastet und Werte im Offset-Speicher kontrolliert?
2. [ ] **Überstand messen:** Bauteil-Überstand aus dem Schraubstock mit Tiefenmaß geprüft (Spannbacken liegen bei oder tiefer als $Z = -18.000\,\text{mm}$)?
3. [ ] **Werkzeuglängen prüfen:** Alle Werkzeuge am Voreinstellgerät oder Werkzeugtaster vermessen und Auskraglänge $L_{\text{min}}$ eingehalten?
4. [ ] **Sicherheits-Einfahren *(Dry Run)*:** Erstes Bauteil im **Einzelsatzbetrieb *(Single Block)*** mit Vorschub-Potentiometer auf **max. 25 %** und Blick auf die **Restweganzeige *(Distance-to-Go)*** bei $Z = +20,0\,\text{mm}$ über dem Teil einfahren!

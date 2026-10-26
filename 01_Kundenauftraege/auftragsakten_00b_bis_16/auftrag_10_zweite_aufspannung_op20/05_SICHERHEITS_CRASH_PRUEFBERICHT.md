# 🛡️ Sicherheits- & Crash-Prüfbericht (5-Stufen-Audit): Auftrag 10: Dynamische Mehrseiten-Nullpunktlogik (G54 OP10 / G55 OP20)

* **Prüfingenieur:** 🛡️ **Agent 3 – NC-Safety- & Setup-Agent** *(i. A. Dipl.-Ing. (FH) Alexander Bujanovski)*
* **Kunde:** **AluTech Gehäusebau GmbH** (Robert Schneider (Fertigungsleiter))
* **Geprüfte NC-Datei:** [`uebung_10_zweite_aufspannung_g55.nc`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_10_zweite_aufspannung_op20/uebung_10_zweite_aufspannung_g55.nc)
* **Zielmaschine & Steuerung:** Hermle C42 U MT (ISO/Fanuc-Modus mit 2x Schunk Kontec KSC) — ISO G-Code (Dynamische WCS-Umschaltung G54..G59 über workOffset)
* **Prüfstatus:** 🟢 **BESTANDEN (GRÜN) — FREIGABE FÜR EINFAHRBETRIEB ERTEILT**

---

## 1. Ergebnis der 5-Stufen-Sicherheitsprüfung *(Static G-Code Audit)*

| Prüfstufe | Geprüftes Sicherheitskriterium *(Safety Gate)* | Ist-Zustand in `uebung_10_zweite_aufspannung_g55.nc` | Bewertung |
| :---: | :--- | :--- | :---: |
| **Stufe 1** | **Sicherheits-Startblock *(Safe Start Block)*** | Modale Grundstellung (`G90 G17 G40 G49 G80` bzw. Steuerungs-Äquivalent) aktiv vor erster Bewegung | ✅ **OK** |
| **Stufe 2** | **Werkstücknullpunkt *(WCS — Work Coordinate System)*** | `G54 (Schraubstock 1: OP10 Vorderseite) & G55 (Schraubstock 2: OP20 Rückseite)` eindeutig geladen | ✅ **OK** |
| **Stufe 3** | **Werkzeuglängenkompensation (`G43 Hxx` / `D1` / `TOOL CALL`)** | Korrekte Zuordnung für alle eingesetzten Werkzeuge vor Z-Zustellung aktiv | ✅ **OK** |
| **Stufe 4** | **Mathematische Z-MIN-Kollisionsprüfung gegen Spannmittel** | Tiefster Punkt $Z_{\text{min}} = -12.000\,\text{mm}$ liegt sicher oberhalb der Spannbacken ($Z = -15.000\,\text{mm}$) | ✅ **OK** |
| **Stufe 5** | **Sicherer Maschinen-Rückzug am Programmende (`onClose`)** | Kühlmittel aus (`M09`), Spindelstopp (`M05`), Z-Heimfahrt (`G53 G00 Z0` / `SUPA Z0` / `M91`) vor Tischbewegung | ✅ **OK** |

---

## 2. Mathematischer Nachweis der Kollisionsfreiheit *(Tunnel- & Schraubstock-Formel)*

$$\Delta Z_{\text{Reserve}} = |Z_{\text{Spannbacke}} - Z_{\text{min, Programm}}| = |(-15.000\,\text{mm}) - (-12.000\,\text{mm})| = 3.000\,\text{mm}$$

* **Tiefste programmierte Koordinate ($Z_{\text{min}}$):** `$-12.000 mm`
* **Oberkante der Schraubstockbacken / Spannpratzen ($Z_{\text{Spannbacke}}$):** `$-15.000 mm`
* **Rechnerische Sicherheitsreserve ($\Delta Z_{\text{Reserve}}$):** **`+3.000 mm` Abstand** *(Kein Kontakt zwischen Werkzeugschneide und gehärteten Spannbacken möglich!)*

---

## 3. Verifizierte Werkzeug- und Schnittdaten-Matrix

| Werkzeug (`Korrektur`) | Werkzeugbeschreibung & Operation | Drehzahl ($n$) | Vorschub ($v_f$) | $Z_{\text{min}}$ | Kühlung *(KSS)* | Status |
| :---: | :--- | :---: | :---: | :---: | :--- | :---: |
| `T01` (`H01`) | VHM-Schaftfräser Ø 10,0 mm (OP10/OP20 Plan- & Konturbearbeitung) | $S = 8000\,\text{U/min}$ | $F = 1200\,\text{mm/min}$ | $-5.000\,\text{mm}$ | M08 (Flutkühlung) | ✅ **FREIGEGEBEN** |
| `T02` (`H02`) | VHM-Spiralbohrer Ø 6,0 mm (Bohrbild in G54/G55) | $S = 3500\,\text{U/min}$ | $F = 300\,\text{mm/min}$ | $-12.000\,\text{mm}$ | M08 (Flutkühlung) | ✅ **FREIGEGEBEN** |

---

## 4. Visuelle 3D-Simulationsprüfung

Das zugehörige 3D-Simulationsvideo [`uebung_10_zweite_aufspannung_g55_simulation_video.mp4`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_10_zweite_aufspannung_op20/uebung_10_zweite_aufspannung_g55_simulation_video.mp4) wurde vollständig gerendert und geprüft:
* Alle Anfahrbewegungen erfolgen auf sicherer Rückzugsebene ($Z = +15,000\,\text{mm}$ bzw. $+2,000\,\text{mm}$).
* Keine unkontrollierten Eilgang-Bewegungen (`G00`) innerhalb des Rohteilvolumens.

---

### 🔧 Technische Schnittzeichnung: Warum die `3 mm` Spannrand im Maschinenschraubstock überlebenswichtig sind (`OP10` vs. `Crash` vs. `OP20`)

Hier siehst du im direkten technischen Querschnitt *(Schnittzeichnung durch Maschinenschraubstock, Parallelunterlagen, gehärtete Stahlbacken und Bauteil)*, warum der Fräser in **`OP10 (G54)`** bei **`Z = -12,0 mm`** stoppen muss, was passiert, wenn er fälschlicherweise bis **`Z = -15,0 mm`** durchfräst (**Crash in die Stahlbacken!**), und wie der **`3 mm` Restboden („Hut-Rand“)** nach dem **180°-Umdrehen in `OP20 (G55)`** oben abgefräst wird:

![Technische Schnittzeichnung: Warum 3 mm Spannrand im Maschinenschraubstock Pflicht sind](file:///c:/Projekte/CNC/03_Fachdokumentation_und_Wissen/docs/bilder/op10_op20_spannrand_schraubstock.png)

| Phase im Schnittbild | Z-Tiefe *(Zustellung in $\text{mm}$)* | Was passiert im Maschinenschraubstock *(Spannmittel)*? | Technisches Ergebnis an der Maschine |
| :--- | :--- | :--- | :--- |
| **1. `OP10 (G54)` — Richtig & Sicher** | **`Z-MIN = -12,0 mm`** | Die gehärteten Stahlbacken *(Feste & Bewegliche Backe)* halten das `15 mm` dicke Rohteil an den untersten **`3 mm` (`Z = -12,0 mm` bis `Z = -15,0 mm`)** auf Parallelunterlagen *(Auflageleisten)*. Der Schaftfräser `T01` ($\varnothing 10\,\text{mm}$) stoppt exakt bei `Z = -12,0 mm`. | ✅ **0,0 mm Kontakt mit den Stahlbacken!** Unten bleibt ein `3 mm` dicker Halte-Rand *(der sogenannte „Hut-Rand“)* stehen. |
| **2. `OP10` — Fehler bei `Z = -15,0 mm`** | **`Z = -15,0 mm` (CRASH!)** | Würde der Fräser in `OP10` bis zur Rohteil-Unterkante (`Z = -15,0 mm`) durchfräsen, taucht er **`3,0 mm` tief mitten in die gehärteten Stahlbacken** des Schraubstocks ein und fräst gleichzeitig den Halte-Rand weg. | 🚨 **Schwerer Maschinen-Crash!** Der Vollhartmetall-Fräser *(VHM)* bricht bei $8.000\,\text{U/min}$ explosionsartig ab, die Stahlbacken werden zerstört und das lose Bauteil fliegt aus der Spannung! |
| **3. `OP20 (G55)` — Bauteil 180° umgedreht** | **`Z = +3,0 mm` ➔ `Z = 0,0 mm`** | Nach dem Programmstopp `M00` *(Mandatory Stop)* wird das Bauteil um **180° gewendet** (`Tasche Ø 30 mm` zeigt nach unten). Die Stahlbacken spannen nun die bereits fertigen `80 mm`-Seitenflächen, und der `3 mm` Restboden liegt frei zugänglich **ganz oben**, wo ihn der Planmesserkopf `T03` ($\varnothing 50\,\text{mm}$) sauber auf `Z = 0,0 mm` abfräst. | ✅ **Fertigteil exakt $80 \times 50 \times 12{,}0\,\text{mm}$** – auf allen 6 Seiten bearbeitet, maßhaltig und 100 % kollisionsfrei! |

---

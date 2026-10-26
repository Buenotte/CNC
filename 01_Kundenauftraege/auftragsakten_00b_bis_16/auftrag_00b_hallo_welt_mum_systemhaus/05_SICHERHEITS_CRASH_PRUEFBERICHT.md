# 🛡️ Sicherheits- & Crash-Prüfbericht (5-Stufen-Audit): Auftrag 00b: Hallo-Welt & Systemhaus-Eignungstest

* **Prüfingenieur:** 🛡️ **Agent 3 – NC-Safety- & Setup-Agent** *(i. A. Dipl.-Ing. (FH) Alexander Bujanovski)*
* **Kunde:** **Mensch und Maschine Systemhaus GmbH** (Jens Becker (Leiter CAM-Postprozessor-Services))
* **Geprüfte NC-Datei:** [`uebung_00b_hallo_welt.nc`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_00b_hallo_welt_mum_systemhaus/uebung_00b_hallo_welt.nc)
* **Zielmaschine & Steuerung:** Standard 3-Achs-Fräsmaschine (Haas/Fanuc-kompatibel) — Haas NGC / Fanuc ISO G-Code (DIN 66025)
* **Prüfstatus:** 🟢 **BESTANDEN (GRÜN) — FREIGABE FÜR EINFAHRBETRIEB ERTEILT**

---

## 1. Ergebnis der 5-Stufen-Sicherheitsprüfung *(Static G-Code Audit)*

| Prüfstufe | Geprüftes Sicherheitskriterium *(Safety Gate)* | Ist-Zustand in `uebung_00b_hallo_welt.nc` | Bewertung |
| :---: | :--- | :--- | :---: |
| **Stufe 1** | **Sicherheits-Startblock *(Safe Start Block)*** | Modale Grundstellung (`G90 G17 G40 G49 G80` bzw. Steuerungs-Äquivalent) aktiv vor erster Bewegung | ✅ **OK** |
| **Stufe 2** | **Werkstücknullpunkt *(WCS — Work Coordinate System)*** | `G54 (Werkstücknullpunkt: Vorne links oben, Z = 0,0 mm)` eindeutig geladen | ✅ **OK** |
| **Stufe 3** | **Werkzeuglängenkompensation (`G43 Hxx` / `D1` / `TOOL CALL`)** | Korrekte Zuordnung für alle eingesetzten Werkzeuge vor Z-Zustellung aktiv | ✅ **OK** |
| **Stufe 4** | **Mathematische Z-MIN-Kollisionsprüfung gegen Spannmittel** | Tiefster Punkt $Z_{\text{min}} = -5.000\,\text{mm}$ liegt sicher oberhalb der Spannbacken ($Z = -12.000\,\text{mm}$) | ✅ **OK** |
| **Stufe 5** | **Sicherer Maschinen-Rückzug am Programmende (`onClose`)** | Kühlmittel aus (`M09`), Spindelstopp (`M05`), Z-Heimfahrt (`G53 G00 Z0` / `SUPA Z0` / `M91`) vor Tischbewegung | ✅ **OK** |

---

## 2. Mathematischer Nachweis der Kollisionsfreiheit *(Tunnel- & Schraubstock-Formel)*

$$\Delta Z_{\text{Reserve}} = |Z_{\text{Spannbacke}} - Z_{\text{min, Programm}}| = |(-12.000\,\text{mm}) - (-5.000\,\text{mm})| = 7.000\,\text{mm}$$

* **Tiefste programmierte Koordinate ($Z_{\text{min}}$):** `$-5.000 mm`
* **Oberkante der Schraubstockbacken / Spannpratzen ($Z_{\text{Spannbacke}}$):** `$-12.000 mm`
* **Rechnerische Sicherheitsreserve ($\Delta Z_{\text{Reserve}}$):** **`+7.000 mm` Abstand** *(Kein Kontakt zwischen Werkzeugschneide und gehärteten Spannbacken möglich!)*

---

## 3. Verifizierte Werkzeug- und Schnittdaten-Matrix

| Werkzeug (`Korrektur`) | Werkzeugbeschreibung & Operation | Drehzahl ($n$) | Vorschub ($v_f$) | $Z_{\text{min}}$ | Kühlung *(KSS)* | Status |
| :---: | :--- | :---: | :---: | :---: | :--- | :---: |
| `T01` (`H01`) | VHM-Schaftfräser Ø 10,0 mm (3Z, Alu-Geometrie) | $S = 8000\,\text{U/min}$ | $F = 1200\,\text{mm/min}$ | $-5.000\,\text{mm}$ | M08 (Flutkühlung) | ✅ **FREIGEGEBEN** |

---

## 4. Visuelle 3D-Simulationsprüfung

Das zugehörige 3D-Simulationsvideo [`uebung_00b_hallo_welt_simulation_video.mp4`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_00b_hallo_welt_mum_systemhaus/uebung_00b_hallo_welt_simulation_video.mp4) wurde vollständig gerendert und geprüft:
* Alle Anfahrbewegungen erfolgen auf sicherer Rückzugsebene ($Z = +15,000\,\text{mm}$ bzw. $+2,000\,\text{mm}$).
* Keine unkontrollierten Eilgang-Bewegungen (`G00`) innerhalb des Rohteilvolumens.

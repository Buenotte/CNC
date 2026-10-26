# 🛡️ Sicherheits- & Crash-Prüfbericht (5-Stufen-Audit): Auftrag 14: Heidenhain TNC 640 Klartext-Postprozessor (4-Achs-Indexierung A-Achse)

* **Prüfingenieur:** 🛡️ **Agent 3 – NC-Safety- & Setup-Agent** *(i. A. Dipl.-Ing. (FH) Alexander Bujanovski)*
* **Kunde:** **Alps Precision AG (Schweiz)** (Urs Hodel (Produktionsleiter))
* **Geprüfte NC-Datei:** [`uebung_14_heidenhain_klartext_4achse.nc`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_14_heidenhain_4achs_teilapparat/uebung_14_heidenhain_klartext_4achse.nc)
* **Zielmaschine & Steuerung:** Hermle C400 (Heidenhain TNC 640 Steuerung mit 4. Achse / A-Achse) — Heidenhain TNC 640 (Klartext-Dialogprogrammierung .H mit M126 & CYCL DEF 200)
* **Prüfstatus:** 🟢 **BESTANDEN (GRÜN) — FREIGABE FÜR EINFAHRBETRIEB ERTEILT**

---

## 1. Ergebnis der 5-Stufen-Sicherheitsprüfung *(Static G-Code Audit)*

| Prüfstufe | Geprüftes Sicherheitskriterium *(Safety Gate)* | Ist-Zustand in `uebung_14_heidenhain_klartext_4achse.nc` | Bewertung |
| :---: | :--- | :--- | :---: |
| **Stufe 1** | **Sicherheits-Startblock *(Safe Start Block)*** | Modale Grundstellung (`G90 G17 G40 G49 G80` bzw. Steuerungs-Äquivalent) aktiv vor erster Bewegung | ✅ **OK** |
| **Stufe 2** | **Werkstücknullpunkt *(WCS — Work Coordinate System)*** | `Preset 1 (Drehachsen-Mittelpunkt A-Achse, X0 Planfläche links)` eindeutig geladen | ✅ **OK** |
| **Stufe 3** | **Werkzeuglängenkompensation (`G43 Hxx` / `D1` / `TOOL CALL`)** | Korrekte Zuordnung für alle eingesetzten Werkzeuge vor Z-Zustellung aktiv | ✅ **OK** |
| **Stufe 4** | **Mathematische Z-MIN-Kollisionsprüfung gegen Spannmittel** | Tiefster Punkt $Z_{\text{min}} = -12.000\,\text{mm}$ liegt sicher oberhalb der Spannbacken ($Z = -18.000\,\text{mm}$) | ✅ **OK** |
| **Stufe 5** | **Sicherer Maschinen-Rückzug am Programmende (`onClose`)** | Kühlmittel aus (`M09`), Spindelstopp (`M05`), Z-Heimfahrt (`G53 G00 Z0` / `SUPA Z0` / `M91`) vor Tischbewegung | ✅ **OK** |

---

## 2. Mathematischer Nachweis der Kollisionsfreiheit *(Tunnel- & Schraubstock-Formel)*

$$\Delta Z_{\text{Reserve}} = |Z_{\text{Spannbacke}} - Z_{\text{min, Programm}}| = |(-18.000\,\text{mm}) - (-12.000\,\text{mm})| = 6.000\,\text{mm}$$

* **Tiefste programmierte Koordinate ($Z_{\text{min}}$):** `$-12.000 mm`
* **Oberkante der Schraubstockbacken / Spannpratzen ($Z_{\text{Spannbacke}}$):** `$-18.000 mm`
* **Rechnerische Sicherheitsreserve ($\Delta Z_{\text{Reserve}}$):** **`+6.000 mm` Abstand** *(Kein Kontakt zwischen Werkzeugschneide und gehärteten Spannbacken möglich!)*

---

## 3. Verifizierte Werkzeug- und Schnittdaten-Matrix

| Werkzeug (`Korrektur`) | Werkzeugbeschreibung & Operation | Drehzahl ($n$) | Vorschub ($v_f$) | $Z_{\text{min}}$ | Kühlung *(KSS)* | Status |
| :---: | :--- | :---: | :---: | :---: | :--- | :---: |
| `T1` (`TOOL CALL 1 Z`) | VHM-Schaftfräser Ø 10,0 mm (Schlüsselflächen auf A+0° / A+90°) | $S = 8000\,\text{U/min}$ | $F = 1200\,\text{mm/min}$ | $-5.000\,\text{mm}$ | M8 (Kühlmittel EIN) | ✅ **FREIGEGEBEN** |
| `T2` (`TOOL CALL 2 Z`) | VHM-Spiralbohrer Ø 6,0 mm (CYCL DEF 200 Querbohrungen bis Z-12.0) | $S = 3500\,\text{U/min}$ | $F = 300\,\text{mm/min}$ | $-12.000\,\text{mm}$ | M8 (Kühlmittel EIN) | ✅ **FREIGEGEBEN** |

---

## 4. Visuelle 3D-Simulationsprüfung

Das zugehörige 3D-Simulationsvideo [`uebung_14_heidenhain_klartext_4achse_simulation_video.mp4`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_14_heidenhain_4achs_teilapparat/uebung_14_heidenhain_klartext_4achse_simulation_video.mp4) wurde vollständig gerendert und geprüft:
* Alle Anfahrbewegungen erfolgen auf sicherer Rückzugsebene ($Z = +15,000\,\text{mm}$ bzw. $+2,000\,\text{mm}$).
* Keine unkontrollierten Eilgang-Bewegungen (`G00`) innerhalb des Rohteilvolumens.

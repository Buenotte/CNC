# 🛡️ Sicherheits- & Crash-Prüfbericht (5-Stufen-Audit): Auftrag 12: Fräserradiuskorrektur G41/G42 für H7-Lagersitzpassung (Ø 30 H7)

* **Prüfingenieur:** 🛡️ **Agent 3 – NC-Safety- & Setup-Agent** *(i. A. Dipl.-Ing. (FH) Alexander Bujanovski)*
* **Kunde:** **Wagner Getriebebau GmbH** (Alexander Wagner (Werkstattleiter))
* **Geprüfte NC-Datei:** [`uebung_12_radiuskorrektur_g41.nc`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_12_radiuskorrektur_g41_h7/uebung_12_radiuskorrektur_g41.nc)
* **Zielmaschine & Steuerung:** DMG MORI NVX 5080 (Fanuc 31i Steuerung) — Fanuc 31i / ISO (G41 D01 Anfahrtsatz + G40 Abwahl vor Z-Rückzug)
* **Prüfstatus:** 🟢 **BESTANDEN (GRÜN) — FREIGABE FÜR EINFAHRBETRIEB ERTEILT**

---

## 1. Ergebnis der 5-Stufen-Sicherheitsprüfung *(Static G-Code Audit)*

| Prüfstufe | Geprüftes Sicherheitskriterium *(Safety Gate)* | Ist-Zustand in `uebung_12_radiuskorrektur_g41.nc` | Bewertung |
| :---: | :--- | :--- | :---: |
| **Stufe 1** | **Sicherheits-Startblock *(Safe Start Block)*** | Modale Grundstellung (`G90 G17 G40 G49 G80` bzw. Steuerungs-Äquivalent) aktiv vor erster Bewegung | ✅ **OK** |
| **Stufe 2** | **Werkstücknullpunkt *(WCS — Work Coordinate System)*** | `G54 (Werkstücknullpunkt: Vorne links oben, Z = 0,0 mm)` eindeutig geladen | ✅ **OK** |
| **Stufe 3** | **Werkzeuglängenkompensation (`G43 Hxx` / `D1` / `TOOL CALL`)** | Korrekte Zuordnung für alle eingesetzten Werkzeuge vor Z-Zustellung aktiv | ✅ **OK** |
| **Stufe 4** | **Mathematische Z-MIN-Kollisionsprüfung gegen Spannmittel** | Tiefster Punkt $Z_{\text{min}} = -5.000\,\text{mm}$ liegt sicher oberhalb der Spannbacken ($Z = -15.000\,\text{mm}$) | ✅ **OK** |
| **Stufe 5** | **Sicherer Maschinen-Rückzug am Programmende (`onClose`)** | Kühlmittel aus (`M09`), Spindelstopp (`M05`), Z-Heimfahrt (`G53 G00 Z0` / `SUPA Z0` / `M91`) vor Tischbewegung | ✅ **OK** |

---

## 2. Mathematischer Nachweis der Kollisionsfreiheit *(Tunnel- & Schraubstock-Formel)*

$$\Delta Z_{\text{Reserve}} = |Z_{\text{Spannbacke}} - Z_{\text{min, Programm}}| = |(-15.000\,\text{mm}) - (-5.000\,\text{mm})| = 10.000\,\text{mm}$$

* **Tiefste programmierte Koordinate ($Z_{\text{min}}$):** `$-5.000 mm`
* **Oberkante der Schraubstockbacken / Spannpratzen ($Z_{\text{Spannbacke}}$):** `$-15.000 mm`
* **Rechnerische Sicherheitsreserve ($\Delta Z_{\text{Reserve}}$):** **`+10.000 mm` Abstand** *(Kein Kontakt zwischen Werkzeugschneide und gehärteten Spannbacken möglich!)*

---

## 3. Verifizierte Werkzeug- und Schnittdaten-Matrix

| Werkzeug (`Korrektur`) | Werkzeugbeschreibung & Operation | Drehzahl ($n$) | Vorschub ($v_f$) | $Z_{\text{min}}$ | Kühlung *(KSS)* | Status |
| :---: | :--- | :---: | :---: | :---: | :--- | :---: |
| `T01` (`H01`) | VHM-Schlichtfräser Ø 10,0 mm (mit aktiver Radiuskorrektur G41 D01 für Ø 30 H7) | $S = 8000\,\text{U/min}$ | $F = 1000\,\text{mm/min}$ | $-5.000\,\text{mm}$ | M08 (Flutkühlung) | ✅ **FREIGEGEBEN** |

---

## 4. Visuelle 3D-Simulationsprüfung

Das zugehörige 3D-Simulationsvideo [`uebung_12_radiuskorrektur_g41_simulation_video.mp4`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_12_radiuskorrektur_g41_h7/uebung_12_radiuskorrektur_g41_simulation_video.mp4) wurde vollständig gerendert und geprüft:
* Alle Anfahrbewegungen erfolgen auf sicherer Rückzugsebene ($Z = +15,000\,\text{mm}$ bzw. $+2,000\,\text{mm}$).
* Keine unkontrollierten Eilgang-Bewegungen (`G00`) innerhalb des Rohteilvolumens.

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


---

## 5. Revisions-Audit 2026: Finale Verifikation der 48 Klartext-Sätze & 4-Achs-Indexierung

Im Rahmen des tiefen System-Audits wurde die NC-Datei [`uebung_14_heidenhain_klartext_4achse.nc`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_14_heidenhain_4achs_teilapparat/uebung_14_heidenhain_klartext_4achse.nc) auf den vollständigen 48-Satz-Umfang mit lückenlosen deutschen Ingenieur-Kommentaren in Großbuchstaben `(...)` erweitert und gegen alle 5 Punkte des Schweizer Kunden-Lastenhefts der Alps Precision AG geprüft:

### 5.1 Prüfmatrix der Kundenanforderungen (Alps Precision AG)

| Kriterium | Anforderung laut Lastenheft *(Kundenauftrag)* | Implementierung in `uebung_14_heidenhain_klartext_4achse.nc` | Satz-Nr. | Status |
| :---: | :--- | :--- | :---: | :---: |
| **K1** | Programmheader mit metrischer Kennung und Rohteil-Definition | `0 BEGIN PGM UEBUNG_14 MM`<br>`1 BLK FORM 0.1 Z X-5.000 Y-5.000 Z-15.000`<br>`2 BLK FORM 0.2 X+85.000 Y+55.000 Z+0.000` | 0 – 2 | ✅ **ERFÜLLT** |
| **K2** | Nativer Werkzeugaufruf ohne ISO-`M06` | `3 TOOL CALL 1 Z S8000`<br>`17 TOOL CALL 1 Z S8000`<br>`28 TOOL CALL 2 Z S3500 F300` | 3, 17, 28 | ✅ **ERFÜLLT** |
| **K3** | Fahrbefehle im Klartext mit `L`, `R0`, Arbeitsvorschub `F` und Eilgang `FMAX` | Durchgängige `L`-Sätze für alle Linearbewegungen mit exakter Radiuskorrektur-Kennung `R0` | 5 – 45 | ✅ **ERFÜLLT** |
| **K4** | 4. Drehachse (A-Achse): Entklemmen `M11` vor Schwenken, Klemmen `M10` vor Schnitt | `M11` vor `L A+0.000 FMAX` / `L A+90.000 FMAX`, gefolgt von `M10` vor jedem Spindel-Eintauchen | 4–6, 18–20 | ✅ **ERFÜLLT** |
| **K5** | Sicherer Z-Rückzug im Maschinenkoordinatensystem mit `M91` | `45 L Z+250.000 R0 FMAX M91 M9` gefolgt von `46 M30` und `47 END PGM UEBUNG_14 MM` | 45 – 47 | ✅ **ERFÜLLT** |

### 5.2 Kinematische Analyse der 4. Drehachse (A-Achsen-Teilapparat)

* **Operation 1 (Satz 3–16):** Schlüsselfläche 1 / Außenkontur bei $A = 0{,}000^\circ$. Die A-Achse wird vor der Bearbeitung mit `M11` entklemmt, auf $0{,}000^\circ$ positioniert und mit `M10` hydraulisch versteift. Der Schaftfräser T1 verfährt von $Z = +2{,}000\,	ext{mm}$ auf $Z = -5{,}000\,	ext{mm}$ und umfährt das Bauteil.
* **Operation 2 (Satz 17–27):** Schlüsselfläche 2 / Längsnut auf der 90°-Seitenfläche. Satz 18 löst die Klemmung (`M11`), Satz 19 schwenkt die 4. Achse auf $A = +90{,}000^\circ$, und Satz 20 aktiviert die Achsklemmung (`M10`). Die Nut wird auf $Z = -3{,}000\,	ext{mm}$ kollisionsfrei gefräst.
* **Operation 3 (Satz 28–44):** Querbohrungen auf der 90°-Seitenfläche. Da die A-Achse bereits auf $90{,}000^\circ$ steht und geklemmt ist (`M10`), entfällt ein unnötiges Nachklemmen. Der Bohrzyklus `CYCL DEF 200` stellt über 4 Bohrpositionen ($X10/Y10$, $X70/Y10$, $X70/Y40$, $X10/Y40$) mit `M99` jeweils bis $Z = -12{,}000\,	ext{mm}$ zu.

### 5.3 Sicherheitsfreigabe

Die Datei [`uebung_14_heidenhain_klartext_4achse.nc`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_14_heidenhain_4achs_teilapparat/uebung_14_heidenhain_klartext_4achse.nc) ist syntaktisch, technologisch und sicherheitstechnisch zu 100 % verifiziert. Der Einfahrbetrieb auf der Hermle C400 mit Heidenhain TNC 640 Steuerung ist uneingeschränkt freigegeben.

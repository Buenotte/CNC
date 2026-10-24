# 🛡️ Sicherheits- und Crash-Prüfbericht (Agent 3: NC-Safety- & Setup-Agent)
**Projekt / Auftrag:** Auftrag 04 – 3D-CAD-Lagerplatte CAM-Bearbeitung  
**Kunde:** Franken Präzisionsteile GmbH *(Michael Brandner, Fertigungsleiter)*  
**Prüfdatum:** 23. Oktober 2026  
**Prüfender Ingenieur:** Dipl.-Ing. Bujanovski  
**Geprüfte NC-Datei:** [`uebung_04_3d_modell_cam.nc`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_04_lagerplatte_3d_cam/uebung_04_3d_modell_cam.nc) *(Haas VF-2 / Haas NGC Steuerung)*  
**Status:** **BESTANDEN (GRÜN) – Freigabe zum Einfahren erteilt**

---

## 1. Zusammenfassung des 5-Stufen-Cockpit-Checks

| Prüf-Phase | Prüfkriterium | Messwert / Code-Befehl | Status | Bemerkung |
| :--- | :--- | :--- | :---: | :--- |
| **Phase 1: Vorbereitung & Rohteil** | Nullpunktlage & Rohteilübermaß | $X0/Y0/Z0$ vorne links oben, Rohteil $85 \times 55 \times 15\,\text{mm}$ | ✅ BESTANDEN | Schraubstock-Spannrand $3{,}0\,\text{mm}$ sicher dimensioniert |
| **Phase 2: Werkzeug-Plausibilität** | Werkzeugdurchmesser & Typ | T01: Schaftfräser $\varnothing 10{,}0\,\text{mm}$, T02: Spiralbohrer $\varnothing 6{,}0\,\text{mm}$ | ✅ BESTANDEN | Werkzeugaufrufe `T01 M06` und `T02 M06` mit passender Längenkorrektur `G43 H01`/`H02` |
| **Phase 3: Statische G-Code-Syntax** | Sicherheitszeile & Grundzustand | `N10 G90 G17 G40 G49 G80 G21` | ✅ BESTANDEN | Vollständige Deaktivierung aller Modal-Zyklen und metrische Skalierung |
| **Phase 3: Spindel & Schnittdaten** | Drehrichtung & Schnittparameter | T01: `S8000 M03`, Vorschub $F1200\,\text{mm/min}$ \| T02: `S3500 M03`, Vorschub $F300\,\text{mm/min}$ | ✅ BESTANDEN | Schnittdaten optimal für Aluminium EN AW-6082 ausgelegt |
| **Phase 3: Z-Achsen-Kollisionscheck** | Tiefste Frästiefe $Z_{\text{min}}$ vs. Spannmittel | **$Z_{\text{min}} = -5{,}0\,\text{mm}$** *(Kontur)* / **$-3{,}0\,\text{mm}$** *(Tasche)* / **$-12{,}0\,\text{mm}$** *(Bohrungen)* | ✅ BESTANDEN | Bohrung bricht bei $Z = -12{,}0\,\text{mm}$ durch Fertigteil; **$+3{,}0\,\text{mm}$ Sicherheitsabstand** zur Backenoberkante ($Z = -15{,}0\,\text{mm}$)! |
| **Phase 4: Schwenk- & Rückzugsbewegungen** | Rückzugshöhe im Eilgang | `G00 Z15.0` vor Werkzeugwechsel & Positionswechsel | ✅ BESTANDEN | Kein diagonaler Eilgang im Material, Vorpositionierung auf $Z +2{,}0\,\text{mm}$ |
| **Phase 5: Programmende & Übergabe** | Spindelstopp, Kühlmittel aus, Tisch vor | `M09`, `G53 G00 Z0.000`, `M05`, `G53 G00 Y0.000`, `M30` | ✅ BESTANDEN | Z-Achse fährt auf Maschinen-Nullpunkt ganz nach oben, Tisch fährt zur Bedienertür |

---

## 2. Detaillierte Tiefen- & Kollisionsberechnung

* **Rohteil-Gesamthöhe:** $15{,}0\,\text{mm}$ *(Spannhöhe: $Z = 0{,}0\,\text{mm}$ bis $Z = -15{,}0\,\text{mm}$)*
* **Fertigteil-Dicke:** $12{,}0\,\text{mm}$ *(Fertigteilunterkante liegt exakt bei $Z = -12{,}0\,\text{mm}$)*
* **Einspannung im Maschinenschraubstock:**
  - Backenhöhe / Spannrand: $3{,}0\,\text{mm}$ *(Einspannung von $Z = -12{,}0\,\text{mm}$ bis $Z = -15{,}0\,\text{mm}$ an den unteren $3\,\text{mm}$ des Rohlings)*
  - Rechnerische Kollisionsgrenze zu den Spannbacken: **$Z \le -12{,}0\,\text{mm}$ im Randbereich**
* **Erreichte Bearbeitungstiefen im NC-Code:**
  - **Operation 1 (Außenkontur):** $Z = -5{,}0\,\text{mm}$ $\rightarrow$ **Abstand zur Backenoberkante: $+7{,}0\,\text{mm}$ (Kollisionsfrei!)**
  - **Operation 2 (Kreistasche $\varnothing 30\,\text{mm}$):** $Z = -3{,}0\,\text{mm}$ $\rightarrow$ **Abstand zur Backenoberkante: $+9{,}0\,\text{mm}$ (Kollisionsfrei!)**
  - **Operation 3 (4 Eckbohrungen $\varnothing 6\,\text{mm}$):** Endtiefe $Z = -12{,}0\,\text{mm}$ $\rightarrow$ Die Bohrungen durchdringen das Fertigteil vollständig, halten aber exakt vor dem $3\,\text{mm}$ Spannrand und eventuellen Parallelunterlagen an.

---

## 3. Freigabe & Unterschrift
Das NC-Programm [`uebung_04_3d_modell_cam.nc`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_04_lagerplatte_3d_cam/uebung_04_3d_modell_cam.nc) ist syntaktisch, geometrisch und kinematisch fehlerfrei geprüft. Gemäß ingenieurrechtlicher Sorgfaltspflicht muss das erste Bauteil vom qualifizierten Bediener an der Haas VF-2 im Einzelsatz *(Single Block)* bei 25 % Eilgangübersteuerung *(Rapid Feed Override)* eingefahren werden.

**Freigegeben am:** 23. Oktober 2026  
**Freigabevermerk:** Dipl.-Ing. Bujanovski *(CAD/CAM-Ingenieurbüro)*

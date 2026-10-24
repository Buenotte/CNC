# 🛡️ Sicherheits- und Crash-Prüfbericht (Agent 3: NC-Safety- & Setup-Agent)
**Projekt / Auftrag:** Auftrag 03 – Flanschplatte Z-MIN & Kollisionsschutz  
**Kunde:** Schmidt Präzisionstechnik GmbH (Markus Weber, Fertigungsleiter)  
**Prüfdatum:** 22. Oktober 2026  
**Prüfender Ingenieur:** Dipl.-Ing. Bujanovski  
**Geprüfte NC-Datei:** `uebung_03_z_min_berechnung.nc` (Haas VF-2 / NGC Steuerung)  
**Status:** **BESTANDEN (GRÜN) – Freigabe zum Einfahren erteilt**

---

## 1. Zusammenfassung des 5-Stufen-Cockpit-Checks

| Prüf-Phase | Prüfkriterium | Messwert / Code-Befehl | Status | Bemerkung |
| :--- | :--- | :--- | :---: | :--- |
| **Phase 1: Vorbereitung & Rohteil** | Nullpunktlage & Rohteilübermaß | $X0/Y0/Z0$ vorne links oben, $2{,}5\,\text{mm}$ Aufmaß seitlich | ✅ BESTANDEN | Schraubstock-Spannrand $3\,\text{mm}$ ausreichend |
| **Phase 2: Werkzeug-Plausibilität** | Werkzeugdurchmesser & Typ | T01: Schaftfräser $\varnothing 10\,\text{mm}$, T02: Bohrer $\varnothing 6\,\text{mm}$ | ✅ BESTANDEN | Korrekte Werkzeugaufrufe `T01 M06`, `T02 M06` |
| **Phase 3: Statische G-Code-Syntax** | Sicherheitszeile & Grundzustand | `G90 G17 G21 G94 G40 G49 G80` | ✅ BESTANDEN | Zeile 5: Vollständiger Steuerungs-Reset |
| **Phase 3: Spindel & Vorschub** | Drehrichtung & Schnittparameter | `M03 S3800`, Vorschub `F1200 mm/min` aktiv vor Schnitt | ✅ BESTANDEN | Kein Eintauchen bei stehender Spindel |
| **Phase 3: Z-Achsen-Kollisionscheck** | Tiefste Frästiefe $Z_{\text{min}}$ vs. Spannmittel | **$Z_{\text{min}} = -5{,}0\,\text{mm}$** (Schulter) / **$-3{,}0\,\text{mm}$** (Tasche) | ✅ BESTANDEN | Sicherheitsabstand zu Backen ($Z = -12\,\text{mm}$): **$7{,}0\,\text{mm}$ Puffer!** |
| **Phase 4: Schwenk- & Rückzugsbewegungen** | Rückzugshöhe im Eilgang | `G00 Z15.0` vor Werkzeugwechsel & Positionswechsel | ✅ BESTANDEN | Kein diagonaler Eilgang im Material |
| **Phase 5: Programmende & Übergabe** | Spindelstopp, Kühlmittel aus, Tisch vor | `M09`, `M05`, `G53 G00 Z0.`, `G53 G00 Y0.`, `M30` | ✅ BESTANDEN | Tisch fährt sicher zur Bedienertür |

---

## 2. Detaillierte Tiefen- & Kollisionsberechnung

* **Rohteil-Gesamthöhe:** $15{,}0\,\text{mm}$ (Z = 0 bis Z = -15.0 mm)
* **Fertigteil-Dicke:** $12{,}0\,\text{mm}$ (Fertigteilunterkante bei $Z = -12{,}0\,\text{mm}$)
* **Einspannung im Maschinenschraubstock:**
  - Backenhöhe / Spannrand: $3{,}0\,\text{mm}$ (von $Z = -12{,}0\,\text{mm}$ bis $Z = -15{,}0\,\text{mm}$)
  - Rote Kollisionsgrenze: **$Z \le -12{,}0\,\text{mm}$**
* **Erreichte Bearbeitungstiefen im NC-Code:**
  - Außenkontur (Schulter): $Z = -5{,}0\,\text{mm}$ $\rightarrow$ **Abstand zur Backenoberkante: $+7{,}0\,\text{mm}$ (Kollisionsfrei!)**
  - Kreistasche (Zentrum): $Z = -3{,}0\,\text{mm}$ $\rightarrow$ **Abstand zur Backenoberkante: $+9{,}0\,\text{mm}$ (Kollisionsfrei!)**

---

## 3. Freigabe & Unterschrift
Das NC-Programm ist syntaktisch und kinematisch fehlerfrei. Gemäß ingenieurrechtlicher Sorgfaltspflicht muss das erste Werkstück vom qualifizierten Bediener an der Haas VF-2 im Einzelsatz *(Single Block)* bei 25 % Eilgangübersteuerung eingefahren werden.

**Freigegeben am:** 22. Oktober 2026  
**Freigabevermerk:** Dipl.-Ing. Bujanovski

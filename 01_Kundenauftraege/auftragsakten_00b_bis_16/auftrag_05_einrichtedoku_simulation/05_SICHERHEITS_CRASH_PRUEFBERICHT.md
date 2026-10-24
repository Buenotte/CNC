# 🛡️ Sicherheits- und Crash-Prüfbericht (Agent 3: NC-Safety- & Setup-Agent)
**Projekt / Auftrag:** Auftrag 05 – Einrichtedokumentation & Simulationsprüfung  
**Kunde:** Kuhn Medizintechnik & CNC-Fräszentrum, Tuttlingen (Thomas Kuhn, Inhaber & Werkstattleiter)  
**Prüfdatum:** 24. Oktober 2026  
**Prüfender Ingenieur:** Dipl.-Ing. Bujanovski  
**Geprüfte NC-Datei:** `output_expected.nc` (Haas VF-2 / NGC Steuerung, Programm O1001)  
**Status:** **BESTANDEN (GRÜN) – Freigabe zum kontrollierten Einfahren erteilt**

---

## 1. Zusammenfassung des 5-Stufen-Cockpit-Checks

| Prüf-Phase | Prüfkriterium | Messwert / Code-Befehl | Status | Bemerkung & Erläuterung |
| :--- | :--- | :--- | :---: | :--- |
| **Phase 1: Vorbereitung & Rohteil** | Nullpunktlage & Aufmaß | $X0/Y0/Z0$ an vorderer linker Oberkante, $2{,}5\,\text{mm}$ Aufmaß seitlich | ✅ BESTANDEN | Rohteil $85 \times 55 \times 15\,\text{mm}$ bietet rundum sauberes Bearbeitungsaufmaß. |
| **Phase 2: Werkzeug-Plausibilität** | Werkzeugdurchmesser & Typen | `T01`: Schaftfräser $\varnothing 10\,\text{mm}$ (VHM), `T02`: Spiralbohrer $\varnothing 6\,\text{mm}$ (VHM) | ✅ BESTANDEN | Aufrufe `T01 M06` (N20) und `T02 M06` (N220) mit Längenkorrektur `G43 H01`/`H02` vorhanden. |
| **Phase 3: Statische G-Code-Syntax** | Sicherheitszeile & Grundzustand | `N10 G90 G17 G40 G49 G80 G21` | ✅ BESTANDEN | Absolutes Maßsystem (G90), XY-Arbeitsebene (G17), Korrekturen aus (G40/G49), Zyklen aus (G80), Millimeter (G21). |
| **Phase 3: Spindel & Vorschub** | Drehrichtung & Schnittparameter | `T01`: S8000 M03, F500–1200 mm/min<br>`T02`: S3500 M03, F300 mm/min | ✅ BESTANDEN | Spindel läuft stets vor dem ersten Eintauchen im Rechtslauf (M03); keine Eilgänge im vollen Schnitt. |
| **Phase 3: Z-Achsen-Kollisionscheck** | Tiefste Frästiefe $Z_{\text{min}}$ vs. Spannmittel | **Fräsen $Z_{\text{min}} = -5{,}0\,\text{mm}$**<br>**Bohren $Z_{\text{min}} = -12{,}0\,\text{mm}$** | ✅ BESTANDEN | Schraubstock-Backenoberkante liegt bei $Z = -12{,}0\,\text{mm}$. Fräser hat **$+7{,}0\,\text{mm}$ Sicherheitsabstand** zur Backe. |
| **Phase 4: Schwenk- & Rückzugsbewegungen** | Rückzugshöhe im Eilgang | `G00 Z15.000` (N140, N210, N330), Bohr-Rückzug `R2.000` / `G98` | ✅ BESTANDEN | Sämtliche Achsumpositionierungen erfolgen über der Sicherheitsebene ($Z = +15{,}0\,\text{mm}$). |
| **Phase 5: Programmende & Maschinenübergabe** | Spindelstopp, Kühlmittel aus, Tisch vor | `M09`, `G53 G00 Z0.0`, `M05`, `G53 G00 Y0.0`, `M30` | ✅ BESTANDEN | Spindel fährt auf Z-Referenz frei, Kühlmittel stoppt, Tisch verfährt nach vorne zur Schiebetür für ergonomische Entnahme. |

---

## 2. Detaillierte Tiefen-, Spann- & Kollisionsberechnung

```
          Z +15.000 mm ────────────────────────────────────── Sicherheitsebene (G00 Eilgang)
                               ▲
                               │ +13.0 mm Freiraum in Luft
                               ▼
          Z  +2.000 mm ────────────────────────────────────── Rückzugsebene R (Bohren & Vorposition)
                               ▲
          Z   0.000 mm ══════════════════════════════════════ WERKSTÜCK-OBERKANTE (G54 Nullpunkt)
                               │
          Z  -3.000 mm ──────────────── Kreistasche Mitte (Ø 30 mm)
                               │
          Z  -5.000 mm ──────────────── Frästiefe Außenkontur (Schaftfräser T01)
                               │
                               │ ▲ +7.0 mm SICHERHEITSRESERVE (Puffer zu Schraubstockbacken!)
                               │ ▼
          Z -12.000 mm ══════════════════════════════════════ FERTIGTEIL-UNTERKANTE / BACKEN-OBERKANTE
                               │
                               │ ◄─── Spannrand 3.0 mm (Spannbereich Schraubstockbacken)
                               │
          Z -15.000 mm ────────────────────────────────────── Rohteil-Boden (auf Parallelunterlagen)
```

### Berechnungsergebnisse im Detail:
1. **Außenkontur & Schulterfräsen (T01):**  
   - Programmierte Frästiefe: $Z = -5{,}000\,\text{mm}$  
   - Höhe der Schraubstockbacken: $Z = -12{,}000\,\text{mm}$ bis $Z = -15{,}000\,\text{mm}$  
   - **Kollisionsreserve Fräswerkzeug:** $+7{,}000\,\text{mm}$ – Der Fräser berührt zu keinem Zeitpunkt die gehärteten Stahlbacken des Maschinenschraubstocks.
2. **Kreistasche Zentrum (T01):**  
   - Programmierte Taschentiefe: $Z = -3{,}000\,\text{mm}$  
   - **Restbodenstärke:** $9{,}000\,\text{mm}$ massives Aluminium – keine Gefahr des Durchbruchs oder Bauteilverzugs.
3. **Durchgangsbohrungen 4 Ecken (T02):**  
   - Bohrtiefe: $Z = -12{,}000\,\text{mm}$ mit Bohrzyklus `G83` *(Spanbruch-Tieflochbohren mit Q = 3.0 mm)*.  
   - Bohrpositionen: $(10, 10)$, $(70, 10)$, $(70, 40)$, $(10, 40)$.  
   - **Spannmittel-Hinweis:** Die Parallelunterlagen *(präzisionsgeschliffene Unterlegleisten)* müssen so positioniert werden, dass die Bohrungsachsen $X10$ und $X70$ frei in den Spankanal zwischen den Unterlagen zielen und keine Unterlage anbohren.

---

## 3. Kinematische Verifikation im 3D-Simulator

* **Verwendeter Simulator:** `3d_auftrag_simulator.html` *(HTML5 Canvas 3D-Viewer nach DIN 66217)*.
* **Ergebnis der visuellen Bahnprüfung:**
  - Anfahrbahn im Eilgang tangential auf Startkoordinaten $X-10{,}0 / Y-10{,}0$ im Freiraum vor dem Bauteil.
  - Vollständiges Umlaufen der Rechteckkontur $80 \times 50\,\text{mm}$ ohne Verweilmarken oder Anschnitte.
  - Kreisbogensegment der Kreistasche (`G03` mit $I-15$) läuft gleichmäßig gegen den Uhrzeigersinn.
  - Alle vier Bohrungen fahren im Eilgang mit $Z+15$ an und ziehen auf $R+2$ zurück.
  - Nullpunkt liegt exakt an der linken vorderen oberen Ecke des Werkstücks ($X0, Y0, Z0$).

---

## 4. Freigabevermerk & Rechtliche Hinweise gem. § 18 EStG

Das NC-Programm `output_expected.nc` ist code- und syntaxtechnisch vollständig freigegeben.

> [!IMPORTANT]
> **Pflichten des Maschinenbedieners vor dem ersten Span:**  
> Gemäß berufsgenossenschaftlicher Vorgaben *(DGUV Regel 109-003 für spanende Formgebung)* und den vertraglichen Sorgfaltspflichten hat der Zerspanungsmechaniker / Ausbilder vor Ort folgende Schritte zwingend einzuhalten:
> 1. Werkstücknullpunkt `G54` mit 3D-Kantentaster auf Werkstückoberkante vorne links einmessen.
> 2. Werkzeuglängen im Magazin mit Werkzeugvoreinstellgerät oder Laser prüfen.
> 3. Erstes Bauteil im **Einzelsatz *(Single Block)*** mit gedrosseltem Eilgang- und Vorschub-Override *(10 % bis 25 %)* und Hand an der Not-Aus- / Vorschub-Halt-Taste einfahren.

**Freigabestatus:** ✅ **VOLLSTÄNDIG FREIGEGEBEN**  
**Datum:** 24. Oktober 2026  
**Prüfender Ingenieur:** Dipl.-Ing. Bujanovski *(Freiberuflicher Ingenieur für CAD/CAM-Systeme)*

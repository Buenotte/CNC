# 📋 CNC-Einrichteblatt & Werkzeugliste (Agent 3: Setup-Sheet-Generator)
**Bauteil-Name:** Flanschplatte / Lagerdeckel OP10  
**Zeichnungs- / Auftragsnummer:** 2026-FL-1001  
**Kunde:** Schmidt Präzisionstechnik GmbH  
**Erstellt von:** Dipl.-Ing. Buenotte (CAD/CAM-Ingenieurbüro)  
**Zielmaschine:** Haas VF-2 (3-Achs Bearbeitungszentrum mit Haas NGC Steuerung)  
**NC-Programm:** `uebung_03_z_min_berechnung.nc`

---

## 1. Werkstück- & Aufspanndaten

| Parameter | Soll-Wert | Erläuterung für den Bediener |
| :--- | :--- | :--- |
| **Material** | Aluminium EN AW-6082 | AlSi1MgMn (gute Zerspanbarkeit) |
| **Rohteil-Abmessungen** | $85{,}0 \times 55{,}0 \times 15{,}0\,\text{mm}$ | Gesägter Aluminium-Zuschnitt |
| **Fertigmaß (OP10)** | $80{,}0 \times 50{,}0 \times 12{,}0\,\text{mm}$ | Aufmaß seitlich je $2{,}5\,\text{mm}$ |
| **Spannmittel** | Maschinenschraubstock | Feste Backe hinten, bewegliche Backe vorne |
| **Spannrand / Einspanntiefe** | **$3{,}0\,\text{mm}$** | Rohteil steht $12{,}0\,\text{mm}$ über Backenoberkante |
| **Unterlagen** | Parallelunterlagen $h = 32\,\text{mm}$ | Zur exakten Höhenausrichtung |
| **Werkstücknullpunkt (G54)** | **Vorne links oben** | $X0 = \text{linke Kante}$, $Y0 = \text{vordere Kante}$, $Z0 = \text{Fertigteil-Oberkante}$ |

---

## 2. Werkzeugliste (Tool Table)

| Platz | Werkzeug-Typ | Durchmesser | Auskraglänge $L_{\text{min}}$ | Drehzahl $S$ | Vorschub $F$ | Operation |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| **T01** | VHM-Schaftfräser (3 Schneiden) | $\varnothing 10{,}0\,\text{mm}$ | $\ge 25{,}0\,\text{mm}$ | $3.800\,\text{U/min}$ | $1.200\,\text{mm/min}$ | Außenkontur ($Z = -5\,\text{mm}$) & Kreistasche ($Z = -3\,\text{mm}$) |
| **T02** | VHM-Spiralbohrer (140° Spitze) | $\varnothing 6{,}0\,\text{mm}$ | $\ge 30{,}0\,\text{mm}$ | $4.200\,\text{U/min}$ | $450\,\text{mm/min}$ | 4 Ecken-Durchgangsbohrungen |

---

## 3. Sicherheitsrelevante Tiefenmaße

* **Eilgang-Sicherheitsebene:** $Z = +15{,}0\,\text{mm}$
* **Rückzugsebene zwischen Schnitten:** $Z = +2{,}0\,\text{mm}$
* **Tiefste Frästiefe im Programm:** **$Z_{\text{min}} = -5{,}0\,\text{mm}$**
* **Oberkante Schraubstockbacken:** $Z = -12{,}0\,\text{mm}$
* **Kollisionsreserve:** **$+7{,}0\,\text{mm}$** Sicherheitsabstand zum Schraubstock!

---

## 4. Bediener-Checkliste vor dem ersten Start (Grüner Start-Knopf)

1. [ ] Nullpunkt G54 mit 3D-Taster an vorderer linker oberer Ecke angetastet und übernommen?
2. [ ] Werkzeuglängen im Magazin gemessen und in Werkzeugtabelle eingetragen?
3. [ ] Rohteil fest im Schraubstock mit Drehmomentschlüssel angezogen ($80\,\text{Nm}$)?
4. [ ] Kühlmitteldüsen auf Schneide gerichtet?
5. [ ] **Einzelsatz *(Single Block)* aktiviert und Eilgang-Override auf 25 % gestellt?**

# 📋 CNC-Einrichteblatt & Werkzeugliste (Agent 3: Setup-Sheet-Generator)
**Bauteil-Name:** Lagerplatte Alu 50 Stück *(Auftrag 04 / Übung 04)*  
**Zeichnungs- / Modelldatei:** `bauteil_1001.stl` / `bauteil_1001.step`  
**Kunde:** Franken Präzisionsteile GmbH *(Michael Brandner, Fertigungsleiter)*  
**Erstellt von:** Dipl.-Ing. Bujanovski *(CAD/CAM-Ingenieurbüro)*  
**Zielmaschine:** Haas VF-2 *(3-Achs-Vertikal-Fräszentrum mit Haas NGC Steuerung)*  
**NC-Programm:** [`uebung_04_3d_modell_cam.nc`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_04_lagerplatte_3d_cam/uebung_04_3d_modell_cam.nc)  

---

## 1. Werkstück- & Aufspanndaten

| Parameter | Soll-Wert | Erläuterung für den Bediener |
| :--- | :--- | :--- |
| **Material** | Aluminium EN AW-6082 | AlMgSi1 *(gut zerspanbare Knetlegierung)* |
| **Rohteil-Abmessungen** | $85{,}0 \times 55{,}0 \times 15{,}0\,\text{mm}$ | Gesägter Aluminium-Zuschnitt |
| **Fertigmaß (OP10)** | $80{,}0 \times 50{,}0 \times 12{,}0\,\text{mm}$ | Aufmaß seitlich je $2{,}5\,\text{mm}$, Aufmaß Planseite $3{,}0\,\text{mm}$ |
| **Spannmittel** | Maschinenschraubstock | Feste Backe hinten, bewegliche Backe vorne |
| **Spannrand / Einspanntiefe** | **$3{,}0\,\text{mm}$** | Rohteil steht $12{,}0\,\text{mm}$ über Backenoberkante heraus |
| **Unterlagen** | Parallelunterlagen $h = 32\,\text{mm}$ | Zur exakten Höhenausrichtung und Entlastung |
| **Werkstücknullpunkt (G54)** | **Vorne links oben** | $X0 = \text{linke Kante}$, $Y0 = \text{vordere Kante}$, $Z0 = \text{Fertigteil-Oberkante}$ |

---

## 2. Werkzeugliste (Tool Table)

| Platz | Werkzeug-Typ | Durchmesser | Auskraglänge $L_{\text{min}}$ | Drehzahl $S$ | Vorschub $F$ | Bearbeitungs-Operation |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| **T01** | VHM-Schaftfräser *(3 Schneiden)* | $\varnothing 10{,}0\,\text{mm}$ | $\ge 25{,}0\,\text{mm}$ | $8.000\,\text{U/min}$ | $1.200\,\text{mm/min}$ | Operation 1: Außenkontur ($Z = -5{,}0\,\text{mm}$)<br>Operation 2: Kreistasche $\varnothing 30\,\text{mm}$ ($Z = -3{,}0\,\text{mm}$) |
| **T02** | VHM-Spiralbohrer *(140° Spitze)* | $\varnothing 6{,}0\,\text{mm}$ | $\ge 30{,}0\,\text{mm}$ | $3.500\,\text{U/min}$ | $300\,\text{mm/min}$ | Operation 3: 4 Eck-Durchgangsbohrungen mit Tiefbohrzyklus `G83` ($Z = -12{,}0\,\text{mm}$) |

---

## 3. Sicherheitsrelevante Tiefenmaße & Kollisionspuffer

* **Eilgang-Sicherheitsebene:** $Z = +15{,}0\,\text{mm}$
* **Rückzugsebene zwischen Schnitten:** $Z = +2{,}0\,\text{mm}$
* **Tiefste Frästiefe (Fräser T01):** **$Z_{\text{min}} = -5{,}0\,\text{mm}$**
* **Endtiefe Bohrungen (Bohrer T02):** **$Z = -12{,}0\,\text{mm}$**
* **Oberkante Schraubstockbacken:** $Z = -12{,}0\,\text{mm}$ *(bezogen auf Werkstückrand)*
* **Rechnerische Kollisionsreserve (Fräser zu Backen):** **$+7{,}0\,\text{mm}$** Sicherheitsabstand über den Schraubstockbacken!

---

## 4. Bediener-Checkliste vor dem ersten Start (Grüner Start-Knopf)

1. [ ] Nullpunkt `G54` mit 3D-Kantentaster an vorderer linker oberer Kante eingemessen und in Steuerung übernommen?
2. [ ] Werkzeuglängen im Werkzeugmagazin eingemessen und den Registern `H01` bzw. `H02` zugewiesen?
3. [ ] Rohteil fest im Maschinenschraubstock mit Drehmomentschlüssel angezogen ($80\,\text{Nm}$)?
4. [ ] Kühlmitteldüsen auf Schneideneingriff ausgerichtet?
5. [ ] **Einzelsatz *(Single Block)* an der Haas VF-2 aktiviert und Eilgang-Potentiometer auf 25 % gestellt?**

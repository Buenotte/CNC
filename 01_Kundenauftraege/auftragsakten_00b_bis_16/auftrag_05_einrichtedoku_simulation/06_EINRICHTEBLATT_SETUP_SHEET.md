# 📋 CNC-Einrichteblatt & Werkzeugliste (Agent 3: Setup-Sheet-Generator)
**Bauteil-Bezeichnung:** Lagerplatte 80×50×12 mm  
**Auftrags- / Projektnummer:** 2026-KUHN-05  
**Kunde:** Kuhn Medizintechnik & CNC-Fräszentrum, Tuttlingen  
**Ansprechpartner:** Thomas Kuhn (Inhaber & Werkstattleiter)  
**Erstellt von:** Dipl.-Ing. Bujanovski (CAD/CAM-Ingenieurbüro)  
**Zielmaschine:** Haas VF-2 (3-Achs CNC-Bearbeitungszentrum mit Haas NGC Steuerung) / Hermle C22  
**NC-Programm:** `output_expected.nc` (Programm O1001)  
**Erstellungsdatum:** 24. Oktober 2026  

---

## 1. Werkstück- & Rohmaterialdaten

| Parameter | Soll-Wert | Erläuterung & Werkstatt-Hinweis |
| :--- | :--- | :--- |
| **Werkstoff** | **Aluminium EN AW-6082 (AlSi1MgMn)** | Zugfestigkeit ca. $310\,\text{N/mm}^2$, hervorragend zerspanbar, medizinische Apparateplatte |
| **Rohteil-Abmessung** | **$85{,}0 \times 55{,}0 \times 15{,}0\,\text{mm}$** | Gesägter Halbzeug-Zuschnitt mit beidseitigem Bearbeitungsaufmaß |
| **Fertigteil-Abmessung** | **$80{,}0 \times 50{,}0 \times 12{,}0\,\text{mm}$** | Planfräs- / Außenkontur-Aufmaß: je $2{,}5\,\text{mm}$ pro Kante |
| **Aufspannung** | **1. Aufspannung (OP10)** | Komplettbearbeitung der Oberseite, Außenkontur, Tasche und 4 Durchgangsbohrungen |

---

## 2. Spannmittel & Aufspannsituation

```
      ◄──────────────────────── 80.0 mm (X-Achse / Länge nach rechts) ────────────────────────►
     ▲ ┌──────────────────────────────────────────────────────────────────────────────────┐
     │ │ [O] (Bohrung 4: X10 Y40)                             (Bohrung 3: X70 Y40) [O]    │
     │ │                                                                                  │
     │ │                           ╭────────────────────╮                                 │
50.0 │ │                           │    Kreistasche     │                                 │
 mm  │ │                           │      Ø 30 mm       │                                 │
(Y)  │ │                           │   (Mitte X40 Y25)  │                                 │
     │ │                           ╰────────────────────╯                                 │
     │ │                                                                                  │
     ▼ │ [O] (Bohrung 1: X10 Y10)                             (Bohrung 2: X70 Y10) [O]    │
       └──────────────────────────────────────────────────────────────────────────────────┘
       ▲
       └── G54 NULLPUNKT (Vorne links auf Werkstück-Oberkante)
```

| Spannparameter | Vorgabe | Sicherheits- & Einstellanweisung |
| :--- | :--- | :--- |
| **Spannmittel-Typ** | **Präzisions-Maschinenschraubstock** | Mechanisch-hydraulischer Schraubstock (z. B. Hilma / Gressel, Backenbreite $\ge 100\,\text{mm}$) |
| **Backenanordnung** | Feste Backe hinten (Y+), bewegliche Backe vorne (Y-) | Referenzanschlag links für wiederholgenauen Werkstückwechsel |
| **Einspanntiefe / Spannrand** | **$3{,}0\,\text{mm}$** | Rohteil wird an den untersten $3{,}0\,\text{mm}$ gespannt (von $Z = -12{,}0$ bis $Z = -15{,}0\,\text{mm}$) |
| **Überstand über Backen** | **$12{,}0\,\text{mm}$ freier Überstand** | Ausreichender Freiraum für Fräserkontur ($Z_{\text{Fräsen}} = -5{,}0\,\text{mm}$) |
| **Parallelunterlagen** | **Paarhöhe $h = 32{,}0\,\text{mm}$** (oder Stufenbacken) | Geschliffene Präzisionsunterlagenpaarung DIN ISO 2768 |
| **Bohrungsfreigang (Tunnel)** | **Freiraum an den Positionen $X10$ und $X70$** | Unterlagen parallel so anordnen, dass der Bohrer T02 bei $Z = -12\,\text{mm}$ in die Luft zwischen die Leisten taucht! |
| **Spannkraft** | **$25\,\text{kN}$ (ca. $80\,\text{Nm}$ am Drehmomentschlüssel)** | Verzugsfreies Spannen ohne plastische Verformung des Aluminium-Grundkörpers |

---

## 3. Werkstück-Nullpunkt (G54)

* **Lage im Raum:** **Vordere linke Ecke der Werkstück-Oberseite** (Blickwinkel des vor der Maschine stehenden Bedieners).
* **X-Achse ($X0{,}000$):** Linke Außenkante des Rohteils (nach Antasten und Abnullen des Kantentasters).
* **Y-Achse ($Y0{,}000$):** Vordere Kante des Rohteils (zum Bediener hin).
* **Z-Achse ($Z0{,}000$):** Oberkante des fertigen Werkstücks bzw. abgezogene Rohteiloberfläche.

---

## 4. Werkzeugliste & Schnittdaten (Tool Table)

| Platz | Werkzeug-Typ | Nenn-Ø | Schneiden | Auskraglänge $L_{\text{min}}$ | Drehzahl $S$ | Vorschub $F$ | Z-Min | Operation |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **T01** | **VHM-Schaftfräser** *(Zylindrisch)* | $\varnothing 10{,}0\,\text{mm}$ | $z = 3$ | $\ge 25{,}0\,\text{mm}$ | $8.000\,\text{U/min}$ | $1.200\,\text{mm/min}$<br>*(Eintauchen: $500$)* | **$-5{,}0\,\text{mm}$** | Op 1: Außenkontur $80 \times 50\,\text{mm}$<br>Op 2: Kreistasche Mitte $\varnothing 30\,\text{mm}$ |
| **T02** | **VHM-Spiralbohrer** *(140° Spitzenwinkel)* | $\varnothing 6{,}0\,\text{mm}$ | $z = 2$ | $\ge 30{,}0\,\text{mm}$ | $3.500\,\text{U/min}$ | $300\,\text{mm/min}$ | **$-12{,}0\,\text{mm}$** | Op 3: 4x Ecken-Durchgangsbohrung $\varnothing 6\,\text{mm}$ mit Bohrzyklus `G83` ($Q = 3{,}0\,\text{mm}$) |

---

## 5. Arbeits- & Programmablauf

1. **Programmstart (Header):**
   - Sicherheitszeile `N10 G90 G17 G40 G49 G80 G21` setzt alle Modalzustände auf sicheren Werkseinstellung-Zustand.
2. **Operation 1 – Außenkontur fräsen (T01):**
   - Werkzeugwechsel auf T01, Spindelstart `S8000 M03`, Kühlmittel `M08` ein.
   - Anfahren im Eilgang vor das Werkstück auf $X-10{,}0 / Y-10{,}0$, Absenken auf $Z+2{,}0$, Eintauchen mit $F500$ auf $Z-5{,}0$.
   - Vorfräsen der Außenkanten $80 \times 50\,\text{mm}$ im Gleichlauf *(Climb Milling)*. Eilgang-Rückzug auf $Z+15{,}0$.
3. **Operation 2 – Kreistasche fräsen (T01):**
   - Eilgang zur Mitte ($X40{,}0 / Y25{,}0$), Eintauchen auf $Z-3{,}0$, Anfahren an Taschenradius ($X55{,}0$), Fräsen der 360°-Kreisbahn mit Kreisinterpolation `G03 I-15.000 J0.000`. Eilgang auf $Z+15{,}0$, Kühlmittel `M09` aus.
4. **Operation 3 – 4 Eckbohrungen Tiefloch (T02):**
   - Werkzeugwechsel auf T02, Spindelstart `S3500 M03`, Kühlmittel `M08` ein.
   - Tiefbohrzyklus `G83` bohrt vier Bohrungen an den Koordinaten:
     - Bohrung 1: $X10{,}0 / Y10{,}0$
     - Bohrung 2: $X70{,}0 / Y10{,}0$
     - Bohrung 3: $X70{,}0 / Y40{,}0$
     - Bohrung 4: $X10{,}0 / Y40{,}0$
   - Zyklus bohrt mit Stufen von $Q = 3{,}0\,\text{mm}$ Spanbruch bis Endtiefe $Z-12{,}0$, Rückzug auf $R+2{,}0$ bzw. Initialebene $Z+15{,}0$.
   - Zyklusabbruch mit `G80`, Rückzug auf Sicherheitshöhe `Z15.0`.
5. **Programmende (Footer):**
   - Kühlmittel aus (`M09`), Z-Achse ganz nach oben im Maschinenkoordinatensystem (`G53 G00 Z0.0`).
   - Spindelstopp (`M05`), Y-Achse nach vorne zur Tür (`G53 G00 Y0.0`), Programm-Reset (`M30`).

---

## 6. Verbindliche Rüst- & Bediener-Prüfliste (Vor dem ersten Start)

Vor dem Drücken der grünen Starttaste an der Steuerung muss der Auszubildende / Bediener folgende Kontrollen lückenlos durchführen und abzeichnen:

- [ ] **1. Spänefreiheit prüfen:** Schraubstockbacken und Parallelunterlagen mit sauberem Putztuch abgewischt; keine eingeklemmten Späne unter dem Rohteil vorhanden.
- [ ] **2. 3-Stufen-Spannkontrolle durchgeführt:**
  - *Schritt A (Wischen & Blasen):* Auflageflächen absolut grat- und spanfrei.
  - *Schritt B (Kupferhammer-Schlag):* Rohteil mit leichtem Schlag nach unten auf die Parallelen gesetzt.
  - *Schritt C (Wackeltest):* Beide Parallelunterlagen lassen sich mit den Fingern **nicht mehr seitlich bewegen** *(festsitzender Formschluss)*.
- [ ] **3. Nullpunkt G54 verifiziert:** Kantentaster hat $X0$, $Y0$ und $Z0$ an der linken vorderen oberen Werkstückecke fehlerfrei erfasst.
- [ ] **4. Werkzeuglängen H01 und H02:** In der Werkzeugkorrekturtabelle der Haas-Steuerung hinterlegt und geprüft.
- [ ] **5. Bohrer-Freiraum:** Parallelunterlagen verdecken die Bohrpositionen $X10$ und $X70$ **nicht**.
- [ ] **6. Einfahr-Modus aktiviert:**
  - **Einzelsatz *(Single Block)* eingeschaltet.**
  - **Vorschub- & Eilgang-Override auf 20 % gedrosselt.**
  - **Linke Hand auf Vorschub-Halt *(Feed Hold)* / Not-Aus.**

---

**Erstellt durch:** Dipl.-Ing. Bujanovski  
**Freigabevermerk Werkstatt:** Thomas Kuhn (Kuhn Medizintechnik & CNC-Fräszentrum)  
**Datum:** 24. Oktober 2026

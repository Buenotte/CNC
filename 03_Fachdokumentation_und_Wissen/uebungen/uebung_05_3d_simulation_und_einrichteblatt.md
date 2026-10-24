# 🔍 Übung 05: 3D-Simulation im Browser & Einrichteblatt (Setup Sheet)

## 💡 Warum gibt es für Übung 5 keine `.cps`-JavaScript-Datei?

Im Gegensatz zu den anderen Übungen ist **Übung 5 keine Software-Programmieraufgabe**, sondern der entscheidende **Sicherheits- und Dokumentationsschritt *(Quality Assurance & Shop Floor Preparation)***:

In der industriellen Praxis programmieren Sie den Postprozessor nicht zum Selbstzweck. Bevor ein Programm an die Maschine geht, müssen Sie:
1. **Die Werkzeugbahnen visuell simulieren:** Prüfen, ob Konturen, Tiefen und Eilgangbewegungen fehlerfrei ablaufen.
2. **Ein Werkstatt-Einrichteblatt *(Setup Sheet)*** erstellen: Damit der Maschinenbediener weiß, wo der Nullpunkt (`G54`) liegt, welche Werkzeuge gerüstet werden müssen und wie das Rohteil gespannt wird.

---

## 📂 Die zu Übung 5 gehörenden Werkzeuge & Dateien:

1. **Der interaktive 3D-Browser-Simulator:**
   * 👉 [`C:\Projekte\CNC\02_Software_und_Tools\web_tools\3d_auftrag_simulator.html`](file:///c:/Projekte/CNC/02_Software_und_Tools/web_tools/3d_auftrag_simulator.html)
   * *(Einfach per Doppelklick im Webbrowser öffnen – visualisiert Rohteil, Koordinatenachsen, Fräsbahnen und Werkzeuge).*
2. **Der Universal 3D CAD/CAM Viewer:**
   * 👉 [`C:\Projekte\CNC\02_Software_und_Tools\web_tools\universal_3d_viewer.html`](file:///c:/Projekte/CNC/02_Software_und_Tools/web_tools/universal_3d_viewer.html)
   * *(Für 3D-STLs mit automatischer Bemaßung von Länge, Breite, Dicke und Bauteilgewicht).*
3. **Das 3D-Bauteilmodell:**
   * 👉 [`C:\Projekte\CNC\01_Kundenauftraege\auftragsakten_00b_bis_16\auftrag_05_einrichtedoku_simulation\bauteil_1001.stl`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_05_einrichtedoku_simulation/bauteil_1001.stl)
4. **Das Referenz-Einrichteblatt:**
   * 👉 [`C:\Projekte\CNC\01_Kundenauftraege\referenz_auftrag_flanschplatte\EINRICHTEBLATT_SETUP_SHEET.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/referenz_auftrag_flanschplatte/EINRICHTEBLATT_SETUP_SHEET.md)
5. **Der zugehörige Kundenauftrags-Ordner:**
   * 👉 [`C:\Projekte\CNC\01_Kundenauftraege\auftragsakten_00b_bis_16\auftrag_05_einrichtedoku_simulation\`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_05_einrichtedoku_simulation/)
6. **Ausführliches Handbuch-Kapitel:**
   * 👉 [`C:\Projekte\CNC\03_Fachdokumentation_und_Wissen\ALLE_UEBUNGEN_HANDBUCH.md#uebung-05`](file:///c:/Projekte/CNC/03_Fachdokumentation_und_Wissen/ALLE_UEBUNGEN_HANDBUCH.md#uebung-05)


---

## 🧠 Fachwissen: Wer legt welchen Nullpunkt fest? (Maschinennullpunkt M vs. Werkstücknullpunkt W nach DIN 66217)

An jeder CNC-Werkzeugmaschine gibt es zwei grundverschiedene Nullpunkte, deren klare Unterscheidung für die Kollisionsvermeidung überlebenswichtig ist:

```
┌──────────────────────────────────────────────────────────────────────────────────┐
│                   DIE ZWEI NULLPUNKTE AN EINER CNC-MASCHINE                      │
├──────────────────────────┬───────────────────────────────────────────────────────┤
│ 1. MASCHINENGROESSE (M)   │ 2. WERKSTÜCKGRÖSSE (W / G54)                          │
│    Maschinennullpunkt    │    Werkstücknullpunkt                                 │
├──────────────────────────┼───────────────────────────────────────────────────────┤
│ Festgelegt durch:        │ Festgelegt durch:                                     │
│ 🏭 Den MASCHINENHERSTELLER│ 📐 SIE als CAM-Ingenieur (im Computer)               │
│    (z. B. Haas, Hermle)  │ 👨‍🔧 Den ZERSPANUNGSMECHANIKER (an der echten Maschine)│
├──────────────────────────┼───────────────────────────────────────────────────────┤
│ Eigenschaft:             │ Eigenschaft:                                          │
│ Fest, unveränderbar      │ Frei wählbar für jedes einzelne Bauteil               │
└──────────────────────────┴───────────────────────────────────────────────────────┘
```

### 1. Der Maschinennullpunkt $M$ *(Maschinen-Ursprung / Machine Zero)*
* **Wer legt ihn fest?**  
  Ausschließlich der **Werkzeugmaschinen-Hersteller** *(wie z. B. Haas Automation, DMG MORI, Hermle AG, Mazak oder Index)* im Herstellerwerk bei der Montage.
* **Kann man ihn verändern?**  
  **Nein, niemals!** Er ist unverrückbar in der Mechanik verankert und wird durch mechanische Endanschläge sowie Referenzmarken auf den optischen Glasmaßstäben bestimmt.
* **Wozu dient er?**  
  Die Steuerung orientiert sich daran für:
  * Den automatischen Werkzeugwechsler *(Tool Changer Position)*
  * Die Software-Endschalter zur Verhinderung von Achskollisionen mit den Maschinenwänden
  * Sichere Rückzugsbewegungen via `G53 G00 Z0.0` *(Spindel fährt im Maschinenkoordinatensystem absolut nach ganz oben frei)*.

### 2. Der Werkstücknullpunkt $W$ *(Workpiece Zero / z. B. G54, G55)*
Hier arbeiten der CAM-Programmierer und der Zerspanungsmechaniker Hand in Hand:

* **Schritt A – Die theoretische Definition im CAM-System:**  
  **Wer?** **SIE als CAM-Ingenieur *(Dipl.-Ing. Bujanovski)***!  
  Beim Erstellen des CAM-Setups in Fusion 360 oder Siemens NX bestimmen Sie die Lage von $X0$, $Y0$ und $Z0$ auf dem 3D-Modell. Sie schreiben diese Festlegung verbindlich in das **Einrichteblatt *(Setup Sheet)***.
* **Schritt B – Das reale Einmessen an der Fräsmaschine:**  
  **Wer?** Der **Zerspanungsmechaniker *(Maschinenbediener)*** direkt vor Ort an der Fräsmaschine!  
  Er spannt das Rohteil ein, fährt mit einem 3D-Kantentaster *(oder einer Renishaw-Funkmesstaster-Sonde)* genau die von Ihnen im Einrichteblatt vorgegebenen Kanten an und speichert die gemessenen Distanzen im `G54`-Register der CNC-Steuerung.

### 3. Warum wählt man in 95 % aller Fälle die *vordere linke obere Ecke*?
1. **Feste Schraubstockbacke:** Die hintere Backe des Schraubstocks ist starr und exakt parallel/rechtwinklig zum Maschinenbett ausgerichtet (Y+).
2. **Fester Werkstückanschlag:** Der wiederholgenaue mechanische Seitenanschlag sitzt in der Werkstattpraxis fast immer auf der **linken Seite** (X0).
3. **Eindeutiger Anschlag-Bezug:** Wenn der Mechaniker das Rohteil einlegt und gegen den linken Anschlag und die feste hintere Backe schiebt, liegt die linke vordere Ecke bei jeder Serie exakt an derselben Stelle.
4. **Durchgängig positive Maße ($+X$ nach rechts, $+Y$ nach hinten):** Nur die Frästiefe ins Material hinein ist negativ ($-Z$). Das verhindert Vorzeichenfehler und Bedienfehler an der Steuerung.


### 4. Wo steht die Spindel und braucht man ihre Koordinaten? (Die automatische 3-Glieder-Kompensation)
* **Braucht der CAM-Programmierer die Spindelkoordinaten?**  
  **NEIN!** Sie müssen die Position der Spindel niemals von Hand wissen oder in den G-Code schreiben.
* **Wie rechnet die Maschine das automatisch?**
  $$\text{Spindelhöhe} = \text{Werkstück-Nullpunkt (G54)} + \text{Werkzeuglänge (G43 H)} + \text{Programmierter Z-Wert}$$
  Sie programmieren lediglich die Frästiefe der Schneide (z. B. `Z -5.0 mm`). Die Steuerung gleicht Werkzeuglänge und Werkstücklage in Mikrosekunden automatisch aus.
* **Wo steht die Spindel physikalisch?**
  1. *Ganz oben:* Beim Werkzeugwechsel (`G53 G00 Z0.0`).
  2. *In Sicherheitsabstand:* Im Eilgang über dem Rohteil (`Z +15.0 mm`).
  3. *Im Schnitt:* Eingetaucht im Material auf Soll-Tiefe (`Z -5.0 mm`).

# Praxis-Simulation: Ihr erster echter Kundenauftrag mit einem 3D-Modell (`Bauteil_1001`)

Dieses Dokument zeigt Ihnen 1:1 (eins zu eins), wie ein echter Auftrag in der Praxis abläuft, wenn Ihnen ein Kunde ein **3D-Modell (dreidimensionale Bauteil-Datei)** schickt und von Ihnen das fertige **CNC-Programm (G-Code-Maschinenprogramm)** sowie das **Einrichteblatt (Setup Sheet – Anleitung für den Maschinenbediener)** haben möchte.

---

## 📩 Teil 1: Die E-Mail vom Kunden (Das Auftrags-Briefing)

So sieht eine typische Anfrage aus, die Sie von einem **Lohnfertiger (Metallbearbeitungsbetrieb)** oder Maschinenbauer per E-Mail erhalten:

> **Betreff:** Anfrage CAM-Programmierung – Lagerplatte Alu (Stückzahl: 50 Stück)
>
> **Hallo,**
> wir haben hier einen Engpass in der Programmierung und bräuchten kurzfristig das fertige **CNC-Programm (G-Code)** inklusive **Einrichteblatt (Setup Sheet)** für das angehängte **3D-Modell (`bauteil_1001.stl` / `bauteil_1001.step`)**.
>
> **Unsere Eckdaten in der Werkstatt:**
> 1. **Fertigmaß des 3D-Bauteils:** `80 mm` lang (X-Achse) $\times$ `50 mm` breit (Y-Achse) $\times$ `12 mm` hoch (Z-Achse).
>    - In der Mitte (bei `X40 / Y25`) sitzt eine runde **Kreistasche (Circular Pocket – kreisförmige Vertiefung)** mit Durchmesser $\varnothing 30\text{ mm}$ und `3 mm` Tiefe (`Z-3.0`).
>    - An den 4 Ecken sitzen **Durchgangsbohrungen (Through Holes – komplett durchgehende Löcher)** mit Durchmesser $\varnothing 6\text{ mm}$ bei `(X10/Y10)`, `(X70/Y10)`, `(X70/Y40)` und `(X10/Y40)`.
> 2. **Rohteil (Stock – gesägter Aluminium-Block):** `85 mm` $\times$ `55 mm` $\times$ `15 mm` (Material: **Aluminium EN AW-6082 / AlSi1MgMn – gut zerspanbare Aluminiumlegierung**). Das Bauteil steht im **Maschinenschraubstock (Spannmittel)** `13 mm` nach oben heraus.
> 3. **Nullpunkt (`G54` – Werkstück-Koordinatensystem / WCS):** Bitte auf die **obere, vordere, linke Ecke des Fertigteils** legen (`X0, Y0, Z0`).
> 4. **Unsere CNC-Maschine:** **Haas VF-2 (3-Achs-Bearbeitungszentrum mit Haas NGC / Fanuc-kompatibler Steuerung)**.
> 5. **Bereits eingespannte Werkzeuge im Magazin:**
>    - **Platz `T01`:** **VHM-Schaftfräser (Vollhartmetall-Fräser)** $\varnothing 10.0\text{ mm}$, 3 Schneiden (Z=3) für Aluminium.
>    - **Platz `T02`:** **VHM-Spiralbohrer (Vollhartmetall-Bohrer)** $\varnothing 6.0\text{ mm}$.

---

## 🖱️ Teil 2: Ihre Klick-für-Klick-Anleitung am 3D-Modell (In Autodesk Fusion / Fusion 360)

Jetzt sitzen Sie vor Ihrem **ThinkPad (Lenovo-Laptop)**. Sie müssen **keine einzige Zeile G-Code von Hand tippen**, sondern arbeiten grafisch am **3D-Modell**:

### Schritt 1: 3D-Modell öffnen und in den CAM-Modus wechseln (2 Minuten)
1. Öffnen Sie **Autodesk Fusion (CAD/CAM-Software)**.
2. Klicken Sie oben links auf **`Datei (File)` $\rightarrow$ `Öffnen (Open)`** und wählen Sie das 3D-Modell [bauteil_1001.stl](file:///C:/Projekte/CNC/01_Kundenauftraege/referenz_auftrag_flanschplatte/bauteil_1001.stl) (oder eine `.step`-Datei des Kunden) aus.
3. Das Bauteil erscheint in **3D (dreidimensional)** auf Ihrem Bildschirm.
4. Klicken Sie oben links auf den Umschalter **`Konstruktion (Design)`** und wählen Sie **`Fertigen (Manufacture)`** – jetzt sind Sie im **CAM-Arbeitsbereich (Computer-Aided Manufacturing – computergestützte Fertigung)**.

### Schritt 2: Das Setup (Rohteil & Nullpunkt `G54`) definieren (3 Minuten)
1. Klicken Sie oben in der Werkzeugleiste auf **`Setup` $\rightarrow$ `Neues Setup (New Setup)`**.
2. **Reiter 1 – Setup (Ausrichtung & Nullpunkt):**
   - Bei **Vorgangstyp (Operation Type)** wählen Sie: **`Fräsen (Milling)`**.
   - Bei **WKS / Nullpunkt (Work Coordinate System / WCS)** wählen Sie **`Rohteil-Punkt (Stock Box Point)`** oder **`Modell-Punkt (Model Box Point)`** und klicken mit der Maus auf die **vordere linke obere Ecke** des 3D-Modells.
   - Prüfen Sie die 3 bunten Pfeile am 3D-Modell:
     - **Roter Pfeil (`X-Achse`):** Zeigt nach rechts entlang der `80 mm` Kante.
     - **Grüner Pfeil (`Y-Achse`):** Zeigt nach hinten entlang der `50 mm` Kante.
     - **Blauer Pfeil (`Z-Achse`):** Zeigt senkrecht nach oben (Richtung Frässpindel!).
3. **Reiter 2 – Rohteil (Stock):**
   - Stellen Sie das Aufmaß seitlich auf `2.5 mm` (damit aus `80 x 50 mm` Fertigmaß das `85 x 55 mm` Rohteil wird) und oben auf `0 mm` (oder `1 mm`, falls plangefräst wird).
4. **Reiter 3 – Postprozessor (Post Process):**
   - Tragen Sie bei **Programmname/Nummer** `1001` ein und bei **Programmkommentar** `CNC FERTIGUNGSPROGRAMM - MUSTERBAUTEIL`.
   - Klicken Sie auf **OK**.

### Schritt 3: Operation 1 am 3D-Modell anlegen – Außenkontur fräsen (5 Minuten)
1. Klicken Sie oben im Menü **`2D`** auf **`2D-Kontur (2D Contour – Umfahren einer Außen- oder Innenwand)`**.
2. **Reiter 1 – Werkzeug (Tool):**
   - Klicken Sie auf **`Auswählen (Select)`**, legen Sie einen **Schaftfräser (Flat End Mill)** mit Durchmesser `10 mm` an und geben Sie ihm die Nummer **`T01`**.
   - Tragen Sie die Schnittdaten für Aluminium ein: **Spindeldrehzahl (`Spindle Speed`)** = `8000 U/min (RPM)` und **Fräsvorschub (`Cutting Feedrate`)** = `1200 mm/min`.
3. **Reiter 2 – Geometrie (Geometry):**
   - Klicken Sie mit der Maus direkt am **3D-Modell** auf die **untere Außenkante** der Platte. Fusion legt sofort einen blauen Pfeil rund um das 3D-Modell.
4. **Reiter 3 – Höhen (Heights):**
   - **Endhöhe (Bottom Height):** Stellen Sie auf `-5.0 mm` (oder Modell-Unterkante).
5. Klicken Sie auf **OK** – Fusion zeichnet sofort die blauen und gelben **Fräsbahnen (Toolpaths)** rund um Ihr 3D-Modell!

---

#### 💡 Wichtige Zerspanungs-Erklärung: Warum fährt der Fräser zuerst außen rum und schneidet nur auf Z = -5 mm?

Häufige Frage: *„Das Rohteil ist doch 15 mm dick und das Fertigteil 12 mm – warum fräst der Fräser bei der Außenkontur nur auf Z = -5 mm und warum fährt er zuerst außen und dann ins Zentrum?“*

Hier ist die physikalische und technologische Begründung:

```
        Z = 0 mm (Oberkante G54)  ═══════════════════════════════════
                                  │                                 │
        Z = -5 mm                 ├── Blaue Fräsbahn (Z = -5 mm) ───┤ <-- OP 1: Außenkontur (5 mm Stufe / Schruppen)
                                  │                                 │
        Z = -12 mm                ├─────────────────────────────────┤ <-- Unterkante Fertigteil (Dicke = 12 mm)
                                  │  [ 3 mm Spannrand / Aufmaß ]    │
        Z = -15 mm (Rohteilboden) ███████████████████████████████████
                                  ▲                                 ▲
                         [ SCHRAUBSTOCK-BACKE ]            [ SCHRAUBSTOCK-BACKE ]
```

1. **Kollisionsschutz gegen den Schraubstock (Der Spannrand):**
   * Das Rohmaterial ist $15\,\text{mm}$ hoch. Die gehärteten Stahlbacken des Schraubstocks spannen das Teil unten an den untersten $3\,\text{mm}$ fest *(Spannrand von $Z = -12\,\text{mm}$ bis $Z = -15\,\text{mm}$)*.
   * Würde der Fräser sofort auf $Z = -15\,\text{mm}$ durchfräsen, würde er mit 8.000 U/min mit voller Wucht in die gehärteten Stahlbacken krachen *(Totalschaden an Werkzeug und Spindel!)*.
2. **Konstruktionsstufe (Flanschabsatz):**
   * Die Flanschplatte hat an den Außenkanten eine $5\,\text{mm}$ tiefe Stufe *(Schulter)*. Die Kanten werden auf $Z = -5\,\text{mm}$ abgesetzt.
3. **Warum zuerst außen rum und dann ins Zentrum?**
   * Das Werkzeug `T01 (Schaftfräser 10 mm)` erledigt zwei Operationen direkt hintereinander, um teure Werkzeugwechselzeiten zu sparen:
     1. Zuerst fräst `T01` außen im Rechteck ($80 \times 50\,\text{mm}$), um das Rohteil ($85 \times 55\,\text{mm}$) auf das exakte Fertigmaß zu bringen und Spannungen abzubauen *(blaue Linie rundherum)*.
     2. Danach zieht die Spindel auf sichere Höhe $Z = +15\,\text{mm}$ hoch *(gelbe gestrichelte Eilgang-Linie)* und fliegt direkt ins Zentrum ($X=40, Y=25$).
     3. Dort taucht `T01` auf $Z = -3\,\text{mm}$ ein und fräst die runde Kreistasche *(blaue Kreisbahn)*.
4. **Wie wird das Teil auf 12 mm Fertigmaß gebracht? (OP10 vs. OP20):**
   * Nach der 1. Aufspannung *(OP10)* wird das Werkstück aus dem Schraubstock genommen, um $180^\circ$ umgedreht *(OP20)* und auf den bereits gefrästen Flächen gespannt.
   * Ein Planfräser *(Messerkopf)* schlichtet dann die überstehenden $3\,\text{mm}$ Rohmaterial von der Rückseite weg – und das Bauteil erreicht exakt seine $12{,}0\,\text{mm}$ Fertighöhe!

---

### Schritt 4: Operation 2 am 3D-Modell anlegen – Kreistasche in der Mitte (3 Minuten)
1. Klicken Sie oben im Menü **`2D`** auf **`2D-Tasche (2D Pocket – Ausräumen einer geschlossenen Vertiefung)`** oder **`Kreistasche (Circular)`**.
2. **Werkzeug (Tool):** Bleibt unser 10-mm-Fräser **`T01`**.
3. **Geometrie (Geometry):** Klicken Sie am **3D-Modell** einfach auf den Boden oder den Rand des runden Lochs in der Mitte ($\varnothing 30\text{ mm}$, Tiefe `-3.0 mm`).
4. Klicken Sie auf **OK** – Fusion berechnet automatisch die **Kreisbewegung (`G03` – Kreisinterpolation gegen den Uhrzeigersinn)**!

### Schritt 5: Operation 3 am 3D-Modell anlegen – Die 4 Löcher bohren (3 Minuten)
1. Klicken Sie oben im Menü **`Bohren (Drilling)`** auf **`Bohren (Drill)`**.
2. **Reiter 1 – Werkzeug (Tool):**
   - Wählen Sie einen **Spiralbohrer (Drill)** mit Durchmesser `6.0 mm` und geben Sie ihm die Nummer **`T02`**.
   - Drehzahl für `6 mm` Bohrer in Alu: `3500 U/min`, Bohrvorschub: `300 mm/min`.
3. **Reiter 2 – Geometrie (Geometry):**
   - Klicken Sie am **3D-Modell** auf eines der 4 Ecklöcher und setzen Sie das Häkchen bei **`Gleicher Durchmesser (Select Same Diameter)`** – Fusion wählt alle 4 Bohrungen automatisch aus!
4. **Reiter 4 – Zyklus (Cycle):**
   - Wählen Sie **`Tiefbohren – vollständiger Rückzug (Deep Drilling – Full Retract / G83)`** mit einer **Zustelltiefe (`Peck Depth / Q`)** von `3.0 mm` (der Bohrer bohrt immer `3 mm` tief, fährt kurz hoch, damit die Späne herausfallen, und bohrt dann weiter bis `-12.0 mm`).
5. Klicken Sie auf **OK**.

### Schritt 6: Der magische Moment – Export über Ihren Postprozessor (`mein_erster_post.cps`)!
1. Klicken Sie oben auf **`Simulieren (Simulate)`**: Schauen Sie sich am Bildschirm an, wie der virtuelle Fräser das 3D-Rohteil abfräst. Wenn der Balken unten komplett grün ist (keine roten Kollisionen), sind Sie bereit!
2. Klicken Sie oben auf **`NC-Programm / Postprozess (Post Process)`**.
3. Wählen Sie bei **Postprozessor (Post)** Ihre eigene Datei [src/mein_erster_post.cps](file:///c:/Projekte/CNC/02_Software_und_Tools/src/mein_erster_post.cps) aus!
4. Rechts im Fenster sehen Sie Ihre selbst programmierten **Properties (Benutzer-Optionen)**:
   - `Entwickler-Name`: Ihr Name
   - `Firmenname / Auftraggeber`: Name des Kunden
   - `Maximale Frästiefe Z-Min ausgeben`: `Ja (true)`
5. Klicken Sie auf **`Postprozess ausführen (Post)`** – und in einer Sekunde fällt hinten genau die fertige Datei [tests/output_expected.nc](file:///c:/Projekte/CNC/02_Software_und_Tools/tests/output_expected.nc) heraus!

---

### Schritt 7: 3D-Freigabe-Video aufnehmen (Mit unserem Web-Studio)
1. Öffnen Sie per Doppelklick die Datei [`cnc_video_generator_web.html`](file:///c:/Projekte/CNC/02_Software_und_Tools/web_tools/cnc_video_generator_web.html).
2. Laden Sie Ihre soeben erzeugte `.nc`-Datei hoch und tragen Sie den Kundennamen ein.
3. Klicken Sie auf **„🔴 Video-Aufnahme starten“** – das System zeichnet die Fräsbewegungen mit 30 FPS als HD-Video auf.
4. Speichern Sie das Video als Datei ab und senden Sie es dem Kunden zur Vorab-Freigabe!

### Schritt 8: Finale Auslieferung nach Eingang der 2. Teilzahlung
1. Sobald der Kunde das Video bestätigt und die restlichen 50 % überwiesen hat:
2. Senden Sie ihm die finale `.nc`-Datei und das ausgefüllte Einrichteblatt ([`Portfolio/Vorlage_Einrichteblatt_und_Werkzeugliste.md`](file:///c:/Projekte/CNC/04_Recht_Steuern_und_Backoffice/Portfolio/Vorlage_Einrichteblatt_und_Werkzeugliste.md)).

---

👉 **Der vollständige Master-Leitfaden von A bis Z:**  
Die komplette Schritt-für-Schritt-Anleitung aller 7 Phasen *(vom Erstkontakt bis zur Rechnungsstellung)* finden Sie in:  
[**`KUNDENAUFTRAG_VOLLSTAENDIGER_PROZESSABLAUF_A_BIS_Z.md`**](file:///c:/Projekte/CNC/01_Kundenauftraege/KUNDENAUFTRAG_VOLLSTAENDIGER_PROZESSABLAUF_A_BIS_Z.md).

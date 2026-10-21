# 🛡️ Sicherheits- und Qualitätsprüfprotokoll für CNC-G-Code

> **Praxis-Leitfaden für Fertigungsplaner, CAM-Programmierer und CNC-Maschinenbediener**  
> *Ziel: 100 % fehlerfreie Programme, Null-Kollisions-Garantie, Schutz von Mensch, Werkzeug, Werkstück und Werkzeugmaschine.*

---

## 📋 Inhaltsverzeichnis
1. [Sicherheitsphilosophie: Warum ist CNC-Prüfung wie der Check im Flugzeugcockpit?](#1-sicherheitsphilosophie-warum-ist-cnc-prüfung-wie-der-check-im-flugzeugcockpit)
2. [Die 5-Stufen-Prüfkette im Überblick](#die-5-stufen-prüfkette-im-überblick)
3. [Phase 1: Prüfungen im CAM-System und Postprozessor (Vor dem Erzeugen des Codes)](#phase-1-prüfungen-im-cam-system-und-postprozessor-vor-dem-erzeugen-des-codes)
4. [Phase 2: Geometrie-, Werkzeug- und Kollisionsprüfung im 3D-Simulator](#phase-2-geometrie--werkzeug--und-kollisionsprüfung-im-3d-simulator)
5. [Phase 3: G-Code-Textinspektion (Befehl für Befehl einfach erklärt)](#phase-3-g-code-textinspektion-befehl-für-befehl-einfach-erklärt)
6. [Phase 4: Rüstprüfung an der echten Werkzeugmaschine (In der Werkstatt)](#phase-4-rüstprüfung-an-der-echten-werkzeugmaschine-in-der-werkstatt)
7. [Phase 5: Erstes Einfahren an der Maschine (First-Part Run & Luftschnitt)](#phase-5-erstes-einfahren-an-der-maschine-first-part-run--luftschnitt)
8. [Druckbare Abnahme-Checkliste für den Kundenauftrag](#druckbare-abnahme-checkliste-für-den-kundenauftrag)
9. [Sofortige Notfall- und Abbruchkriterien (Wann MUSS sofort gestoppt werden?)](#sofortige-notfall--und-abbruchkriterien-wann-muss-sofort-gestoppt-werden)

---

## 1. Sicherheitsphilosophie: Warum ist CNC-Prüfung wie der Check im Flugzeugcockpit?

An einer modernen CNC-Fräsmaschine *(Computerized Numerical Control – computergestützte Werkzeugmaschine)* wirken gewaltige Kräfte:
* Eine Frässpindel *(Hauptantriebsmotor für das Werkzeug)* leistet typischerweise **15 bis 30 Kilowatt (kW)** und dreht sich mit **8.000 bis 24.000 Umdrehungen pro Minute (U/min)**.
* Im Eilgang *(Schnellgang ohne Schnitt)* beschleunigen die Achsen meterlange Stahltische in Bruchteilen einer Sekunde auf **30 bis 60 Meter pro Minute (m/min)**.

Wenn bei diesen Geschwindigkeiten ein Fräser ungebremst in einen Stahlschraubstock oder Maschinentisch kracht *(ein sogenannter Maschinencrash)*:
1. Reißt das Werkzeug explosionsartig ab, und Splitter fliegen durch die Kabine.
2. Werden die hochpräzisen Keramik-Spindellager zerstört. Eine Spindelreparatur kostet sofort **15.000 € bis 40.000 €**, zuzüglich wochenlangem Maschinenausfall.
3. Verliert der Kunde das Vertrauen, und Sie haften als Programmierer für den Schaden.

**Die goldene Werkstattregel lautet daher:**  
*Ein Flugkapitän startet niemals, ohne vorher Punkt für Punkt seine Checkliste abgehakt zu haben. Genau dieselbe Sorgfaltspflicht gilt für jeden, der einen G-Code *(Maschinencode)* an eine Fräsmaschine übergibt!*

---

## Die 5-Stufen-Prüfkette im Überblick

Ein Crash entsteht fast nie durch einen einzigen großen Fehler, sondern durch eine Kette kleiner Versäumnisse. Deshalb wird jedes NC-Programm *(Numerical Control – maschinenlesbare Steuerungsdatei)* in fünf aufeinander aufbauenden Sicherheitsstufen geprüft:

```
[Phase 1: CAM & Postprozessor]  -->  [Phase 2: 3D-Simulation]  -->  [Phase 3: G-Code-Inspektion]
(Nullpunkt, Aufmaß, Halter)         (Farben, Tiefen, Maße)         (Sicherheitszeilen, G43, Z_min)
                                                                                  |
[Phase 5: Luftschnitt & Span]   <--  [Phase 4: Maschinen-Rüsten] <----------------+
(Z+50 mm, Einzelsatz, Poti)          (Einmessen, Spannen, KSS)
```

---

## Phase 1: Prüfungen im CAM-System und Postprozessor (Vor dem Erzeugen des Codes)

Bevor Sie den Postprozessor *(Übersetzer von CAM-Bearbeitungsbahnen in CNC-Maschinencode)* starten, müssen im CAM-System *(Computer-Aided Manufacturing – rechnergestützte Fertigungsplanung, z. B. Autodesk Fusion)* vier elementare Punkte geprüft werden:

### 1. Der Bauteil-Nullpunkt (WCS - Work Coordinate System / Werkstück-Koordinatensystem `G54`):
* **Was bedeutet das einfach erklärt?**  
  Die Maschine weiß von Natur aus nicht, wo auf dem riesigen Tisch Ihr Metallklotz liegt. Der Nullpunkt ist die „Heimat-Adresse“ *(X0, Y0, Z0)*, von der aus alle Maße gerechnet werden.
* **Was muss exakt stimmen?**
  * **X0 und Y0:** Liegen sie an einer festen Anschlagkante *(meistens die feste Backe links hinten am Schraubstock)*? Wenn der Programmierer den Nullpunkt oben links setzt, der Bediener aber unten rechts antastet, fährt der Fräser spiegelverkehrt in den Schraubstock!
  * **Z0 (Die Höhe):** Liegt `Z0` auf der **Fertigteil-Oberkante** oder auf der **Rohteil-Oberkante**?  
    * *Empfohlener Industriestandard:* `Z0` immer auf die geplante Fertigteil-Oberseite legen. Wenn das Rohteil 2 mm dicker aus der Säge kommt, fräst das Werkzeug im Planfräsgang einfach 2 mm Span ab (`Z +2.0` bis `Z 0.0`), ohne dass Konturen zu tief geraten.
  * **Dokumentationspflicht:** Die Lage von `X0 Y0 Z0` muss unverwechselbar im Einrichteblatt ([`EINRICHTEBLATT_SETUP_SHEET.md`](file:///c:/Projekte/CNC/kundenauftrag_01_flanschplatte/EINRICHTEBLATT_SETUP_SHEET.md)) mit einer Skizze vermerkt sein!

### 2. Das Rohteil-Aufmaß (Stock Allowance / Materialzugabe):
* **Was bedeutet das einfach erklärt?**  
  Das Fertigteil ist 80 × 50 × 12 mm groß. Der rohe Klotz aus der Säge ist aber 85 × 55 × 15 mm. Der Überschuss *(5 mm in der Länge, 5 mm in der Breite, 3 mm in der Dicke)* ist das Rohteilaufmaß.
* **Was muss geprüft werden?**
  * Stimmen die im CAM eingegebenen Maße mit dem gelieferten Sägezuschnitt überein?
  * Liegt das Aufmaß symmetrisch um das Teil? Wenn der Sägeschnitt schief ist und auf einer Seite 4 mm Aufmaß stehen, kann der Fräser beim ersten Anschnitt überlastet werden und abbrechen *(Vollschnitt-Schock)*.

### 3. Spannmittel-Schutzkörper (Fixture / Schraubstock und Spannbacken):
* **Was bedeutet das einfach erklärt?**  
  Der Schraubstock hält das Metallteil fest. Seine Spannbacken bestehen aus extrem hartem Einsatzstahl.
* **Was muss geprüft werden?**
  * Wurde der Schraubstock im CAM als **Schutzkörper *(Kollisionszone)*** hinterlegt?
  * **Sicherheitsabstand einhalten:** Die tiefste Konturfräsung muss mindestens **3 bis 5 mm Luft** über den Oberkanten der Stahlbacken bleiben.

![Z-MIN und Kollisionsschutz am Maschinenschraubstock](file:///c:/Projekte/CNC/docs/bilder/cnc_z_min_mit_10mm_beschriftung.jpg)

### 4. Werkzeug-Auskraglänge und Halterkollision (Tool Gauge Length):
* **Was bedeutet das einfach erklärt?**  
  Ein Fräser ist in eine Spannzange *(Werkzeugaufnahme)* eingespannt. Wie weit der Fräser aus dem Futter herausragt, nennt man Auskraglänge.
* **Was muss geprüft werden?**
  * Ist die Schneidenlänge *(Nutzlänge mit Schärfe)* mindestens so lang wie die Frästiefe? Wenn der zylindrische Schaft ohne Schneide an der Werkstückwand reibt, verglüht das Werkzeug durch Reibungshitze.
  * Schlägt der dicke Werkzeughalter *(Spannfutter / SK40 / HSK63)* bei tiefen Taschen oben am Werkstück an? Im CAM muss der Halter modelliert sein, damit die Software warnt: *„Halter berührt Bauteil!“*.

### 5. Entwickler-Checkliste: Die 5 unveränderlichen Standard-Regeln im Postprozessor-Code:
Als Postprozessor-Programmierer müssen Sie keine Werkzeugmaschinen einmessen. Für Ihre JavaScript-Dateien (`.cps`) müssen Sie vor der Ausgabe lediglich diese 5 Regeln verifizieren:
1. **Sicherheitszeile in `onOpen()`:** `G90 G21 G17 G40 G80` *(Reset aller alten Achs- und Zyklus-Zustände)*.
2. **Feste Reihenfolge in `onSection()`:** Werkzeugwechsel `T.. M06` $\rightarrow$ Drehzahl `S.. M03` $\rightarrow$ Bauteil-Nullpunkt `G54` $\rightarrow$ Längenkorrektur `G43 H.. Z15.0 M08`.
3. **Zuerst Z nach oben *(Crash-Schutz)*:** Vor jeder Tischbewegung muss die Z-Achse mit `G53 G00 Z0.` an die Decke gezogen werden.
4. **Syntax-Schutz:** Niemals runde Klammern in runden Klammern verschachteln *(stürzt bei Fanuc/Haas ab; immer `writeComment()` nutzen)*.
5. **Sauberes Programmende in `onClose()`:** Kühlmittel AUS (`M09`) $\rightarrow$ Z ganz hoch (`G53 Z0.`) $\rightarrow$ Spindelstopp (`M05`) $\rightarrow$ Tisch zur Tür (`G53 Y0.`) $\rightarrow$ Programmende (`M30`).

---

## Phase 2: Geometrie-, Werkzeug- und Kollisionsprüfung im 3D-Simulator

Nachdem der Postprozessor die Maschinendatei erzeugt hat, laden Sie die `.nc`-Datei in den interaktiven Simulator:  
👉 [**`kundenauftrag_01_flanschplatte/3d_auftrag_simulator.html`**](file:///c:/Projekte/CNC/kundenauftrag_01_flanschplatte/3d_auftrag_simulator.html)

Hier sehen Sie räumlich in 3D *(dreidimensional)*, was der Maschinencode Zeile für Zeile bewirken wird:

### 1. Visuelle Bahnfarben-Prüfung (Was bedeuten die Linien?):

* **🔴 Rote gestrichelte Linien (`G00` Eilgang / Schnellgang):**
  * **Bedeutung:** Das Werkzeug bewegt sich mit Höchstgeschwindigkeit durch die Luft, um von Position A nach Position B zu springen.
  * **Lebenswichtige Regel:** Rote Linien dürfen **niemals** den grauen Bauteilkörper, das Rohteil oder die Spannbacken schneiden! 
  * *Faustregel:* Wenn eine rote Linie ins Metall sticht, kracht die Maschine unweigerlich mit Höchstgeschwindigkeit in das massive Material. Das Programm muss sofort gestoppt werden!

* **🟢 Grüne durchgezogene Linien (`G01` Arbeitsvorschub / Spanabtrag):**
  * **Bedeutung:** Hier dreht sich die Spindel, und der Fräser schält Späne ab.
  * **Prüfung:** Fährt das Werkzeug sanft ein? Ein Schaftfräser darf nicht wie ein Bohrer senkrecht ins volle Metall stempeln *(axiales Eintauchen ist verboten, außer bei Spezialbohrfräsern)*. Das Eintauchen muss über eine **Helix *(Schraubenlinie)*** oder **Rampe *(schräges Eintauchen)*** erfolgen.

* **🔵 / 🔷 Türkise und blaue Kreisbögen (`G02 / G03` Zirkularinterpolation):**
  * **Bedeutung:** `G02` fräst Kreisbögen im Uhrzeigersinn, `G03` gegen den Uhrzeigersinn.
  * **Prüfung:** Fährt das Werkzeug tangential *(weich im Bogen)* an die Wand an *(Lead-In / Anfahrkreis)*? Ein hartes rechtwinkliges Einstechen hinterlässt unschöne Rattermarken auf der Werkstückoberfläche.

* **🟡 Gelbe Sicherheits- und Nullpunkt-Markierung (`G54`):**
  * **Bedeutung:** Zeigt den Nullpunkt und die Z-Sicherheitsebene an.
  * **Prüfung:** Steht das Werkzeug vor dem ersten Schnitt mindestens **15 mm** über der Werkstückoberfläche (`Z +15.0`)?

### 2. Prüfung der echten Sollmaße mit dem Schalter `📐 Maße Ein/Aus`:
* Klicken Sie oben rechts im Simulator auf **`📐 Maße Ein/Aus`**.
* Vergleichen Sie die eingeblendeten CAD-Bemaßungen mit der Konstruktionszeichnung:
  * Außenlänge: **80 mm**
  * Außenbreite: **50 mm**
  * Gesamtdicke: **12 mm**
  * Kreistasche zentrisch: **Ø 30 mm**, Tiefe **4 mm**
  * 4 Bohrungen: **Ø 6 mm**, symmetrisch auf Abstand platziert.
* Wenn eine Fräsbahn über die 80 × 50 mm Begrenzung hinausschießt, ist entweder der Nullpunkt falsch verrechnet oder die Werkzeugradiuskorrektur fehlerhaft.

### 3. Grenzen der Simulation: Kann man sich bezüglich Crashes zu 100 % auf die Simulation verlassen?

**Klare Antwort für den Fertigungsalltag: JEIN!**  
*(Ja für die digitale Geometrie am Bildschirm – aber NEIN als Alleingarantie für die physische Werkshalle!)*

Ein Simulator ist ein mächtiges Prüfwerkzeug, aber er sieht nur die virtuelle 3D-Welt. Er schützt zuverlässig vor Programmierfehlern, kann jedoch physische Realitäten in der Werkhalle nicht erraten.

#### Worauf Sie sich in der Simulation zu 100 % verlassen können:
1. **Mathematische Vorzeichen- und Tippfehler im G-Code:**  
   Vergisst der Programmierer ein Minus *(z. B. `Z12` statt `Z-12`)* oder tippt versehentlich `Z-50` statt `Z-5`, schlägt der Simulator sofort visuell und im HUD rot Alarm.
2. **Kollisionen bei Eilgang-Bewegungen (`G00`):**  
   Fährt der Eilgang mit Höchstgeschwindigkeit quer durch das Werkstück oder schräg in eine Kontur, wird dies sofort als gelbe Crash-Linie sichtbar.
3. **Durchbrüche und Maximaltiefen:**  
   Die Simulation zeigt millimetergenau an, ob ein Bohrer oder Fräser die Bauteil-Unterkante ($Z = -12\,\text{mm}$) durchbricht und wie weit er ins Freie austritt *(z. B. $Z = -14{,}5\,\text{mm}$ bei Durchgangsbohrungen)*.

#### Was ein Simulator NIEMALS wissen kann (Die physische Realität in der Werkstatt):
1. **Die reale Höhe der Schraubstockbacken:**  
   Der Simulator weiß nicht, ob an der echten Maschine flache Stufenbacken ($25\,\text{mm}$) oder hohe Standardbacken ($50\,\text{mm}$) montiert sind. Liegen die echten Backen bei $Z = -10{,}0\,\text{mm}$, aber der Bohrer fährt auf $Z = -14{,}5\,\text{mm}$, rammt der Bohrer in der Realität in gehärteten Stahl!
2. **Die reale Werkzeug-Auskraglänge *(Einspanntiefe im Futter)***:  
   Der Simulator nimmt idealisiert an, dass die Schneide lang genug ist. Hat der Bediener an der Maschine den Fräser jedoch nur $18\,\text{mm}$ kurz eingespannt, schlägt die rotierende Spannzangenmutter bei einer $20\,\text{mm}$ tiefen Tasche auf das Bauteil auf.
3. **Menschliche Antastfehler am Werkstück-Nullpunkt (`G54`):**  
   Hat der Bediener beim Antasten mit dem 3D-Messtaster den Kugelradius ($5{,}0\,\text{mm}$) vergessen oder das falsche Koordinatensystem aktiviert, fährt das gesamte Programm um Millimeter versetzt in den Schraubstock.
4. **Falsches Werkzeug im Magazinplatz:**  
   Befindet sich auf Platz `T01` wirklich der vorgesehene $\varnothing 10\,\text{mm}$ Schaftfräser oder hat ein Kollege versehentlich einen $\varnothing 50\,\text{mm}$ Planfräskopf stecken gelassen?

#### Die Brücke zwischen Simulator und Werkstatt: Der Z-MIN-Header im Postprozessor
Genau deshalb berechnet unser Postprozessor für jedes Werkzeug die absolut tiefste Koordinate (`Z-MIN`) und druckt sie gut lesbar in den Programmkopf:
```gcode
(T01 | D=10.000MM | Z-MIN=-5.000MM  | SCHAFTFRAESER 10MM VHM)
(T02 | D=5.000MM  | Z-MIN=-14.500MM | SPIRALBOHRER 5MM VHM)
```
Der Zerspanungsmechaniker liest diese Werte vor dem Starten der Spindel und vergleicht sie mit seiner realen Aufspannung. Erst diese Kombination aus **virtueller 3D-Simulation + Z-MIN-Postprozessor-Prüfung + Luftschnitt/Einzelsatz an der Maschine** garantiert eine 100 %ige Null-Crash-Sicherheit!

---

## Phase 3: G-Code-Textinspektion (Befehl für Befehl einfach erklärt)

Öffnen Sie die erzeugte `.nc`-Datei in einem Texteditor. Führen Sie die folgende Zeilenprüfung durch:

| Schritt | G-Code-Befehl | Was bedeutet der Befehl einfach erklärt? | Warum ist er unverzichtbar? (Gefahr bei Fehlen) |
| :--- | :--- | :--- | :--- |
| **1. Sicherheitszeile** | `G90 G17 G21 G94 G40 G49 G80` | **Grund-Reset der Steuerung:**<br>• `G90`: Alle Maße sind absolut vom Nullpunkt.<br>• `G17`: Bearbeitungsebene ist XY.<br>• `G21`: Alle Maße in Millimeter.<br>• `G94`: Vorschub in mm/min.<br>• `G40`: Fräserradiuskorrektur ausschalten.<br>• `G49`: Werkzeuglängenkorrektur löschen.<br>• `G80`: Alle Bohrzyklen abbrechen. | Stand die Maschine vorher im Modus `G20` *(Zoll)* oder `G91` *(Kettenmaße / Relativmaße)*, fährt sie ohne diese Zeile um das 25,4-fache zu weit oder addiert Verfahrwege auf – **sofortiger Totalschaden!** |
| **2. Werkzeugwechsel** | `T01 M06` | **Werkzeug holen:** Holt Werkzeug Platz 1 *(Schaftfräser Ø 10 mm)* aus dem Magazin und wechselt es in die Spindel ein. | Steht hier `T05`, wechselt die Maschine vielleicht ein Sägeblatt oder einen Zentrierbohrer ein und ruiniert das Teil. |
| **3. Spindelstart** | `S8000 M03` | **Motor einschalten:** Dreht die Frässpindel mit 8.000 U/min im Uhrzeigersinn *(Rechtslauf)*. | Fährt das Werkzeug ins Aluminium, während die Spindel noch stillsteht, bricht der Fräser sofort mit einem lauten Knall ab! |
| **4. Längenkorrektur** | `G43 H01 Z15.0` | **Werkzeuglänge aktivieren:** `G43` liest aus Register `H01` die exakt vermessene Länge von Werkzeug 1 aus und stoppt 15 mm über dem Teil. | Fehlt `G43`, weiß die Steuerung nicht, wie lang das Werkzeug ist, nimmt Länge 0 an und rammt das Futter ungebremst in den Maschinentisch. |
| **5. Kühlung an** | `M08` | **Kühlschmierstoff an:** Schaltet die KSS-Pumpe ein, die Wasser-Öl-Emulsion auf die Schneide spritzt. | Ohne Kühlung verschmilzt weiches Aluminium bei 8.000 U/min innerhalb von 3 Sekunden mit dem Fräser *(Aufbauschneide)* – Fräser reißt ab. |
| **6. Tiefenprüfung** | `Z -12.5` *(Beispiel)* | **Maximale Frästiefe (`Z_min`):** Der tiefste Punkt, den die Z-Achse im gesamten Programm anfährt. | Wenn das Bauteil 12 mm dick ist und `Z -35.0` im Code steht, bohrt das Werkzeug 23 mm tief in den Schraubstock oder Maschinentisch! |
| **7. Sicherer Rückzug** | `G53 G00 Z0` *(oder `G28 G91 Z0`)* | **Maschinen-Referenzpunkt:** Fährt die Z-Achse senkrecht nach oben auf den maximalen mechanischen Endanschlag der Maschine *(Maschinenkoordinatensystem G53)*. | Fährt die Maschine nach dem Fräsen zuerst in X/Y zur Seite, bevor Z oben ist, reißt der Fräser alle Schraubstockbacken und Spannpratzen ab! |
| **8. Programmende** | `M05 M09 M30` | **Sicheres Abschalten:**<br>• `M05`: Spindel stoppen.<br>• `M09`: Kühlmittel ausschalten.<br>• `M30`: Programm beenden und Cursor an den Anfang zurücksetzen. | Fehlt `M30`, bleibt die Spindel mit Kühlwassernebel weiterdrehen; der Bediener öffnet die Tür in eine rotierende Gefahrenquelle. |

---

## Phase 4: Rüstprüfung an der echten Werkzeugmaschine (In der Werkstatt)

Selbst wenn der G-Code fehlerfrei geschrieben ist: Wenn an der realen Maschine ein Parameter falsch eingestellt ist, passiert trotzdem ein Schaden. Vor dem Drücken der grünen Start-Taste gelten folgende Kontrollen:

### 1. Werkzeugeinmessung (Tool Presetting):
* **Werkzeuglänge:** Wurde jedes Werkzeug mit der Messuhr, dem Werkzeugvoreinstellgerät oder dem Laser-Taster *(z. B. Renishaw / Blum)* vermessen?
* **Werkzeugradius:** Ist im Werkzeugspeicher der echte Radius hinterlegt *(z. B. Fräser Ø 10 mm $\rightarrow$ Radius 5,000 mm)*?
* **Magazinplatz:** Befindet sich `T01` wirklich auf Platz 1 und `T02` wirklich auf Platz 2? *(Häufige Fehlerquelle: Der Vorgänger hat einen Bohrer auf Platz 1 vergessen)*.

### 2. Werkstück-Nullpunktaufnahme (`G54`):
* **3D-Kantentaster:** Ankratzen der X-, Y- und Z-Kanten mit der Tastkugel.
* **Kugeldurchmesser abziehen:** Haben Sie daran gedacht, bei X und Y den Kugelradius *(meist 5,00 mm bei einer Ø 10 mm Kugel)* zu verrechnen? Wenn man das vergisst, sitzt das ganze Bauteil 5 mm versetzt!
* **Z-Achse abnullen:** Liegt `Z0` haargenau auf der Werkstück-Oberseite?

### 3. Mechanischer Sitz im Schraubstock:
* **Späne entfernen:** Liegen unter den Parallelunterlagen winzige Aluspäne? Schon ein 0,1 mm dicker Span sorgt dafür, dass das Werkstück schief eingespannt wird und am Ende unbrauchbarer Ausschuss entsteht.
* **Schonhammer benutzen:** Nach dem Festziehen mit dem Kunststoff- oder Kupferhammer kräftig von oben auf das Bauteil schlagen, damit es satt und spielfrei auf den Parallelunterlagen aufliegt.
* **Drehmomentschlüssel:** Wurde der Schraubstock mit der vorgeschriebenen Spannkraft angezogen *(z. B. 60 bis 80 Newtonmeter [Nm])*, damit das Teil beim Fräsen nicht herausgerissen wird?

---

## Phase 5: Erstes Einfahren an der Maschine (First-Part Run & Luftschnitt)

Das erste Bauteil eines neuen Programms wird **niemals vollautomatisch mit 100 % Geschwindigkeit** gestartet! In jeder professionellen CNC-Fertigung gilt das **3-Stufen-Einfahrverfahren**:

```
Schritt 1: Luftschnitt (Z +50 mm)  -->  Schritt 2: Einzelsatz (Single Block)  -->  Schritt 3: Serie mit 100 %
```

### Schritt 1: Die "Luftschnitt-Methode" (Dry Run in Z +50 mm)
1. Gehen Sie in der Maschinensteuerung in den Nullpunktspeicher für `G54`.
2. Addieren Sie auf den Wert von `Z` temporär **+50,00 mm** hinzu *(wenn Z vorher `-180.00` war, tragen Sie `-130.00` ein)*.
3. Starten Sie das Programm: Die Maschine führt alle Fräsbewegungen, Taschen und Bohrungen **exakt 50 mm über dem Werkstück in der freien Luft** aus!
4. **Was Sie mit den Augen prüfen:**
   * Dreht die Spindel in die richtige Richtung?
   * Fährt das Werkzeug an die richtige Ecke?
   * Stimmt die Reihenfolge der Arbeitsgänge?
   * Reicht der Schwenkbereich beim Werkzeugwechsel aus?
5. Nach erfolgreichem Luftschnitt: Den Z-Nullpunkt wieder um **50,00 mm nach unten** auf den echten Bauteilwert setzen!

### Schritt 2: Der erste echte Span im Einzelsatz (Single Block)
* **`Single Block` *(Einzelsatz-Taste)* aktivieren:**  
  Die Steuerung führt jetzt nach jedem Druck auf die grüne Start-Taste **genau eine einzige Zeile G-Code** aus und stoppt danach automatisch.
* **Vorschub-Poti *(Feedrate Override - Drehknopf)*** auf **10 % bis 20 %** drosseln.
* **Blick auf die Restweganzeige (Distance-to-go):**
  * Vor jedem Start-Tastendruck schauen Sie auf das Display: *„Restweg in Z: noch -3.0 mm“*.
  * Sie blicken durch das Sichtfenster: Ist das Werkzeug noch weit genug vom Material entfernt? Wenn die Anzeige sagt *„noch -40 mm“*, das Werkzeug aber schon fast das Bauteil berührt, **sofort STOPP drücken!** Der Nullpunkt oder die Werkzeuglänge stimmt nicht!
* **Schrittweises Beschleunigen:**  
  Sobald der Fräser die ersten Späne sauber abhebt, kein ungewöhnliches Geräusch auftritt und die Späne schön silbrig glänzend abfliegen, schalten Sie den Einzelsatz ab und drehen das Vorschub-Poti langsam von 20 % über 50 % auf 100 %.

### Schritt 3: Rechtliche & fachliche Verantwortung – Wer haftet, wenn der Fräser falsche Werte einstellt?

**Klare juristische und fachliche Antwort:**  
👉 **Der externe CAM-Programmierer / Postprozessor-Entwickler haftet NICHT für Rüst- und Einstellfehler an der realen Maschine!**

In der industriellen Fertigung gilt die klare Trennung der Verantwortungsbereiche:

1. **Die Pflicht des externen CAM-Ingenieurs *(Ihre Verantwortung)***:
   * Sie liefern den fehlerfreien G-Code und das Einrichteblatt.
   * Sie weisen im Programmkopf transparent und exakt die maximalen Tiefen aus: `(T02 | BOHRER D=5.0MM | Z-MIN=-14.500MM)`.
   * Sie haften ausschließlich für die Übereinstimmung Ihres Codes mit dem gelieferten 3D-CAD-Modell.
2. **Die Letztverantwortung des Maschinenbedieners *(Verantwortung der Werkstatt vor Ort)***:
   * Ein Zerspanungsmechaniker ist eine gesetzlich anerkannte Fachkraft.
   * Zu seinen Kernpflichten gehört das **Überprüfen der Rüstsituation**: Er allein entscheidet vor Ort, welche Backenhöhe montiert wird, wie dick die Parallelunterlagen sind und wie weit das Werkzeug ausgespannt wird.
   * Wählt der Fräser trotz des ausgewiesenen Wertes `Z-MIN = -14.500 mm` zu flache Unterlagen oder tastet den Nullpunkt `G54` falsch an, handelt es sich um einen **Bedien- und Rüstfehler der Werkstatt**.
3. **Grobe Fahrlässigkeit bei Blindstart ohne Einzelsatz:**
   * Nach den Unfallverhütungsvorschriften *(DGUV / Berufsgenossenschaft)* und gängiger Rechtsprechung muss jedes Erstteil im **Einzelsatz *(Single Block)*** mit Hand am Poti angefahren werden.
   * Drückt ein Bediener einfach auf Start und lässt die Maschine unkontrolliert crashen, handelt er **grob fahrlässig** *(Verletzung der elementaren handwerklichen Sorgfaltspflicht)*.
4. **Vertraglicher Haftungsschutz (AGB & Einrichteblatt-Klausel):**
   * Mit dem Freigabeprotokoll in [`Portfolio/Vorlage_Einrichteblatt_und_Werkzeugliste.md`](file:///c:/Projekte/CNC/Portfolio/Vorlage_Einrichteblatt_und_Werkzeugliste.md) und der Abnahme-Checkliste zeichnet der Kunde vor Ort ab, dass er die Rüstung eigenverantwortlich geprüft hat.

---

## Druckbare Abnahme-Checkliste für den Kundenauftrag

*Drucken Sie dieses Formular für jeden neuen Kundenauftrag aus. Jeder Kasten muss mit einem Haken `[X]` versehen und abgezeichnet werden, bevor das erste Serienteil ausgeliefert wird:*

```markdown
================================================================================
          CNC-QUALITÄTS- UND FREIGABE-PROTOKOLL (NULL-CRASH-GARANTIE)
================================================================================
Auftrags-Nr.:    ..........................    Datum:             ..............
Kundenname:      ..........................    Programmierer:     ..............
Bauteil-Name:    ..........................    Maschine:          ..............
NC-Programm:     ..........................    Steuerungs-Typ:    ..............
================================================================================

[ ] 1. CAM- & POSTPROZESSOR-PRÜFUNG:
    [ ] Nullpunkt G54 eindeutig festgelegt (X0/Y0 an Kante, Z0 auf Fertigteil-Oberseite)
    [ ] Rohteilaufmaß geprüft (Sägezuschnitt passt zu den CAM-Maßen)
    [ ] Schraubstock als Schutzkörper definiert (mind. 3-5 mm Sicherheitsabstand)
    [ ] Freie Werkzeugauskragung länger als maximale Bauteilfrästiefe

[ ] 2. 3D-SIMULATION (3d_auftrag_simulator.html):
    [ ] Keine rote Eilganglinie (G00) berührt Werkstück, Schraubstock oder Spannmittel
    [ ] Materialeintauchen erfolgt weich über Helix oder schräge Rampe
    [ ] Bemaßungs-Check (📐 Maße Ein/Aus) stimmt mit Zeichnung überein
    [ ] Werkzeugrückzug Z >= 15 mm vor jedem Positionswechsel gewährleistet

[ ] 3. G-CODE-INSPEKTION (.nc Datei):
    [ ] Sicherheitszeile (G90 G17 G21 G94 G40 G49 G80) am Programmanfang vorhanden
    [ ] Werkzeugaufruf (T.. M06) stimmt mit Werkzeugliste überein
    [ ] Spindelbefehl (S.. M03) vor der ersten Schnittbewegung aktiv
    [ ] Werkzeuglängenkorrektur (G43 H.. Z..) aufgerufen
    [ ] Tiefste Frästiefe (Z_min) geprüft und gegen Schraubstock kollisionsfrei
    [ ] Freifahren im Maschinen-Koordinatensystem (G53 Z0 / G28 Z0) am Ende vorhanden
    [ ] Sicheres Programmende mit M05 M09 M30 programmiert

[ ] 4. MASCHINEN-EINRICHTUNG & RÜSTUNG:
    [ ] Werkzeuglängen und Radien mit Messtaster/Voreinstellgerät exakt eingemessen
    [ ] Nullpunkt G54 mit 3D-Taster angetastet und Tastkugelradius (5 mm) verrechnet
    [ ] Schraubstockauflagen mit Druckluft gereinigt, Werkstück mit Hammer niedergeschlagen
    [ ] Schraubstock mit Drehmomentschlüssel (60-80 Nm) fest angezogen
    [ ] Kühlschmierstoff-Füllstand geprüft und Düsen auf Fräserspitze gerichtet

[ ] 5. EINFAHR-PROTOKOLL AN DER MASCHINE:
    [ ] Trockenlauf / Luftschnitt in sicherer Höhe (Z +50 mm) fehlerfrei durchgeführt
    [ ] Z-Nullpunkt wieder auf Originalwert (0.00) zurückgesetzt
    [ ] Erster Schnitt im Einzelsatz (Single Block) mit Vorschub-Poti auf 10-20 %
    [ ] Restweg-Anzeige (Distance-to-go) vor jeder Zustellbewegung kontrolliert
    [ ] Erstes Fertigteil gereinigt, entgratet und alle Maße mit Messschieber/Mikrometer
        auf Maßhaltigkeit gemäß Zeichnungstoleranz überprüft

================================================================================
AUFTRAGS-FREIGABE ERTEILT (SERIENFERTIGUNG / KUNDENAUSLIEFERUNG ERLAUBT):

Unterschrift CAM-Programmierer: ...........................   Datum: ...........
Unterschrift Maschinenbediener: ...........................   Datum: ...........
================================================================================
```

---

## Sofortige Notfall- und Abbruchkriterien (Wann MUSS sofort gestoppt werden?)

Halten Sie beim Einfahren immer eine Hand in der Nähe des **roten Not-Aus-Schlagtasters** oder der **roten Vorschub-Halt-Taste *(Feed Hold)***. In folgenden Situationen müssen Sie **sekundenschnell stoppen**:

1. **Kreischendes, extrem schrilles Pfeifen oder dröhnendes Rattern:**
   * **Ursache:** Das Werkzeug schwingt *(selbsterregte Ratterschwingungen / Chatter)*. Entweder ist der Fräser zu weit ausgespannt, die Drehzahl passt nicht zur Schneidenzahl, oder die Zustellung ist zu aggressiv.
   * **Sofortmaßnahme:** Vorschub-Halt drücken, Drehzahl leicht verändern oder Schnitttiefe verringern.

2. **Späne-Knäuel und Spanstau in tiefen Nuten:**
   * **Ursache:** Die Kühlmitteldüsen spülen die Späne nicht weg. Der Fräser walzt über seine eigenen heißen Späne *(Nachschneiden)*.
   * **Gefahr:** Das Werkzeug setzt sich in Sekundenbruchteilen mit Aluschmelze zu und bricht mit lautem Knall ab.
   * **Sofortmaßnahme:** Stop drücken, Späne mit Druckluft entfernen, Kühlmitteldruck erhöhen.

3. **Restweganzeige auf dem Bildschirm widerspricht den Augen:**
   * **Szenario:** Das Werkzeug steht nur noch 2 mm über dem Metall, aber die Z-Restweganzeige zeigt an, dass die Maschine noch 30 mm nach unten rasen will.
   * **Sofortmaßnahme:** Sofort Not-Aus oder Vorschub-Halt betätigen! Längenoffset `H` und Werkstücknullpunkt `G54` sofort nachprüfen.

4. **Rauchentwicklung oder Brandgeruch:**
   * **Ursache:** Keine Späneabfuhr, stumpfe Schneiden oder die Spindel dreht falsch herum *(Linkslauf M04 statt Rechtslauf M03)*. Das Metall reibt trocken aufeinander, statt geschnitten zu werden.
   * **Sofortmaßnahme:** Spindel-Stop, Werkzeug und Schneidkanten prüfen.

---
*Dokumenten-Referenz:* Zentrales Sicherheits- und Qualitätsprotokoll des CNC-Entwicklungsbereichs ([`C:\Projekte\CNC`](file:///c:/Projekte/CNC)). Verknüpft mit dem Praxis-Kundenauftrag ([`kundenauftrag_01_flanschplatte/EINRICHTEBLATT_SETUP_SHEET.md`](file:///c:/Projekte/CNC/kundenauftrag_01_flanschplatte/EINRICHTEBLATT_SETUP_SHEET.md)) und dem Simulator ([`3d_auftrag_simulator.html`](file:///c:/Projekte/CNC/kundenauftrag_01_flanschplatte/3d_auftrag_simulator.html)).

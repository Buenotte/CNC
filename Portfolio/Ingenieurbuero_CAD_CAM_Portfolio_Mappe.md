# Ingenieurbüro für CAD/CAM-Fertigungstechnik, CNC-Prozessauslegung & Postprozessor-Entwicklung

**Inhaber:** [Dein Vor- und Nachname], Diplom-Ingenieur *(in Deutschland offiziell anerkannter Hochschulabschluss)* & Senior Software Engineer  
**Standort:** 63526 Erlensee *(Einsatzgebiet: Rhein-Main-Gebiet / Hanau / Frankfurt / Aschaffenburg sowie Metropolregion Nürnberg / Fürth / Erlangen – bundesweit per Remote-Engineering)*  
**Kontakt:** [Deine E-Mail-Adresse] | [Deine Telefonnummer]

---

## 1. Ingenieurprofil & Mehrwert für Ihren Fertigungsbetrieb

Als klassisch ausgebildeter **Diplom-Ingenieur *(Studium mit Schwerpunkt Technische Mechanik, Darstellende Geometrie und Höhere Mathematik)*** mit jahrzehntelanger Praxis als **Software Engineer *(Spezialist für Softwarearchitektur, Algorithmen und Schnittstellenprogrammierung)*** verbinde ich zwei Welten, die in der modernen CNC-Zerspanung *(computergesteuerten Metall- und Kunststoffbearbeitung)* selten in einer Person zusammenkommen:

1. **Sichere CAM-Fertigungsplanung & Kollisionsfreie NC-Programme:**
   Auslegung wirtschaftlicher Fräs- und Drehprozesse vom einfachen 2,5D-Serienteil über **3+2-Achsen-Mehrseitenbearbeitung *(angestellte 5-Achs-Bearbeitung in einer Aufspannung)*** bis zur **5-Achs-Simultanbearbeitung *(gleichzeitige Bewegung aller fünf Maschinenachsen für Freiformflächen)*** – inklusive realistischer Schnittdaten *(Drehzahl $n$, Vorschub $v_f$, Schnitttiefe $a_p$, Schnittbreite $a_e$)* und glasklarer **Einrichteblätter *(Setup Sheets für den Maschinenbediener)***.
2. **Postprozessor-Entwicklung & CAM-Automatisierung:**
   Anpassung und Neuprogrammierung Ihrer **Postprozessoren *(Übersetzungsprogramme zwischen CAM-System und CNC-Steuerung)*** für **Heidenhain Klartext *(z. B. iTNC 530, TNC 640, TNC7)***, **Siemens Sinumerik *(840D sl, Sinumerik ONE)***, **Fanuc / Mazak / Haas** – damit Ihre Maschinenbediener an der Steuerung keine einzige Zeile mehr von Hand korrigieren müssen.

---

## 2. Übersicht der 4 technischen Referenzprojekte (Arbeitsproben)

Da echte Kundenzeichnungen in der Zerspanungsindustrie strenger **Geheimhaltung *(NDA – Non-Disclosure Agreement / Zeichnungsschutz)*** unterliegen, finden Sie auf den folgenden Seiten vier vollständig ausgearbeitete **Referenz-Fertigungspakete *(inklusive Aufspannkonzept, Werkzeugliste, Zykluszeitberechnung, Maschinensimulation und echtem NC-Quellcode)***.

---

### Referenzprojekt 01: 2,5D-Präzisionsfrästeil (Lagergehäuse aus 42CrMo4)
* **Ordner im Projektverzeichnis:** [Projekt_01_25D_Praezisionsfraesteil](file:///c:/Projekte/CNC/Portfolio/Projekt_01_25D_Praezisionsfraesteil/Fertigungspaket_Projekt_01.md)
* **Werkstoff:** `42CrMo4` *(1.7225 – Vergütungsstahl mit ca. $900\text{–}1100\,\text{N/mm}^2$ Zugfestigkeit)*
* **Rohteilmaße:** $150 \times 100 \times 45\,\text{mm}$ (Sägezuschnitt mit $2{,}5\,\text{mm}$ Aufmaß pro Seite)
* **Fertigmaße:** $145 \times 95 \times 40\,\text{mm}$ mit zentraler Lagersitzpassung $\varnothing\,52\,\text{H7}$ *(Toleranzfeld $+0 / +0{,}030\,\text{mm}$)* und $6 \times \text{M8}$-Befestigungsgewinden.
* **Technologische Highlights:**
  * **Aufspannkonzept in 2 Operationen:** **OP10 *(Erste Aufspannung im Hochdruckspanner mit Grip-Backen auf $3\,\text{mm}$ Spannrand)*** und **OP20 *(Rückseitenbearbeitung in überfrästen weichen Spannbacken [Formbacken] zur Einhaltung der Planparallelität von $0{,}015\,\text{mm}$)*.**
  * **Trochoidales Hochleistungsschruppen *(HPC – High Performance Cutting / Wirbelfräsen)*** mit konstantem Eingriffswinkel, $a_p = 28\,\text{mm}$ und $a_e = 1{,}2\,\text{mm}$ zur maximalen Schonung der Spindel und gleichmäßigem Verschleiß über die gesamte Schneidenlänge.
  * **Vollständige Entgratung auf der Maschine:** Alle Außenkonturen, Taschenränder und Querbohrungen werden mit einem $90^\circ$-NC-Anbohrer/Fasenfräser ($0{,}3 \times 45^\circ$) mannlos entgratet.
  * **Berechnete Hauptzeit (OP10 + OP20):** `14 Min. 22 Sek.`

---

### Referenzprojekt 02: 3+2-Achsen-Mehrseitenbearbeitung (Hydraulik-Ventilblock aus EN AW-7075)
* **Ordner im Projektverzeichnis:** [Projekt_02_3plus2_Mehrseiten_Ventilblock](file:///c:/Projekte/CNC/Portfolio/Projekt_02_3plus2_Mehrseiten_Ventilblock/Fertigungspaket_Projekt_02.md)
* **Werkstoff:** `EN AW-7075 T6` *(AlZn5,5MgCu – hochfeste Luftfahrt-Aluminiumlegierung)*
* **Maschinenkonzept:** 5-Achs-Bearbeitungszentrum mit Dreh-Schwenktisch *(AC- oder BC-Kinematik)* und 5-Achs-Zentrischspanner *(z. B. Lang Makro-Grip mit Formschluss-Prägung)*.
* **Technologische Highlights:**
  * **5-Seiten-Komplettbearbeitung in einer Aufspannung:** Vermeidung von Umspannfehlern bei schräg zueinander liegenden Kanalbohrungen ($35^\circ$ und $60^\circ$ Raumwinkel).
  * **Sichere Ebenen-Transformation:** Saubere Programmierung über **`PLANE SPATIAL` + `TURN` / `MOVE` *(Heidenhain TNC 640)*** bzw. **`CYCLE800` *(Siemens Sinumerik 840D sl / ONE)*** mit definierter Rückzugsstrategie auf sichere Kugelhöhe vor jeder Schwenkbewegung.
  * **Dynamische Kollisionsprüfung:** Auslegung der **Auskraglängen *(freie Werkzeuglänge aus dem Schrumpffutter HSK-A63)*** so kurz wie möglich (maximale Steifigkeit) und nur so lang wie für den Freigang zum Schwenktisch nötig.
  * **Berechnete Hauptzeit (OP10):** `19 Min. 48 Sek.`

---

### Referenzprojekt 03: 3D-Freiformflächen & 5-Achs-Simultanbearbeitung (Strömungs-Leitrad / Formeinsatz)
* **Ordner im Projektverzeichnis:** [Projekt_03_3D_Freiform_und_5Achs](file:///c:/Projekte/CNC/Portfolio/Projekt_03_3D_Freiform_und_5Achs/Fertigungspaket_Projekt_03.md)
* **Werkstoff:** `1.2379 (X153CrMoV12)` *(Kaltarbeitsstahl für den Werkzeug- und Formenbau)* bzw. `TiAl6V4` *(Titanlegierung für Strömungsbauteile)*.
* **Technologische Highlights:**
  * **Mathematisch geglättete 5-Achs-Vektorführung:** Kontinuierliche Anpassung des **Vorhaltewinkels *(Neigungswinkel des Werkzeugs in Vorschubrichtung)*** und **Seitenwinkels *(Kippwinkel quer zur Vorschubrichtung)*** zur Vermeidung eines Schnitts mit der Zentrumsschneide *(Schnittgeschwindigkeit $v_c = 0\,\text{m/min}$ an der Kugelspitze)*.
  * **Kreissegmentfräser *(Tonnenfräser / Linsenfräser)*** im Schlichtprozess: Reduzierung der Zeilenanzahl um **65 %** bei gleichzeitig besserer theoretischer Rautiefe ($R_z < 2\,\mu\text{m}$) im Vergleich zum klassischen Vollkugelfräser.
  * **Automatische Restmaterial-Kaskade:** Stufenweise Hohlkehlen-Nachbearbeitung ($\varnothing\,6\,\text{mm} \rightarrow \varnothing\,3\,\text{mm} \rightarrow \varnothing\,1{,}5\,\text{mm}$) mit sanften tangentialen Ein- und Ausfahrbögen ohne sichtbare Werkzeugansätze.

---

### Referenzprojekt 04: Postprozessor-Engineering & Automatisierte Fertigungsdokumentation
* **Ordner im Projektverzeichnis:** [Projekt_04_Postprozessor_und_CAM_Automatisierung](file:///c:/Projekte/CNC/Portfolio/Projekt_04_Postprozessor_und_CAM_Automatisierung/Fertigungspaket_Projekt_04.md)
* **Aufgabenstellung:** Standard-Postprozessoren geben oft unübersichtlichen Code aus, vergessen wichtige Maschinenbefehle oder zwingen den Bediener zu gefährlichen Handeingriffen an der Maschine.
* **Entwickelte Ingenieurlösung:**
  * **Maßgeschneiderter Heidenhain- & Sinumerik-Postprozessor:**
    * Automatische Generierung einer vollständigen **Werkzeugübersicht im Programmkopf *(Header-Kommentarblock mit Werkzeugnummer, Name, Durchmesser, Eckenradius und minimaler erforderlicher Auskraglänge)***.
    * Automatische Einfügung von **Taktil-/Laser-Werkzeugbruchkontrollen *(z. B. Blum LaserControl oder Renishaw nach kritischen Schrupp- oder Gewindebohrzyklen)***.
    * Saubere **Unterprogramm-Struktur *(LBL-Aufrufe bei Heidenhain / Unterprogrammtechnik bei Siemens)***, sodass der Maschinenbediener jederzeit problemlos bei einem bestimmten Werkzeug wieder einsteigen kann (**Satzvorlauf-Sicherheit**).
  * **1-Klick-Generator für Einrichteblätter:** Automatisches Auslesen der CAM-Parameter zur Erzeugung eines druckfertigen PDF-/HTML-Einrichteblatts ohne Tippfehler.

---

## 3. Unser risikofreies Angebot zum Kennenlernen: Ihr 1. Probebauteil ist 100 % kostenlos!

Überzeugen Sie sich ohne jedes finanzielle Risiko direkt an Ihrer eigenen CNC-Maschine von der Qualität meiner Arbeit:

1. **Sie senden mir:** Eine 3D-STEP-Datei (`.stp`) + Zeichnung eines aktuellen oder bereits gefertigten Bauteils sowie **ein beliebiges altes NC-Programm Ihrer Maschine** *(damit ich Ihren gewohnten Programmaufbau, Ihre Steuerungszyklen und Ihre Nullpunkt-Logik 1:1 übernehme)*.
2. **Ich liefere Ihnen kostenlos:** Das fertige, kollisionsgeprüfte **NC-Programm**, das komplette **Einrichteblatt mit Aufspannskizze**, die **Werkzeugliste** und ein **Video der Maschinensimulation**.
3. **Sie entscheiden erst danach:** Nur wenn Ihr Maschinenbediener sagt *„Das Programm läuft auf Anhieb sauber und spart uns Zeit“*, unterstützen wir Sie künftig flexibel bei Auftragsspitzen, komplexen 5-Achs-Bauteilen, Urlaubsvertretungen oder Postprozessor-Anpassungen.

# 📘 Großes Praxis-Übungshandbuch: Alle Übungen für CNC-Programmierung (3D-Modelle) & Postprozessor-Entwicklung (JavaScript)

In dieser zentralen Datei sammeln wir **alle praktischen Übungen** Ihres Projekts – Schritt für Schritt, **in einfacher Sprache erklärt** und mit allen **Fachbegriffen in Klammern `(...)` erläutert**. 
Jede neue Übung, die wir gemeinsam machen, wird hier vollständig dokumentiert und ergänzt.

---

## 💡 GRUNDWISSEN VORAB: Warum muss man für CNC-Maschinen JavaScript programmieren – und warum zahlen Metall-Firmen dafür 400 € bis 800 €?

Bevor du mit Übung 1 startest, ist hier in 3 einfachen Punkten erklärt, **warum** du in diesem Handbuch sowohl **CNC-G-Code** als auch **JavaScript (`.cps`)** lernst und warum genau diese Kombination deine Goldgrube ist:

### 1. Warum muss man für eine CNC-Fräsmaschine überhaupt JavaScript programmieren?
* Wenn ein Betrieb im Büro ein **3D-CAM-Programm *(Software zur Fertigungsplanung am PC, z. B. Autodesk Fusion 360)*** nutzt, klickt man dort nur mit der Maus auf ein 3D-Bauteil.
* Jede CNC-Fräsmaschine in der Werkhalle spricht aber einen **anderen Dialekt** *(Heidenhain Klartext, Siemens Sinumerik, Fanuc, Haas, Mazak)* und jeder Werkstatt-Chef hat eigene Sicherheits-Sonderwünsche *(z. B. eine automatische Werkzeugliste am Programmanfang, die Berechnung der tiefsten Frästiefe `Z-MIN` gegen Schraubstock-Crashs oder das Parken des Tisches an der Kabinentür)*.
* **Das Entscheidende:** Für diese Sonderwünsche gibt es im CAM-Programm **keine Knöpfe zum Anklicken**! Stattdessen benutzt das CAM-Programm im Hintergrund eine **Übersetzungs-Datei mit der Endung `.cps` (den Postprozessor)** – und diese Datei ist zu **100 % in der Programmiersprache JavaScript** geschrieben *(bei Siemens NX in Tcl/Python)*. Wer also möchte, dass aus dem CAM-Programm auf Knopfdruck perfekter, sicherer Maschinencode herauskommt, **muss diese `.cps`-JavaScript-Datei öffnen und darin JavaScript-Code programmieren**!

### 2. Warum können der Chef der Metall-Firma („Herr Müller“) und seine Fräser das nicht selbst?
* Ein **Zerspanungsmechaniker *(CNC-Fräser)*** oder **Industriemeister Metall** lernt in seiner 3,5-jährigen Ausbildung alles über Stahl, Aluminium, Fräser, Schraubstöcke und Messschieber – aber **keine einzige Stunde Softwareentwicklung oder JavaScript**!
* Wenn Herr Müller die Datei `mein_erster_post.cps` öffnet und dort 4.000 Zeilen JavaScript-Code (`function onOpen()`, `for`-Schleifen, `getGlobalZRange()`) sieht, versteht er kein Wort.
* Umgekehrt verstehen normale Web-/App-Programmierer zwar JavaScript, wissen aber nicht, was ein Schraubstock, Kühlmittel (`M08`), Gewindebohren (`G84`) oder eine Frästiefe (`Z-MIN`) ist.

### 3. Wofür zahlt Herr Müller DIR mit Freude 400 € bis 800 €?
* Ohne angepassten Postprozessor sieht der Arbeiter an der 200.000-€-Fräsmaschine am Programmanfang nicht, welche Werkzeuge er braucht und wie tief der Fräser nach unten fährt (`Z-MIN`). Spannt er das Metallteil 5 mm zu tief in den Schraubstock, knallt der Fräser in den Stahl-Schraubstock (**5.000 € bis 15.000 € Reparaturkosten!**).
* Du als **Software Engineer & Diplom-Ingenieur** baust Herrn Müller genau die Funktionen aus diesen **16 Übungen** *(automatische Werkzeugliste, `Z-MIN`-Tiefe, Schnittdaten-Check, sicherer Rückzug)* in seine `.cps`-JavaScript-Datei ein.
* Herr Müller bezahlt dich **einmalig (z. B. 400 € bis 800 €)**, bekommt deine umprogrammierte `.cps`-Datei per E-Mail geschickt, und ab diesem Tag kommt bei ihm in der Firma bei jedem Knopfdruck automatisch der perfekte, crashsichere Maschinencode heraus!

### 4. Spielt das Material eine Rolle? (Stahl vs. Aluminium vs. Holz & Kunststoff)
Hier gibt es eine ganz wichtige Unterscheidung:
* **Für die Postprozessor-Programmierung in JavaScript (`.cps`): NEIN – das Material ist zu 99 % egal!**
  Egal ob eine CNC-Maschine **Stahl**, **Aluminium**, **Kunststoff (Plastik)** oder **Holz *(in einer Schreinerei / Tischlerei / im Möbel- und Messebau)*** fräst: **Jede** CNC-Maschine braucht einen Postprozessor (`.cps`), der aus dem 3D-Modell den Maschinencode erzeugt! Und ein Tischlermeister (Holz) kann genauso wenig JavaScript programmieren wie ein Metallbauer. Gerade Schreinereien und Aluminium-/Kunststoff-Betriebe kaufen sich extrem oft *Autodesk Fusion 360* und zahlen dir gutes Geld dafür, dass du ihren Postprozessor anpasst *(z. B. damit sich bei einer Holz-CNC-Fräse automatisch die **Staubabsaugung [Späneabsaugung]** und der **Vakuumtisch [Unterdruck-Plattenspannung]** einschalten statt Kühlwasser!)*.
* **Für die CAM-Programmierung der Schnittdaten (siehe Übung 9): JA – hier entscheidet das Material über Drehzahl (`S`), Vorschub (`F`) und Kühlung!**
  * **Holz & Kunststoff:** Sehr weich $\rightarrow$ extrem hohe Drehzahl (`S18000`–`S24000` U/min), sehr schneller Vorschub (`F3000`–`F8000` mm/min) und **niemals Kühlwasser (`M08` verboten, sonst quillt das Holz auf!)**, sondern nur **Luft / Staubabsaugung (`M07`)**.
  * **Aluminium:** Mittelweich $\rightarrow$ hohe Drehzahl (`S8000`–`S15000` U/min), hoher Vorschub (`F1500`–`F3000` mm/min), spezielle Alu-Fräser mit 2–3 Schneiden *(damit das weiche Alu nicht am Fräser festklebt)*.
  * **Stahl & Edelstahl:** Hart und zäh $\rightarrow$ niedrige Drehzahl (`S1500`–`S4000` U/min), langsamer Vorschub (`F300`–`F800` mm/min) und **viel Kühlwasser (`M08`)**, damit der Fräser nicht ausglüht.

---

## 🧭 Inhaltsverzeichnis aller 16 Übungen (+ 2 Einsteiger-Basis-Übungen)

* **🟢 Einsteiger-Vorübungen:**
  * **[Basis-Übung A](#🟢-stufe-2--basis-übung-a-die-5-wichtigsten-g-code-zeilen-lesen-lernen-schwierigkeit-):** Die 5 wichtigsten **G-Code-Zeilen (Maschinenbefehle)** lesen lernen (`T01 M06`, `S8000 M03`, `M08`, `G00`, `G01`).
  * **[Übung 00b: Hallo Welt (Erste eigene Zeile im Postprozessor)](#übung-00b-hallo-welt-erste-eigene-zeile-im-postprozessor):** Die allererste eigene Code-Zeile mit `writeComment("HALLO WELT...")` und `writeBlock(...)` in der Quellcodedatei [`uebungen/uebung_00b_hallo_welt.cps`](file:///C:/Projekte/CNC/uebungen/uebung_00b_hallo_welt.cps) schreiben, übersetzen und simulieren *(entspricht Basis-Übung B)*.
* **🔵 Grund- & Auftrags-Übungen (Übung 1 bis 8):**
  1. **[Übung 1](#übung-1-der-erste-eigene-text-im-g-code-entwickler-infoblock-in-onopen):** Der erste eigene Text im **G-Code (Maschinensprache)** – Entwickler-Infoblock in `onOpen()` programmieren *(Grundlage aus Ihrer `doc.txt`)*.
  2. **[Übung 2](#übung-2-automatische-werkzeugliste-tool-table-ganz-oben-im-programm-ausgeben):** Automatische **Werkzeugliste (`Tool Table` – Übersicht aller Fräser und Bohrer)** ganz oben im Programm ausgeben.
  3. **[Übung 3](#übung-3-sicherheits-schutz-gegen-maschinencrash--tiefste-frästiefe-z-min-berechnen):** Sicherheits-Schutz gegen **Maschinencrash (Kollision mit dem Schraubstock)** – Tiefste Frästiefe (`Z-MIN`) automatisch berechnen.
  4. **[Übung 4](#übung-4-ein-3d-modell-als-kundenauftrag-bearbeiten-vom-3d-bauteil-zum-g-code):** Ein **3D-Modell (dreidimensionales Bauteil)** als Kundenauftrag bearbeiten – Klick-für-Klick vom 3D-Bauteil zum fertigen **G-Code**.
  5. **[Übung 5](#übung-5-3d-simulation-im-browser--einrichteblatt-setup-sheet-für-den-kunden-erstellen):** **3D-Simulation (visuelle Prüfung am Bildschirm)** durchführen & das **Einrichteblatt (`Setup Sheet` – Rüstplan für die Werkstatt)** erstellen.
  6. **[Übung 6](#übung-6-sicherer-rückzug-safe-retract--tisch-am-programmende-zur-tür-fahren-onclose):** **Sicherer Rückzug (`Safe Retract`)** & Maschinentisch am Programmende (`onClose`) automatisch zur Kabinentür fahren.
  7. **[Übung 7](#übung-7-eigenen-schalter-property-für-zusatzfunktionen-wie-blasluft-m07-oder-späneförderer-bauen):** Eigenen Schalter (`Property` – Auswahlfeld im Menü) für Zusatzfunktionen wie **Blasluft (`M07`)** oder **Späneförderer (Förderband für Metallspäne)** einbauen.
  8. **[Übung 8](#übung-8-zwei-steuerungs-sprachen-vergleichen-haasfanuc-vs-siemens-sinumerik):** Zwei Steuerungs-Sprachen vergleichen und umschalten (**Haas/Fanuc ISO-Dialekt** vs. **Siemens Sinumerik Dialekt**).
* **🟣 Fortgeschrittene Profi-Übungen für echte Online-Aufträge (Übung 9 bis 16):**
  9. **[Übung 9](#übung-9-schnittdaten-s-drehzahl--f-vorschub-berechnen--warum-aluminium-baustahl-und-edelstahl-völlig-andere-werte-brauchen):** **Schnittdaten (`S` Drehzahl & `F` Vorschub)** berechnen – Warum Aluminium, Baustahl und Edelstahl völlig andere Werte brauchen.
  10. **[Übung 10](#übung-10-die-2-aufspannung-g55--op20--wie-das-3d-bauteil-umgedreht-und-der-restboden-auf-der-rückseite-plangefräst-wird):** **Die 2. Aufspannung (`G55` / `OP20`)** – Wie das 3D-Bauteil umgedreht und der Restboden auf der Rückseite plangefräst wird.
  11. **[Übung 11](#übung-11-gewindebohren-g84-rigid-tapping--m6--und-m8-schraubengewinde-ohne-werkzeugbruch-programmieren-f--s--steigung):** **Gewindebohren (`G84` Rigid Tapping)** – `M6`- und `M8`-Schraubengewinde ohne Werkzeugbruch programmieren (`F = S × Steigung`).
  12. **[Übung 12](#übung-12-werkzeugradiuskorrektur-g41--g42--g40--wie-der-kunde-an-der-maschine-001-mm-genauigkeit-für-passungen-einstellt):** **Werkzeugradiuskorrektur (`G41` / `G42` / `G40`)** – Wie der Kunde an der Maschine `0,01 mm` Genauigkeit für Passungen einstellt.
  13. **[Übung 13](#übung-13-echte-3d-freiformflächen--3d-adaptive-clearing-wirbelfräsen--3d-schlichten-mit-kugelfräser-ball-end-mill):** **Echte 3D-Freiformflächen** – `3D Adaptive Clearing` (Wirbelfräsen) & `3D-Schlichten` mit **Kugelfräser (`Ball End Mill`)**.
  14. **[Übung 14](#übung-14-heidenhain-klartext-steuerung-tool-call-l--fmax--4-drehachse-a-achse-für-aufträge-im-deutschsprachigen-raum):** **Heidenhain Klartext-Steuerung (`TOOL CALL`, `L ... FMAX`) & 4. Drehachse (`A-Achse`)** für Aufträge im deutschsprachigen Raum.
  15. **[Übung 15](#übung-15-kanten-entgraten-am-3d-modell-2d-fase--chamfer-milling-mit-einem-45-fasenfräser-t04):** **Kanten entgraten am 3D-Modell (`2D-Fase / Chamfer Milling`)** mit einem $90^\circ$/$45^\circ$-Fasenfräser (`T04`).
  16. **[Übung 16](#übung-16-die-komplette-5-punkte-endabnahme-im-simulator-vor-der-auslieferung-an-den-online-kunden-meister-prüfung):** **Die komplette 5-Punkte-Endabnahme im Simulator** vor der Auslieferung an den Online-Kunden (Meister-Prüfung).
* **🛡️ Meister-Sicherheits- und Qualitätsprüfung:**
  * **[Sicherheits- und Qualitätsprüfprotokoll für CNC-G-Code (Null-Kollisions-Garantie & Abnahme-Checkliste)](file:///c:/Projekte/CNC/SICHERHEITS_UND_QUALITAETS_PRUEFLISTE_GCODE.md):** Umfassende 5-Stufen-Prüfkette vor dem Ausliefern an den Kunden oder dem ersten Span auf der Fräsmaschine *(CAM-Prüfung, 3D-Simulation, G-Code-Syntaxcheck, Maschinen-Rüsten, Luftschnitt)*.

---

## 📂 Zentrale Übersicht: Alle Source-Dateien (Quellcode-Dateien) für jede Übung

### 🔗 Was verbindet die Einzeldateien in `uebungen/` mit dem Haupt-Postprozessor `src/mein_erster_post.cps`?

Um die Architektur Ihres Projekts auf einen Blick zu verstehen:

1. **Die Einzeldateien (`uebungen/uebung_01_...cps` bis `uebung_16_...cps`):**  
   Das sind **isolierte Trainings- und Lernbausteine**. Jede dieser Dateien enthält nur die rund 30 bis 50 Zeilen Code, die genau zu diesem einen Thema gehören *(z. B. nur der `onOpen`-Header, nur die `Z-MIN`-Schleife oder nur der `G84`-Gewindezyklus)*.  
   * **Vorteil:** Sie können den Code in Sekunden erfassen, ohne sich in tausenden Zeilen zu verirren, und die Datei unabhängig testen.

2. **Der Haupt-Postprozessor (`src/mein_erster_post.cps`):**  
   Das ist das **Gesamtkunstwerk (das fertige Endprodukt)**. Hier sind **alle 16 Bausteine aus den Übungen zusammengeführt** und bilden einen vollständigen, 500-zeiligen Postprozessor für 3-Achs-Fräsmaschinen.

3. **Der rote Faden (Die Verbindung):**  
   * Jede Funktion, die Sie in einer Einzeldatei isoliert testen *(z. B. `writeComment` in Übung 1, `getToolTable` in Übung 2, `getGlobalZRange` in Übung 3 oder `onClose` in Übung 6)*, ist **haargenau an der entsprechenden Stelle in `src/mein_erster_post.cps` eingebaut**.
   * Wenn Sie eine Einzeldatei verstanden und geändert haben, können Sie denselben Codeblock 1:1 in den Haupt-Postprozessor übernehmen.
   * Am Ende mündet alles in **Übung 16 ([`uebung_16_endabnahme_meister_post.cps`](file:///C:/Projekte/CNC/uebungen/uebung_16_endabnahme_meister_post.cps))**, die die geprüfte Essenz des gesamten Projekts darstellt.

---

### 📋 Tabelle aller Übungsdateien und ihrer Gegenstücke:

Alle Quellcodedateien *(JavaScript `.cps` Postprozessoren, 3D-CAD-Modelle und Simulatoren)* befinden sich fertig vorbereitet im Ordner [`C:\Projekte\CNC\uebungen\`](file:///C:/Projekte/CNC/uebungen/) sowie im Kundenauftrags-Ordner. Sie können jede dieser Dateien einzeln in Visual Studio Code öffnen, anpassen und direkt im Terminal *(Befehlsfenster)* mit dem Simulator ausführen:

| Nr. | Übungsthema | Quelldatei *(Pfad)* | Ausführen & Testen im Terminal *(Befehl)* |
|---|---|---|---|
| **00b** | Basis-Übung B *(Hallo Welt)* | [`uebungen/uebung_00b_hallo_welt.cps`](file:///C:/Projekte/CNC/uebungen/uebung_00b_hallo_welt.cps) | `node tests/simuliere_post.js uebungen/uebung_00b_hallo_welt.cps` |
| **01** | Entwickler-Header *(onOpen)* | [`uebungen/uebung_01_entwickler_header.cps`](file:///C:/Projekte/CNC/uebungen/uebung_01_entwickler_header.cps) | `node tests/simuliere_post.js uebungen/uebung_01_entwickler_header.cps` |
| **02** | Werkzeugliste *(Tool Table)* | [`uebungen/uebung_02_werkzeugliste.cps`](file:///C:/Projekte/CNC/uebungen/uebung_02_werkzeugliste.cps) | `node tests/simuliere_post.js uebungen/uebung_02_werkzeugliste.cps` |
| **03** | Z-MIN Berechnung *(Crashschutz)* | [`uebungen/uebung_03_z_min_berechnung.cps`](file:///C:/Projekte/CNC/uebungen/uebung_03_z_min_berechnung.cps) | `node tests/simuliere_post.js uebungen/uebung_03_z_min_berechnung.cps` |
| **04** | 3D-Modell CAM-Operationen | [`uebungen/uebung_04_3d_modell_cam.cps`](file:///C:/Projekte/CNC/uebungen/uebung_04_3d_modell_cam.cps) & [`bauteil_1001.stl`](file:///C:/Projekte/CNC/kundenauftrag_01_flanschplatte/bauteil_1001.stl) | `node tests/simuliere_post.js uebungen/uebung_04_3d_modell_cam.cps` |
| **05** | 3D-Simulator & Einrichteblatt | [`3d_auftrag_simulator.html`](file:///C:/Projekte/CNC/kundenauftrag_01_flanschplatte/3d_auftrag_simulator.html) & [`EINRICHTEBLATT.md`](file:///C:/Projekte/CNC/kundenauftrag_01_flanschplatte/EINRICHTEBLATT_SETUP_SHEET.md) | Doppelklick im Windows-Explorer auf `3d_auftrag_simulator.html` |
| **06** | Sicherer Rückzug *(Safe Retract)* | [`uebungen/uebung_06_sicherer_rueckzug.cps`](file:///C:/Projekte/CNC/uebungen/uebung_06_sicherer_rueckzug.cps) | `node tests/simuliere_post.js uebungen/uebung_06_sicherer_rueckzug.cps` |
| **07** | Späneförderer Schalter *(Property)* | [`uebungen/uebung_07_spaenefoerderer_schalter.cps`](file:///C:/Projekte/CNC/uebungen/uebung_07_spaenefoerderer_schalter.cps) | `node tests/simuliere_post.js uebungen/uebung_07_spaenefoerderer_schalter.cps` |
| **08** | Fanuc vs. Siemens Sinumerik | [`uebungen/uebung_08_fanuc_siemens_dialekt.cps`](file:///C:/Projekte/CNC/uebungen/uebung_08_fanuc_siemens_dialekt.cps) | `node tests/simuliere_post.js uebungen/uebung_08_fanuc_siemens_dialekt.cps` |
| **09** | Schnittdaten-Plausibilitätsprüfung | [`uebungen/uebung_09_schnittdaten_check.cps`](file:///C:/Projekte/CNC/uebungen/uebung_09_schnittdaten_check.cps) | `node tests/simuliere_post.js uebungen/uebung_09_schnittdaten_check.cps` |
| **10** | 2. Aufspannung *(G55 OP20)* | [`uebungen/uebung_10_zweite_aufspannung_g55.cps`](file:///C:/Projekte/CNC/uebungen/uebung_10_zweite_aufspannung_g55.cps) | `node tests/simuliere_post.js uebungen/uebung_10_zweite_aufspannung_g55.cps` |
| **11** | Gewindebohren *(G84 Rigid Tapping)*| [`uebungen/uebung_11_gewindebohren_g84.cps`](file:///C:/Projekte/CNC/uebungen/uebung_11_gewindebohren_g84.cps) | `node tests/simuliere_post.js uebungen/uebung_11_gewindebohren_g84.cps` |
| **12** | Radiuskorrektur *(G41/G42/G40)* | [`uebungen/uebung_12_radiuskorrektur_g41.cps`](file:///C:/Projekte/CNC/uebungen/uebung_12_radiuskorrektur_g41.cps) | `node tests/simuliere_post.js uebungen/uebung_12_radiuskorrektur_g41.cps` |
| **13** | 3D-Freiformflächen-Fräsen | [`uebungen/uebung_13_3d_freiformflaechen.cps`](file:///C:/Projekte/CNC/uebungen/uebung_13_3d_freiformflaechen.cps) | `node tests/simuliere_post.js uebungen/uebung_13_3d_freiformflaechen.cps` |
| **14** | Heidenhain Klartext & 4. Achse | [`uebungen/uebung_14_heidenhain_klartext_4achse.cps`](file:///C:/Projekte/CNC/uebungen/uebung_14_heidenhain_klartext_4achse.cps) | `node tests/simuliere_post.js uebungen/uebung_14_heidenhain_klartext_4achse.cps` |
| **15** | Fasenfräsen & Entgraten *(45°)* | [`uebungen/uebung_15_fasenfraesen_entgraten.cps`](file:///C:/Projekte/CNC/uebungen/uebung_15_fasenfraesen_entgraten.cps) | `node tests/simuliere_post.js uebungen/uebung_15_fasenfraesen_entgraten.cps` |
| **16** | Meister-Post Endabnahme | [`uebungen/uebung_16_endabnahme_meister_post.cps`](file:///C:/Projekte/CNC/uebungen/uebung_16_endabnahme_meister_post.cps) | `node tests/simuliere_post.js uebungen/uebung_16_endabnahme_meister_post.cps` |

* **🤖 Nach den 16 Übungen – Deine 4 KI-Agenten im Praxiseinsatz:**
  * **[WANN und WIE du deine 4 KI-Agenten verwendest (Zeilen 935–971)](#🤖-wann-und-wie-du-deine-4-ki-agenten-verwendest-goldene-regel-für-die-übungen--praxisanleitung-nach-übung-16):** Warum du Übung 1–15 erst selbst ohne KI machst und welcher KI-Agent dir ab Übung 16 welche Übungen zu 80 % abnimmt.

---

## 🛡️ WANN und WIE wendest du die Sicherheits- und Qualitätsprüfliste an?

Viele stellen sich die Frage: *„Muss ich das Dokument [`SICHERHEITS_UND_QUALITAETS_PRUEFLISTE_GCODE.md`](file:///c:/Projekte/CNC/SICHERHEITS_UND_QUALITAETS_PRUEFLISTE_GCODE.md) als allererstes komplett von vorn bis hinten durchlesen?“*

### Die kurze Antwort: NEIN, auf keinen Fall als Erstes auswendig lernen!
* **Die Sicherheitsprüfliste ist dein Referenz-Handbuch und Schutzschild:**  
  Genau wie die Checkliste im Cockpit eines Passagierflugzeugs liest man sie nicht wie einen Roman durch, sondern nutzt sie als **begleitenden Spickzettel und professionelles Abnahme-Protokoll**.
* **Für deine Übungen gilt:** Du beginnst ganz entspannt Schritt für Schritt mit **Übung 01** ([`uebungen/uebung_01_entwickler_header.cps`](file:///c:/Projekte/CNC/uebungen/uebung_01_entwickler_header.cps)). Jede Übung baut genau einen Baustein dieser Sicherheitskette auf.

### 🗺️ Fahrplan: Welche Übung baut welche Phase der Sicherheitsprüfliste auf?

| Phase aus [`SICHERHEITS_UND_QUALITAETS_PRUEFLISTE_GCODE.md`](file:///c:/Projekte/CNC/SICHERHEITS_UND_QUALITAETS_PRUEFLISTE_GCODE.md) | Was wird dort geprüft? | In welchen Übungen lernst und baust du das? |
| :--- | :--- | :--- |
| **Phase 1:<br>CAM-System & Postprozessor** | Nullpunkt `G54` *(Werkstück-Koordinatensystem)*, Rohteilaufmaß, Spannmittelschutz, Auskraglänge | • **Übung 4:** 3D-Modell CAM-Setup und Nullpunkt `G54`<br>• **Übung 9:** Schnittdatenprüfung Drehzahl `S` und Vorschub `F`<br>• **Übung 10:** 2. Aufspannung `G55` *(umgedrehtes Teil)* |
| **Phase 2:<br>3D-Simulation & Bemaßung** | Rote Eilganglinien `G00` *(Schnellgang)*, grüne Schnittbahnen `G01` *(Arbeitsgang)*, Maße-Check `📐` | • **Übung 00b:** Erste Simulation im Browser<br>• **Übung 5:** 3D-Simulation und Einrichteblatt<br>• **Übung 13:** 3D-Freiformflächen im Simulator prüfen |
| **Phase 3:<br>G-Code-Textinspektion** | Sicherheitszeile (`G90 G17...`), Werkzeugliste, Längenkorrektur `G43`, tiefste Tiefe `Z_min`, Rückzug `G53 Z0` | • **Übung 01:** Entwickler-Header & Sicherheitszeile in `onOpen()`<br>• **Übung 02:** Automatische Werkzeugtabelle *(Tool Table)*<br>• **Übung 03:** Automatische Berechnung von `Z_min` *(Crash-Schutz)*<br>• **Übung 06:** Sicherer Rückzug in `onClose()`<br>• **Übung 11 & 12:** `G84` Gewindebohren & `G41` Radiuskorrektur |
| **Phase 4:<br>Maschinen-Rüstung** | Werkzeug einmessen, 3D-Taster, Spannkraft im Schraubstock | • **Übung 5 & Portfolio:** Einrichteblatt für den Maschinenbediener mit allen Rüstdaten |
| **Phase 5:<br>Einfahren & First-Part Run** | Luftschnitt (`Z +50 mm`), Einzelsatz (`Single Block`), Vorschub-Poti | • **Übung 16:** Die komplette 5-Punkte-Endabnahme vor der Auslieferung an den Kunden! |

### 🚀 Wann holst du die Checkliste ganz konkret heraus?
1. **Beim Lernen (Übung 1–15):** Wann immer eine Übung eine neue Zeile G-Code erzeugt, wirfst du einen kurzen Blick in die Spickzettel-Tabelle von Phase 3, um den Befehl auf Deutsch zu verstehen.
2. **Bei Übung 16 (Meisterprüfung):** Du nimmst die **Druckbare Abnahme-Checkliste** aus [`SICHERHEITS_UND_QUALITAETS_PRUEFLISTE_GCODE.md`](file:///c:/Projekte/CNC/SICHERHEITS_UND_QUALITAETS_PRUEFLISTE_GCODE.md) und hakst Punkt für Punkt ab.
3. **Im echten Kundenauftrag (Später im Beruf / bei Freelancer-Aufträgen):** Du druckst die Checkliste aus, hakst sie ab und legst sie unterschrieben deiner Rechnung bei – damit hat der Kunde 100 % Vertrauen und du bist rechtlich gegen Regressansprüche abgesichert!

---

## 📌 DER GROSSE CNC-MEISTER-SPICKZETTEL: Alle G-Code- & M-Code-Kennzeichen auf einen Blick

Bevor Sie eine Übung starten, finden Sie hier die **zentrale Schnellreferenz aller Maschinenbefehle**. Mehr als diese Kennzeichen benötigen 95 % aller CNC-Fräsmaschinen weltweit nicht!

| Kennzeichen | Fachbegriff & Erklärung | Was die Fräsmaschine exakt tut: |
|---|---|---|
| **`(...)`** | **Kommentar *(Bediener-Notiz)*** | Reiner Text für den Fräser am Bildschirm. Die Steuerung ignoriert den Text und führt keine Achsbewegung aus. |
| **`G90`** | **Absolutmaß *(Absolute Positioning)*** | Alle Verfahrkoordinaten $X, Y, Z$ beziehen sich fest auf den Bauteil-Nullpunkt `G54`. |
| **`G91`** | **Inkrementalmaß / Kettenmaß *(Incremental)*** | Maße beziehen sich relativ auf die jeweils letzte Werkzeugposition. |
| **`G17`** | **XY-Bearbeitungsebene *(Plane Selection)*** | Standard-Fräsebene von oben *(Werkzeugachse ist die Z-Achse)*. |
| **`G21`** | **Metrisches Einheitensystem *(Metric Mode)*** | Alle Weg- und Vorschubangaben werden in **Millimetern** interpretiert. |
| **`G20`** | **Zoll-Einheitensystem *(Imperial Mode)*** | Alle Wegangaben werden in **Inch / Zoll** ($1\,\text{Zoll} = 25,4\,\text{mm}$) interpretiert. |
| **`G94`** | **Vorschub pro Minute *(Feed per Minute)*** | Vorschubgeschwindigkeit $F$ wird in **$\text{mm/min}$ *(Millimeter pro Minute)*** gerechnet. |
| **`G00`** | **Eilgang *(Rapid Traverse)*** | Schnellstmögliche Bewegung der Achsen durch die Luft *(ohne Materialberührung)*. |
| **`G01`** | **Linearer Fräsvorschub *(Linear Interpolation)*** | Gerade Schnittbewegung im Werkstoff mit programmierter Arbeitsgeschwindigkeit $F$. |
| **`G02`** | **Kreisbogen im Uhrzeigersinn *(Circular CW)*** | Fräst eine kreisförmige Bahn nach rechts mit Radius $R$ oder Mittelpunkt $I, J$. |
| **`G03`** | **Kreisbogen gegen Uhrzeigersinn *(Circular CCW)*** | Fräst eine kreisförmige Bahn nach links *(Standard beim Gleichlauffräsen von Taschen)*. |
| **`G28`** | **Referenzpunktfahrt *(Return to Home)*** | Fährt die Achsen an die festen Maschinen-Endschalter *(z. B. `G28 G91 Z0.` ganz nach oben)*. |
| **`G53`** | **Maschinen-Koordinatensystem *(Machine Coordinates)*** | Nicht-verschiebbarer Nullpunkt der Fräsmaschine *(meist oben an der Kabinendecke)*. |
| **`G54`–`G59`**| **Werkstück-Koordinatensysteme *(Work Offsets)*** | Bauteil-Nullpunkte: `G54` = 1. Aufspannung, `G55` = 2. Aufspannung *(umgedrehtes Teil)*. |
| **`G40`** | **Radiuskorrektur ABWÄHLEN *(Cutter Comp Off)*** | Schaltet Fräserradiuskorrekturen aus; Werkzeug fährt exakt mit der Mitte auf der Kontur. |
| **`G41`** | **Fräserradiuskorrektur LINKS *(Cutter Comp Left)*** | Fräser fährt links an der Werkstückkontur entlang *(für Passungen auf 0,01 mm genau)*. |
| **`G42`** | **Fräserradiuskorrektur RECHTS *(Cutter Comp Right)***| Fräser fährt rechts an der Kontur entlang *(Gegenlauffräsen)*. |
| **`G43`** | **Werkzeuglängenkorrektur EIN *(Tool Length Comp)***| Aktiviert die gespeicherte Werkzeuglänge `H...` aus der Vermessung. |
| **`G80`** | **Bohrzyklen ABBRECHEN *(Cancel Canned Cycle)*** | Beendet alle aktiven Bohrbefehle sicher vor dem nächsten Schritt. |
| **`G81`** | **Bohrzyklus Standard *(Drilling Cycle)*** | Einfaches Zentrieren und Bohren bis zur Tiefe $Z$, danach sofortiger Rückzug. |
| **`G83`** | **Tieflochbohren mit Spanbruch *(Peck Drilling)*** | Bohrer taucht stufenweise ein (`Q`), zieht zwischendurch ganz heraus, um Späne auszuwerfen. |
| **`G84`** | **Gewindebohren synchronisiert *(Rigid Tapping)*** | Schneidet Schraubengewinde synchron mit Drehzahl und Steigung *(Vorschub $F = S \times \text{Steigung}$)*. |
| **`T01`–`T99`**| **Tool-Nummer *(Werkzeugplatz)*** | Nummer des Werkzeugs im Magazin-Karussell der Fräsmaschine. |
| **`M06`** | **Werkzeugwechsel *(Tool Change)*** | Mechanischer Greifarm holt das gewählte Werkzeug $T$ physisch in die Spindel. |
| **`S...`** | **Spindeldrehzahl *(Speed)*** | Rotationsgeschwindigkeit der Spindel in $\text{U/min}$ *(Umdrehungen pro Minute)*. |
| **`M03`** | **Spindel Rechtslauf EIN *(Spindle Clockwise)***| Startet den Spindelmotor im Uhrzeigersinn *(Schneidrichtung von 99 % aller Fräser)*. |
| **`M04`** | **Spindel Linkslauf EIN *(Spindle CCW)*** | Startet Spindel gegen den Uhrzeigersinn *(für Linksgewinde oder Linksschneider)*. |
| **`M05`** | **Spindel-Stopp *(Spindle Stop)*** | Schaltet den Spindelmotor sicher ab. |
| **`M07`** | **Blasluft / Minimalmengenschmierung *(Air Blast)*** | Schaltet Druckluft oder Späneabsaugung EIN *(wichtig für Holz und Kunststoff)*. |
| **`M08`** | **Kühlmittel EIN *(Flood Coolant)*** | Schaltet die Hochdruck-Kühlwasserpumpe EIN *(wichtig für Stahl und Aluminium)*. |
| **`M09`** | **Kühlmittel AUS *(Coolant Off)*** | Schaltet alle Kühlmittelpumpen und Luftdüsen AUS. |
| **`M30`** | **Programmende & Rücksprung *(Program End)*** | Beendet das Fräsprogramm, schaltet Aggregate aus und setzt den Zeiger auf Zeile 1 zurück. |

---

## 🔌 Ihre installierten Visual Studio Code (VSC) Erweiterungen: Wie Sie diese für die Übungen benutzen

Auf Ihrem System sind die wichtigsten Erweiterungen bereits installiert. Hier ist die genaue Übersicht, welche davon für Ihre CNC-Postprozessor-Übungen unverzichtbar sind und wie Sie sie mit wenigen Klicks bedienen:

### 1. `Autodesk HSM Post Processor` (`autodesk.hsm-post-processor`) – Der offizielle Post-Simulator von Autodesk
Dies ist die wichtigste Profi-Erweiterung für Autodesk Fusion Postprozessoren!
* **Wofür ist sie da?**  
  Sie ermöglicht es, eine `.cps`-Datei direkt in VS Code per Mausklick gegen echte CAM-Testdateien *(sogenannte `.intermediate` oder `.cnc` Benchmark-Werkzeugwege)* laufen zu lassen – ganz ohne Fusion 360 installieren zu müssen!
* **Wie benutzen Sie diese Erweiterung Schritt für Schritt?**
  1. Öffnen Sie eine `.cps`-Datei *(z. B. `uebungen/uebung_01_entwickler_header.cps` oder `src/mein_erster_post.cps`)*.
  2. Drücken Sie die Tastenkombination `Strg + Umschalt + P` *(öffnet die VS Code Befehlspalette)*.
  3. Tippen Sie ein: `Post Process` und wählen Sie den Befehl **`Autodesk Fusion Post Processor: Post Process`**.
  4. Die Erweiterung fragt Sie nach einer Benchmark-Datei *(z. B. 2D-Fräsen oder 3D-Kontur)*.
  5. **Ergebnis:** Rechts neben Ihrem Code öffnet sich automatisch ein zweiter Editor-Reiter mit dem frisch erzeugten CNC-Code!

### 2. `Stingray Debug` (`jschmidt42.stingray-debug`) – Der Postprozessor-Debugger
* **Wofür ist sie da?**  
  Arbeitet nahtlos mit der Autodesk Post-Erweiterung zusammen. Sie erlaubt es, **Breakpoints (rote Haltepunkte)** im JavaScript-Code zu setzen.
* **Wie benutzen Sie sie?**
  * Wenn Sie links neben eine Zeilennummer im Code klicken *(roter Punkt erscheint)*, stoppt die Ausführung bei `Post Process` genau an dieser Zeile, und Sie können sich den Inhalt aller Variablen *(z. B. Werkzeugdurchmesser oder Z-Höhen)* live ansehen.

### 3. `GitHub Copilot & Copilot Chat` (`github.copilot`, `github.copilot-chat`) & `Claude Code`
* **Wofür sind sie da?**  
  Ihre KI-Programmier-Assistenten direkt in der Seitenleiste von VS Code.
* **Wie benutzen Sie sie?**
  * Klicken Sie ganz links in der Seitenleiste auf das Chat-Symbol *(Sprechblase)*.
  * Sie können Fragen stellen wie: *„Erkläre mir Zeile 25 in uebung_03_z_min_berechnung.cps auf Deutsch“* oder *„Schreibe mir eine Sicherheitsabfrage für die Spindeldrehzahl“*.
  * *(Hinweis: Wie im Handbuch empfohlen, sollten Sie die Übungen 1 bis 15 zuerst selbst durchführen, um die Mechanik wirklich zu verstehen, und die KI als Erklär-Helfer nutzen).*

### 4. `Markdown PDF` (`yzane.markdown-pdf`) – Handbuch und Einrichteblatt als PDF drucken
* **Wofür ist sie da?**  
  Wandelt Markdown-Dokumente (`.md`) mit einem Klick in druckbare PDF-Dateien für den Kunden oder Maschinenbediener um.
* **Wie benutzen Sie sie?**
  1. Öffnen Sie eine Dokumentationsdatei *(z. B. `ALLE_UEBUNGEN_HANDBUCH.md` oder `EINRICHTEBLATT_SETUP_SHEET.md`)*.
  2. Machen Sie einen Rechtsklick irgendwo in den Text.
  3. Wählen Sie im Kontextmenü **`Markdown PDF: Export (pdf)`**.
  4. In wenigen Sekunden liegt eine fertige, professionell formatierte PDF-Datei im selben Ordner!

---

# Übung 00b: Hallo Welt (Erste eigene Zeile im Postprozessor)

### 📌 Spickzettel dieser Übung: Alle verwendeten G-Code- & M-Code-Kennzeichen in Übung 00b

| Kennzeichen | Fachbegriff & Erklärung | Bedeutung & Funktion in dieser Übung |
|---|---|---|
| **`(...)`** | **Kommentar *(Bediener-Notiz / Information für den Fräser)*** | Schreibt reine Notizen wie `writeComment("HALLO WELT...")`, die von der Fräsmaschinen-Steuerung komplett ignoriert werden. |
| **`G90`** | **Absolutmaß *(Absolute Mode)*** | Alle Maße beziehen sich auf den Werkstück-Nullpunkt `G54`. |
| **`G17`** | **XY-Bearbeitungsebene *(Plane Selection)*** | Standard-Fräsebene von oben *(Werkzeugachse ist die Z-Achse)*. |
| **`G21`** | **Metrisches Einheitensystem *(Metric Mode)*** | Alle Maßangaben sind in Millimetern. |
| **`G94`** | **Vorschub-Einheit *(Feed per Minute)*** | Vorschubgeschwindigkeit $F$ wird in $\text{mm/min}$ *(Millimeter pro Minute)* gerechnet. |
| **`G28 G91 Z0.`** | **Referenzpunktfahrt Z *(Return to Home Z)*** | Z-Achse fährt senkrecht nach oben an den oberen Maschinen-Endschalter *(Crash-Schutz)*. |
| **`T1` / `T2`** | **Werkzeugnummer *(Tool Number)*** | `T1` = Schaftfräser $\varnothing 10\,\text{mm}$ \| `T2` = Spiralbohrer $\varnothing 6\,\text{mm}$. |
| **`M06`** | **Werkzeugwechsel *(Tool Change)*** | Mechanischer Greifarm holt das Werkzeug $T$ physisch in die Frässpindel. |
| **`S8000` / `S3500`** | **Spindeldrehzahl *(Spindle Speed)*** | Drehzahl des Fräsers in $\text{U/min}$ *(Umdrehungen pro Minute)*. |
| **`M03`** | **Spindel Rechtslauf EIN *(Spindle Clockwise)*** | Schaltet den Frässpindelmotor im Uhrzeigersinn ein. |
| **`G54`** | **Werkstück-Nullpunkt 1 *(Work Coordinate System)*** | Nullpunkt-Lage an der vorderen linken oberen Bauteilecke. |
| **`M05`** | **Spindel-Stopp *(Spindle Stop)*** | Schaltet den Frässpindelmotor am Programmende aus. |
| **`M09`** | **Kühlmittel AUS *(Coolant Off)*** | Schaltet die Kühlwasserpumpe aus. |
| **`G28 Y0.`** | **Tisch zur Schutztür *(Table to Door)*** | Fährt den Maschinentisch nach vorne zum bequemen Entnehmen des fertigen Werkstücks. |
| **`M30`** | **Programmende *(Program End and Rewind)*** | Beendet die Abarbeitung und setzt den Programmzeiger im Speicher auf Zeile 1 zurück. |

### 💡 Worum geht es in einfacher Sprache?

Bevor Sie mit Variablen oder komplexen Schleifen arbeiten, ist **Übung 00b** das sogenannte **„Hallo Welt“-Programm *(der klassische allererste Test in der Softwareentwicklung)***.
Das Ziel ist es, zu verstehen, wie Sie mit der JavaScript-Funktion `writeComment(...)` eine eigene Textzeile in runden Klammern `(...)` und mit `writeBlock(...)` echte **G-Code-Maschinenbefehle *(Steuerbefehle für die CNC-Fräsmaschine)*** in die Maschinendatei schreiben.

### 🛠️ Wo im Code wird das gemacht?

Für diese Übung steht Ihnen die fertige Quellcodedatei zur Verfügung:  
👉 [`uebungen/uebung_00b_hallo_welt.cps`](file:///C:/Projekte/CNC/uebungen/uebung_00b_hallo_welt.cps)

In dieser Datei sehen Sie in der Funktion **`onOpen()`** *(wird immer automatisch ganz zu Beginn der Übersetzung aufgerufen)*:

```javascript
function onOpen() {
  // Hier steht Ihre allererste eigene Zeile im CNC-Code:
  writeComment("========================================"); // Optische Trennlinie als Kommentar
  writeComment("HALLO WELT - MEIN ERSTER CNC POSTPROZESSOR"); // Begrüßungstext in runden Klammern (...)
  writeComment("ERFOLGREICH ERSTE ZEILE EINGEFUEGT");        // Bestätigungskommentar
  writeComment("========================================"); // Trennlinie

  // Grundinitialisierung der Fräsmaschine:
  // G90 = Absolute Maßangaben in Bezug auf das Werkstück (Nullpunkt G54)
  // G17 = Fräsbearbeitung in der XY-Hauptebene (Z-Achse ist die Spindelachse)
  // G21 = Alle Maßeinheiten sind in Millimeter (metrisches System)
  // G94 = Vorschubgeschwindigkeit F wird in mm/min (Millimeter pro Minute) interpretiert
  writeBlock("G90", "G17", "G21", "G94");

  // Sicherheitsfahrt der Z-Achse auf den Referenzpunkt:
  // G28 = Fahre auf Maschinen-Referenzpunkt (feste Endschalter der Fräsmaschine)
  // G91 = Relativmaß (Inkrementell / Kettenmaß)
  // Z0. = Relativ um 0 mm verfahren, also direkt senkrecht nach oben auf Z-Referenzhöhe
  writeBlock("G28", "G91", "Z0.");

  // G90 = Sofort wieder zurückschalten in den Absolutmaß-Modus für alle weiteren Befehle
  writeBlock("G90");
}

function onSection() {
  var tool = currentSection.getTool();
  writeComment("--- WERKZEUGWECHSEL ---");
  // T.. = Werkzeugplatz im Magazin (Tool Number)
  // M06 = Automatischer Werkzeugwechsel durch mechanischen Greifer
  writeBlock("T" + tool.number, "M06");

  // S.. = Spindeldrehzahl in U/min (Spindle Speed)
  // M03 = Frässpindel im Uhrzeigersinn (Rechtslauf) starten
  writeBlock("S" + tool.spindleRPM, "M03");

  // G54 = 1. Werkstück-Koordinatensystem (Nullpunkt an Bauteilecke)
  writeBlock("G54");
}

function onClose() {
  writeComment("--- PROGRAMMENDE ---");
  // M05 = Frässpindel ausschalten (Spindel-Stopp)
  writeBlock("M05");

  // M09 = Kühlschmierstoff ausschalten (KSS AUS)
  writeBlock("M09");

  // G28 G91 Z0. = Z-Achse ganz nach oben auf Maschinenreferenz fahren
  writeBlock("G28", "G91", "Z0.");

  // G28 Y0. = Maschinentisch nach vorne zur Kabinentür fahren
  writeBlock("G28", "Y0.");

  // M30 = Hauptprogramm-Ende, Reset und Speicher auf Zeile 1 zurücksetzen
  writeBlock("M30");
}
```

### 🖥️ Schritt-für-Schritt: So führen Sie Übung 00b aus und prüfen das Ergebnis

1. **Datei in Visual Studio Code öffnen:**  
   Klicken Sie in der linken Datei-Leiste auf den Ordner `uebungen/` und öffnen Sie [`uebung_00b_hallo_welt.cps`](file:///C:/Projekte/CNC/uebungen/uebung_00b_hallo_welt.cps).
2. **Text nach Wunsch anpassen:**  
   Ändern Sie z. B. `"HALLO WELT - MEIN ERSTER CNC POSTPROZESSOR"` in Ihren eigenen Namen oder Grußtext. Speichern Sie die Datei mit `Strg + S`.
3. **Im Terminal übersetzen (Simulation ausführen):**  
   Öffnen Sie das Terminal in Visual Studio Code (`Strg + Ö` oder Menü `Terminal` $\rightarrow$ `Neues Terminal`) und geben Sie folgenden Befehl ein:
   ```powershell
   node tests/simuliere_post.js uebungen/uebung_00b_hallo_welt.cps
   ```
4. **Ergebnis-Datei ansehen:**  
   Der Postprozessor erzeugt blitzschnell die Maschinendatei [`uebungen/uebung_00b_hallo_welt.nc`](file:///C:/Projekte/CNC/uebungen/uebung_00b_hallo_welt.nc).  
   Dort sehen Sie ganz oben Ihre eigenen Zeilen:
   ```gcode
   (========================================)
   (HALLO WELT - MEIN ERSTER CNC POSTPROZESSOR)
   (ERFOLGREICH ERSTE ZEILE EINGEFUEGT)
   (========================================)
   G90 G17 G21 G94
   G28 G91 Z0.
   G90
   ```
5. **Im interaktiven 3D-Simulator ansehen:**  
   Öffnen Sie [`kundenauftrag_01_flanschplatte/3d_auftrag_simulator.html`](file:///C:/Projekte/CNC/kundenauftrag_01_flanschplatte/3d_auftrag_simulator.html) im Browser.  
   Wählen Sie oben im Menü *(Selectbox)* einfach **„Übung 00b: Hallo Welt Postprozessor“** aus.  
   Sie sehen sofort die exakten G-Code-Zeilen, können mit `⏮ Vorheriger` und `⏭ Nächster Schritt` jede Zeile einzeln durchschalten und mit `🎥 3D-Ansicht Reset` jederzeit zur Startansicht zurückspringen!

### 🛡️ Prüfliste dieser Übung: Wann ist Übung 00b zu 100 % bestanden?

| Prüfpunkt | Was muss im Code / Simulator zu sehen sein? | Bestanden? |
| :--- | :--- | :---: |
| **1. Terminal-Erfolg** | Der Befehl `node tests/simuliere_post.js ...` läuft fehlerfrei durch und meldet `SIMULATION ERFOLGREICH`. | [ ] |
| **2. Kommentar im Code** | In [`uebungen/uebung_00b_hallo_welt.nc`](file:///C:/Projekte/CNC/uebungen/uebung_00b_hallo_welt.nc) steht in runden Klammern `(HALLO WELT...)`. | [ ] |
| **3. Grundinitialisierung** | Die Sicherheitszeile `G90 G17 G21 G94` sowie der Z-Rückzug `G28 G91 Z0.` stehen direkt unter dem Kommentar. | [ ] |
| **4. 3D-Simulator-Check** | Im Browser steht das Werkzeug sicher über dem Bauteil-Nullpunkt `G54` auf Höhe `Z +15.0`. | [ ] |

---

---

# Übung 1: Der erste eigene Text im G-Code (Entwickler-Infoblock in `onOpen()`)

### 📌 Spickzettel dieser Übung: Alle verwendeten G-Code- & M-Code-Kennzeichen in Übung 1

| Kennzeichen | Fachbegriff & Erklärung | Bedeutung & Funktion in dieser Übung |
|---|---|---|
| **`(...)`** | **Kommentar *(Bediener-Information)*** | Schreibt Ihren Entwicklernamen, Betrieb und Datum in runden Klammern, ignoriert von der Maschinensteuerung. |
| **`%`** | **Übertragungs-Start/Ende *(Paper Tape Rewind)*** | Leitet auf Fanuc- und Haas-Maschinen die Dateiübertragung über Netzwerk/RS232 ein. |
| **`O1001`** | **Hauptprogramm-Nummer *(Program Number)*** | Die vierstellige Programmnummer im Speicher der Fräsmaschine. |
| **`G90`** | **Absolutmaß *(Absolute Mode)*** | Alle Maße beziehen sich auf den Werkstück-Nullpunkt `G54`. |
| **`G21`** | **Metrisches Einheitensystem *(Metric Mode)*** | Schaltet die Maschine fest auf Millimeter ein. |
| **`G17`** | **XY-Bearbeitungsebene *(Plane Selection)*** | Standard-Fräsebene von oben *(Werkzeugachse ist die Z-Achse)*. |
| **`G40`** | **Radiuskorrektur AUS *(Cutter Comp Cancel)*** | Schaltet eventuell noch aktive Korrekturwerte aus vorigen Programmen ab. |
| **`G80`** | **Bohrzyklen ABBRECHEN *(Cancel Canned Cycles)*** | Bricht alle aktiven Bohrzyklen zur Sicherheit ab. |
| **`G53 G00 Z0.0`** | **Sicherheits-Rückzug Z *(Safe Z Retract)*** | Fährt die Z-Achse senkrecht nach ganz oben an die Decke der Fräskabine. |
| **`M30`** | **Programmende *(Program End and Rewind)*** | Beendet die Bearbeitung und setzt den Speicher auf Zeile 1 zurück. |

### 💡 Worum geht es in einfacher Sprache?

Wenn eine **CNC-Maschine (computergesteuerte Fräsmaschine)** ein Programm liest, ignoriert sie alles, was in **runden Klammern `(...)`** steht. Das sind **Kommentare (Notizen nur für den Menschen an der Maschine)**.
In dieser ersten Übung bringen wir unserem **JavaScript-Übersetzer ([`src/mein_erster_post.cps`](file:///C:/Projekte/CNC/src/mein_erster_post.cps))** bei, ganz am Anfang jedes Programms automatisch eine Visitenkarte mit Ihrem Namen, dem Firmennamen und dem aktuellen Datum in den **G-Code (Maschinencode)** zu schreiben.

### 🛠️ Wo im Code wird das gemacht?

Für diese Übung stehen Ihnen **zwei Quellcode-Dateien** zur Verfügung:
1. **Als eigene, kompakte Übungs-Datei (Empfohlen für den Start):**  
   [`uebungen/uebung_01_entwickler_header.cps`](file:///C:/Projekte/CNC/uebungen/uebung_01_entwickler_header.cps) – Hier sehen Sie ausschließlich den Code von Übung 1 ohne störenden Ballast.
2. **Im großen Gesamt-Postprozessor des Projekts:**  
   [`src/mein_erster_post.cps`](file:///C:/Projekte/CNC/src/mein_erster_post.cps#L194-L221) – Hier ist diese Funktion in die gesamte Fräsmaschinen-Übersetzung integriert.

In beiden Dateien geschieht die Magie in der Funktion **`onOpen()`** *(diese Funktion wird immer **automatisch als allererstes** gestartet, sobald der Postprozessor aufgerufen wird)*.

### 🖥️ Schritt-für-Schritt: So öffnen, bearbeiten, starten und simulieren Sie Übung 1 in Visual Studio Code (VSC)

Hier ist die genaue Anleitung, wie Sie in **Visual Studio Code (VSC)** arbeiten:

#### Schritt 1: Datei in Visual Studio Code öffnen
1. Drücken Sie in VS Code auf Ihrer Tastatur die Tastenkombination `Strg + P` *(Schnellöffnung)*.
2. Tippen Sie ein: `uebung_01_entwickler_header.cps` und drücken Sie `Enter` *(Eingabetaste)*.
3. Die Datei öffnet sich im Editor. Ändern Sie z. B. in Zeile 16 Ihren Wunschnamen oder Text.
4. Speichern Sie die Datei mit `Strg + S`.

#### Schritt 2: Programm im Terminal ausführen & testen
1. Öffnen Sie das Terminal *(Befehlszeilenfenster)* in VS Code mit der Tastenkombination ``Strg + ` `` *(Gravis-Taste oben links neben der 1)* oder klicken Sie im oberen Menü auf **Terminal -> New Terminal (Neues Terminal)**.
2. Tippen Sie folgenden Befehl ein und drücken Sie `Enter`:
   ```powershell
   node tests/simuliere_post.js uebungen/uebung_01_entwickler_header.cps
   ```
3. Der Simulator startet sofort! Im Terminal sehen Sie direkt das Testergebnis mit grünem Haken.

#### Schritt 3: Den erzeugten G-Code ansehen
Der Simulator schreibt den fertigen CNC-Maschinencode in die Datei [`tests/mein_generierter_gcode.nc`](file:///C:/Projekte/CNC/tests/mein_generierter_gcode.nc).
* Öffnen Sie die Datei mit `Strg + P` und der Eingabe: `mein_generierter_gcode.nc`.
* Dort sehen Sie Ihren Entwickler-Header ganz oben in den Zeilen 1 bis 10!

#### Schritt 4: 3D-Simulation visuell im Webbrowser prüfen
1. Öffnen Sie die Datei [`tests/mein_generierter_gcode.nc`](file:///C:/Projekte/CNC/tests/mein_generierter_gcode.nc).
2. Drücken Sie `Strg + A` *(alles markieren)* und `Strg + C` *(kopieren)*.
3. Öffnen Sie in Ihrem Browser die Webseite **[https://ncviewer.com](https://ncviewer.com)**.
4. Markieren Sie den Text im linken Textfeld von NCViewer, drücken Sie `Strg + V` *(einfügen)* und klicken Sie auf **Plot** bzw. **Play**.
5. Sie sehen nun die visualisierten Fahrbewegungen und können mit der Computermaus das Bauteil in 3D *(dreidimensional)* drehen!

---

### 📝 Schritt-für-Schritt-Erklärung des Codes:

```javascript
// 1. Wir holen uns das aktuelle Datum und die Uhrzeit vom Computer:
var now = new Date();
var dateString = now.getFullYear() + "-" +
                 ("0" + (now.getMonth() + 1)).slice(-2) + "-" +
                 ("0" + now.getDate()).slice(-2) + " " +
                 ("0" + now.getHours()).slice(-2) + ":" +
                 ("0" + now.getMinutes()).slice(-2);

// 2. Mit writeComment(...) schreiben wir Text in runden Klammern in den G-Code:
writeComment("==================================================");
writeComment("AUTOMATISCH GENERIERTER CNC G-CODE (MASCHINENCODE)");
writeComment("ENTWICKLER : " + getProperty("developerName"));
writeComment("BETRIEB    : " + getProperty("companyName"));
writeComment("DATUM/ZEIT : " + dateString);
writeComment("EINHEITEN  : " + (unit == MM ? "MILLIMETER (METRISCH G21)" : "INCH / ZOLL (G20)"));
writeComment("==================================================");

// 3. Sicherheits-Startblock (Safe Start Block):
// G90 = Absolute Maßangaben (alle Koordinaten beziehen sich auf den Werkstück-Nullpunkt G54)
// G21 = Metrisches Einheitensystem in Millimeter (mm)
// G17 = Arbeitsebene XY (Standard für Fräsen von oben)
// G40 = Werkzeugradiuskorrektur ABWÄHLEN (keine alten Bahnverschiebungen aktiv)
// G80 = Alle aktiven Bohrzyklen ABBRECHEN und löschen
writeWords("G90", "G21", "G17", "G40", "G80");

// 4. Sicherer Programmabschluss in onClose():
// G53 = Maschinen-Koordinatensystem
// G00 = Eilgang (Schnellgang ohne Materialkontakt)
// Z0.0 = Spindel senkrecht nach ganz oben fahren (Kollisionsschutz)
writeWords("G53", "G00", "Z0.0");

// M30 = Hauptprogramm-Ende, Reset und Rücklauf zum Programmanfang
writeWords("M30");
```

* **Was macht `getProperty("developerName")`?**  
  Es liest Ihren Namen aus dem Einstellungs-Bereich [`properties`](file:///C:/Projekte/CNC/src/mein_erster_post.cps#L38-L54) oben in der Datei aus.
* **Was macht `writeComment(...)`?**  
  Es wandelt Ihren Text in Großbuchstaben um, entfernt verbotene Sonderzeichen und setzt runde Klammern `(...)` darum, damit die **CNC-Steuerung (der Computer der Fräsmaschine)** keinen Fehler meldet.

### ✅ So sieht das Ergebnis im fertigen G-Code ([`tests/output_expected.nc`](file:///C:/Projekte/CNC/tests/output_expected.nc#L1-L9)) aus:

```gcode
%
O1001 (CNC FERTIGUNGSPROGRAMM - MUSTERBAUTEIL)
(==================================================)
(AUTOMATISCH GENERIERTER CNC G-CODE - MASCHINENCODE)
(ENTWICKLER : JAVASCRIPT CNC-ENTWICKLER)
(BETRIEB    : PRAEZISIONS-ZERSPANUNG GMBH)
(DATUM/ZEIT : 2026-10-16 14:15)
(EINHEITEN  : MILLIMETER - METRISCH G21)
(==================================================)
G90 G21 G17 G40 G80 (SICHERHEITSZEILE: G90 ABSOLUT | G21 METRISCH MM | G17 XY-EBENE | G40 RADIUSKORREKTUR AUS | G80 BOHRZYKLEN AUS)
G53 G00 Z0.0 (G53 MASCHINEN-KOORDINATENSYSTEM | G00 EILGANG | Z0 SPINDEL GANZ NACH OBEN FAHREN)
M30 (M30 HAUPTPROGRAMMENDE, RESET UND RUECKSPRUNG AUF ZEILE 1)
%
```

### 🛡️ Prüfliste dieser Übung: Wann ist Übung 1 zu 100 % bestanden?

| Prüfpunkt | Was muss im Code / Simulator zu sehen sein? | Bestanden? |
| :--- | :--- | :---: |
| **1. Entwickler-Name** | In Zeile 4 steht Ihr eigener Name oder `JAVASCRIPT CNC-ENTWICKLER` in runden Klammern. | [ ] |
| **2. Firma & Datum** | Firmenname und aktuelles Systemdatum mit Uhrzeit werden automatisch formatiert ausgegeben. | [ ] |
| **3. Keine Umlaute / Sonderzeichen** | Der Text ist in Großbuchstaben formatiert und enthält keine Sonderzeichen wie `ä, ö, ü, ß`, die eine alte Steuerung zum Absturz bringen würden. | [ ] |
| **4. Konsistenzprüfung** | In [`tests/mein_generierter_gcode.nc`](file:///C:/Projekte/CNC/tests/mein_generierter_gcode.nc) erscheint der Header fehlerfrei und ohne Warnmeldungen. | [ ] |

---

# Übung 2: Automatische Werkzeugliste (`Tool Table`) ganz oben im Programm ausgeben

### 📌 Spickzettel dieser Übung: Alle verwendeten G-Code- & M-Code-Kennzeichen in Übung 2

| Kennzeichen | Fachbegriff & Erklärung | Bedeutung & Funktion in dieser Übung |
|---|---|---|
| **`T01`, `T02`** | **Werkzeugnummer *(Tool Number)*** | Platznummer des Werkzeugs im Magazinkarussell der Fräsmaschine. |
| **`D=...MM`** | **Werkzeug-Durchmesser *(Diameter)*** | Dicke $\varnothing$ des Fräsers oder Bohrers *(z. B. `10.000MM`)* für die Bahnbreite. |
| **`ECKE R=...`** | **Eckenradius *(Corner Radius)*** | `R=0.000` = scharfkantiger Fräser, `R=1.000` = Torusfräser, `R=5.000` = Kugelfräser. |
| **`writeComment`** | **Kommentar-Ausgabe *(Comment Output)*** | Schreibt jede Zeile der Werkzeugliste formatiert in runden Klammern `(...)` an den Programmanfang. |

### 💡 Worum geht es in einfacher Sprache?

Stellen Sie sich vor, Sie wollen im Haushalt ein Möbelstück aufbauen. Bevor Sie anfangen, schauen Sie auf Seite 1 der Anleitung nach, welches Werkzeug Sie brauchen (z. B. einen Kreuzschlitz-Schraubendreher und einen 8er-Bohrer).
Genauso ist es an der **CNC-Maschine (Werkzeugmaschine)**: Der **Maschinenbediener (Mitarbeiter an der Fräse)** möchte ganz oben in der Datei sofort sehen, welche Fräser und Bohrer er in die Maschine einbauen muss, ohne erst 5.000 Zeilen Programmcode durchzulesen.

### 🛠️ Wo im Code wird das gemacht?

Für diese Übung stehen Ihnen **zwei Quellcode-Dateien** zur Verfügung:
1. **Als eigene, kompakte Übungs-Datei:**  
   [`uebungen/uebung_02_werkzeugliste.cps`](file:///C:/Projekte/CNC/uebungen/uebung_02_werkzeugliste.cps) – Enthält übersichtlich nur den Code zur Werkzeuglisten-Generierung.
2. **Im großen Gesamt-Postprozessor des Projekts:**  
   [`src/mein_erster_post.cps`](file:///C:/Projekte/CNC/src/mein_erster_post.cps#L223-L248) – Hier ist die Funktion in die Gesamt-Ausgabe integriert.

### 🖥️ Schritt-für-Schritt: So öffnen, bearbeiten, starten und simulieren Sie Übung 2 in Visual Studio Code (VSC)

#### Schritt 1: Datei in Visual Studio Code öffnen
1. Drücken Sie in VS Code `Strg + P` *(Schnellöffnung)*.
2. Tippen Sie ein: `uebung_02_werkzeugliste.cps` und drücken Sie `Enter`.

#### Schritt 2: Programm im Terminal ausführen & testen
1. Öffnen Sie das Terminal mit ``Strg + ` `` *(oder Menü: Terminal -> Neues Terminal)*.
2. Führen Sie folgenden Befehl aus:
   ```powershell
   node tests/simuliere_post.js uebungen/uebung_02_werkzeugliste.cps
   ```
3. Der Simulator liest die CAM-Werkzeuge ein und zeigt Ihnen das Testergebnis grün an.

#### Schritt 3: Den erzeugten G-Code ansehen
* Öffnen Sie mit `Strg + P` die Datei [`tests/mein_generierter_gcode.nc`](file:///C:/Projekte/CNC/tests/mein_generierter_gcode.nc).
* Dort sehen Sie die Werkzeugliste am Programmanfang (`T01 Schaftfräser`, `T02 Spiralbohrer`).

#### Schritt 4: 3D-Simulation visuell prüfen
* Kopieren Sie den Inhalt von `mein_generierter_gcode.nc` (`Strg + A`, `Strg + C`).
* Öffnen Sie [https://ncviewer.com](https://ncviewer.com), fügen Sie den Code ein (`Strg + V`) und klicken Sie auf **Plot** bzw. **Play**.

---

### 🛠️ Wie funktioniert das im JavaScript-Code ([`src/mein_erster_post.cps`](file:///C:/Projekte/CNC/src/mein_erster_post.cps#L223-L248))?

Die **Autodesk Post-API (Programmierschnittstelle von Autodesk)** schenkt uns den fertigen Befehl `getToolTable()` (Hole die Liste aller benutzten Werkzeuge). Wir müssen diese Liste nur noch mit einer einfachen `for`-Schleife (Wiederholungsschleife in JavaScript) durchlaufen:

```javascript
if (getProperty("writeToolList")) {
  writeComment("--- BENOETIGTE WERKZEUGE (TOOL TABLE) ---");
  var tools = getToolTable(); // Holt alle Werkzeuge aus dem 3D-CAM-Projekt
  if (tools.getNumberOfTools() > 0) {
    for (var i = 0; i < tools.getNumberOfTools(); ++i) {
      var tool = tools.getTool(i); // Nimmt das aktuelle Werkzeug aus der Liste
      var toolInfo = "T" + ("0" + tool.number).slice(-2) +
                     " | D=" + xyzFormat.format(tool.diameter) + (unit == MM ? "MM" : "IN") +
                     " | ECKE R=" + xyzFormat.format(tool.cornerRadius);
      if (tool.description) {
        toolInfo += " | " + tool.description;
      }
      writeComment(toolInfo);
    }
  }
  writeComment("-----------------------------------------");
}

// Sicherheits-Startblock (Safe Start Block):
// G90 = Absolutmaß (alle Koordinaten beziehen sich fest auf den Werkstück-Nullpunkt G54)
// G21 = Metrisches Einheitensystem (Maßeinheit Millimeter mm)
// G17 = Fräsbearbeitung in der XY-Hauptebene (Z-Achse ist die Spindelachse)
// G40 = Fräserradiuskorrektur ABWÄHLEN (schaltet alte Fräsermittenbahn-Verschiebungen sicher aus)
// G80 = Alle aktiven Bohrzyklen ABBRECHEN und löschen
writeWords("G90", "G21", "G17", "G40", "G80");

// Programmende in onClose():
// G53 = Maschinen-Koordinatensystem
// G00 = Eilgang (Schnellstmöglicher Verfahrweg ohne Spanabtrag)
// Z0.0 = Spindel senkrecht nach ganz oben fahren
writeWords("G53", "G00", "Z0.0");

// M30 = Hauptprogramm-Ende, Reset und Rücklauf zum Programmanfang
writeWords("M30");
```

* **`tool.number`**: Die Platznummer des Werkzeugs im Karussell der Maschine (z. B. `1` wird zu `T01`).
* **`tool.diameter`**: Die Dicke (der Durchmesser $\varnothing$) des Fräsers oder Bohrers (z. B. `10.000MM`).
* **`tool.cornerRadius`**: Der Radius an der unteren Schneidenecke (`0.000` bedeutet: scharfe 90-Grad-Ecke).

### ✅ So sieht das Ergebnis im fertigen G-Code aus:

```gcode
(--- BENOETIGTE WERKZEUGE - TOOL TABLE ---)
(T01 | D=10.000MM | ECKE R=0.000 | SCHAFTFRAESER 10MM VHM)
(T02 | D=6.000MM  | ECKE R=0.000 | SPIRALBOHRER 6MM VHM)
(-----------------------------------------)
G90 G21 G17 G40 G80 (SICHERHEITSZEILE: G90 ABSOLUT | G21 METRISCH MM | G17 XY-EBENE | G40 RADIUSKORREKTUR AUS | G80 BOHRZYKLEN AUS)
G53 G00 Z0.0 (G53 MASCHINEN-KOORDINATENSYSTEM | G00 EILGANG | Z0 SPINDEL GANZ NACH OBEN FAHREN)
M30 (M30 HAUPTPROGRAMMENDE, RESET UND RUECKSPRUNG AUF ZEILE 1)
%
```

### 🛡️ Prüfliste dieser Übung: Wann ist Übung 2 zu 100 % bestanden?

| Prüfpunkt | Was muss im Code / Simulator zu sehen sein? | Bestanden? |
| :--- | :--- | :---: |
| **1. Werkzeugtabelle aktiv** | Schalter `writeToolList: true` gibt den Block `(--- BENOETIGTE WERKZEUGE ---)` aus. | [ ] |
| **2. Werkzeugnummern formatiert** | Werkzeuge werden sauber 2-stellig als `T01` und `T02` formatiert. | [ ] |
| **3. Durchmesser & Eckenradius** | Fräser-Durchmesser `D=10.000MM` und Eckradius `ECKE R=0.000` werden exakt ausgewiesen. | [ ] |
| **4. Konsistenzprüfung** | In [`tests/mein_generierter_gcode.nc`](file:///C:/Projekte/CNC/tests/mein_generierter_gcode.nc) erscheint die Werkzeugliste direkt unter dem Programmkopf. | [ ] |

---

# Übung 3: Sicherheits-Schutz gegen Maschinencrash – Tiefste Frästiefe (`Z-MIN`) berechnen

### 📌 Spickzettel dieser Übung: Alle verwendeten G-Code- & M-Code-Kennzeichen in Übung 3

| Kennzeichen | Fachbegriff & Erklärung | Bedeutung & Funktion in dieser Übung |
|---|---|---|
| **`Z0.000`** | **Bauteil-Oberkante *(Top of Part)*** | Höhen-Nullpunkt des Werkstücks. |
| **`Z+...`** | **Sicherheitshöhe in der Luft *(Clearance Height)*** | Positive Z-Werte *(z. B. `Z15.000`)* über dem Bauteil, in denen der Fräser kollisionsfrei verfährt. |
| **`Z-...`** | **Frästiefe im Material *(Depth of Cut)*** | Negative Z-Werte *(z. B. `Z-5.000` Kontur, `Z-12.000` Bohrung)* tief im Metall. |
| **`Z-MIN`** | **Tiefster Z-Punkt *(Minimum Z Depth)*** | Der absolut tiefste Punkt, den ein Werkzeug erreicht. Schützt den Schraubstock vor Kollisionen. |

### 💡 Worum geht es in einfacher Sprache?

Das ist einer der **beliebtesten bezahlten Kundenaufträge** für Einsteiger!
Das Werkstück (der Metallblock) wird in der Maschine unten von einem massiven **Schraubstock aus Stahl (Spannmittel)** festgehalten. 

* Die Oberfläche des Bauteils hat die Höhe **`Z = 0.000 mm`**.
* Alles, was **über** dem Bauteil in der Luft ist, hat **Plus-Werte** (z. B. `Z15.000` = 15 mm in der Luft über dem Bauteil).
* Alles, was **in das Metall hinein** fräst oder bohrt, hat **Minus-Werte** (z. B. `Z-5.000` = 5 mm tief im Metall; `Z-12.000` = 12 mm tief im Metall).

**Die Gefahr:** Wenn das Metallstück nur `10 mm` weit aus dem Schraubstock herausschaut, aber der Bohrer bis auf `Z-12.000 mm` nach unten fährt, bohrt er `2 mm` tief mitten in den teuren Stahl-Schraubstock hinein (**Kollision / Maschinencrash**)!
Deshalb lassen wir unser JavaScript-Programm automatisch ausrechnen, wie tief jedes Werkzeug maximal nach unten fährt (**`Z-MIN` – kleinster Z-Wert**).

### 🛠️ Wo im Code wird das gemacht?

Für diese Übung stehen Ihnen **zwei Quellcode-Dateien** zur Verfügung:
1. **Als eigene, kompakte Übungs-Datei:**  
   [`uebungen/uebung_03_z_min_berechnung.cps`](file:///C:/Projekte/CNC/uebungen/uebung_03_z_min_berechnung.cps) – Berechnet die Z-MIN-Werte und gibt bei Crash-Gefahr eine Sicherheitswarnung aus.
2. **Im großen Gesamt-Postprozessor des Projekts:**  
   [`src/mein_erster_post.cps`](file:///C:/Projekte/CNC/src/mein_erster_post.cps#L181-L195) – Integriert in den Workflow.

### 🖥️ Schritt-für-Schritt: So öffnen, bearbeiten, starten und simulieren Sie Übung 3 in Visual Studio Code (VSC)

#### Schritt 1: Datei in Visual Studio Code öffnen
1. Drücken Sie `Strg + P` in VS Code.
2. Tippen Sie ein: `uebung_03_z_min_berechnung.cps` und drücken Sie `Enter`.

#### Schritt 2: Programm im Terminal ausführen & testen
1. Öffnen Sie das Terminal mit ``Strg + ` ``.
2. Führen Sie aus:
   ```powershell
   node tests/simuliere_post.js uebungen/uebung_03_z_min_berechnung.cps
   ```
3. Der Simulator prüft die Z-Tiefen aller CAM-Schritte und zeigt die Z-MIN-Werte im Terminal.

#### Schritt 3: Den erzeugten G-Code ansehen
* Öffnen Sie [`tests/mein_generierter_gcode.nc`](file:///C:/Projekte/CNC/tests/mein_generierter_gcode.nc) mit `Strg + P`.
* Achten Sie auf die Zeilen `(SICHERHEITS-INFO: OP Z-MIN=-12.000MM)`.

#### Schritt 4: 3D-Simulation visuell prüfen
* Kopieren Sie den G-Code in [https://ncviewer.com](https://ncviewer.com).
* Drehen Sie das Werkstück auf die Seitenansicht *(X/Z oder Y/Z)*: Sie sehen exakt, wie tief der Fräser und Bohrer in das Bauteil eintauchen!

---

### 🛠️ Wie haben wir das in [`src/mein_erster_post.cps`](file:///C:/Projekte/CNC/src/mein_erster_post.cps#L181-L195) programmiert?

```javascript
function getToolMinimumZ(tool) {
  var zMin = undefined;
  var numberOfSections = getNumberOfSections(); // Wie viele Arbeitsschritte gibt es insgesamt?
  for (var i = 0; i < numberOfSections; ++i) {
    var section = getSection(i); // Schau dir Arbeitsschritt Nummer i an
    if (section.getTool().number == tool.number) {
      // Wenn in diesem Arbeitsschritt unser Werkzeug benutzt wird:
      var zRange = section.getGlobalZRange(); // Hole den Höhenbereich (von Z-Min bis Z-Max)
      var currentMin = zRange.getMinimum();   // Lies den tiefsten Punkt (Z-Min) aus
      if (zMin === undefined || currentMin < zMin) {
        zMin = currentMin; // Merke dir den bisher tiefsten Wert!
      }
    }
  }
  return zMin;
}
```

Zusätzlich geben wir in [`onSection()`](file:///C:/Projekte/CNC/src/mein_erster_post.cps#L281-L288) vor jedem einzelnen Arbeitsschritt die Tiefe dieser Operation aus:

```javascript
if (getProperty("showZMinInfo")) {
  var sectionZRange = currentSection.getGlobalZRange();
  writeComment(
    "SICHERHEITS-INFO: OP Z-MIN=" + xyzFormat.format(sectionZRange.getMinimum()) + "MM" +
    " | OP Z-MAX=" + xyzFormat.format(sectionZRange.getMaximum()) + "MM"
  );
}
```

### ✅ So sieht das Ergebnis im fertigen G-Code ([`tests/output_expected.nc`](file:///C:/Projekte/CNC/tests/output_expected.nc#L10-L20)) aus:

```gcode
(--- BENOETIGTE WERKZEUGE - TOOL TABLE ---)
(T01 | D=10.000MM | ECKE R=0.000 | Z-MIN=-5.000MM | SCHAFTFRAESER 10MM VHM)
(T02 | D=6.000MM  | ECKE R=0.000 | Z-MIN=-12.000MM | SPIRALBOHRER 6MM VHM)
(-----------------------------------------)
N10 G90 G17 G40 G49 G80 G21 (SICHERHEITSZEILE: G90 ABSOLUT | G17 XY-EBENE | G40 RADIUSKORREKTUR AUS | G49 LAENGENKORREKTUR AUS | G80 BOHRZYKLEN AUS | G21 METRISCH MM)

(OPERATION: 1. AUSSENKONTUR FRAESEN - 2D KONTUR)
(SICHERHEITS-INFO: OP Z-MIN=-5.000MM | OP Z-MAX=15.000MM)
N20 T01 M06 (T01 WERKZEUGPLATZ 1 | M06 AUTOMATISCHER WERKZEUGWECHSEL DURCH GREIFER)
N30 G54 (G54 ERSTES WERKSTUECK-KOORDINATENSYSTEM / NULLPUNKT AUF BAUTEILECKE)
N40 S8000 M03 (S8000 SPINDELDREHZAHL 8000 U/MIN | M03 SPINDEL RECHTSLAUF EIN)
N50 G43 H01 Z15.000 M08 (G43 LAENGENKORREKTUR EIN | H01 REGISTER | Z15.0 SICHERHEITSHOEHE | M08 KUEHLMITTEL AN)
```

Der Arbeiter an der Maschine sieht sofort: **`T02` fährt bis `Z-12.000MM`** – ich muss den Aluminium-Block also mindestens `14 mm` weit oben aus dem Schraubstock herausschauen lassen!

### 🛡️ Prüfliste dieser Übung: Wann ist Übung 3 zu 100 % bestanden?

| Prüfpunkt | Was muss im Code / Simulator zu sehen sein? | Bestanden? |
| :--- | :--- | :---: |
| **1. Z-MIN-Berechnung** | Im Header steht für jedes Werkzeug der korrekte tiefste Z-Wert (z. B. `Z-MIN=-5.000MM` und `Z-MIN=-12.000MM`). | [ ] |
| **2. Operations-Z-Info** | Vor jeder einzelnen Fräsoperation wird `(SICHERHEITS-INFO: OP Z-MIN=... | OP Z-MAX=...)` ausgegeben. | [ ] |
| **3. Kollisionsschutz** | Der Fräser fährt niemals tiefer als das Bauteil plus Mindest-Spannbackenabstand. | [ ] |
| **4. Konsistenz im Simulator** | In [`tests/mein_generierter_gcode.nc`](file:///C:/Projekte/CNC/tests/mein_generierter_gcode.nc) stimmen die berechneten Werte mit der 3D-Geometrie überein. | [ ] |

---

# Übung 4: Ein 3D-Modell als Kundenauftrag bearbeiten (Vom 3D-Bauteil zum G-Code)

### 📌 Spickzettel dieser Übung: Alle verwendeten G-Code- & M-Code-Kennzeichen in Übung 4

| Kennzeichen | Fachbegriff & Erklärung | Bedeutung & Funktion in dieser Übung |
|---|---|---|
| **`T01`, `T02`** | **Werkzeugnummer *(Tool Number)*** | `T01` = Schaftfräser $\varnothing 10\,\text{mm}$ \| `T02` = Spiralbohrer $\varnothing 6\,\text{mm}$. |
| **`M06`** | **Werkzeugwechsel *(Tool Change)*** | Befiehlt der Fräsmaschine, das Werkzeug mechanisch in die Spindel einzuwechseln. |
| **`S8000`, `S3500`** | **Spindeldrehzahl *(Spindle Speed)*** | Drehzahl in $\text{U/min}$ *(Umdrehungen pro Minute)* passend zum Werkzeugdurchmesser und Aluminium. |
| **`M03`** | **Spindel Rechtslauf EIN *(Spindle Clockwise)*** | Startet die Frässpindel im Uhrzeigersinn. |
| **`G54`** | **Werkstück-Nullpunkt 1 *(Work Coordinate System)*** | Nullpunkt-Lage an der vorderen linken oberen Bauteilecke `(X0, Y0, Z0)`. |
| **`G00`** | **Eilgang *(Rapid Move)*** | Schnelle Positionierbewegung im Vollgas ohne Werkstoffkontakt. |
| **`G01`** | **Linearer Arbeitsvorschub *(Linear Feed)*** | Fräsbewegung im Metall mit definierter Vorschubgeschwindigkeit $F$. |
| **`G03`** | **Kreisbogen gegen Uhrzeigersinn *(Circular Interpolation CCW)*** | Fräst die runde Kreistasche $\varnothing 30\,\text{mm}$ mit Kreisradius-Parametern $I$ und $J$. |
| **`G83`** | **Tiefbohrzyklus mit Spanbruch *(Deep Hole Peck Drilling)*** | Bohrt stufenweise mit Zustelltiefe $Q$, zieht periodisch zum Spanbrechen ab. |
| **`Q3.0`** | **Zustelltiefe pro Spanbruch *(Peck Depth)*** | Bohrer taucht jeweils $3\,\text{mm}$ tiefer ein, bevor er kurz entlastet. |
| **`G43 H...`** | **Werkzeuglängenkorrektur EIN *(Tool Length Compensation)*** | Aktiviert die im Werkzeugspeicher hinterlegte Längenmessung der Werkzeugspitze. |
| **`M08`** | **Kühlmittel EIN *(Coolant On)*** | Schaltet die Kühlmittelpumpe für Sprüh- oder Flutkühlung an. |
| **`M09`** | **Kühlmittel AUS *(Coolant Off)*** | Schaltet das Kühlmittel am Operations- oder Programmende ab. |
| **`M05`** | **Spindel-Stopp *(Spindle Stop)*** | Hält die Spindeldrehung sicher an. |
| **`G53`** | **Maschinen-Koordinatensystem *(Machine Coordinate System)*** | Fährt bezogen auf den absoluten Maschinen-Nullpunkt *(z. B. Spindel ganz nach oben `Z0`)*. |
| **`M30`** | **Hauptprogramm-Ende *(Program End and Rewind)*** | Beendet das CNC-Programm und setzt den Programmzeiger auf Zeile 1 zurück. |

### 💡 Worum geht es in einfacher Sprache?

Viele Kunden wollen gar keinen eigenen **Postprozessor (`.cps`-Übersetzer)** kaufen, sondern schicken Ihnen direkt eine **3D-Datei Ihres Bauteils** (z. B. [kundenauftrag_01_flanschplatte/bauteil_1001.stl](file:///C:/Projekte/CNC/kundenauftrag_01_flanschplatte/bauteil_1001.stl) oder eine `.step`-Datei) und sagen:
*„Bitte mach mir für dieses 3D-Bauteil das fertige CNC-Programm (G-Code), damit ich es auf meiner Maschine fräsen kann!“*

In dieser Übung lernen Sie die **6 einfachen Schritte**, wie Sie aus einem **3D-Modell** ohne händisches Tippen von Koordinaten das fertige **G-Code-Programm** erzeugen.
*(Die komplette Vorlage liegt für Sie im Ordner [kundenauftrag_01_flanschplatte/KUNDEN_AUFTRAG_UND_KLICK_ANLEITUNG.md](file:///C:/Projekte/CNC/kundenauftrag_01_flanschplatte/KUNDEN_AUFTRAG_UND_KLICK_ANLEITUNG.md)).*

### 🛠️ Wo im Code wird das gemacht?

Für diese Übung stehen Ihnen die folgenden Dateien zur Verfügung:
1. **Als CAM-Postprozessor-Quelldatei:**  
   [`uebungen/uebung_04_3d_modell_cam.cps`](file:///C:/Projekte/CNC/uebungen/uebung_04_3d_modell_cam.cps)
2. **Als 3D-CAD-Bauteil:**  
   [`kundenauftrag_01_flanschplatte/bauteil_1001.stl`](file:///C:/Projekte/CNC/kundenauftrag_01_flanschplatte/bauteil_1001.stl)
3. **Im Haupt-Postprozessor:**  
   [`src/mein_erster_post.cps`](file:///C:/Projekte/CNC/src/mein_erster_post.cps)

### 🖥️ Schritt-für-Schritt: So öffnen, starten und simulieren Sie Übung 4 in Visual Studio Code (VSC)

#### Schritt 1: Datei in Visual Studio Code öffnen
1. Drücken Sie in VS Code `Strg + P`.
2. Tippen Sie ein: `uebung_04_3d_modell_cam.cps` und drücken Sie `Enter`.

#### Schritt 2: Programm im Terminal ausführen & testen
1. Öffnen Sie das Terminal mit ``Strg + ` ``.
2. Geben Sie ein:
   ```powershell
   node tests/simuliere_post.js uebungen/uebung_04_3d_modell_cam.cps
   ```
3. Der Simulator erzeugt den kompletten Maschinencode für die Flanschplatte.

#### Schritt 3: Den erzeugten G-Code ansehen
* Öffnen Sie mit `Strg + P` die Datei [`tests/mein_generierter_gcode.nc`](file:///C:/Projekte/CNC/tests/mein_generierter_gcode.nc).

#### Schritt 4: 3D-Simulation visuell prüfen
* Öffnen Sie per Doppelklick die Datei [`kundenauftrag_01_flanschplatte/3d_auftrag_simulator.html`](file:///C:/Projekte/CNC/kundenauftrag_01_flanschplatte/3d_auftrag_simulator.html) direkt im Webbrowser oder nutzen Sie [https://ncviewer.com](https://ncviewer.com).

---

### 📝 Die 6 Schritte am 3D-Modell einfach erklärt:

1. **Das 3D-Modell einladen:**
   Sie öffnen die 3D-Datei (`bauteil_1001.stl` – eine Aluminium-Platte mit den Maßen `80 mm` lang, `50 mm` breit, `12 mm` dick) in **Autodesk Fusion (3D-CAD/CAM-Programm)** und schalten oben links von **„Konstruktion“** auf **„Fertigen (CAM)“** um.
2. **Das Rohteil (`Stock`) und den Nullpunkt (`G54`) festlegen:**
   - **Rohteil:** In der echten Welt sägt der Kunde ein Stück Aluminium ab, das etwas größer ist als das fertige Teil (hier: `85 x 55 x 15 mm`). Das tragen Sie bei „Rohteil“ ein.
   - **Nullpunkt (`G54`):** Die CNC-Maschine muss wissen, wo auf dem Metallblock der Punkt `(X=0, Y=0, Z=0)` liegt. Wir klicken mit der Maus einfach auf die **vordere, linke, obere Ecke** unseres 3D-Modells.
3. **Arbeitsschritt 1 am 3D-Modell klicken – Außenkontur fräsen (`2D-Kontur`):**
   - Wir wählen Werkzeug **`T01` (10 mm Schaftfräser)** mit Drehzahl `8000 U/min` (`S8000`) und Geschwindigkeit `1200 mm/min` (`F1200`).
   - Wir klicken am 3D-Modell auf den äußeren Rand und geben als Tiefe `-5.0 mm` ein.
   - Das Programm berechnet automatisch die 4 geraden Bahnen (`G01`) rund um das Rechteck (`X0/Y0` $\rightarrow$ `X80/Y0` $\rightarrow$ `X80/Y50` $\rightarrow$ `X0/Y50` $\rightarrow$ `X0/Y0`).
4. **Arbeitsschritt 2 am 3D-Modell klicken – Runde Tasche in der Mitte fräsen (`Kreistasche`):**
   - In der Mitte der Platte (`X40, Y25`) soll eine runde Vertiefung mit Durchmesser `30 mm` (Radius `15 mm`) und Tiefe `-3.0 mm` gefräst werden.
   - Wir klicken am 3D-Modell einfach auf den Kreis in der Mitte.
   - Das Programm erzeugt daraus automatisch den Kreis-Befehl **`G03` (Kreisfahrt gegen den Uhrzeigersinn)**:  
     `N210 G17 G03 X55.000 Y25.000 I-15.000 J0.000 F1000`
5. **Arbeitsschritt 3 am 3D-Modell klicken – Die 4 Ecklöcher bohren (`Bohren G83`):**
   - Wir wechseln auf Werkzeug **`T02` (6 mm Spiralbohrer)** mit Drehzahl `3500 U/min` (`S3500`).
   - Wir klicken die 4 Löcher am 3D-Modell an: `(X10/Y10)`, `(X70/Y10)`, `(X70/Y40)`, `(X10/Y40)` mit einer Tiefe von `-12.0 mm` (einmal komplett durch die `12 mm` dicke Platte hindurch).
   - Als Bohrmethode wählen wir **Tiefbohren (`G83`)** mit `Q3.0` (das heißt: der Bohrer bohrt immer `3 mm` tief, zieht kurz hoch, damit die Alu-Späne aus dem Loch fliegen und der Bohrer nicht verstopft, und bohrt dann weiter bis `-12 mm`).
6. **Auf „Postprozess“ drücken (G-Code erzeugen):**
   - Sie wählen Ihren Postprozessor [`src/mein_erster_post.cps`](file:///C:/Projekte/CNC/src/mein_erster_post.cps) aus, klicken auf **Start**, und fertig ist die Datei [`tests/output_expected.nc`](file:///C:/Projekte/CNC/tests/output_expected.nc)!

### ✅ So sieht das komplette fertige CNC-Programm mit Erklärungen aller Zeilen aus:

```gcode
%
O1001 (KUNDENAUFTRAG FLANSCHPLATTE 80X50X12 MM)
(--- BENOETIGTE WERKZEUGE - TOOL TABLE ---)
(T01 | D=10.000MM | ECKE R=0.000 | Z-MIN=-5.000MM | SCHAFTFRAESER 10MM VHM)
(T02 | D=6.000MM  | ECKE R=0.000 | Z-MIN=-12.000MM | SPIRALBOHRER 6MM VHM)
(-----------------------------------------)
N10 G90 G17 G40 G49 G80 G21 (SICHERHEITSZEILE: G90 ABSOLUT | G17 XY-EBENE | G40 RADIUSKORREKTUR AUS | G49 LAENGENKORREKTUR AUS | G80 BOHRZYKLEN AUS | G21 METRISCH MM)

(OPERATION 1: AUSSENKONTUR FRAESEN 80X50X5 MM)
(SICHERHEITS-INFO: OP Z-MIN=-5.000MM | OP Z-MAX=15.000MM)
N20 T01 M06 (T01 SCHAFTFRAESER 10MM | M06 AUTOMATISCHER WERKZEUGWECHSEL)
N30 G54 (G54 ERSTES WERKSTUECK-KOORDINATENSYSTEM / NULLPUNKT AUF BAUTEILECKE)
N40 S8000 M03 (S8000 DREHZAHL 8000 U/MIN | M03 SPINDEL RECHTSLAUF EIN)
N50 G43 H01 Z15.000 M08 (G43 LAENGENKORREKTUR | H01 REGISTER 1 | Z15 SICHERHEITSHOEHE | M08 KUEHLMITTEL AN)
N60 G00 X-10.000 Y-10.000 (G00 EILGANG VOR DAS WERKSTUECK IN DIE LUFT)
N70 G00 Z2.000 (G00 EILGANG BIS 2MM UEBER DIE BAUTEIL-OBERFLAECHE)
N80 G01 Z-5.000 F500 (G01 EINTAUCHEN AUF FRAESTIEFE -5MM MIT VORSCHUB 500 MM/MIN)
N90 G01 X0.000 Y0.000 F1200 (G01 ANFAHREN AN NULLPUNKT MIT FRAESVORSCHUB 1200 MM/MIN)
N100 G01 X80.000 Y0.000 F1200 (G01 UNTERE KANTE ENTLANGFRAESEN BIS X80)
N110 G01 X80.000 Y50.000 F1200 (G01 RECHTE KANTE FRAESEN BIS Y50)
N120 G01 X0.000 Y50.000 F1200 (G01 OBERE KANTE FRAESEN BIS X0)
N130 G01 X0.000 Y0.000 F1200 (G01 LINKE KANTE FRAESEN ZURUECK ZU Y0)
N140 G00 Z15.000 (G00 EILGANG SENKRECHT NACH OBEN AUF FREIFAHRHOEHE 15MM)

(OPERATION 2: KREISTASCHE MITTE D30 TIEFE 3MM)
(SICHERHEITS-INFO: OP Z-MIN=-3.000MM | OP Z-MAX=15.000MM)
N150 G00 X40.000 Y25.000 (G00 EILGANG ZUR TASCHENMITTE BEI X40 Y25)
N160 G00 Z2.000 (G00 EILGANG AUF VORPOSITION Z2)
N170 G01 Z-3.000 F400 (G01 EINTAUCHEN AUF TASCHENTIEFE -3MM MIT VORSCHUB 400 MM/MIN)
N180 G01 X55.000 Y25.000 F800 (G01 LINEAR AN DEN KREISRAND X55 ANFAHREN - RADIUS 15MM)
N190 G17 G03 X55.000 Y25.000 I-15.000 J0.000 F1000 (G03 KREISBAHN GEGEN DEN UHRZEIGERSINN MIT MITTELPUNKTVERSATZ I-15)
N200 G01 X40.000 Y25.000 F1200 (G01 ZURUECK IN DIE TASCHENMITTE FAHREN)
N210 G00 Z15.000 M09 (G00 EILGANG AUF SICHERHEITSHOEHE 15MM | M09 KUEHLMITTEL AUS)

(OPERATION 3: 4 ECKLOECHER D6 TIEFE 12MM BOHREN)
(SICHERHEITS-INFO: OP Z-MIN=-12.000MM | OP Z-MAX=15.000MM)
N220 T02 M06 (T02 SPIRALBOHRER 6MM | M06 AUTOMATISCHER WERKZEUGWECHSEL)
N230 G54 (G54 NULLPUNKT AUF BAUTEILECKE BEIBEHALTEN)
N240 S3500 M03 (S3500 DREHZAHL 3500 U/MIN FUER D6 BOHRER | M03 SPINDEL RECHTSLAUF)
N250 G43 H02 Z15.000 M08 (G43 LAENGENKORREKTUR REGISTER 2 | Z15 SICHERHEITSHOEHE | M08 KUEHLWASSER AN)
N260 G00 X10.000 Y10.000 (G00 EILGANG ZUR ERSTEN BOHRUNG UNTEN LINKS)
N270 G00 Z2.000 (G00 EILGANG AUF RUECKZUGSEBENE Z2)
N280 G98 G83 X10.000 Y10.000 Z-12.000 R2.000 Q3.000 F300 (G98 RUECKZUG Z15 | G83 TIEFBOHRZYKLUS | ENDTIEFE Z-12 | SPANBRUCH Q3 | VORSCHUB F300)
N290 X70.000 Y10.000 (BOHRUNG 2: UNTEN RECHTS MIT GLEICHEM ZYKLUS)
N300 X70.000 Y40.000 (BOHRUNG 3: OBEN RECHTS MIT GLEICHEM ZYKLUS)
N310 X10.000 Y40.000 (BOHRUNG 4: OBEN LINKS MIT GLEICHEM ZYKLUS)
N320 G80 (G80 BOHRZYKLUS G83 SICHER ABBRECHEN UND DEAKTIVIEREN)
N330 G00 Z15.000 (G00 EILGANG AUF SICHERHEITSHOEHE 15MM)

(--- SICHERES PROGRAMMENDE - SAFE FOOTER ---)
N340 M09 (M09 KUEHLSCHMIERSTOFF AUSSCHALTEN)
N350 G53 G00 Z0.000 (G53 MASCHINENKOORDINATEN | G00 EILGANG | Z0 SPINDEL GANZ NACH OBEN FAHREN)
N360 M05 (M05 FRAESSPINDEL ANHALTEN)
N370 G53 G00 Y0.000 (G53 MASCHINENKOORDINATEN | G00 EILGANG | Y0 TISCH NACH VORNE ZUR TUER FAHREN)
N380 M30 (M30 HAUPTPROGRAMMENDE, RESET UND SPEICHER AUF ZEILE 1 ZURUECKSETZEN)
%
```

### 🛡️ Prüfliste dieser Übung: Wann ist Übung 4 zu 100 % bestanden?

| Prüfpunkt | Was muss im Code / Simulator zu sehen sein? | Bestanden? |
| :--- | :--- | :---: |
| **1. Außenkontur vollständig** | Vier lineare Verfahrsätze `G01` umschließen das Rechteck $80 \times 50\,\text{mm}$ auf Tiefe `Z-5.000`. | [ ] |
| **2. Kreistasche zentriert** | Befehl `G03` fräst Kreis $\varnothing 30\,\text{mm}$ bei `X40 Y25` auf Tiefe `Z-3.000` mit `I-15.000`. | [ ] |
| **3. Tiefbohrzyklus G83 aktiv** | Alle 4 Löcher werden mit Spanbruch `Q3.0` bis auf `Z-12.000` gebohrt und mit `G80` abgewählt. | [ ] |
| **4. Sicheres Programmende** | Spindel fährt mit `G53 G00 Z0.` hoch, Kühlung stoppt mit `M09`, Tisch verfährt mit `G53 G00 Y0.` zur Tür, `M30` schließt ab. | [ ] |

---

# Übung 5: 3D-Simulation im Browser & Einrichteblatt (`Setup Sheet`) für den Kunden erstellen

### 📌 Spickzettel dieser Übung: Alle Einrichte- & Simulations-Kennzeichen in Übung 5

| Kennzeichen | Fachbegriff & Erklärung | Bedeutung & Funktion in dieser Übung |
|---|---|---|
| **`Setup Sheet`** | **Einrichteblatt *(Maschineneinrichte-Dokument)*** | Verbindliches Datenblatt für den Bediener an der Fräse *(Nullpunkt, Werkzeuge, Rohmaße, Spannmittel)*. |
| **`G54 (X0, Y0, Z0)`** | **Nullpunkt-Lage *(WCS Origin)*** | Exakte physische Position des Werkstück-Nullpunkts *(z. B. linke vordere Oberkante Fertigteil)*. |
| **`Stock / Rohteil`** | **Rohteilabmessungen *(Billet / Raw Stock Dimensions)*** | Mindestmaße des Sägezuschnitts *(hier: $85 \times 55 \times 15\,\text{mm}$)* inklusive Aufmaß. |
| **`Z-MIN & L_min`** | **Tiefster Punkt & Mindest-Auskraglänge *(Minimum Tool Extension)*** | Erforderliche freie Werkzeuglänge aus der Spannzange: $L_{\text{min}} > \lvert Z_{\text{min}}\rvert + 5\,\text{mm}$. |
| **`Kollisionsprüfung`** | **Spannbacken-Sicherheitsabstand *(Clamping Clearance)*** | Garantiert mindestens $2\,\text{mm}$ Luft zwischen Fräser und Schraubstockbacken. |

### 💡 Worum geht es in einfacher Sprache?

Bevor Sie den fertigen **G-Code (Maschinencode)** an Ihren Kunden schicken und Geld dafür verlangen, müssen Sie zwei Dinge tun:

1. **Visuelle 3D-Kontrolle (Simulation):** Sie prüfen am Bildschirm in einer 3D-Animation, ob das Werkzeug wirklich genau dort fräst und bohrt, wo es soll.
2. **Einrichteblatt (`Setup Sheet`) beilegen:** Sie füllen ein übersichtliches Datenblatt aus, damit der Arbeiter an der Maschine weiß, wo der Nullpunkt (`G54`) liegt und welche Werkzeuge er in Platz `T01` und `T02` stecken muss.

### 🛠️ Schritt-für-Schritt ausprobieren (Direkt auf Ihrem Laptop!):

1. **Ihren eigenen interaktiven 3D-Simulator öffnen:**
   - Öffnen Sie im Windows-Explorer den Ordner `C:\Projekte\CNC\kundenauftrag_01_flanschplatte\` und machen Sie einen **Doppelklick** auf die Datei [3d_auftrag_simulator.html](file:///C:/Projekte/CNC/kundenauftrag_01_flanschplatte/3d_auftrag_simulator.html).
   - Die Datei öffnet sich sofort in Ihrem Webbrowser!
   - **Was Sie dort sehen und testen können:**
     - Rechts sehen Sie das **3D-Modell (`80 x 50 x 12 mm`)** mit der runden Kreistasche in der Mitte und den 4 Bohrlöchern.
     - **Bedeutung aller Linienfarben in der 3D-Simulation:**
       - 🔴 **Rote Linie:** **X-Achse *(Längsachse / Verfahrachse nach rechts)*** – zeigt die Bauteillänge von `80 mm`.
       - 🟢 **Grüne Linie:** **Y-Achse *(Querachse / Verfahrachse nach hinten)*** – zeigt die Bauteilbreite von `50 mm`.
       - 🔵 **Blaue Linie:** **Z-Achse *(Höhenachse / Spindelachse senkrecht nach oben)*** – Werte über 0 liegen sicher in der Luft, Werte unter 0 tauchen tief ins Metall ein.
       - 🎯 **Punkt `(0, 0, 0)`:** **Werkstück-Nullpunkt `G54` *(Work Coordinate System / Referenzpunkt)*** – vordere linke obere Bauteilecke.
       - 🟡 **Gelbe gestrichelte Linien:** **`G00` Eilgang-Bahnen *(Rapid Positioning / Eilgang im Vollgas)*** – schnelle Positionierung des Werkzeugs durch die Luft ohne Materialkontakt *(Crash-Gefahr, wenn zu tief!)*.
       - 🔷 **Cyan / Hellblaue Linien:** **`G01` / `G03` Fräsbahn *(Feedrate Moves / Arbeitsvorschub)*** – hier schneidet der Fräser echte Späne ins Metall.
       - 🔴 **Roter Zylinder mit Ring:** Das **Fräswerkzeug *(Spindel und Fräser/Bohrer)*** an seiner aktuellen Live-Position `(X, Y, Z)`.
       - ⬜ **Fester grauer Rahmen:** Die Fertigmaße des **Fertigteils *(Fertigteil-Kontur: 80×50×12 mm Aluminium EN AW-6082)***.
       - 🔲 **Gestrichelter grauer Kasten:** Das **Rohteil (`Stock` / roher Sägezuschnitt vor dem Fräsen: 85×55×15 mm)**.
     - 💡 **Interaktive Tooltips *(Maus-Hover-Info)*:**  
       Fahren Sie mit dem Mauszeiger einfach über **irgendeine farbige Linie, eine Fräsbahn, das Werkzeug oder den Nullpunkt** im 3D-Fenster: Sofort erscheint ein informatives **Popup-Fenster *(Tooltip)*** mit genauer deutscher Erklärung, den aktuellen Koordinaten und der zugehörigen Zeile Maschinencode!
     - Halten Sie die linke Maustaste im 3D-Fenster gedrückt, um das Bauteil von allen Seiten zu drehen, und nutzen Sie das Mausrad zum Heranzoomen. Mit dem Button **`🎥 3D-Ansicht Reset`** oder einem **Doppelklick ins 3D-Fenster** setzen Sie die Ansicht jederzeit zurück.
     - 📏 **G-Code-Fenstergröße frei anpassen *(Höhe & Breite)***:  
       Das Maschinencode-Fenster links unten lässt sich mit den 3 Buttons (`↕ 260px`, `↕ 450px`, `↕ 650px`) per Klick vergrößern oder mit der Maus an der rechten unteren Ecke frei auf jede Wunschhöhe ziehen. Außerdem kann die gesamte linke Seitenleiste über den senkrechten Schieberbalken *(Trennlinie zwischen Code und 3D)* mit der Maus beliebig breit gezogen werden.
2. **Das fertige Einrichteblatt (`Setup Sheet`) prüfen:**
   - Öffnen Sie die Datei [kundenauftrag_01_flanschplatte/EINRICHTEBLATT_SETUP_SHEET.md](file:///C:/Projekte/CNC/kundenauftrag_01_flanschplatte/EINRICHTEBLATT_SETUP_SHEET.md).
   - Dieses Dokument drucken Sie als **PDF (Portable Document Format)** aus und schicken es zusammen mit der Datei [tests/output_expected.nc](file:///C:/Projekte/CNC/tests/output_expected.nc) an den Kunden. Damit ist Ihr Auftrag zu 100 % professionell abgeschlossen!

### 🛡️ Prüfliste dieser Übung: Wann ist Übung 5 zu 100 % bestanden?

| Prüfpunkt | Was muss im Code / Simulator zu sehen sein? | Bestanden? |
| :--- | :--- | :---: |
| **1. 3D-Simulation fehlerfrei** | Das Werkzeug fährt im Browser in [`3d_auftrag_simulator.html`](file:///C:/Projekte/CNC/kundenauftrag_01_flanschplatte/3d_auftrag_simulator.html) kollisionsfrei alle Fräsbahnen und Bohrungen ab. | [ ] |
| **2. Nullpunkt eindeutig definiert** | Das Einrichteblatt weist `G54` mit `X0 Y0 Z0` an der vorderen linken Bauteil-Oberkante aus. | [ ] |
| **3. Werkzeugliste & Mindestlänge** | Alle Fräser/Bohrer sind mit Nummer, Durchmesser und Mindestauskraglänge $L_{\text{min}}$ dokumentiert. | [ ] |
| **4. Rohteil- und Spannmaße** | Rohteilmaß $85 \times 55 \times 15\,\text{mm}$ und Einspanntiefe von $3\,\text{mm}$ sind für den Maschinenbediener verbindlich vorgegeben. | [ ] |

---

# Übung 6: Sicherer Rückzug (`Safe Retract`) & Tisch am Programmende zur Tür fahren (`onClose`)

### 📌 Spickzettel dieser Übung: Alle verwendeten G-Code- & M-Code-Kennzeichen in Übung 6

| Kennzeichen | Fachbegriff & Erklärung | Bedeutung & Funktion in dieser Übung |
|---|---|---|
| **`M09`** | **Kühlmittel AUS *(Coolant Off)*** | Stoppt den Kühlmittelfluss vor dem Rückzug, damit die Kabine nicht vollgespritzt wird. |
| **`G53`** | **Maschinen-Koordinatensystem *(Machine Coordinate System)*** | Fährt bezogen auf den festen Maschinen-Nullpunkt *(unabhängig vom Werkstück-Nullpunkt `G54`)*. |
| **`G00`** | **Eilgang *(Rapid Move)*** | Schnelle Verfahrbewegung ohne Schnitt. |
| **`Z0.000` (bei `G53`)** | **Oberer Z-Endpunkt *(Spindle Home / Top of Z-Axis)*** | Fährt die Spindel senkrecht ganz nach oben an die Maschinendecke *(Crash-Schutz)*. |
| **`M05`** | **Spindel-Stopp *(Spindle Stop)*** | Schaltet den Spindeldrehantrieb nach Verlassen des Bauteils aus. |
| **`Y0.000` (bei `G53`)** | **Tisch vor zur Kabinentür *(Table to Front Door)*** | Fährt den Maschinentisch ganz nach vorne zum bequemen Werkstückwechsel. |
| **`G28 G91 Z0.`** | **Inkrementelle Referenzpunktfahrt Z *(Incremental Return to Reference)*** | Haas/Fanuc-Alternative zu `G53 Z0`: Fährt Z um `0 mm` inkrementell zum Maschinenreferenzpunkt. |
| **`G90`** | **Absolutmaß *(Absolute Distance Mode)*** | Stellt das System nach `G91` sofort wieder auf absolute Koordinaten zurück. |
| **`M30`** | **Programmende und Rücklauf *(Program End and Rewind)*** | Beendet den Programmlauf und springt zurück auf die allererste Programmzeile. |

### 💡 Worum geht es in einfacher Sprache?

Wenn das Fräsprogramm fertig ist (oder bevor ein neues Werkzeug eingewechselt wird), steckt der Fräser oft noch tief unten am Bauteil. 
**Die wichtigste goldene Regel in der gesamten CNC-Technik lautet:**

> **Zuerst IMMER die Z-Achse (Spindel) senkrecht nach ganz oben ziehen – und erst DANACH den Tisch in X oder Y bewegen!**

Warum? Wenn Sie zuerst den Tisch nach vorne zur Tür fahren (`Y0`), während der Bohrer noch auf `Z-12.0 mm` im Loch steckt, reißt der Bohrer sofort ab!
Außerdem wünscht sich fast jeder Kunde am Ende des Programms (`onClose`), dass:

1. Das **Spritzwasser / Kühlmittel (`M09`)** ausgeht,
2. Die **Spindel ganz nach oben fährt (`G53 G00 Z0`)**,
3. Der **Spindelmotor stoppt (`M05`)**,
4. Und der **Maschinentisch nach vorne zur Kabinentür fährt (`G53 G00 Y0`)**, damit der Arbeiter sich nicht tief in die nasse Maschine hineinbeugen muss, um das fertige Bauteil herauszunehmen.

### 🛠️ Wo im Code wird das gemacht?

Für diese Übung stehen Ihnen **zwei Quellcode-Dateien** zur Verfügung:
1. **Als eigene, kompakte Übungs-Datei:**  
   [`uebungen/uebung_06_sicherer_rueckzug.cps`](file:///C:/Projekte/CNC/uebungen/uebung_06_sicherer_rueckzug.cps) – Zeigt isoliert die sichere 2-Stufen-Rückzugslogik in `onClose()`.
2. **Im großen Gesamt-Postprozessor des Projekts:**  
   [`src/mein_erster_post.cps`](file:///C:/Projekte/CNC/src/mein_erster_post.cps#L441-L499) – Am Ende des Bearbeitungslaufs.

### 🖥️ Schritt-für-Schritt: So öffnen, bearbeiten, starten und simulieren Sie Übung 6 in Visual Studio Code (VSC)

#### Schritt 1: Datei in Visual Studio Code öffnen
1. Drücken Sie `Strg + P` in VS Code.
2. Tippen Sie ein: `uebung_06_sicherer_rueckzug.cps` und drücken Sie `Enter`.

#### Schritt 2: Programm im Terminal ausführen & testen
1. Öffnen Sie das Terminal mit ``Strg + ` ``.
2. Geben Sie ein:
   ```powershell
   node tests/simuliere_post.js uebungen/uebung_06_sicherer_rueckzug.cps
   ```
3. Der Simulator führt den Postprozessor aus und bestätigt den sicheren Rückzug.

#### Schritt 3: Den erzeugten G-Code ansehen
* Öffnen Sie [`tests/mein_generierter_gcode.nc`](file:///C:/Projekte/CNC/tests/mein_generierter_gcode.nc) mit `Strg + P`.
* Scrollen Sie ganz nach unten: Sie sehen `G28 G91 Z0.` gefolgt von `G28 Y0.` und `M30`.

#### Schritt 4: 3D-Simulation visuell prüfen
* Kopieren Sie den G-Code in [https://ncviewer.com](https://ncviewer.com).
* Am Ende der Simulation sehen Sie, wie das Werkzeug senkrecht nach oben fährt, bevor der Tisch verfährt!

---

### 🛠️ Wie ist das in [`src/mein_erster_post.cps`](file:///C:/Projekte/CNC/src/mein_erster_post.cps#L441-L499) programmiert?

```javascript
function onClose() {
  writeln("");
  writeComment("--- SICHERES PROGRAMMENDE (SAFE FOOTER) ---");

  // Schritt 1: Kühlmittel ausschalten (M09)
  writeBlock(mFormat.format(9));

  // Schritt 2: ZUERST die Z-Achse (Spindel) ganz nach oben an die Decke fahren!
  writeRetract(Z);

  // Schritt 3: Spindel-Drehung anhalten (M05)
  writeBlock(mFormat.format(5));

  // Schritt 4: ERST JETZT den Tisch nach vorne zur Tür fahren (G53 G00 Y0.000)
  if (getProperty("useG28SafeRetract")) {
    writeBlock(gFormat.format(28), gAbsIncModal.format(91), "Y" + xyzFormat.format(0));
    writeBlock(gAbsIncModal.format(90));
  } else {
    writeBlock(gFormat.format(53), gMotionModal.format(0), "Y" + xyzFormat.format(0));
  }

  // Schritt 5: Programm beenden und zum Anfang zurückspulen (M30)
  writeBlock(mFormat.format(30));
  writeln("%");
}
```

* **Was ist der Unterschied zwischen `G54` und `G53`?**
  - **`G54` (Werkstück-Nullpunkt):** Bezieht sich auf Ihr **Bauteil im Schraubstock**. `Z0` bei `G54` ist also direkt auf dem Metallblock!
  - **`G53` (Maschinen-Koordinatensystem):** Bezieht sich fest auf das **Gehäuse der CNC-Maschine**. `G53 G00 Z0.000` bedeutet bei **Haas**, **Siemens** und **Fanuc** immer: *„Fahre die Spindel ganz nach oben unter das Maschinendach, so weit weg vom Schraubstock wie möglich!“*

### ✅ So sieht das Ergebnis am Ende des G-Codes ([`tests/output_expected.nc`](file:///C:/Projekte/CNC/tests/output_expected.nc#L59-L66)) aus:

```gcode
(--- SICHERES PROGRAMMENDE - SAFE FOOTER ---)
N370 M09 (M09 KUEHLSCHMIERSTOFF AUSSCHALTEN)
N380 G53 G00 Z0.000 (G53 MASCHINENKOORDINATEN | G00 EILGANG | Z0 SPINDEL GANZ NACH OBEN FAHREN)
N390 M05 (M05 FRAESSPINDELMOTOR AUSSCHALTEN - SPINDELSTOPP)
N400 G53 G00 Y0.000 (G53 MASCHINENKOORDINATEN | G00 EILGANG | Y0 TISCH NACH VORNE ZUR TUER FAHREN)
N410 M30 (M30 HAUPTPROGRAMMENDE, RESET UND SPEICHER AUF ZEILE 1 ZURUECKSETZEN)
%
```

### 🛡️ Prüfliste dieser Übung: Wann ist Übung 6 zu 100 % bestanden?

| Prüfpunkt | Was muss im Code / Simulator zu sehen sein? | Bestanden? |
| :--- | :--- | :---: |
| **1. Zuerst Z-Rückzug** | Die Z-Achse fährt in Zeile N380 mit `G53 G00 Z0.` ganz nach oben, BEVOR sich die Y-Achse bewegt. | [ ] |
| **2. Spindel-Stopp** | Der Spindelmotor wird mit `M05` erst ausgeschaltet, nachdem das Werkzeug das Bauteil verlassen hat. | [ ] |
| **3. Bedienerkomfort** | Der Tisch fährt in Zeile N400 mit `Y0.` vor zur Kabinentür. | [ ] |
| **4. Konsistenz im Simulator** | Im 3D-Simulator hebt das Werkzeug senkrecht ab und parkt kollisionsfrei. | [ ] |

---

# Übung 7: Eigenen Schalter (`Property`) für Zusatzfunktionen wie Blasluft (`M07`) oder Späneförderer bauen

### 📌 Spickzettel dieser Übung: Alle verwendeten G-Code- & M-Code-Kennzeichen in Übung 7

| Kennzeichen | Fachbegriff & Erklärung | Bedeutung & Funktion in dieser Übung |
|---|---|---|
| **`useChipConveyor`**| **Benutzer-Einstellung *(Postprocessor Property)*** | Ein/Aus-Schalter (`boolean`), der in CAM-Dialogen als Häkchen erscheint. |
| **`M31`** | **Späneförderer EIN Vorwärts *(Chip Conveyor Forward On)*** | Startet das Späne-Kratzband oder die Förderschnecke am Programmanfang. |
| **`M33`** | **Späneförderer AUS *(Chip Conveyor Stop)*** | Stoppt den Fördermotor am Programmende vor dem Hauptspindel-Reset. |
| **`M07`** | **Minimalmengenschmierung / Blasluft *(Air Blast / Mist Coolant)*** | Schaltet Druckluft oder Mikrosprühen ein *(Trockenfräsen)*. |
| **`M08`** | **Flutkühlung EIN *(Flood Coolant On)*** | Standard-Kühlmittel mit hoher Fördermenge. |
| **`M30`** | **Programmende *(Program End)*** | Schließt die Programmausführung ab. |

### 💡 Worum geht es in einfacher Sprache?

Ein Kunde ruft Sie an und sagt:
*„Wenn wir Aluminium trocken fräsen, wollen wir manchmal kein flüssiges Kühlwasser (`M08`), sondern unser neues **Späneförderband (Förderband unten in der Maschine, das die Späne heraustransportiert)** automatisch beim Programmstart mit dem Befehl **`M31`** einschalten und am Programmende mit **`M33`** wieder ausschalten. Kannst du mir dafür einen Schalter in den Postprozessor einbauen?“*

Für solche kleinen Anpassungen berechnen Postprozessor-Entwickler oft pauschal **150 € bis 300 €**, und die Umsetzung dauert in **JavaScript** keine 5 Minuten!

### 🛠️ Wo im Code wird das gemacht?

Für diese Übung stehen Ihnen **zwei Quellcode-Dateien** zur Verfügung:
1. **Als eigene, kompakte Übungs-Datei:**  
   [`uebungen/uebung_07_spaenefoerderer_schalter.cps`](file:///C:/Projekte/CNC/uebungen/uebung_07_spaenefoerderer_schalter.cps) – Enthält den einsatzbereiten Schalter für den Späneförderer.
2. **Im großen Gesamt-Postprozessor des Projekts:**  
   [`src/mein_erster_post.cps`](file:///C:/Projekte/CNC/src/mein_erster_post.cps)

### 🖥️ Schritt-für-Schritt: So öffnen, bearbeiten, starten und simulieren Sie Übung 7 in Visual Studio Code (VSC)

#### Schritt 1: Datei in Visual Studio Code öffnen
1. Drücken Sie in VS Code `Strg + P`.
2. Tippen Sie ein: `uebung_07_spaenefoerderer_schalter.cps` und drücken Sie `Enter`.
3. Ändern Sie z. B. in Zeile 16 `enableChipConveyor: true` auf `false` und wieder zurück.

#### Schritt 2: Programm im Terminal ausführen & testen
1. Öffnen Sie das Terminal mit ``Strg + ` ``.
2. Führen Sie aus:
   ```powershell
   node tests/simuliere_post.js uebungen/uebung_07_spaenefoerderer_schalter.cps
   ```
3. Der Simulator schaltet den Späneförderer automatisch ein und wieder aus.

#### Schritt 3: Den erzeugten G-Code ansehen
* Öffnen Sie [`tests/mein_generierter_gcode.nc`](file:///C:/Projekte/CNC/tests/mein_generierter_gcode.nc) mit `Strg + P`.
* Suchen Sie nach dem Befehl `M31` am Anfang und `M33` am Ende.

#### Schritt 4: 3D-Simulation visuell prüfen
* Kopieren Sie den G-Code in [https://ncviewer.com](https://ncviewer.com).

---

### 🛠️ So bauen Sie das in 3 Schritten ein:

#### Schritt 1: Den Schalter oben in `properties` eintragen

Damit der Kunde beim Exportieren ein Häkchen setzen kann, fügen wir in `properties` diesen Block hinzu:

```javascript
  useChipConveyor: {
    title      : "Späneförderer automatisch starten (Use Chip Conveyor M31/M33)",
    description: "Schaltet am Programmstart das Späneförderband mit M31 ein und am Ende mit M33 wieder aus.",
    group      : "safety",
    type       : "boolean", // boolean = einfacher Ja/Nein-Haken (Checkbox)
    value      : false,     // Standardmäßig ausgeschaltet
    scope      : "post"
  }
```

#### Schritt 2: In `onOpen()` (Programmstart) abfragen, ob der Haken gesetzt ist

```javascript
  if (getProperty("useChipConveyor")) {
    writeComment("SPAENEFOERDERER AUTOMATISCH STARTEN");
    // M31 = Späneförderer (Kratzband / Förderschnecke) VORWÄRTS STARTEN
    writeBlock(mFormat.format(31)); // Gibt "N... M31" im G-Code aus
  }
```

#### Schritt 3: In `onClose()` (Programmende) wieder ausschalten

```javascript
  if (getProperty("useChipConveyor")) {
    writeComment("SPAENEFOERDERER STOPPEN");
    // M33 = Späneförderer STOPP (Bandantrieb anhalten)
    writeBlock(mFormat.format(33)); // Gibt "N... M33" im G-Code aus
  }
```

### ✅ So sieht das Ergebnis im fertigen G-Code mit aktivem Späneförderer (`M31` / `M33`) aus:

```gcode
%
O1001 (PROGRAMM MIT AUTOMATISCHEM SPAENEFOERDERER)
(==================================================)
(SPAENEFOERDERER AUTOMATISCH STARTEN)
N15 M31 (M31 SPAENEFOERDERER EIN - KRATZBAND LAEUFT VORWAERTS)
(==================================================)
N20 G90 G21 G17 G40 G80 (SICHERHEITSZEILE: ABSOLUT | METRISCH | XY-EBENE | RADIUSKORREKTUR AUS | BOHREN AUS)
...
(--- SICHERES PROGRAMMENDE - SAFE FOOTER ---)
N370 M09 (M09 KUEHLMITTEL AUS)
N380 G53 G00 Z0.000 (G53 MASCHINENKOORDINATEN | G00 EILGANG | Z0 SPINDEL GANZ NACH OBEN)
N390 M05 (M05 SPINDELSTOPP)
N395 M33 (M33 SPAENEFOERDERER STOPPEN - BANDANTRIEB AUSSCHALTEN)
N400 G53 G00 Y0.000 (G53 MASCHINENKOORDINATEN | G00 EILGANG | Y0 TISCH VOR ZUR TUER)
N410 M30 (M30 HAUPTPROGRAMMENDE, RESET UND RUECKSPRUNG)
%
```

### 🛡️ Prüfliste dieser Übung: Wann ist Übung 7 zu 100 % bestanden?

| Prüfpunkt | Was muss im Code / Simulator zu sehen sein? | Bestanden? |
| :--- | :--- | :---: |
| **1. Schalter in Properties** | Die Eigenschaft `useChipConveyor` ist als Ja/Nein-Schalter (`boolean`) definiert. | [ ] |
| **2. Einschalten bei Start** | Wenn `true`, steht oben im G-Code: `M31` *(Späneförderer AN)*. | [ ] |
| **3. Ausschalten bei Ende** | Wenn `true`, steht am Programmende vor `M30`: `M33` *(Späneförderer AUS)*. | [ ] |
| **4. Deaktivierungstest** | Wenn `false`, taucht weder `M31` noch `M33` im Maschinencode auf. | [ ] |

---

# Übung 8: Zwei Steuerungs-Sprachen vergleichen (Haas/Fanuc vs. Siemens Sinumerik)

### 📌 Spickzettel dieser Übung: Alle verwendeten Steuerungs-Kennzeichen in Übung 8

| Kennzeichen | Fachbegriff & Erklärung | Bedeutung & Funktion in dieser Übung |
|---|---|---|
| **`controllerDialect`** | **Steuerungs-Auswahl *(Post Dialect Property)*** | Wählt im Postprozessor zwischen `FANUC` *(ISO)* und `SIEMENS` *(Sinumerik)*. |
| **`(...)` vs. `;`** | **Kommentar-Syntax *(Comment Syntax)*** | Fanuc/Haas verlangt runde Klammern `(...)`, Siemens ein Semikolon `;`. |
| **`G21` vs. `G71`** | **Metrisches Einheitensystem *(Metric Mode)*** | Fanuc nutzt `G21` für Millimeter, Siemens Sinumerik nutzt `G71`. |
| **`G83` vs. `CYCLE83`** | **Tiefbohr-Befehl *(Deep Hole Drilling Cycle)*** | Fanuc nutzt modalen Zyklus `G83 Q3.0`, Siemens den Hochsprachenzyklus `CYCLE83(...)`. |
| **`G53` vs. `SUPA`** | **Maschinenkoordinaten-Rückzug *(Machine Coordinate Retract)*** | Fanuc nutzt `G53 G00 Z0.`, Siemens `SUPA G00 Z0.` *(Satzweise Unterdrückung programmierbarer Nullpunktverschiebungen)*. |

### 💡 Worum geht es in einfacher Sprache?

In Ihrer [doc.txt](file:///C:/Projekte/CNC/doc.txt) wurde erklärt, dass verschiedene Maschinenhersteller unterschiedliche „Sprachen“ (**G-Code-Dialekte**) sprechen – genau wie Deutsch und Englisch.
In dieser Übung schauen wir uns direkt nebeneinander an, wie **haargenau dieselbe Bohrung** (bei `X10, Y10`, Tiefe `Z-12 mm`) auf einer amerikanischen/japanischen **Haas/Fanuc-Steuerung** und auf einer deutschen **Siemens Sinumerik Steuerung** aussieht – und wie Ihr **JavaScript-Code** den Unterschied erzeugt!

### 🛠️ Wo im Code wird das gemacht?

Für diese Übung stehen Ihnen **zwei Quellcode-Dateien** zur Verfügung:
1. **Als eigene, kompakte Übungs-Datei:**  
   [`uebungen/uebung_08_fanuc_siemens_dialekt.cps`](file:///C:/Projekte/CNC/uebungen/uebung_08_fanuc_siemens_dialekt.cps) – Enthält den Dialekt-Umschalter zwischen Fanuc und Siemens Sinumerik.
2. **Im großen Gesamt-Postprozessor des Projekts:**  
   [`src/mein_erster_post.cps`](file:///C:/Projekte/CNC/src/mein_erster_post.cps)

### 🖥️ Schritt-für-Schritt: So öffnen, bearbeiten, starten und simulieren Sie Übung 8 in Visual Studio Code (VSC)

#### Schritt 1: Datei in Visual Studio Code öffnen
1. Drücken Sie in VS Code `Strg + P`.
2. Tippen Sie ein: `uebung_08_fanuc_siemens_dialekt.cps` und drücken Sie `Enter`.
3. In Zeile 16 können Sie `dialect: "FANUC"` auf `dialect: "SIEMENS"` ändern und speichern (`Strg + S`).

#### Schritt 2: Programm im Terminal ausführen & testen
1. Öffnen Sie das Terminal mit ``Strg + ` ``.
2. Führen Sie aus:
   ```powershell
   node tests/simuliere_post.js uebungen/uebung_08_fanuc_siemens_dialekt.cps
   ```
3. Der Simulator gibt je nach gewählter Einstellung Fanuc- oder Siemens-Code aus.

#### Schritt 3: Den erzeugten G-Code ansehen
* Öffnen Sie [`tests/mein_generierter_gcode.nc`](file:///C:/Projekte/CNC/tests/mein_generierter_gcode.nc) mit `Strg + P`.
* Vergleichen Sie: Bei Siemens sehen Sie `;` als Kommentar und `CYCLE83`, bei Fanuc `(...)` und `G83`.

#### Schritt 4: 3D-Simulation visuell prüfen
* Kopieren Sie den G-Code in [https://ncviewer.com](https://ncviewer.com).

---

### 📊 Der direkte Vergleich der beiden Steuerungs-Sprachen:

| Was soll die Maschine tun?                           | Sprache 1: Haas / Fanuc (ISO-Standard)                | Sprache 2: Siemens Sinumerik (840D / ONE)                                                               |
|:---------------------------------------------------- |:----------------------------------------------------- |:------------------------------------------------------------------------------------------------------- |
| **Einen Kommentar (Notiz) schreiben**                | In runden Klammern:<br>`(BOHRUNG STARTEN)`            | Mit einem Semikolon am Zeilenanfang:<br>`; BOHRUNG STARTEN`                                             |
| **Werkzeug 2 einwechseln**                           | `T02 M06`                                             | `T="BOHRER_6MM" D1`<br>`M06`                                                                            |
| **Tiefbohrung bis `Z-12 mm` (mit `3 mm` Spanbruch)** | `G90 G83 X10.000 Y10.000 Z-12.000 R2.000 Q3.000 F300` | `F300`<br>`MCALL CYCLE83(15.0, 0.0, 2.0, -12.0, , -3.0, , 1, , , 1, 0)`<br>`X10.000 Y10.000`<br>`MCALL` |
| **Programmende**                                     | `M30`                                                 | `M30`                                                                                                   |

### 🛠️ Wie entscheidet Ihr JavaScript-Postprozessor, welche Sprache er schreibt?

Mit einer einfachen `if / else`-Abfrage (Wenn-Dann-Entscheidung) in Ihrem **JavaScript-Code**:

```javascript
// Beispiel 1: Kommentar-Funktion je nach Steuerung anpassen
function writeComment(text) {
  if (getProperty("controllerDialect") == "siemens") {
    // Siemens Sinumerik nutzt ein Semikolon ";" vor Kommentaren:
    writeln("; " + String(text).toUpperCase());
  } else {
    // Haas und Fanuc nutzen runde Klammern "(...)":
    writeln("(" + filterText(String(text).toUpperCase(), permittedCommentChars) + ")");
  }
}

// Beispiel 2: Start-Initialisierung je nach Steuerung:
if (isSiemens) {
  // Siemens Sinumerik Initialisierung:
  // G90 = Absolutmaß
  // G71 = Maßeinheit Millimeter (metrisch nach DIN/ISO)
  // G17 = Fräsebene XY
  writeWords("G90", "G71", "G17");
} else {
  // Haas / Fanuc ISO Initialisierung:
  // G90 = Absolutmaß
  // G21 = Maßeinheit Millimeter (metrisch)
  // G17 = Fräsebene XY
  // G40 = Radiuskorrektur ausschalten
  // G80 = Bohrzyklen abbrechen
  writeWords("G90", "G21", "G17", "G40", "G80");
}

// Beispiel 3: Z-Rückzug am Programmende:
// Siemens: SUPA G00 Z0.0 (SUPA = Satzweise Unterdrückung programmierbarer Nullpunktverschiebungen / Maschinen-Z0)
// Fanuc: G53 G00 Z0.0 (G53 = Maschinen-Koordinatensystem im Eilgang G00)
writeWords(isSiemens ? "SUPA G00 Z0.0" : "G53 G00 Z0.0");
```

Genau deshalb ist **JavaScript** für diesen Beruf so mächtig: Das **3D-Modell** und die **Fräsbahnen** bleiben zu 100 % gleich – nur Ihr kurzes JavaScript-Skript formt den Text am Ende so um, dass jede Maschine der Welt ihn versteht!

### 🛡️ Prüfliste dieser Übung: Wann ist Übung 8 zu 100 % bestanden?

| Prüfpunkt | Was muss im Code / Simulator zu sehen sein? | Bestanden? |
| :--- | :--- | :---: |
| **1. Dialekt-Auswahl** | Das Dropdown/Property erlaubt die Wahl zwischen `Haas/Fanuc` und `Siemens Sinumerik`. | [ ] |
| **2. Kommentar-Syntax** | Bei Fanuc stehen runde Klammern `(...)`, bei Siemens steht ein Semikolon `;` am Zeilenanfang. | [ ] |
| **3. Metrik-Befehl** | Bei Fanuc wird `G21` ausgegeben, bei Siemens korrekt `G71`. | [ ] |
| **4. Rückzugsbefehl** | Bei Fanuc steht `G53 G00 Z0.`, bei Siemens steht der herstellerspezifische Befehl `SUPA G00 Z0.`. | [ ] |

---

# 📈 Teil 2: Die perfekte Lern-Reihenfolge (Sortiert von „Kinderleicht“ bis „Profi“ – Aufsteigende Komplexität)

> **Wichtiger Hinweis zur Reihenfolge:**  
> Oben wurden die Übungen 1 bis 8 in der Reihenfolge dokumentiert, in der sie in unserem Gespräch entstanden sind.  
> Wenn Sie jedoch **bei Null starten und Schritt für Schritt vom Einfachsten zum Schwersten lernen wollen**, ist z. B. **Übung 3 (`Z-MIN` mit Schleifen)** schwerer als **Übung 5 (3D-Simulator anschauen)** oder **Übung 7 (einfacher `if`-Schalter)**.
>
> Deshalb finden Sie hier den **optimal sortierten Lernpfad (Stufe 1 bis Stufe 10, streng aufsteigend nach Schwierigkeit)** – inklusive zwei ganz einfacher **Einsteiger-Übungen (Stufe 1 & Stufe 2)** für den allerersten Start!

---

## 📊 Übersichtstabelle: Alle 16 Übungen (+ 2 Basis-Übungen) sortiert nach Schwierigkeit (Stufe 1 bis Stufe 18)

| Lern-Reihenfolge     | Schwierigkeit           | Welche Übung machen Sie?                                                                                                                                         | Was lernen Sie dabei? (Konzept)                                                                                                                                                |
|:-------------------- |:----------------------- |:---------------------------------------------------------------------------------------------------------------------------------------------------------------- |:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Stufe 1 (Start)**  | ⭐☆☆☆☆ (Sehr leicht)     | **[Übung 5](#übung-5-3d-simulation-im-browser--einrichteblatt-setup-sheet-für-den-kunden-erstellen)** *(3D-Simulator im Browser öffnen)*                         | Erst einmal mit den eigenen Augen sehen: Wie sieht das 3D-Bauteil aus, wie fährt der Fräser und was macht der **G-Code (Maschinencode)**? (Noch gar kein Programmieren nötig!) |
| **Stufe 2**          | ⭐☆☆☆☆ (Sehr leicht)     | **[Basis-Übung A (Unten)](#stufe-2--basis-übung-a-die-5-wichtigsten-g-code-zeilen-lesen-lernen)** *(G-Code lesen wie ein Buch)*                                  | Verstehen, was `G00` (Eilgang), `G01` (Fräsen), `M03` (Spindel an), `M08` (Wasser an) und `M30` (Ende) bedeuten.                                                               |
| **Stufe 3**          | ⭐⭐☆☆☆ (Leicht)          | **[Basis-Übung B (Unten)](#stufe-3--basis-übung-b-eine-einzige-zeile-text-im-code-ändern)** *(Erste Zeile in JavaScript ändern)*                                 | Einen einzigen festen Satz mit `writeComment("MEIN ERSTER TEST")` in [`src/mein_erster_post.cps`](file:///C:/Projekte/CNC/src/mein_erster_post.cps) schreiben.                 |
| **Stufe 4**          | ⭐⭐☆☆☆ (Leicht)          | **[Übung 1](#übung-1-der-erste-eigene-text-im-g-code-entwickler-infoblock-in-onopen)** *(Entwickler-Infoblock mit Datum in `onOpen`)*                            | Variablen (`var`) nutzen, das aktuelle Datum (`new Date()`) auslesen und mit `getProperty()` Ihren Namen einfügen.                                                             |
| **Stufe 5**          | ⭐⭐☆☆☆ (Leicht–Mittel)   | **[Übung 6](#übung-6-sicherer-rückzug-safe-retract--tisch-am-programmende-zur-tür-fahren-onclose)** *(Programmende `onClose` verstehen & anpassen)*              | Einfache Maschinenbefehle (`M09`, `M05`, `M30`) und den sicheren Rückzug nach oben (`G53 G00 Z0`) verstehen.                                                                   |
| **Stufe 6**          | ⭐⭐⭐☆☆ (Mittel)          | **[Übung 7](#übung-7-eigenen-schalter-property-für-zusatzfunktionen-wie-blasluft-m07-oder-späneförderer-bauen)** *(Eigenen Ja/Nein-Schalter `Property` bauen)*   | Eine `if`-Bedingung (Wenn-Dann-Abfrage) schreiben: *„Wenn der Kunde das Häkchen setzt, schalte den Späneförderer `M31` ein.“*                                                  |
| **Stufe 7**          | ⭐⭐⭐☆☆ (Mittel)          | **[Übung 4](#übung-4-ein-3d-modell-als-kundenauftrag-bearbeiten-vom-3d-bauteil-zum-g-code)** *(3D-Modell im CAM-Programm bearbeiten)*                            | Das 3D-Bauteil (`bauteil_1001.stl`) nehmen, Nullpunkt `G54` setzen, Fräsbahnen anklicken und mit dem Postprozessor exportieren.                                                |
| **Stufe 8**          | ⭐⭐⭐⭐☆ (Fortgeschritten) | **[Übung 2](#übung-2-automatische-werkzeugliste-tool-table-ganz-oben-im-programm-ausgeben)** *(Werkzeugliste `Tool Table` mit `for`-Schleife)*                   | Eine `for`-Schleife (Wiederholungsschleife) nutzen, um alle Werkzeuge aus `getToolTable()` automatisch aufzulisten.                                                            |
| **Stufe 9**          | ⭐⭐⭐⭐☆ (Fortgeschritten) | **[Übung 3](#übung-3-sicherheits-schutz-gegen-maschinencrash--tiefste-frästiefe-z-min-berechnen)** *(Tiefste Frästiefe `Z-MIN` über alle Operationen berechnen)* | Eine eigene Hilfsfunktion `getToolMinimumZ(tool)` schreiben, die alle Arbeitsschritte durchsucht und den kleinsten Z-Wert findet.                                              |
| **Stufe 10 (Profi)** | ⭐⭐⭐⭐⭐ (Experte)         | **[Übung 8](#übung-8-zwei-steuerungs-sprachen-vergleichen-haasfanuc-vs-siemens-sinumerik)** *(Mehrsprachiger Postprozessor: Haas/Fanuc vs. Siemens)*             | Komplexe Steuerungs-Unterschiede (`CYCLE83` vs. `G83` und `;` vs. `(...)`) im selben Postprozessor umschaltbar machen.                                                         |
| **Stufe 11**         | ⭐⭐⭐☆☆ (Mittel)          | **[Übung 9](#übung-9-schnittdaten-s-drehzahl--f-vorschub-berechnen--warum-aluminium-baustahl-und-edelstahl-völlig-andere-werte-brauchen)** *(Schnittdaten `S` & `F` berechnen)* | Drehzahl $n$ und Vorschub $v_f$ für Aluminium, Stahl und Edelstahl formelgerecht auslegen und im Postprozessor prüfen.                                                         |
| **Stufe 12**         | ⭐⭐⭐☆☆ (Mittel)          | **[Übung 15](#übung-15-kanten-entgraten-am-3d-modell-2d-fase--chamfer-milling-mit-einem-45-fasenfräser-t04)** *(Kanten entgraten / `2D-Fase`)*                   | Mit einem $90^\circ$-Fasenfräser und Spitzen-Versatz (`Tip Offset`) alle Bauteilkanten automatisch auf der Maschine entgraten.                                                |
| **Stufe 13**         | ⭐⭐⭐⭐☆ (Fortgeschritten) | **[Übung 10](#übung-10-die-2-aufspannung-g55--op20--wie-das-3d-bauteil-umgedreht-und-der-restboden-auf-der-rückseite-plangefräst-wird)** *(2. Aufspannung `G55` / `OP20`)* | Werkstück nach Programmstopp (`M00`) umdrehen, zweiten Nullpunkt `G55` aktivieren und den Spannrand auf Fertigmaß abfräsen.                                                    |
| **Stufe 14**         | ⭐⭐⭐⭐☆ (Fortgeschritten) | **[Übung 11](#übung-11-gewindebohren-g84-rigid-tapping--m6--und-m8-schraubengewinde-ohne-werkzeugbruch-programmieren-f--s--steigung)** *(Gewindebohren `G84`)*   | Synchron-Vorschub $F = S \times P$ exakt berechnen und im Zyklus `G84` programmieren, damit kein Gewindebohrer abreißt.                                                        |
| **Stufe 15**         | ⭐⭐⭐⭐☆ (Fortgeschritten) | **[Übung 12](#übung-12-werkzeugradiuskorrektur-g41--g42--g40--wie-der-kunde-an-der-maschine-001-mm-genauigkeit-für-passungen-einstellt)** *(Radiuskorrektur `G41`/`G42`)* | Passungen ($\text{H7}$) mit `G41` / `G40` programmieren, damit der Bediener an der Maschine Hundertstel-Millimeter nachstellen kann.                                           |
| **Stufe 16**         | ⭐⭐⭐⭐⭐ (Experte)         | **[Übung 13](#übung-13-echte-3d-freiformflächen--3d-adaptive-clearing-wirbelfräsen--3d-schlichten-mit-kugelfräser-ball-end-mill)** *(3D-Freiformflächen & Kugelfräser)* | 3D-Schruppen (`Adaptive Clearing`) und 3D-Feinschlichten gekrümmter Oberflächen mit einem Kugelfräser (`Ball End Mill`).                                                       |
| **Stufe 17**         | ⭐⭐⭐⭐⭐ (Experte)         | **[Übung 14](#übung-14-heidenhain-klartext-steuerung-tool-call-l--fmax--4-drehachse-a-achse-für-aufträge-im-deutschsprachigen-raum)** *(Heidenhain Klartext & 4. Achse)* | Den wichtigsten deutschen Steuerungs-Standard (`BEGIN PGM`, `TOOL CALL`, `L ... FMAX`) und Drehachsen (`A-Achse`) verstehen.                                                   |
| **Stufe 18 (Meister)**| ⭐⭐⭐⭐⭐ (Meister-Prüfung) | **[Übung 16](#übung-16-die-komplette-5-punkte-endabnahme-im-simulator-vor-der-auslieferung-an-den-online-kunden-meister-prüfung)** *(5-Punkte-Endabnahme im Simulator)* | Kompletter Qualitäts- und Sicherheitscheck jedes Kundenprogramms vor der Online-Auslieferung.                                                                                   |

---

## 🟢 Stufe 2 – Basis-Übung A: Die 5 wichtigsten G-Code-Zeilen lesen lernen (Schwierigkeit: ⭐☆☆☆☆)

Bevor Sie irgendeinen **JavaScript-Code (Programmcode)** ändern, schauen wir uns in [tests/output_expected.nc](file:///C:/Projekte/CNC/tests/output_expected.nc) nur **5 Zeilen** an. Wenn Sie diese 5 Zeilen verstehen, verstehen Sie bereits 80 % jedes CNC-Programms!

### 📝 Schauen Sie sich diese 5 Zeilen an:

```gcode
N30 T01 M06
N40 S8000 M03
N80 M08
N90 G00 Z2.000
N100 G01 Z-5.000 F500
```

### 🔍 Was bedeutet jede Zeile auf ganz einfache Weise?

1. **`N30 T01 M06`**
   * `N30` = Zeilennummer 30 (nur zur Orientierung für den Menschen).
   * `T01` = Nimm **Werkzeug Nummer 1 (`Tool 01`)** aus dem Magazin.
   * `M06` = **Wechsle das Werkzeug jetzt in die Spindel ein!**
2. **`N40 S8000 M03`**
   * `S8000` = Stelle die **Drehzahl (`Speed`)** auf **8.000 Umdrehungen pro Minute** ein.
   * `M03` = **Schalte den Spindelmotor ein** (Drehrichtung im Uhrzeigersinn).
3. **`N80 M08`**
   * `M08` = **Schalte die Wasserkühlung (`Coolant`) ein**, damit der Fräser nicht heiß wird.
4. **`N90 G00 Z2.000`**
   * `G00` = **Eilgang (Vollgas-Geschwindigkeit in der Luft)**.
   * `Z2.000` = Fahre mit der Werkzeugspitze bis auf **`2 Millimeter` über das Bauteil** (noch in der Luft!).
5. **`N100 G01 Z-5.000 F500`**
   * `G01` = **Arbeits-Bewegung (Vorsichtiges Fahren im Metall)**.
   * `Z-5.000` = Tauche **`5 Millimeter` tief in das Metall hinein** (deshalb das Minuszeichen `-`).
   * `F500` = Fahre dabei mit einer **Geschwindigkeit (`Feedrate` / Vorschub)** von **`500 Millimetern pro Minute`**.

**Übungs-Aufgabe zum Selbsttest:**  
Öffnen Sie [tests/output_expected.nc](file:///C:/Projekte/CNC/tests/output_expected.nc) und suchen Sie Zeile `N250` und `N260`. Welches Werkzeug wird dort eingewechselt und wie schnell dreht es sich?  
*(Lösung: In `N250` wird mit `T02 M06` das Werkzeug Nummer 2 eingewechselt, und in `N260` dreht es sich mit `S3500`, also 3.500 Umdrehungen pro Minute).*

---

## 🟢 Stufe 3 – Basis-Übung B: Eine einzige Zeile Text im Code ändern (Schwierigkeit: ⭐⭐☆☆☆)

### 📌 Spickzettel dieser Übung: Alle verwendeten G-Code- & M-Code-Kennzeichen in Übung 00b

| Kennzeichen | Fachbegriff & Erklärung | Bedeutung & Funktion in dieser Übung |
|---|---|---|
| **`(...)`** | **Kommentar *(Bediener-Notiz)*** | Schreibt reine Notizen wie `writeComment("HALLO WELT...")`, die von der Fräse ignoriert werden. |
| **`G90`** | **Absolutmaß *(Absolute Coordinates)*** | Alle Maße beziehen sich auf den Werkstück-Nullpunkt `G54`. |
| **`G17`** | **XY-Bearbeitungsebene *(Plane Selection)*** | Standard-Fräsebene von oben *(Werkzeugachse ist die Z-Achse)*. |
| **`G21`** | **Metrisches Einheitensystem *(Metric Mode)*** | Alle Maßangaben sind in Millimetern. |
| **`G94`** | **Vorschub-Einheit *(Feed per Minute)*** | Vorschubgeschwindigkeit $F$ wird in $\text{mm/min}$ gerechnet. |
| **`G28 G91 Z0.`** | **Referenzpunktfahrt Z *(Return to Home Z)*** | Z-Achse fährt senkrecht nach oben an den oberen Maschinen-Endschalter *(Crash-Schutz)*. |
| **`T1` / `T2`** | **Werkzeugnummer *(Tool Number)*** | `T1` = Schaftfräser $\varnothing 10\,\text{mm}$ \| `T2` = Spiralbohrer $\varnothing 6\,\text{mm}$. |
| **`M06`** | **Werkzeugwechsel *(Tool Change)*** | Mechanischer Greifarm holt das Werkzeug $T$ physisch in die Spindel. |
| **`S8000` / `S3500`**| **Spindeldrehzahl *(Spindle Speed)*** | Drehzahl des Fräsers in $\text{U/min}$ *(Umdrehungen pro Minute)*. |
| **`M03`** | **Spindel Rechtslauf EIN *(Spindle Clockwise)*** | Schaltet den Frässpindelmotor im Uhrzeigersinn ein. |
| **`G54`** | **Werkstück-Nullpunkt 1 *(Work Coordinate System)*** | Nullpunkt-Lage an der vorderen linken Bauteilecke. |
| **`M05`** | **Spindel-Stopp *(Spindle Stop)*** | Schaltet den Spindelmotor am Programmende aus. |
| **`M09`** | **Kühlmittel AUS *(Coolant Off)*** | Schaltet die Kühlwasserpumpe aus. |
| **`G28 Y0.`** | **Tisch zur Schutztür *(Table to Door)*** | Fährt den Tisch nach vorne zum bequemen Entnehmen des Bauteils. |
| **`M30`** | **Programmende *(Program End)*** | Schließt die Abarbeitung ab und setzt den Programmzeiger auf Zeile 1 zurück. |

Bevor Sie mit Variablen oder Schleifen arbeiten, machen wir die **einfachste Programmier-Übung überhaupt**: Wir fügen eine einzige eigene Textzeile in den Postprozessor ein.

### 🛠️ Schritt-für-Schritt-Anleitung:

1. Öffnen Sie die Datei [`src/mein_erster_post.cps`](file:///C:/Projekte/CNC/src/mein_erster_post.cps#L213-L222).
2. Suchen Sie um Zeile 219 nach dieser Stelle in `onOpen()`:

   ```javascript
   writeComment("EINHEITEN  : " + (unit == MM ? "MILLIMETER (METRISCH G21)" : "INCH / ZOLL (G20)"));
   writeComment("==================================================");
   ```
3. Schreiben Sie direkt darunter eine eigene Zeile mit `writeComment(...)`:

   ```javascript
   writeComment("HALLO WELT - DIES IST MEIN ERSTER EIGENER CNC-BEFEHL");
   ```
4. **Was passiert beim Export?**  
   Der Postprozessor schreibt genau an dieser Stelle im **G-Code (Maschinencode)** die Zeile:  
   `(HALLO WELT - DIES IST MEIN ERSTER EIGENER CNC-BEFEHL)`  
   Damit haben Sie erfolgreich Ihre allererste Code-Änderung an einem CNC-Postprozessor durchgeführt!

---

## 🏆 Zusammenfassung: Wie Sie ab jetzt mit diesem Handbuch arbeiten sollten

Arbeiten Sie die Stufen einfach **von Stufe 1 bis Stufe 18** der Reihe nach ab:

1. Starten Sie mit **Stufe 1 ([Übung 5 – 3D-Simulator öffnen](#übung-5-3d-simulation-im-browser--einrichteblatt-setup-sheet-für-den-kunden-erstellen))** und **Stufe 2 ([Basis-Übung A – 5 Zeilen G-Code lesen](#stufe-2--basis-übung-a-die-5-wichtigsten-g-code-zeilen-lesen-lernen))**.
2. Machen Sie danach die leichten Code-Übungen **Stufe 3 ([Basis-Übung B](#stufe-3--basis-übung-b-eine-einzige-zeile-text-im-code-ändern))**, **Stufe 4 ([Übung 1](#übung-1-der-erste-eigene-text-im-g-code-entwickler-infoblock-in-onopen))**, **Stufe 5 ([Übung 6](#übung-6-sicherer-rückzug-safe-retract--tisch-am-programmende-zur-tür-fahren-onclose))** und **Stufe 6 ([Übung 7](#übung-7-eigenen-schalter-property-für-zusatzfunktionen-wie-blasluft-m07-oder-späneförderer-bauen))**.
3. Gehen Sie danach zu den Auftrags- und Schleifen-Themen **Stufe 7 ([Übung 4 – 3D-Modell im CAM](#übung-4-ein-3d-modell-als-kundenauftrag-bearbeiten-vom-3d-bauteil-zum-g-code))**, **Stufe 8 ([Übung 2 – Werkzeuglisten-Schleife](#übung-2-automatische-werkzeugliste-tool-table-ganz-oben-im-programm-ausgeben))**, **Stufe 9 ([Übung 3 – Z-MIN Berechnung](#übung-3-sicherheits-schutz-gegen-maschinencrash--tiefste-frästiefe-z-min-berechnen))** und **Stufe 10 ([Übung 8 – Siemens vs. Fanuc](#übung-8-zwei-steuerungs-sprachen-vergleichen-haasfanuc-vs-siemens-sinumerik))**.
4. Krönen Sie Ihr Wissen mit den **Profi-Übungen für echte Online-Aufträge**: **Stufe 11 ([Übung 9 – Schnittdaten](#übung-9-schnittdaten-s-drehzahl--f-vorschub-berechnen--warum-aluminium-baustahl-und-edelstahl-völlig-andere-werte-brauchen))**, **Stufe 12 ([Übung 15 – Entgraten](#übung-15-kanten-entgraten-am-3d-modell-2d-fase--chamfer-milling-mit-einem-45-fasenfräser-t04))**, **Stufe 13 ([Übung 10 – 2. Aufspannung G55](#übung-10-die-2-aufspannung-g55--op20--wie-das-3d-bauteil-umgedreht-und-der-restboden-auf-der-rückseite-plangefräst-wird))**, **Stufe 14 ([Übung 11 – Gewindebohren G84](#übung-11-gewindebohren-g84-rigid-tapping--m6--und-m8-schraubengewinde-ohne-werkzeugbruch-programmieren-f--s--steigung))**, **Stufe 15 ([Übung 12 – Radiuskorrektur G41](#übung-12-werkzeugradiuskorrektur-g41--g42--g40--wie-der-kunde-an-der-maschine-001-mm-genauigkeit-für-passungen-einstellt))**, **Stufe 16 ([Übung 13 – 3D-Freiformflächen](#übung-13-echte-3d-freiformflächen--3d-adaptive-clearing-wirbelfräsen--3d-schlichten-mit-kugelfräser-ball-end-mill))**, **Stufe 17 ([Übung 14 – Heidenhain Klartext](#übung-14-heidenhain-klartext-steuerung-tool-call-l--fmax--4-drehachse-a-achse-für-aufträge-im-deutschsprachigen-raum))** und **Stufe 18 ([Übung 16 – 5-Punkte-Endabnahme](#übung-16-die-komplette-5-punkte-endabnahme-im-simulator-vor-der-auslieferung-an-den-online-kunden-meister-prüfung))**.

---

# 🧪 Teil 3: Wie Sie JEDE Übung live im Simulator testen (Schritt-für-Schritt-Anleitung)

Sie haben völlig recht: Zu jeder Übung gehört der genaue Weg, **wie Sie Ihre Änderung am Code sofort ausführen und im Simulator sichtbar machen**!

Wenn Sie in [`src/mein_erster_post.cps`](file:///C:/Projekte/CNC/src/mein_erster_post.cps) eine Zeile JavaScript ändern, passiert der Test immer in **2 Schritten**:

* **Schritt A (Übersetzen / Kompilieren):** Ihr JavaScript-Postprozessor (`mein_erster_post.cps`) wird ausgeführt und erzeugt eine neue **G-Code-Textdatei (`.nc`-Datei)**.
* **Schritt B (Im 3D-Simulator anschauen):** Diese erzeugte `.nc`-Datei schauen Sie sich im **3D-Simulator** an.

Dafür stehen Ihnen auf Ihrem **ThinkPad (Laptop)** ab sofort **4 einfache Wege** zur Verfügung:

---

## 🚀 Weg 0 (Neu & Komfortabel: Eigene `.nc`-Datei direkt im 3D-Simulator auswählen):

Unser interaktiver **3D-Auftrags-Simulator** verfügt ab sofort über einen direkten **Dateiauswahl-Button *(File Picker)*** sowie **Drag & Drop *(Ziehen und Ablegen mit der Maus)*** für jede beliebige `.nc`-Datei:

1. Öffnen Sie die Datei [`kundenauftrag_01_flanschplatte/3d_auftrag_simulator.html`](file:///C:/Projekte/CNC/kundenauftrag_01_flanschplatte/3d_auftrag_simulator.html) per Doppelklick in Ihrem Webbrowser *(Chrome, Edge oder Firefox)*.
2. Klicken Sie links oben auf den auffälligen grünen Button:  
   👉 **`📂 Eigene .nc Datei von Festplatte auswählen & laden`**  
   *(Alternativ können Sie eine beliebige `.nc`-Datei auch einfach mit der Maus vom Windows-Explorer direkt in das Browserfenster ziehen!)*
3. Wählen Sie Ihre gewünschte Datei aus *(z. B. [`uebungen/uebung_00b_hallo_welt.nc`](file:///C:/Projekte/CNC/uebungen/uebung_00b_hallo_welt.nc), [`uebungen/uebung_01_entwickler_header.nc`](file:///C:/Projekte/CNC/uebungen/uebung_01_entwickler_header.nc) oder [`tests/mein_generierter_gcode.nc`](file:///C:/Projekte/CNC/tests/mein_generierter_gcode.nc))*.
4. **Was sofort passiert:**
   * Ein grünes Erfolgs-Badge zeigt an: `✅ Geladene Datei: uebung_00b_hallo_welt.nc (... Zeilen)`.
   * Der Maschinencode wird links im Textfeld zeilengenau aufgeschlüsselt.
   * Der 3D-Simulator zentriert das Bauteil automatisch und fährt die Werkzeugwege mit Fräser oder Bohrer in 3D ab!
   * Sie können mit `▶ Abspielen`, `⏮ Vorheriger`, `⏭ Nächster Schritt` oder per Klick auf eine Zeile jeden Schritt einzeln prüfen.

---

## ⚡ Weg 1 (Der schnellste Weg – Direkt hier ohne Zusatz-Installation): Mit unserem lokalen Simulator-Skript `tests/simuliere_post.js`

Ich habe Ihnen im Ordner `tests/` das Programm **[`tests/simuliere_post.js`](file:///C:/Projekte/CNC/tests/simuliere_post.js)** gebaut. Es nutzt **Node.js (Ihre bereits installierte JavaScript-Laufzeitumgebung)**, liest Ihre Datei [`src/mein_erster_post.cps`](file:///C:/Projekte/CNC/src/mein_erster_post.cps) ein und erzeugt daraus echten **G-Code**!

### So führen Sie es nach jeder Übung aus:

1. Öffnen Sie in Ihrer **Antigravity IDE (Entwicklungsumgebung)** unten das **Terminal (Eingabeaufforderung / PowerShell)** mit der Tastenkombination `` Strg + Ö `` (oder über das Menü `Terminal` $\rightarrow$ `New Terminal`).
2. Tippen Sie diesen kurzen Befehl ein und drücken Sie `Enter`:

   ```powershell
   node tests/simuliere_post.js
   ```
3. **Was sofort passiert:**
   * Im Terminal erscheint sofort Ihr frisch erzeugter **G-Code (Maschinencode)**!
   * Gleichzeitig wird die Datei **`C:\Projekte\CNC\tests\mein_generierter_gcode.nc`** neu geschrieben.
   * Jede Änderung, die Sie in [`src/mein_erster_post.cps`](file:///C:/Projekte/CNC/src/mein_erster_post.cps) gespeichert haben (`Strg + S`), sehen Sie sofort in dieser Datei!

---

## 🌐 Weg 2 (Visuelle 3D-Prüfung im Online-Simulator): Mit `NCViewer.com` (Kostenlos im Browser)

Wenn Sie sehen wollen, wie eine echte **CNC-Fräsmaschine (Werkzeugmaschine)** Ihren frisch erzeugten **G-Code** abfährt:

1. Öffnen Sie nach dem Ausführen von `node tests/simuliere_post.js` die neu erzeugte Datei **`tests/mein_generierter_gcode.nc`** (oder [tests/output_expected.nc](file:///C:/Projekte/CNC/tests/output_expected.nc)).
2. Markieren Sie den gesamten Text mit `Strg + A` und kopieren Sie ihn mit `Strg + C`.
3. Öffnen Sie in Ihrem Internet-Browser die Webseite: **`https://ncviewer.com`**
4. Klicken Sie links in das Feld **`GCode File`**, löschen Sie den dortigen Beispieltext und fügen Sie Ihren eigenen G-Code mit `Strg + V` ein.
5. Klicken Sie auf den blauen Knopf **`Plot` (Zeichnen)** und unten auf **`Play` (Abspielen / Dreieck-Symbol)**.
6. **Wie Sie im NCViewer testen:**
   * Klicken Sie im linken Textfenster auf **irgendeine Zeile Ihres G-Codes** (z. B. `N120 G01 X80.000 Y0.000` oder `N310 G90 G83 X10.000 Y10.000 Z-12.000...`).
   * Sofort springt der **virtuelle Fräser im 3D-Fenster rechts** exakt an diese Stelle am Bauteil!

---

## 🖥️ Weg 3 (Mit dem offiziellen Autodesk-Plugin direkt in Antigravity IDE):

Wenn Sie im Bereich **Extensions (Erweiterungen)** (`Strg + Umschalt + X`) das Plugin **`Autodesk Fusion Post Processor Utility`** installiert haben:

1. Öffnen Sie [`src/mein_erster_post.cps`](file:///C:/Projekte/CNC/src/mein_erster_post.cps) im Editor.
2. Drücken Sie `Strg + Umschalt + P` (öffnet die **Befehlspalette / Command Palette**).
3. Tippen Sie `Post Process` ein und wählen Sie **`Autodesk Fusion Post Processor: Post Process`**.
4. Wählen Sie eine der mitgelieferten Beispiel-Dateien aus der Liste – sofort öffnet sich rechts ein zweites Fenster mit dem fertig übersetzten **G-Code**!

---

## 🎯 Konkrete Simulator-Prüfanleitung für JEDE einzelne Übung (Stufe 1 bis Stufe 10)

Hier steht für **jede Übung aus diesem Handbuch** ganz genau, worauf Sie im Simulator achten müssen, um zu prüfen, ob Sie alles richtig gemacht haben:

### 🔹 Test für Stufe 1 & Übung 5 (3D-Auftrags-Simulator im Browser):

1. Machen Sie im Windows-Explorer einen Doppelklick auf [kundenauftrag_01_flanschplatte/3d_auftrag_simulator.html](file:///C:/Projekte/CNC/kundenauftrag_01_flanschplatte/3d_auftrag_simulator.html).
2. **Was Sie im Simulator prüfen:**
   - Klicken Sie auf **`Rohteil (85×55×15) Ein/Aus`**: Sie sehen den gestrichelten Rohblock um das Fertigteil.
   - Beobachten Sie oben links die Anzeige **`POS (G54)`**: Wenn das Werkzeug in die 4 Löcher bohrt, muss die Anzeige bei `Z` bis auf **`-12.000`** herunterzählen.

### 🔹 Test für Stufe 2 / Basis-Übung A (Die 5 wichtigsten G-Code-Zeilen):

1. Öffnen Sie **`https://ncviewer.com`** und fügen Sie den Inhalt von [tests/output_expected.nc](file:///C:/Projekte/CNC/tests/output_expected.nc) ein.
2. Klicken Sie auf **`Plot`**.
3. **Was Sie im Simulator prüfen:**
   - Klicken Sie links im G-Code einzeln auf die Zeilen `N90 G00 Z2.000` (Fräser steht `2 mm` über der Ecke in der Luft), dann auf `N100 G01 Z-5.000` (Fräser taucht `5 mm` nach unten) und dann auf `N120 G01 X80.000 Y0.000` (Fräser fährt `80 mm` nach rechts). Sie sehen bei jedem Klick live im 3D-Bild, wohin das Werkzeug springt!

### 🔹 Test für Stufe 3 / Basis-Übung B („Hallo Welt“ Kommentar) & Stufe 4 / Übung 1 (Entwickler-Infoblock):

1. Ändern Sie in [`src/mein_erster_post.cps`](file:///C:/Projekte/CNC/src/mein_erster_post.cps#L44) Ihren Namen (oder fügen Sie in `onOpen()` Ihre `writeComment("HALLO WELT...")`-Zeile ein) und speichern Sie die Datei mit `Strg + S`.
2. Starten Sie im Terminal:

   ```powershell
   node tests/simuliere_post.js
   ```
3. **Was Sie prüfen:**
   - Schauen Sie in die ersten 10 Zeilen der Ausgabe im Terminal (oder in `tests/mein_generierter_gcode.nc`): Steht Ihr neuer Text in runden Klammern `(...)`?
   - Kopieren Sie den kompletten Text in **`https://ncviewer.com`** und klicken Sie auf **`Plot`**: Läuft die 3D-Simulation trotz Ihres neuen Textes ohne Fehlermeldung durch? *(Wenn Sie aus Versehen Klammern innerhalb von Klammern geschrieben hätten, würde ein echter CNC-Simulator sofort stoppen – unsere Funktion `writeComment()` schützt Sie davor!).*

### 🔹 Test für Stufe 5 / Übung 6 (Sicherer Rückzug `G53 Z0` & Tisch zur Tür `G53 Y0` am Programmende):

1. Öffnen Sie [tests/output_expected.nc](file:///C:/Projekte/CNC/tests/output_expected.nc) in **`https://ncviewer.com`** oder in [3d_auftrag_simulator.html](file:///C:/Projekte/CNC/kundenauftrag_01_flanschplatte/3d_auftrag_simulator.html).
2. Scrollen Sie im G-Code ganz nach unten zu den Zeilen `N360` bis `N410`:

   ```gcode
   N360 G00 Z15.000
   (--- SICHERES PROGRAMMENDE - SAFE FOOTER ---)
   N370 M09
   N380 G53 G00 Z0.000
   N390 M05
   N400 G53 G00 Y0.000
   N410 M30
   ```
3. **Was Sie im 3D-Simulator prüfen:**
   - Klicken Sie erst auf Zeile `N340 X10.000 Y40.000` (der Bohrer steckt noch im letzten Bohrloch hinten links).
   - Klicken Sie dann auf `N360 G00 Z15.000` und `N380 G53 G00 Z0.000`: Sie sehen im 3D-Fenster, wie der Bohrer **senkrecht nach oben aus dem Loch herausgezogen wird**, BEVOR er in Zeile `N400` in Richtung `Y0.000` (nach vorne zur Tür) fährt!
   - **Bonus-Experiment:** Ändern Sie in [`src/mein_erster_post.cps`](file:///C:/Projekte/CNC/src/mein_erster_post.cps#L92) bei `useG28SafeRetract` den Wert von `false` auf `true`, speichern Sie (`Strg + S`) und führen Sie `node tests/simuliere_post.js` aus. Jetzt steht am Ende statt `G53 G00 Z0.000` plötzlich `G28 G91 Z0.000`!

### 🔹 Test für Stufe 6 / Übung 7 (Eigenen Schalter `useChipConveyor` für Späneförderer `M31/M33` testen):

1. Bauen Sie den Schalter `useChipConveyor` wie in [Übung 7](#übung-7-eigenen-schalter-property-für-zusatzfunktionen-wie-blasluft-m07-oder-späneförderer-bauen) beschrieben in [`src/mein_erster_post.cps`](file:///C:/Projekte/CNC/src/mein_erster_post.cps) ein.
2. **Testlauf 1 (Schalter steht auf `value: false`):**  
   Führen Sie `node tests/simuliere_post.js` aus $\rightarrow$ Im erzeugten G-Code taucht **kein** `M31` und **kein** `M33` auf.
3. **Testlauf 2 (Schalter steht auf `value: true`):**  
   Ändern Sie `value: true`, speichern Sie (`Strg + S`) und führen Sie `node tests/simuliere_post.js` erneut aus $\rightarrow$ Jetzt erscheint oben im G-Code automatisch `M31` (Späneförderer ein) und unten vor `M30` automatisch `M33` (Späneförderer aus)!

### 🔹 Test für Stufe 7 / Übung 4 (3D-Modell `bauteil_1001.stl` in 3D-Software öffnen & prüfen):

1. Öffnen Sie die 3D-Datei [kundenauftrag_01_flanschplatte/bauteil_1001.stl](file:///C:/Projekte/CNC/kundenauftrag_01_flanschplatte/bauteil_1001.stl) im **Windows 3D-Viewer**, in **FreeCAD** oder in **Autodesk Fusion**.
2. Vergleichen Sie die Maße des 3D-Modells (`80 x 50 x 12 mm`) mit den Fräsbahnen in [kundenauftrag_01_flanschplatte/3d_auftrag_simulator.html](file:///C:/Projekte/CNC/kundenauftrag_01_flanschplatte/3d_auftrag_simulator.html).

### 🔹 Test für Stufe 8 / Übung 2 (Werkzeugliste `Tool Table`) & Stufe 9 / Übung 3 (`Z-MIN` Sicherheitsprüfung):

1. Führen Sie `node tests/simuliere_post.js` aus und kopieren Sie den erzeugten G-Code in **`https://ncviewer.com`**.
2. **Wie Sie im Simulator beweisen, dass Ihre `Z-MIN`-Rechnung in JavaScript stimmt:**
   - Ihr Header oben sagt: `(T01 | ... | Z-MIN=-5.000MM)` und `(T02 | ... | Z-MIN=-12.000MM)`.
   - Drehen Sie in **NCViewer** die 3D-Ansicht genau von der Seite (klicken Sie im NCViewer oben rechts auf den Ansichtswürfel **`Front` / Vorne**).
   - Jetzt sehen Sie die Fräsbahnen exakt von der Seite:
     - Die blaue Außenkontur von Werkzeug `T01` liegt exakt auf Höhe `-5.000 mm`.
     - Der blaue Kreis in der Mitte liegt auf Höhe `-3.000 mm`.
     - Die 4 Bohrlöcher von Werkzeug `T02` ragen am tiefsten nach unten bis auf `-12.000 mm`!
   - Damit haben Sie visuell im Simulator bewiesen, dass Ihre JavaScript-Funktion [`getToolMinimumZ(tool)`](file:///C:/Projekte/CNC/src/mein_erster_post.cps#L181-L195) auf den tausendstel Millimeter genau rechnet!


---

# 🟣 Teil 4: Fortgeschrittene Profi-Übungen für echte Online-Aufträge (Übung 9 bis Übung 16)

In diesem vierten Teil findest du die **Übungen 9 bis 16**, die dich vom Einsteiger zum vollwertigen **CAM- und Postprozessor-Profi für echte Online-Kundenaufträge *(Upwork, Fiverr, Malt & CAM-Systemhäuser)*** machen.

---

# Übung 9: Schnittdaten (`S` Drehzahl & `F` Vorschub) berechnen – Warum Aluminium, Baustahl und Edelstahl völlig andere Werte brauchen

### 📌 Spickzettel dieser Übung: Alle verwendeten Schnittdaten- & Technologie-Kennzeichen in Übung 9

| Kennzeichen | Fachbegriff & Erklärung | Bedeutung & Funktion in dieser Übung |
|---|---|---|
| **`v_c`** | **Schnittgeschwindigkeit *(Cutting Speed in $\text{m/min}$)*** | Umfangsgeschwindigkeit der Schneide am Werkstück *(Alu $300\,\text{m/min}$, Baustahl $160\,\text{m/min}$, Edelstahl $80\,\text{m/min}$)*. |
| **`S` / $n$** | **Spindeldrehzahl *(Spindle Speed in $\text{U/min}$)*** | Drehzahl der Spindel: $n = (v_c \times 1000) / (\pi \times D)$. Im G-Code: `S8000`. |
| **`F` / $v_f$**| **Vorschubgeschwindigkeit *(Feedrate in $\text{mm/min}$)*** | Verfahrgeschwindigkeit des Fräsers im Schnitt: $v_f = n \times z \times f_z$. Im G-Code: `F1200`. |
| **$f_z$** | **Zahnvorschub *(Feed per Tooth in $\text{mm}$)*** | Materialabtrag pro Schneidzahn und Umdrehung *(Alu $0{,}06\,\text{mm}$, Stahl $0{,}05\,\text{mm}$)*. |
| **$z$** | **Zähnezahl *(Number of Flutes)*** | Anzahl der wirksamen Schneiden am Fräser *(Alu meist 3 Zähne, Stahl meist 4–5 Zähne)*. |
| **`M03`** | **Spindel Rechtslauf EIN *(Spindle Clockwise)*** | Schaltet den Spindelmotor im Uhrzeigersinn ein. |
| **`M08`** | **Kühlmittel EIN *(Flood Coolant On)*** | Verhindert Überhitzung der Schneide und spült Späne fort. |

### 💡 Worum geht es in einfacher Sprache?

Wenn dir ein Online-Kunde ein 3D-Modell schickt, steht auf der Zeichnung immer der **Werkstoff *(das Material, z. B. Aluminium, Baustahl oder Edelstahl)***.
Der häufigste Anfängerfehler im CAM ist es, für Stahl dieselbe **Spindeldrehzahl (`S` – Umdrehungen pro Minute)** und denselben **Vorschub (`F` – Fahrgeschwindigkeit in Millimetern pro Minute)** wie für weiches Aluminium zu lassen:
* Fräst du **Edelstahl** mit Aluminium-Drehzahl (`S10000`), glüht der Fräser innerhalb von **2 Sekunden** rot auf und bricht sofort ab!
* Fräst du **Aluminium** mit langsamer Edelstahl-Drehzahl (`S1500`), klebt das weiche Aluminium an den Schneiden fest (**Aufbauschneide *(Materialverschweißung am Fräser)***).

### 📐 Die 2 einfachen Grundformeln der Zerspanung (Die jeder Ingenieur sofort versteht):

1. **Formel für die Spindeldrehzahl $n$ (`S` im G-Code):**
   $$n = \frac{v_c \cdot 1000}{\pi \cdot D}$$
   * $v_c$: **Schnittgeschwindigkeit *(Cutting Speed in $\text{m/min}$ – steht auf der Verpackung des Fräsers oder im Katalog)***.
   * $D$: **Durchmesser des Fräsers *(in $\text{mm}$, z. B. $10\,\text{mm}$)***.
   * $\pi$: Kreiszahl ($\approx 3{,}1416$).

2. **Formel für den Vorschub $v_f$ (`F` im G-Code):**
   $$v_f = n \cdot z \cdot f_z$$
   * $n$: Die eben berechnete **Drehzahl (`S`)**.
   * $z$: **Anzahl der Schneiden (Zähne)** am Fräser *(für Alu meist $z=3$, für Stahl meist $z=4$ oder $z=5$)*.
   * $f_z$: **Zahnvorschub *(Feed per Tooth in $\text{mm/Zahn}$ – wie viel Millimeter Metall jede einzelne Schneide pro Umdrehung abnimmt)***.

### 📊 Praxis-Vergleich für einen $\varnothing\,10\,\text{mm}$ Vollhartmetall-Schaftfräser (VHM):

| Werkstoff (Material) | Schnittgeschwindigkeit $v_c$ [m/min] | Schneiden $z$ | Zahnvorschub $f_z$ [mm] | Berechnete Drehzahl `S` [U/min] | Berechneter Vorschub `F` [mm/min] |
| :--- | :--- :---: | :---: | :---: | :---: | :---: |
| **1. Aluminium (`EN AW-6061 / 7075`)** | $300\,\text{m/min}$ | $3$ | $0{,}06\,\text{mm}$ | **`S9550`** | **`F1720`** |
| **2. Baustahl / Vergütungsstahl (`S235 / 42CrMo4`)** | $160\,\text{m/min}$ | $4$ | $0{,}05\,\text{mm}$ | **`S5090`** | **`F1020`** |
| **3. Edelstahl rostfrei (`1.4301 / V2A`)** | $80\,\text{m/min}$ | $4$ | $0{,}035\,\text{mm}$ | **`S2550`** | **`F357`** |

### 🛠️ Wo im Code wird das gemacht?

Für diese Übung stehen Ihnen die folgenden Dateien zur Verfügung:
1. **Als eigene, kompakte Übungs-Datei:**  
   [`uebungen/uebung_09_schnittdaten_check.cps`](file:///C:/Projekte/CNC/uebungen/uebung_09_schnittdaten_check.cps) – Prüft die Schnittdaten (vc, Drehzahl, Vorschub) und gibt Sicherheits-Warnungen aus.
2. **Im Haupt-Postprozessor:**  
   [`src/mein_erster_post.cps`](file:///C:/Projekte/CNC/src/mein_erster_post.cps)

### 🖥️ Schritt-für-Schritt: So öffnen, starten und simulieren Sie Übung 9 in Visual Studio Code (VSC)

#### Schritt 1: Datei in Visual Studio Code öffnen
1. Drücken Sie in VS Code `Strg + P`.
2. Tippen Sie ein: `uebung_09_schnittdaten_check.cps` und drücken Sie `Enter`.

#### Schritt 2: Programm im Terminal ausführen & testen
1. Öffnen Sie das Terminal mit ``Strg + ` ``.
2. Führen Sie aus:
   ```powershell
   node tests/simuliere_post.js uebungen/uebung_09_schnittdaten_check.cps
   ```
3. Der Simulator berechnet die Schnittgeschwindigkeiten für die Werkzeuge.

#### Schritt 3: Den erzeugten G-Code ansehen
* Öffnen Sie [`tests/mein_generierter_gcode.nc`](file:///C:/Projekte/CNC/tests/mein_generierter_gcode.nc) mit `Strg + P`.
* Achten Sie auf den Kommentar: `(TECHNOLOGIE-CHECK: SCHNITTGESCHWINDIGKEIT VC = ...)`.

#### Schritt 4: 3D-Simulation visuell prüfen
* Kopieren Sie den G-Code in [https://ncviewer.com](https://ncviewer.com).

---

### 🛠️ Automatische Sicherheitsprüfung im JavaScript-Postprozessor:
Du kannst in deinem Postprozessor (`onSection()`) eine automatische Schnittdaten-Berechnung und Sicherheitswarnung einbauen, falls im CAM eine zu hohe Schnittgeschwindigkeit eingegeben wurde:

```javascript
// Sicherheitsprüfung in onSection(): Maximale Schnittgeschwindigkeit vc berechnen und prüfen
var tool = currentSection.getTool();
// Formel: vc = (pi * Werkzeugdurchmesser * Spindeldrehzahl) / 1000 in m/min
var vc = (Math.PI * tool.diameter * spindleSpeed) / 1000.0;
writeComment("TECHNOLOGIE-CHECK: SCHNITTGESCHWINDIGKEIT VC = " + Math.round(vc) + " M/MIN");

// Warnung bei kritischer Überschreitung (z. B. vc > 400 m/min bei Schaftfräsern):
if (vc > 400 && tool.diameter > 6) {
  writeComment("ACHTUNG: SCHNITTGESCHWINDIGKEIT SEHR HOCH! WERKZEUGVERSCHLEISS PRUEFEN!");
}
```

### ✅ So sieht das Ergebnis im fertigen G-Code aus:

```gcode
(OPERATION 1: AUSSENKONTUR SCHRUPPEN ALUMINIUM)
(TECHNOLOGIE-CHECK: SCHNITTGESCHWINDIGKEIT VC = 251 M/MIN)
N20 T01 M06 (T01 SCHAFTFRAESER D10MM VHM | M06 WERKZEUGWECHSEL)
N30 G54 (G54 WERKSTUECK-NULLPUNKT AKTIVIEREN)
N40 S8000 M03 (S8000 SPINDELDREHZAHL 8000 U/MIN | M03 SPINDEL RECHTSLAUF EIN)
N50 G43 H01 Z15.000 M08 (G43 LAENGENKORREKTUR | H01 SPEICHER 1 | Z15 FREIFAHRHOEHE | M08 KUEHLMITTEL AN)
N60 G00 X-10.000 Y-10.000 (G00 EILGANG VOR DAS MATERIAL)
N70 G00 Z2.000 (G00 EILGANG AUF SICHERHEITSABSTAND 2MM)
N80 G01 Z-5.000 F500 (G01 EINTAUCHEN MIT VORSCHUB 500 MM/MIN)
N90 G01 X0.000 Y0.000 F1200 (G01 FRAESVORSCHUB 1200 MM/MIN ENTSPRICHT FZ = 0.05 MM/ZAHN BEI 3 ZAEHNEN)
```

### 🛡️ Prüfliste dieser Übung: Wann ist Übung 9 zu 100 % bestanden?

| Prüfpunkt | Was muss im Code / Simulator zu sehen sein? | Bestanden? |
| :--- | :--- | :---: |
| **1. vc-Berechnung aktiv** | Der Postprozessor schreibt `(TECHNOLOGIE-CHECK: SCHNITTGESCHWINDIGKEIT VC = ... M/MIN)` vor die Operation. | [ ] |
| **2. Plausibilität Aluminium** | Für $\varnothing 10\,\text{mm}$ und `S8000` liegt $v_c$ bei ca. $251\,\text{m/min}$ *(voll im grünen Bereich für Alu)*. | [ ] |
| **3. Vorschub passend zu Zähnen** | Der Vorschub `F1200` ergibt bei 3 Zähnen $f_z = 0{,}05\,\text{mm/Zahn}$, was für Schaftfräser optimal ist. | [ ] |
| **4. Keine Werkzeugüberlastung** | Keine Spindeldrehzahlen über der Maschinenobergrenze *(z. B. max. $12.000\,\text{U/min}$)*. | [ ] |

---

# Übung 10: Die 2. Aufspannung (`G55` / `OP20`) – Wie das 3D-Bauteil umgedreht und der Restboden auf der Rückseite plangefräst wird

### 📌 Spickzettel dieser Übung: Alle verwendeten G-Code- & M-Code-Kennzeichen in Übung 10

| Kennzeichen | Fachbegriff & Erklärung | Bedeutung & Funktion in dieser Übung |
|---|---|---|
| **`G54`** | **1. Werkstück-Nullpunkt *(Work Coordinate System OP10)*** | Nullpunkt für die erste Seite *(Oberseite, Kontur, Bohrungen)*. |
| **`G55`** | **2. Werkstück-Nullpunkt *(Work Coordinate System OP20)*** | Zweiter Nullpunkt für die Rückseite nach dem Umspannen *(im zweiten Schraubstock)*. |
| **`M00`** | **Programmstopp Zwingend *(Mandatory Program Stop)*** | Hält die CNC-Maschine an, Spindel stoppt, wartet auf Bediener-Quittierung *(Bauteil wenden)*. |
| **`T01 M06`** | **Werkzeugwechsel *(Tool Change)*** | Wechselt das Planfräswerkzeug ein. |
| **`S8000 M03`** | **Spindelstart *(Spindle On Clockwise)*** | Drehzahl $8.000\,\text{U/min}$ im Uhrzeigersinn. |
| **`G43 H01`** | **Längenkorrektur *(Length Offset 1)*** | Verrechnet die Werkzeuglänge aus Speicher 1. |
| **`M08`** | **Kühlmittel EIN *(Coolant On)*** | Spült Späne weg und kühlt beim Planfräsen. |
| **`G01 Z0.0`** | **Arbeitsvorschub auf Fertigmaß *(Linear Feed to Z0)*** | Fräst den $3\,\text{mm}$ dicken Spannrand exakt auf Endmaß $12{,}0\,\text{mm}$ ab. |

### 💡 Worum geht es in einfacher Sprache?

In **Übung 4** haben wir unsere Flanschplatte (`12 mm` dick) aus einem `15 mm` dicken Aluminium-Rohblock gefräst.
Warum mussten wir einen `15 mm` dicken Block nehmen, wenn das fertige Teil nur `12 mm` hoch ist?
* Weil der **Maschinenschraubstock *(Spannmittel)*** das Bauteil ganz unten an den letzten **`3 Millimetern` (`Spannrand`)** festhalten muss! Würde der Fräser in der ersten Aufspannung (**`OP10`**) bis ganz nach unten fräsen, würde er in die Stahlbacken des Schraubstocks fräsen.
* Deshalb läuft fast jedes CNC-Bauteil in der Industrie in **2 Aufspannungen**:
  1. **1. Aufspannung (`OP10` mit Nullpunkt `G54`):** Oberseite planfräsen, Außenkontur bis `12,5 mm` Tiefe umfräsen, Taschen und Löcher fertigen. Unten bleibt ein `3 mm` dicker „Hutrand“ stehen.
  2. **Bauteil umdrehen (`OP20` mit zweitem Nullpunkt `G55`):** Der Arbeiter nimmt das Teil aus dem Schraubstock, dreht es auf den Kopf, spannt es in einen zweiten Schraubstock (mit Nullpunkt **`G55`**) und fräst den übrig gebliebenen `3 mm` Boden weg + entgratet die unteren Kanten!

### 🛠️ Wo im Code wird das gemacht?

Für diese Übung stehen Ihnen die folgenden Dateien zur Verfügung:
1. **Als eigene, kompakte Übungs-Datei:**  
   [`uebungen/uebung_10_zweite_aufspannung_g55.cps`](file:///C:/Projekte/CNC/uebungen/uebung_10_zweite_aufspannung_g55.cps) – Erzeugt den automatischen Programmstopp `M00` und schaltet auf `G55` um.
2. **Im Haupt-Postprozessor:**  
   [`src/mein_erster_post.cps`](file:///C:/Projekte/CNC/src/mein_erster_post.cps)

### 🖥️ Schritt-für-Schritt: So öffnen, bearbeiten, starten und simulieren Sie Übung 10 in Visual Studio Code (VSC)

#### Schritt 1: Datei in Visual Studio Code öffnen
1. Drücken Sie `Strg + P` in VS Code.
2. Tippen Sie ein: `uebung_10_zweite_aufspannung_g55.cps` und drücken Sie `Enter`.

#### Schritt 2: Programm im Terminal ausführen & testen
1. Öffnen Sie das Terminal mit ``Strg + ` ``.
2. Führen Sie aus:
   ```powershell
   node tests/simuliere_post.js uebungen/uebung_10_zweite_aufspannung_g55.cps
   ```
3. Der Simulator gibt die 1. Aufspannung (`G54`), den Stopp `M00` und die 2. Aufspannung (`G55`) aus.

#### Schritt 3: Den erzeugten G-Code ansehen
* Öffnen Sie [`tests/mein_generierter_gcode.nc`](file:///C:/Projekte/CNC/tests/mein_generierter_gcode.nc).
* Suchen Sie nach dem Befehl `M00` und dem nachfolgenden Aufruf `G55`.

#### Schritt 4: 3D-Simulation visuell prüfen
* Kopieren Sie den Code in [https://ncviewer.com](https://ncviewer.com) und beobachten Sie die Fräsbahn der Planbearbeitung.

---

### 🛠️ Wie steuert der JavaScript-Postprozessor den Nullpunktwechsel in `onSection()`?

```javascript
// Automatische Erkennung des Werkstück-Koordinatensystems (WCS):
// currentSection.workOffset: 1 = G54, 2 = G55, 3 = G56, usw.
var wcsNumber = currentSection.workOffset;
if (wcsNumber == 2) {
  // Wenn Aufspannung 2 (G55) beginnt, zwingenden Programmstopp einfügen:
  writeComment("==================================================");
  writeComment("AUFSPANNUNG 2 - OP20: RUECKSEITE PLANFRAESEN");
  writeComment("==================================================");
  // M00 = Maschine stoppt Spindel und Vorschub, wartet auf Bediener-Startknopf
  writeBlock(mFormat.format(0));
  // G55 = Zweiter Nullpunkt
  writeBlock(gFormat.format(55));
} else {
  // G54 = Erster Standard-Nullpunkt
  writeBlock(gFormat.format(54));
}
```

### ✅ So sieht der Wechsel von Aufspannung 1 (`G54`) zu Aufspannung 2 (`G55`) im G-Code aus:

```gcode
(==================================================)
(AUFSPANNUNG 2 - OP20: RUECKSEITE PLANFRAESEN AUF 12.0 MM)
(NULLPUNKT: G55 - LINKER SCHRAUBSTOCK / Z0 = FERTIGMASS)
(==================================================)
N500 M00 (M00 PROGRAMMSTOPP: BAUTEIL UMDREHEN UND IN SCHRAUBSTOCK 2 SPANNEN!)
N510 T01 M06 (T01 SCHAFTFRAESER 10MM VHM | M06 AUTOMATISCHER WERKZEUGWECHSEL)
N520 S8000 M03 (S8000 SPINDELDREHZAHL 8000 U/MIN | M03 SPINDEL RECHTSLAUF EIN)
N530 G55 (G55 ZWEITEN WERKSTUECK-NULLPUNKT OP20 AKTIVIEREN)
N540 G00 X-10.000 Y25.000 (G00 EILGANG VOR DIE LINKE BAUTEILKANTE)
N550 G43 H01 Z15.000 M08 (G43 LAENGENKORREKTUR | H01 SPEICHER 1 | Z15 FREIFAHRHOEHE | M08 KUEHLMITTEL AN)
N560 G01 Z0.000 F1500 (G01 EINTAUCHEN AUF FERTIGHOEHE Z0 MIT VORSCHUB 1500 MM/MIN)
N570 G01 X90.000 F1200 (G01 PLANFRAESEN UEBER DAS BAUTEIL BIS X90 MIT VORSCHUB 1200 MM/MIN)
```

* **Was macht `M00` *(Programmstopp / Mandatory Stop)***?  
  Die Maschine hält automatisch an, schaltet die Spindel ab und wartet, bis der Bediener das Bauteil im Schraubstock gewendet hat und wieder auf den grünen **Start-Knopf (`Cycle Start`)** drückt!

### 🛡️ Prüfliste dieser Übung: Wann ist Übung 10 zu 100 % bestanden?

| Prüfpunkt | Was muss im Code / Simulator zu sehen sein? | Bestanden? |
| :--- | :--- | :---: |
| **1. Programmstopp M00** | Vor Beginn der Operation `OP20` steht `M00`, damit die Maschine beim Umspannen sicher stoppt. | [ ] |
| **2. Nullpunkt G55 aktiviert** | Vor der ersten Verfahrbewegung der Rückseite wird `G55` im Maschinencode aufgerufen. | [ ] |
| **3. Sichere Freifahrhöhe** | Vor und nach `M00` befindet sich das Werkzeug auf sicherer Höhe `Z15.000` oder `G53 Z0.`. | [ ] |
| **4. Planfräsen auf Z0** | Die Fräsbahn schneidet auf Höhe `Z0.000` den $3\,\text{mm}$ Restspannrand sauber ab. | [ ] |

---

# Übung 11: Gewindebohren (`G84` Rigid Tapping) – `M6`- und `M8`-Schraubengewinde ohne Werkzeugbruch programmieren (`F = S × Steigung`)

### 📌 Spickzettel dieser Übung: Alle verwendeten Gewindebohr- & Synchron-Kennzeichen in Übung 11

| Kennzeichen | Fachbegriff & Erklärung | Bedeutung & Funktion in dieser Übung |
|---|---|---|
| **`M29 S...`** | **Starres Gewindebohren EIN *(Rigid Tapping Mode)*** | Schaltet Fanuc/Haas in den Synchronmodus: Spindel-Drehwinkel und Z-Achsenantrieb werden elektronisch starr gekoppelt. |
| **`G84`** | **Gewindebohrzyklus *(Right-Hand Tapping Cycle)*** | Fährt mit Rechtslauf bis Endtiefe $Z$, stoppt, schaltet automatisch auf Linkslauf `M04` um und fährt auf Rückzugsebene heraus. |
| **`G98`** | **Rückzug auf Ausgangsebene *(Return to Initial Level)*** | Zieht nach dem Gewindebohren ganz nach oben auf die sichere Ausgangshöhe *(z. B. `Z15.000`)* zurück. |
| **`P` / Steigung**| **Gewindesteigung *(Thread Pitch in $\text{mm}$)*** | Steigung des Gewindes *(M6 = $1{,}0\,\text{mm}$, M8 = $1{,}25\,\text{mm}$, M10 = $1{,}5\,\text{mm}$)*. |
| **`F = S × P`** | **Synchroner Gewindevorschub *(Synchronous Feedrate)*** | Verfahrgeschwindigkeit der Z-Achse in $\text{mm/min}$. Bei $S=600\,\text{U/min}$ und $P=1{,}25\,\text{mm}$ zwingend $F=750\,\text{mm/min}$. |
| **`R...`** | **Rückzugsebene *(Reference Return Plane)*** | Höhenposition kurz vor dem Bauteil *(z. B. `R2.000`)*, ab der der Arbeitsvorschub synchron einsetzt. |
| **`G80`** | **Bohrzyklus abwählen *(Cancel Modal Canned Cycle)*** | Beendet den Zyklus `G84` nach dem letzten Gewindeloch sicher. |

### 💡 Worum geht es in einfacher Sprache?

In fast jedes Metallbauteil müssen später Schrauben gedreht werden (z. B. ein **`M8`-Gewinde** für eine 8-Millimeter-Schraube).
Beim **Gewindebohren (`G84` – Synchron-Gewindebohren / Rigid Tapping)** fährt ein **Gewindebohrer (`Tap`)** in das vorgebohrte Loch hinein, stoppt unten am Grund des Lochs, **dreht die Spindel rückwärts (`M04`)** und schraubt sich wieder heraus.

> **⚠️ Lebenswichtige Regel gegen Werkzeugbruch beim Gewindebohren:**  
> Beim Gewindebohren darf man den Vorschub `F` **NIEMALS** frei schätzen!  
> Wenn sich der Gewindebohrer pro Umdrehung um genau eine **Gewindesteigung $P$ *(Abstand von Gewindegang zu Gewindegang)*** nach unten schraubt, muss der Tisch der Maschine **millimetergenau synchron** mitfahren:
> $$\mathbf{F = S \times P}$$
> *(Vorschub `F` = Spindeldrehzahl `S` mal Gewindesteigung $P$ in $\text{mm}$)*

### 📊 Die wichtigsten Metrischen Regelgewinde (ISO-Standard) zum Nachschlagen:

| Gewinde-Größe | Kernloch-Bohrer $\varnothing$ *(Vorbohr-Durchmesser!)* | Gewindesteigung $P$ [mm] | Beispiel-Drehzahl `S` [U/min] | Zwingend exakter Vorschub `F` ($S \times P$) |
| :--- | :---: | :---: | :---: | :---: |
| **`M5`** | $\varnothing\,4{,}2\,\text{mm}$ | $0{,}80\,\text{mm}$ | `S800` | **`F640`** ($800 \times 0{,}8$) |
| **`M6`** | $\varnothing\,5{,}0\,\text{mm}$ | $1{,}00\,\text{mm}$ | `S800` | **`F800`** ($800 \times 1{,}0$) |
| **`M8`** | $\varnothing\,6{,}8\,\text{mm}$ | $1{,}25\,\text{mm}$ | `S600` | **`F750`** ($600 \times 1{,}25$) |
| **`M10`** | $\varnothing\,8{,}5\,\text{mm}$ | $1{,}50\,\text{mm}$ | `S500` | **`F750`** ($500 \times 1{,}5$) |
| **`M12`** | $\varnothing\,10{,}2\,\text{mm}$ | $1{,}75\,\text{mm}$ | `S400` | **`F700`** ($400 \times 1{,}75$) |

### 🛠️ Wo im Code wird das gemacht?

Für diese Übung stehen Ihnen die folgenden Dateien zur Verfügung:
1. **Als eigene, kompakte Übungs-Datei:**  
   [`uebungen/uebung_11_gewindebohren_g84.cps`](file:///C:/Projekte/CNC/uebungen/uebung_11_gewindebohren_g84.cps) – Berechnet den Synchron-Vorschub $F = S \times P$ und erzeugt den Zyklus `G84` mit Spindel-Rückzug `M29`.
2. **Im Haupt-Postprozessor:**  
   [`src/mein_erster_post.cps`](file:///C:/Projekte/CNC/src/mein_erster_post.cps)

### 🖥️ Schritt-für-Schritt: So öffnen, starten und simulieren Sie Übung 11 in Visual Studio Code (VSC)

#### Schritt 1: Datei in Visual Studio Code öffnen
1. Drücken Sie in VS Code `Strg + P`.
2. Tippen Sie ein: `uebung_11_gewindebohren_g84.cps` und drücken Sie `Enter`.

#### Schritt 2: Programm im Terminal ausführen & testen
1. Öffnen Sie das Terminal mit ``Strg + ` ``.
2. Führen Sie aus:
   ```powershell
   node tests/simuliere_post.js uebungen/uebung_11_gewindebohren_g84.cps
   ```
3. Der Simulator berechnet exakt den Vorschub für Gewinde.

#### Schritt 3: Den erzeugten G-Code ansehen
* Öffnen Sie [`tests/mein_generierter_gcode.nc`](file:///C:/Projekte/CNC/tests/mein_generierter_gcode.nc) mit `Strg + P`.
* Kontrollieren Sie den Gewindebohrzyklus `G84` und den Vorschub `F`.

#### Schritt 4: 3D-Simulation visuell prüfen
* Kopieren Sie den G-Code in [https://ncviewer.com](https://ncviewer.com).

---

### 🛠️ Wie wird `G84` im JavaScript-Postprozessor (`onCyclePoint`) ausgegeben?

```javascript
case "tapping":
case "right-tapping":
  // 1. Exakte Berechnung des Synchron-Vorschubs: F = Drehzahl S * Gewindesteigung (tool.threadPitch)
  var tapFeedrate = spindleSpeed * tool.threadPitch;

  // 2. Starres Gewindebohren einschalten (M29 bei Fanuc/Haas):
  writeBlock(mFormat.format(29), sOutput.format(spindleSpeed));

  // 3. Modalen Zyklus G84 mit Rückzugsebene R und Vorschub F schreiben:
  // G98 = Rueckzug auf Ausgangshoehe Z15.000
  // G90 = Absolutmass-Programmierung
  // G84 = Gewindebohrzyklus Rechtsgewinde
  writeBlock(
    gRetractModal.format(98),
    gAbsIncModal.format(90),
    gCycleModal.format(84),
    getCommonCycle(x, y, z, cycle.retract),
    "F" + feedFormat.format(tapFeedrate)
  );
  break;
```

### ✅ So sieht das Ergebnis im fertigen G-Code aus:

```gcode
(OPERATION: GEWINDEBOHREN 4X M8 TIEFE 10MM)
N240 T03 M06 (T03 GEWINDEBOHRER M8 STEIGUNG 1.25MM VHM | M06 AUTOMATISCHER WERKZEUGWECHSEL)
N250 G54 (G54 WERKSTUECK-NULLPUNKT AKTIVIEREN)
N260 M29 S600 (M29 SYNCHRON-GEWINDEBOHREN STARRES TAPPING MIT 600 U/MIN)
N270 G43 H03 Z15.000 M08 (G43 LAENGENKORREKTUR | H03 SPEICHER 3 | Z15 FREIFAHRHOEHE | M08 KUEHLMITTEL AN)
N280 G00 X10.000 Y10.000 (G00 EILGANG ZUR ERSTEN BOHRUNG)
N290 G98 G90 G84 X10.000 Y10.000 Z-10.000 R2.000 F750 (G98 RUECKZUG Z15 | G90 ABSOLUT | G84 GEWINDEZYKLUS | ENDTIEFE Z-10 | R2 VORPOSITION | F750 SYNCHRONVORSCHUB 600*1.25)
N300 X70.000 Y10.000 (GEWINDE 2 UNTEN RECHTS MIT GLEICHEM ZYKLUS)
N310 X70.000 Y40.000 (GEWINDE 3 OBEN RECHTS MIT GLEICHEM ZYKLUS)
N320 X10.000 Y40.000 (GEWINDE 4 OBEN LINKS MIT GLEICHEM ZYKLUS)
N330 G80 (G80 GEWINDEBOHRZYKLUS G84 SICHER ABBRECHEN UND DEAKTIVIEREN)
N340 G00 Z15.000 M09 (G00 EILGANG AUF SICHERHEITSHOEHE | M09 KUEHLMITTEL AUS)
```

### 🛡️ Prüfliste dieser Übung: Wann ist Übung 11 zu 100 % bestanden?

| Prüfpunkt | Was muss im Code / Simulator zu sehen sein? | Bestanden? |
| :--- | :--- | :---: |
| **1. Synchronformel F = S × P** | Der Vorschub `F` entspricht exakt $\text{Drehzahl } S \times \text{Steigung } P$ *(z. B. $600 \times 1{,}25 = 750$)*. | [ ] |
| **2. Rigid Tapping M29 aktiv** | Vor dem Zyklus `G84` wird `M29 S...` ausgegeben, damit die Steuerung Z-Achse und Spindel elektronisch koppelt. | [ ] |
| **3. Rückzugsebene R** | `R2.000` liegt mindestens $2\,\text{mm}$ über dem Bauteil in der Luft vor Beginn des Gewindeschnitts. | [ ] |
| **4. Zyklus-Abwahl G80** | Nach dem letzten Gewindeloch wird der Zyklus mit `G80` sicher deaktiviert, bevor freigefahren wird. | [ ] |

---

# Übung 12: Werkzeugradiuskorrektur (`G41` / `G42` / `G40`) – Wie der Kunde an der Maschine `0,01 mm` Genauigkeit für Passungen einstellt

### 📌 Spickzettel dieser Übung: Alle verwendeten Radiuskorrektur-Kennzeichen in Übung 12

| Kennzeichen | Fachbegriff & Erklärung | Bedeutung & Funktion in dieser Übung |
|---|---|---|
| **`G41`** | **Fräserradiuskorrektur LINKS *(Cutter Compensation Left)*** | Verschiebt die Fräsermitte um den Werkzeugradius nach links von der programmierten Kontur *(Gleichlauffräsen)*. |
| **`G42`** | **Fräserradiuskorrektur RECHTS *(Cutter Compensation Right)*** | Verschiebt die Fräsermitte nach rechts von der Kontur *(Gegenlauffräsen)*. |
| **`G40`** | **Radiuskorrektur ABWÄHLEN *(Cancel Cutter Compensation)*** | Schaltet jede aktive Bahnkorrektur sicher aus *(muss bei linearer Abfahrbewegung erfolgen!)*. |
| **`D...` / `D01`**| **Korrekturspeicher-Register *(Diameter Compensation Offset)*** | Gibt an, aus welchem Speicher an der Steuerung das Verschleißmaß gelesen wird *(z. B. `D01` zu `T01`)*. |
| **`G03`** | **Kreisinterpolation *(Circular Move CCW)*** | Fräst die Passungs-Kreistasche $\varnothing 30\,\text{H7}$ gegen den Uhrzeigersinn. |
| **`I-15.000`** | **Kreismittelpunkts-Vektor in X *(Incremental Arc Center X)*** | Relativer Abstand vom Startpunkt zum Kreismittelpunkt $(15\,\text{mm}$ nach links in der X-Achse$)$. |

### 💡 Worum geht es in einfacher Sprache?

Ein neuer $\varnothing\,10{,}00\,\text{mm}$ Fräser nutzt sich beim Fräsen von Stahl langsam ab – nach einer Stunde hat er vielleicht nur noch $\varnothing\,9{,}96\,\text{mm}$.
Wenn der Kunde auf der Zeichnung eine hochpräzise **Passung *(z. B. $\varnothing\,30\,\text{H7}$, die auf $0{,}02\,\text{mm}$ genau sein muss)*** hat, will er nicht wegen $0{,}04\,\text{mm}$ Verschleiß bei dir anrufen, damit du ein neues CAM-Programm schickst!

**Die Lösung heißt Werkzeugradiuskorrektur (`G41` / `G42` bei Fanuc/Siemens bzw. `RL` / `RR` bei Heidenhain):**
* **`G41` *(Cutter Compensation Left)***: Schaltet die Korrektur **links** von der Fahrtrichtung ein (Standard beim **Gleichlauffräsen *(Climb Milling)***).
* **`G42` *(Cutter Compensation Right)***: Schaltet die Korrektur **rechts** von der Fahrtrichtung ein.
* **`G40` *(Cancel Cutter Compensation)***: Schaltet die Korrektur nach dem Schlichtschnitt wieder **aus**.

### 🛠️ Wo im Code wird das gemacht?

Für diese Übung stehen Ihnen die folgenden Dateien zur Verfügung:
1. **Als eigene, kompakte Übungs-Datei:**  
   [`uebungen/uebung_12_radiuskorrektur_g41.cps`](file:///C:/Projekte/CNC/uebungen/uebung_12_radiuskorrektur_g41.cps) – Enthält die korrekte An- und Abfahrlogik für `G41` und `G40`.
2. **Im Haupt-Postprozessor:**  
   [`src/mein_erster_post.cps`](file:///C:/Projekte/CNC/src/mein_erster_post.cps)

### 🖥️ Schritt-für-Schritt: So öffnen, bearbeiten, starten und simulieren Sie Übung 12 in Visual Studio Code (VSC)

#### Schritt 1: Datei in Visual Studio Code öffnen
1. Drücken Sie in VS Code `Strg + P`.
2. Tippen Sie ein: `uebung_12_radiuskorrektur_g41.cps` und drücken Sie `Enter`.

#### Schritt 2: Programm im Terminal ausführen & testen
1. Öffnen Sie das Terminal mit ``Strg + ` ``.
2. Führen Sie aus:
   ```powershell
   node tests/simuliere_post.js uebungen/uebung_12_radiuskorrektur_g41.cps
   ```
3. Der Simulator erzeugt die Schlichtkontur mit Radiuskorrektur.

#### Schritt 3: Den erzeugten G-Code ansehen
* Öffnen Sie [`tests/mein_generierter_gcode.nc`](file:///C:/Projekte/CNC/tests/mein_generierter_gcode.nc) mit `Strg + P`.
* Achten Sie auf `G41 D...` bei der Anfahrbewegung und `G40` beim Verlassen des Bauteils.

#### Schritt 4: 3D-Simulation visuell prüfen
* Kopieren Sie den G-Code in [https://ncviewer.com](https://ncviewer.com) und prüfen Sie die Kreisbahnen.

---

### 🛠️ Wie steuert der JavaScript-Postprozessor (`onLinear`) die Radiuskorrektur?

```javascript
// In onLinear() wird die Radiuskorrektur automatisch bei der Anfahrbewegung aktiviert:
if (pendingRadiusCompensation >= 0) {
  // G41 = Links / G42 = Rechts / G40 = Aus
  var compCode = (pendingRadiusCompensation == RADIUS_COMPENSATION_LEFT) ? 41 :
                 (pendingRadiusCompensation == RADIUS_COMPENSATION_RIGHT) ? 42 : 40;
  
  if (compCode != 40) {
    // Einschalten mit Korrekturspeicher-Nummer D... (entspricht Werkzeugnummer tool.number):
    writeBlock(
      gFormat.format(compCode),
      "D" + ("0" + tool.number).slice(-2),
      gMotionModal.format(1),
      xOutput.format(x), yOutput.format(y), feedOutput.format(feed)
    );
  } else {
    // Ausschalten mit G40 bei der Abfahrbewegung:
    writeBlock(gFormat.format(40), gMotionModal.format(1), xOutput.format(x), yOutput.format(y), feedOutput.format(feed));
  }
  pendingRadiusCompensation = -1;
}
```

### ✅ So sieht eine saubere Schlicht-Operation mit `G41` und `G40` im G-Code aus:

```gcode
(--- SCHLICHTEN KREISTASCHE D30 H7 MIT WERKZEUGRADIUSKORREKTUR G41 ---)
N200 G00 X40.000 Y25.000 (G00 EILGANG ZUR TASCHENMITTE BEI X40 Y25)
N210 G01 Z-3.000 F500    (G01 EINTAUCHEN AUF TASCHENTIEFE -3MM MIT VORSCHUB 500 MM/MIN)
N220 G41 D01 G01 X55.000 Y25.000 F800 (G41 RADIUSKORREKTUR LINKS EIN | D01 REGISTER 1 | LINEARE ANFAHRBAHN X55 | F800 VORSCHUB)
N230 G03 X55.000 Y25.000 I-15.000 J0.000 (G03 VOLLKREIS GEGEN UHRZEIGERSINN FRAESEN | RADIUS 15MM DURCH I-15)
N240 G40 G01 X40.000 Y25.000 F1000 (G40 RADIUSKORREKTUR AUSSCHALTEN | LINEARE ABFAHRBAHN ZUR TASCHENMITTE | F1000 VORSCHUB)
N250 G00 Z15.000 (G00 EILGANG SENKRECHT AUF SICHERHEITSHOEHE 15MM)
```

Jetzt kann der Maschinenbediener direkt an seinem Bildschirm in der Werkzeughalter-Tabelle (`D01`) einfach `-0.02 mm` eintippen – und die Tasche wird sofort um zwei Hundertstel Millimeter größer, ohne dass dein Programm geändert werden muss!

### 🛡️ Prüfliste dieser Übung: Wann ist Übung 12 zu 100 % bestanden?

| Prüfpunkt | Was muss im Code / Simulator zu sehen sein? | Bestanden? |
| :--- | :--- | :---: |
| **1. Anfahrbewegung mit G41** | `G41 D01` wird auf einer linearen Anfahrbewegung vor Konturkontakt aktiviert. | [ ] |
| **2. Korrekturspeicher D** | Das Register `D01` stimmt mit der aktuellen Werkzeugnummer `T01` überein. | [ ] |
| **3. Vollkreisbahn G03** | Die Passung $\varnothing 30\,\text{mm}$ wird kreisförmig mit Mittelpunkts-Vektor `I-15.000` abgefahren. | [ ] |
| **4. Sichere Abwahl G40** | Beim Verlassen der Wandung wird die Korrektur mit `G40` auf linearer Bahn wieder ausgeschaltet. | [ ] |

---

# Übung 13: Echte 3D-Freiformflächen – `3D Adaptive Clearing` (Wirbelfräsen) & `3D-Schlichten` mit Kugelfräser (`Ball End Mill`)

### 📌 Spickzettel dieser Übung: Alle verwendeten 3D-Freiform- & Kugelfräser-Kennzeichen in Übung 13

| Kennzeichen | Fachbegriff & Erklärung | Bedeutung & Funktion in dieser Übung |
|---|---|---|
| **`TOOL_MILLING_END_BALL`**| **Werkzeugtyp Kugelfräser *(Ball End Mill)*** | Vollradiusfräser mit halbkugelförmiger Spitze $(R = D/2)$, verhindert Treppenstufen auf Freiformflächen. |
| **`G01 X... Y... Z...`** | **Simultane 3-Achs-Linearbewegung *(3D Linear Move)*** | Alle 3 Raumachsen verfahren gleichzeitig mit Vorschub $F$, um gekrümmte Hügel und Mulden abzufahren. |
| **`3D Adaptive Clearing`** | **Trochoidales Schruppen *(High Speed Roughing)*** | Räumt das Rohteil volumenoptimiert mit konstanter Werkzeugumschlingung aus. |
| **`Scallop / Parallel`** | **3D-Zeilenschlichten *(3D Finishing Strategy)*** | Fährt feine Zeilen *(z. B. $0{,}15\,\text{mm}$ Abstand)* mit Kugelfräser für spiegelglatte Oberflächen ab. |
| **`Toleranz (0.005 mm)`** | **Sehnen-Toleranz *(Chordal Tolerance / Chord Error)*** | Maximale Abweichung der G-Code-Geraden von der perfekten CAD-Freiformkurve. |

### 💡 Worum geht es in einfacher Sprache?

Bisher hatten unsere Bauteile gerade Wände und flache Böden (**2,5D-Bearbeitung**).
Was machst du aber, wenn ein Kunde dir eine **Gussform, eine Computermous-Schale oder ein Turbinenblatt** mit geschwungenen Hügeln und Tälern (**3D-Freiformfläche**) schickt?

Das erledigst du im CAM-System immer in **2 Schritten**:

1. **Schritt 1 – Grobbearbeitung mit `3D Adaptive Clearing` *(3D-Wirbelfräsen / Trochoidales Schruppen)***:
   * Ein normaler Schaftfräser ($\varnothing\,10\,\text{mm}$ oder $\varnothing\,12\,\text{mm}$) trägt das Material in Stufen ab und lässt auf der gewölbten Fläche überall `0,3 mm` **Aufmaß *(Stock to Leave)*** stehen. As Resultat sieht das Bauteil zunächst aus wie eine feine Höhenlinien-Treppe.
2. **Schritt 2 – Feinbearbeitung mit `3D Parallel / Scallop` *(3D-Zeilenschlichten mit Kugelfräser)***:
   * Jetzt wechselst du auf einen **Kugelfräser *(Ball End Mill – ein Fräser, der unten komplett rund wie eine Halbkugel geformt ist, z. B. $\varnothing\,6\,\text{mm}$ mit Eckenradius $R = 3{,}0\,\text{mm}$)*.**
   * Weil die Spitze rund ist, hinterlässt sie keine Treppenstufen, sondern fährt in ganz feinen Bahnen (Zeilenabstand `0,15 mm`) über die Hügel und erzeugt eine glänzende, glatte 3D-Oberfläche!

### 🛠️ Wo im Code wird das gemacht?

Für diese Übung stehen Ihnen die folgenden Dateien zur Verfügung:
1. **Als eigene, kompakte Übungs-Datei:**  
   [`uebungen/uebung_13_3d_freiformflaechen.cps`](file:///C:/Projekte/CNC/uebungen/uebung_13_3d_freiformflaechen.cps) – Unterstützt hochauflösende 3D-Linearbewegungen und erkennt Kugelfräser.
2. **Im Haupt-Postprozessor:**  
   [`src/mein_erster_post.cps`](file:///C:/Projekte/CNC/src/mein_erster_post.cps)

### 🖥️ Schritt-für-Schritt: So öffnen, starten und simulieren Sie Übung 13 in Visual Studio Code (VSC)

#### Schritt 1: Datei in Visual Studio Code öffnen
1. Drücken Sie in VS Code `Strg + P`.
2. Tippen Sie ein: `uebung_13_3d_freiformflaechen.cps` und drücken Sie `Enter`.

#### Schritt 2: Programm im Terminal ausführen & testen
1. Öffnen Sie das Terminal mit ``Strg + ` ``.
2. Führen Sie aus:
   ```powershell
   node tests/simuliere_post.js uebungen/uebung_13_3d_freiformflaechen.cps
   ```
3. Der Simulator erzeugt 3D-Schlichtbahnen mit Kugelfräser.

#### Schritt 3: Den erzeugten G-Code ansehen
* Öffnen Sie [`tests/mein_generierter_gcode.nc`](file:///C:/Projekte/CNC/tests/mein_generierter_gcode.nc) mit `Strg + P`.
* Beobachten Sie die simultanen 3-Achs-Verfahrbefehle `X... Y... Z...`.

#### Schritt 4: 3D-Simulation visuell prüfen
* Kopieren Sie den G-Code in [https://ncviewer.com](https://ncviewer.com).

---

### 🛠️ Wie erkennst du einen Kugelfräser im JavaScript-Postprozessor?

```javascript
// Automatische Erkennung des Werkzeugtyps in onSection():
if (tool.type == TOOL_MILLING_END_BALL) {
  // Gibt Werkzeugdurchmesser und Kugelradius (Hälfte des Durchmessers) im G-Code aus:
  writeComment(
    "3D-FREIFORM-WERKZEUG: KUGELFRAESER D=" +
    xyzFormat.format(tool.diameter) +
    " (R=" + xyzFormat.format(tool.diameter / 2) + ")"
  );
}
```

### ✅ So sieht das Ergebnis im 3D-Freiform-G-Code aus:

```gcode
(OPERATION: 3D FREIFORMFLAECHEN SCHLICHTEN MIT KUGELFRAESER)
(3D-FREIFORM-WERKZEUG: KUGELFRAESER D=6.000 (R=3.000))
N210 T03 M06 (T03 KUGELFRAESER D6MM VHM R3 | M06 AUTOMATISCHER WERKZEUGWECHSEL)
N220 G54 (G54 WERKSTUECK-NULLPUNKT AKTIVIEREN)
N230 S10000 M03 (S10000 HOHE DREHZAHL FUER KUGELSPITZE | M03 SPINDEL RECHTSLAUF)
N240 G43 H03 Z15.000 M08 (G43 LAENGENKORREKTUR | H03 SPEICHER 3 | Z15 FREIFAHRHOEHE | M08 KUEHLUNG AN)
N250 G00 X20.000 Y15.000 (G00 EILGANG ZUM STARTPUNKT DER 3D-KUPPEL)
N260 G00 Z2.000 (G00 EILGANG AUF SICHERHEITSABSTAND 2MM)
N270 G01 Z-1.250 F800 (G01 EINTAUCHEN AUF KONTURHOEHE MIT VORSCHUB 800 MM/MIN)
N280 G01 X20.350 Y15.100 Z-1.230 F1500 (G01 DREIDIMENSIONALE LINEARBEWEGUNG IN X, Y UND Z SIMULTAN)
N290 G01 X20.700 Y15.200 Z-1.205 F1500 (G01 FEINE 3D-BAHNAUFLOESUNG FUER GLATTE OBERFLAECHE)
N300 G01 X21.050 Y15.300 Z-1.170 F1500 (G01 KONTURPUNKT FOLGT DER MATHEMATISCHEN KUPPELKURVE)
N310 G00 Z15.000 M09 (G00 EILGANG FREIFAHREN AUF SICHERHEITSHOEHE | M09 KUEHLUNG AUS)
```

### 🛡️ Prüfliste dieser Übung: Wann ist Übung 13 zu 100 % bestanden?

| Prüfpunkt | Was muss im Code / Simulator zu sehen sein? | Bestanden? |
| :--- | :--- | :---: |
| **1. Kugelfräser-Erkennung** | Der Postprozessor identifiziert `TOOL_MILLING_END_BALL` und weist Radius $R = D/2$ aus. | [ ] |
| **2. Simultaner 3D-Satz** | In den Sätzen `N280` bis `N300` verfahren $X$, $Y$ und $Z$ gleichzeitig in einem einzigen `G01`-Satz. | [ ] |
| **3. Vorschub & Drehzahl** | Ausreichend hohe Drehzahl `S10000`, da die Umfangsgeschwindigkeit der Kugelspitze bei $Z$-Mitte gegen Null geht. | [ ] |
| **4. Kollisionsfreier Rückzug** | Nach dem Schlichten hebt die $Z$-Achse mit `G00 Z15.000` kollisionsfrei von der gewölbten Freiformfläche ab. | [ ] |

---

# Übung 14: Heidenhain Klartext-Steuerung (`TOOL CALL`, `L ... FMAX`) & 4. Drehachse (`A-Achse`) für Aufträge im deutschsprachigen Raum

### 📌 Spickzettel dieser Übung: Alle verwendeten Heidenhain-Klartext- & Achsen-Kennzeichen in Übung 14

| Kennzeichen | Fachbegriff & Erklärung | Bedeutung & Funktion in dieser Übung |
|---|---|---|
| **`BEGIN PGM ... MM`** | **Programmanfang *(Program Header)*** | Startet das Klartext-Programm mit Programmnummer/-name in metrischer Maßeinheit *(Millimeter)*. |
| **`BLK FORM 0.1 / 0.2`** | **Rohteil-Definition *(Blank Form Min/Max)*** | Definiert die Minimal- und Maximalkoordinaten des unzerspanten Rohteilblocks für die Maschinen-Grafik. |
| **`TOOL CALL <T> Z S...`**| **Werkzeugaufruf *(Tool Call)*** | Wechselt Werkzeug $T$ ein, definiert Spindelachse $Z$ und startet Spindeldrehzahl $S$ *(ohne `M06`!)*. |
| **`L ... R0 FMAX`** | **Linearer Eilgangsatz *(Linear Rapid)*** | Verfahrbewegung mit Maximalgeschwindigkeit `FMAX` ohne Fräserradiuskorrektur `R0`. |
| **`L ... R0 F...`** | **Linearer Arbeitsvorschubsatz *(Linear Feed)*** | Geradliniger Schnitt im Material mit Vorschub $F$ in $\text{mm/min}$. |
| **`M11 / M10`** | **Klemmung der 4. Drehachse *(Rotary Axis Unclamp / Clamp)*** | `M11` löst die hydraulische Klemmung vor dem Drehen, `M10` klemmt die Achse für steifes Fräsen wieder fest. |
| **`L A+90.000`** | **4. Drehachse drehen *(4th Axis Rotary Move)*** | Dreht den Teilapparat oder Rundtisch um $90^\circ$ für mehrseitige Bearbeitung. |
| **`M91`** | **Maschinen-Nullpunkt-Bezug *(Machine Datum System)*** | Entspricht ISO `G53`: Verfährt bezogen auf den festen Maschinen-Nullpunkt *(z. B. `L Z+250 R0 FMAX M91`)*. |
| **`END PGM ... MM`** | **Programmende *(Program End)*** | Schließt das Heidenhain-Programm ab. |

### 💡 Worum geht es in einfacher Sprache?

In den USA (auf Upwork) nutzen fast alle Werkstätten **Haas** oder **Fanuc** (`G00`, `G01`, `M06`).
In **Deutschland, Österreich und der Schweiz (DACH-Raum)** ist jedoch **Heidenhain Klartext *(TNC 640, iTNC 530, TNC7)*** der unangefochtene König im Werkzeug- und Maschinenbau!
Heidenhain nutzt keine `G00`/`G01`-Nummern, sondern lesbare Klartext-Wörter:

### 🛠️ Wo im Code wird das gemacht?

Für diese Übung stehen Ihnen die folgenden Dateien zur Verfügung:
1. **Als eigene, kompakte Übungs-Datei:**  
   [`uebungen/uebung_14_heidenhain_klartext_4achse.cps`](file:///C:/Projekte/CNC/uebungen/uebung_14_heidenhain_klartext_4achse.cps) – Schreibt Heidenhain-Klartextsätze (`TOOL CALL`, `L X... Y... FMAX`, `L A...`).
2. **Im Haupt-Postprozessor:**  
   [`src/mein_erster_post.cps`](file:///C:/Projekte/CNC/src/mein_erster_post.cps)

### 🖥️ Schritt-für-Schritt: So öffnen, starten und simulieren Sie Übung 14 in Visual Studio Code (VSC)

#### Schritt 1: Datei in Visual Studio Code öffnen
1. Drücken Sie `Strg + P`.
2. Tippen Sie ein: `uebung_14_heidenhain_klartext_4achse.cps` und drücken Sie `Enter`.

#### Schritt 2: Programm im Terminal ausführen & testen
1. Öffnen Sie das Terminal mit ``Strg + ` ``.
2. Führen Sie aus:
   ```powershell
   node tests/simuliere_post.js uebungen/uebung_14_heidenhain_klartext_4achse.cps
   ```
3. Der Simulator erzeugt Heidenhain-Klartextcode (`.h`).

#### Schritt 3: Den erzeugten G-Code ansehen
* Öffnen Sie [`tests/mein_generierter_gcode.nc`](file:///C:/Projekte/CNC/tests/mein_generierter_gcode.nc) mit `Strg + P`.
* Achten Sie auf `BEGIN PGM`, `TOOL CALL 1 Z S8000` und `L A+90.000 R0 FMAX`.

#### Schritt 4: 3D-Simulation visuell prüfen
* Kopieren Sie den Code in [https://ncviewer.com](https://ncviewer.com).

---

### 📊 Die 6 wichtigsten Heidenhain-Klartext-Befehle im direkten Vergleich zu Fanuc/Haas:

| Funktion | Haas / Fanuc (ISO G-Code) | Heidenhain Klartext (`.H`-Datei) |
| :--- | :--- | :--- |
| **Programmanfang** | `O1001` | `0 BEGIN PGM BAUTEIL_1001 MM` |
| **Werkzeug 1 mit `S8000` aufrufen** | `T01 M06`<br>`S8000 M03` | `TOOL CALL 1 Z S8000` *(wechselt automatisch ein!)* |
| **Eilgang in der Luft (`G00`)** | `G00 X10.000 Y20.000` | `L X+10.000 Y+20.000 R0 FMAX` *(`L` = Gerade, `FMAX` = Vollgas)* |
| **Fräsen im Metall mit Vorschub `F1200`** | `G01 X80.000 Y20.000 F1200` | `L X+80.000 Y+20.000 R0 F1200` |
| **4. Drehachse (`A-Achse`) auf $90^\circ$ drehen** | `G00 A90.000` | `L A+90.000 R0 FMAX` |
| **Programmende** | `M30` | `END PGM BAUTEIL_1001 MM` |

*(Praxis-Beispiele für vollständige Heidenhain-Programme findest du bereits in deinen 4 Referenzprojekten im Ordner `c:\Projekte\CNC\Portfolio\`!)*

### 🛠️ Wie erzeugt der JavaScript-Postprozessor Heidenhain-Sätze?

```javascript
// Heidenhain Werkzeugaufruf in onSection():
writeWords("TOOL CALL " + tool.number + " Z S" + Math.round(spindleSpeed));
writeWords("M3"); // Spindel Rechtslauf
writeWords("M8"); // Kuehlmittel ein

// 4. Achse positionieren (z. B. auf 90 Grad fuer Seitenbearbeitung):
if (currentSection.isMultiAxis && currentSection.isMultiAxis()) {
  writeWords("M11"); // Klemmung der Rundachse loesen
  writeWords("L A+90.000 R0 FMAX"); // Drehung im Eilgang FMAX
  writeWords("M10"); // Rundachse wieder hydraulisch klemmen
}

// Linearer Verfahrsatz in onLinear():
writeWords("L " + xOutput.format(x) + " " + yOutput.format(y) + " R0 F" + feedOutput.format(feed));
```

### ✅ So sieht das vollständige Heidenhain-Klartext-Programm aus:

```gcode
0 BEGIN PGM BAUTEIL_1001 MM (HEIDENHAIN KLARTEXT PROGRAMMSTART METRISCH MM)
1 BLK FORM 0.1 Z X-5.000 Y-5.000 Z-15.000 (ROHTEIL-MINIMALPUNKT ECKE UNTEN LINKS)
2 BLK FORM 0.2 X+85.000 Y+55.000 Z+0.000 (ROHTEIL-MAXIMALPUNKT ECKE OBEN RECHTS)
3 TOOL CALL 1 Z S8000 (TOOL CALL 1 SCHAFTFRAESER D10 | SPINDELACHSE Z | DREHZAHL 8000 U/MIN)
4 M3 (M3 SPINDEL RECHTSLAUF STARTEN)
5 M8 (M8 KUEHLMITTEL EINSCHALTEN)
6 M11 (M11 4. DREHACHSE ACHSKLEMMUNG LOESEN)
7 L A+90.000 R0 FMAX (L LINEARSATZ | A+90 RUNDACHSE DREHEN | R0 KEINE RADIUSKORREKTUR | FMAX EILGANG)
8 M10 (M10 4. DREHACHSE WIEDER FESTKLEMMEN FUER HOHE FRAESSTEIFIGKEIT)
9 L X+10.000 Y+20.000 R0 FMAX (L EILGANGPOSITIONIERUNG AUF STARTKOORDINATEN)
10 L Z+2.000 R0 FMAX (L EILGANG BIS 2MM UEBER DIE BAUTEIL-OBERFLAECHE)
11 L Z-5.000 R0 F500 (L EINTAUCHEN AUF FRAESTIEFE -5MM MIT VORSCHUB 500 MM/MIN)
12 L X+80.000 Y+20.000 R0 F1200 (L FRAESBEWEGUNG BIS X80 MIT ARBEITSVORSCHUB 1200 MM/MIN)
13 L Z+250.000 R0 FMAX M91 (L Z-ACHSE GANZ NACH OBEN FAHREN | M91 MASCHINEN-NULLPUNKT BEZUG WIE G53)
14 M9 (M9 KUEHLWASSER AUSSCHALTEN)
15 M5 (M5 SPINDELDREHUNG ANHALTEN)
16 END PGM BAUTEIL_1001 MM (END PGM PROGRAMMENDE UND RUECKSPRUNG AUF SATZ 0)
```

### 🛡️ Prüfliste dieser Übung: Wann ist Übung 14 zu 100 % bestanden?

| Prüfpunkt | Was muss im Code / Simulator zu sehen sein? | Bestanden? |
| :--- | :--- | :---: |
| **1. Heidenhain Syntax** | Programm beginnt mit `0 BEGIN PGM ... MM` und endet mit `END PGM ... MM`. | [ ] |
| **2. TOOL CALL Format** | Werkzeugwechsel erfolgt in einem Satz: `TOOL CALL <T> Z S<Drehzahl>` ohne getrenntes `M06`. | [ ] |
| **3. 4. Achse geklemmt** | Vor der Drehung wird mit `M11` entklemmt, nach Erreichen von `A+90.` wird mit `M10` geklemmt. | [ ] |
| **4. Sicherer Rückzug M91** | Der Z-Rückzug erfolgt maschinenbezogen mit `M91` (`L Z+250 R0 FMAX M91`), bevor der Bediener entnimmt. | [ ] |

---

# Übung 15: Kanten entgraten am 3D-Modell (`2D-Fase / Chamfer Milling`) mit einem 45°-Fasenfräser (`T04`)

### 📌 Spickzettel dieser Übung: Alle verwendeten Fasenfräs- & Entgrat-Kennzeichen in Übung 15

| Kennzeichen | Fachbegriff & Erklärung | Bedeutung & Funktion in dieser Übung |
|---|---|---|
| **`T04`** | **Fasenfräser *(Chamfer Mill / NC-Spot Drill)*** | $90^\circ$-Spitzkegelfräser mit $45^\circ$-Fasenwinkel an den Schneidflanken. |
| **`Tip Offset`** | **Spitzenversatz *(Tip Offset in $\text{mm}$)*** | Taucht die theoretische Fräserspitze um $1{,}5$ bis $2{,}0\,\text{mm}$ unter die Bauteilkante, damit eine schneidende Flankengeschwindigkeit vorliegt. |
| **`Z-2.300`** | **Effektive Fasentiefe *(Chamfer Z Depth)*** | Berechnet sich aus: $\text{Fasenbreite } (0{,}3\,\text{mm}) + \text{Spitzenversatz } (2{,}0\,\text{mm}) = 2{,}3\,\text{mm}$ Frästiefe im $Z$-Minus. |
| **`G41`** | **Radiuskorrektur LINKS *(Cutter Compensation)*** | Hält den Kegel auf exaktem Schneidenabstand zur scharfen Werkstückkante. |
| **`M08`** | **Kühlmittel EIN *(Flood Coolant On)*** | Verhindert Gratbildung und Aufschweißen von Aluminium an der empfindlichen Fasenschneide. |

### 💡 Worum geht es in einfacher Sprache?

Wenn man Metall fräst, bleibt an jeder oberen Kante ein messerscharfer Metallgrat stehen, an dem sich der Arbeiter sofort in den Finger schneidet.
Früher musste der Arbeiter jedes Teil mit einer Handfeile oder Klinge mühsam von Hand entgraten (**Handentgraten**).
Heute erwartet jeder gute Kunde von dir als **CAM-Spezialist**, dass dein Programm am Ende automatisch einen **$90^\circ$-Fasenfräser (`Chamfer Mill` / `NC-Anbohrer`)** einwechselt und einmal mit einer kleinen $45^\circ$-Schräge (**Fase von z. B. $0{,}3 \times 45^\circ$**) um alle Außenkanten und Taschenränder fährt!

### 🛠️ Wo im Code wird das gemacht?

Für diese Übung stehen Ihnen die folgenden Dateien zur Verfügung:
1. **Als eigene, kompakte Übungs-Datei:**  
   [`uebungen/uebung_15_fasenfraesen_entgraten.cps`](file:///C:/Projekte/CNC/uebungen/uebung_15_fasenfraesen_entgraten.cps) – Berechnet die Fasentiefe inklusive Spitzenversatz (`Tip Offset`).
2. **Im Haupt-Postprozessor:**  
   [`src/mein_erster_post.cps`](file:///C:/Projekte/CNC/src/mein_erster_post.cps)

### 🖥️ Schritt-für-Schritt: So öffnen, starten und simulieren Sie Übung 15 in Visual Studio Code (VSC)

#### Schritt 1: Datei in Visual Studio Code öffnen
1. Drücken Sie in VS Code `Strg + P`.
2. Tippen Sie ein: `uebung_15_fasenfraesen_entgraten.cps` und drücken Sie `Enter`.

#### Schritt 2: Programm im Terminal ausführen & testen
1. Öffnen Sie das Terminal mit ``Strg + ` ``.
2. Führen Sie aus:
   ```powershell
   node tests/simuliere_post.js uebungen/uebung_15_fasenfraesen_entgraten.cps
   ```
3. Der Simulator berechnet die $45^\circ$-Fasenbahn mit `G41` Radiuskorrektur.

#### Schritt 3: Den erzeugten G-Code ansehen
* Öffnen Sie [`tests/mein_generierter_gcode.nc`](file:///C:/Projekte/CNC/tests/mein_generierter_gcode.nc) mit `Strg + P`.
* Prüfen Sie die effektive Fasentiefe `Z-2.300` (Fase + Spitzenversatz).

#### Schritt 4: 3D-Simulation visuell prüfen
* Kopieren Sie den G-Code in [https://ncviewer.com](https://ncviewer.com).

---

### 🛠️ Die goldene Regel beim Fasenfräsen:
* Fahre niemals mit der **exakten Spitze (`D = 0 mm`)** des $90^\circ$-Kegels an der Kante entlang (dort ist die Schnittgeschwindigkeit gleich null, das gibt eine hässliche Kante!).
* Stelle im CAM den **Spitzen-Versatz (`Tip Offset`)** immer auf **`1,5 mm` bis `2,0 mm`** ein: Dann taucht die Spitze des Kegelfräsers `2 mm` tiefer neben der Wand ein und schneidet die $45^\circ$-Fase sauber mit der seitlichen Schneidenflanke!

### 🛠️ Wie berechnet der JavaScript-Postprozessor die Fasentiefe?

```javascript
// Automatische Erkennung und Fasentiefen-Berechnung in onSection():
if (tool.type == TOOL_MILLING_CHAMFER) {
  var tipOffset = 2.0; // 2 mm Spitzenversatz neben der Bauteilkante
  var chamferWidth = 0.3; // 0.3 mm Kantenbrechung
  var targetZ = -(tipOffset + chamferWidth);
  writeComment(
    "FASEN-BERECHNUNG: BREITE=" + chamferWidth + "MM | TIP-OFFSET=" + tipOffset + "MM | Z-TIEFE=" + targetZ + "MM"
  );
}
```

### ✅ So sieht das Ergebnis im fertigen G-Code aus:

```gcode
(--- OPERATION 40: ALLE KANTEN AUTOMATISCH ENTGRATEN 0.3 x 45 GRAD ---)
(FASEN-BERECHNUNG: BREITE=0.3MM | TIP-OFFSET=2.0MM | Z-TIEFE=-2.3MM)
N350 T04 M06 (T04 FASENFRAESER 90 GRAD D10MM VHM | M06 AUTOMATISCHER WERKZEUGWECHSEL)
N360 S6000 M03 (S6000 SPINDELDREHZAHL 6000 U/MIN | M03 SPINDEL RECHTSLAUF EIN)
N370 G54 G00 X-5.000 Y0.000 (G54 WERKSTUECK-NULLPUNKT | G00 EILGANG VOR DIE KONTUR)
N380 G43 H04 Z15.000 M08 (G43 LAENGENKORREKTUR | H04 SPEICHER 4 | Z15 FREIFAHRHOEHE | M08 KUEHLMITTEL AN)
N390 G00 Z2.000 (G00 EILGANG AUF SICHERHEITSHOEHE 2MM)
N400 G01 Z-2.300 F800 (G01 EINTAUCHEN: 2.0MM SPITZENVERSATZ + 0.3MM FASE = Z-2.3MM | F800 VORSCHUB)
N410 G01 X80.000 Y0.000 F1000 (G01 UNTERE KANTE ENTGRATEN BIS X80 MIT VORSCHUB 1000 MM/MIN)
N420 G01 X80.000 Y50.000 F1000 (G01 RECHTE KANTE ENTGRATEN BIS Y50)
N430 G01 X0.000 Y50.000 F1000 (G01 OBERE KANTE ENTGRATEN BIS X0)
N440 G01 X0.000 Y0.000 F1000 (G01 LINKE KANTE ENTGRATEN ZURUECK ZU Y0)
N450 G00 Z15.000 M09 (G00 EILGANG SENKRECHT AUF FREIFAHRHOEHE 15MM | M09 KUEHLMITTEL AUS)
```

### 🛡️ Prüfliste dieser Übung: Wann ist Übung 15 zu 100 % bestanden?

| Prüfpunkt | Was muss im Code / Simulator zu sehen sein? | Bestanden? |
| :--- | :--- | :---: |
| **1. Spitzenversatz aktiv** | Die $Z$-Frästiefe liegt bei `Z-2.300`, so dass der Schnitt auf der aktiven Schneidflanke des $90^\circ$-Fräsers erfolgt. | [ ] |
| **2. Kantenverlauf lückenlos** | Alle 4 Außenkanten des Rechtecks $80 \times 50\,\text{mm}$ werden im geschlossenen Umlauf entgratet. | [ ] |
| **3. Kühlung aktiv** | `M08` kühlt die feine Fräserspitze, um Riefenbildung und Materialaufschweißen zu verhindern. | [ ] |
| **4. Sauberer Rückzug** | In Satz `N450` zieht die Z-Achse mit `G00 Z15.000` senkrecht nach oben ab, bevor das Werkzeug geparkt wird. | [ ] |

---

# Übung 16: Die komplette 5-Punkte-Endabnahme im Simulator vor der Auslieferung an den Online-Kunden (Meister-Prüfung)

### 📌 Spickzettel dieser Übung: Alle verwendeten Meister-Endabnahme-Kennzeichen in Übung 16

| Kennzeichen | Fachbegriff & Erklärung | Bedeutung & Funktion in dieser Übung |
|---|---|---|
| **`G54 (X0, Y0, Z0)`** | **Nullpunkt-Prüfung *(WCS Origin Audit)*** | Verifiziert die Lage des Nullpunkts am 3D-Modell und Einrichteblatt. |
| **`Z-MIN & L_min`** | **Kollisions- & Spannprüfmaß *(Minimum Depth & Stickout)*** | Schützt Schraubstockbacken vor Crash und verhindert Werkzeugauszug aus der Spannzange. |
| **`G00 (Z > 0)`** | **Eilgang-Sicherheitskontrolle *(Rapid Move Clearance)*** | Stellt sicher, dass Eilgänge niemals bei $Z \le 0$ im Metall stattfinden. |
| **`S, F, M03, M08`** | **Technologie-Vierklang *(Machining Parameters Audit)*** | Prüft Drehzahl, Vorschub, Spindeldrehrichtung und Kühlmittelversorgung. |
| **`Safe Footer G53`** | **Sicherer 2-Stufen-Rückzug *(Two-Stage Safe Footer)*** | Garantiert: Zuerst Z-Achse hoch, Spindelstopp, erst danach Tisch nach vorne zur Tür. |

### 💡 Worum geht es in einfacher Sprache?

Bevor du einem Online-Kunden auf **Upwork**, **Fiverr**, **Malt** oder per **E-Mail** die fertige `.nc`- / `.H`- / `.MPF`-Datei schickst, führst du immer diese **5-Punkte-Meisterprüfung** durch (dabei hilft dir später auch dein **KI-Agent Nr. 3 `NC-Safety- & Setup-Agent`** und unser Python-Skript [`cnc_setup_sheet_extractor.py`](file:///C:/Projekte/CNC/GitHub_Projekte/cnc_setup_sheet_extractor.py)):

### 🛠️ Wo im Code wird das gemacht?

Für diese Übung stehen Ihnen die folgenden Dateien zur Verfügung:
1. **Als Meister-Postprozessor-Quelldatei:**  
   [`uebungen/uebung_16_endabnahme_meister_post.cps`](file:///C:/Projekte/CNC/uebungen/uebung_16_endabnahme_meister_post.cps) – Kombiniert alle 16 Sicherheits- und Steuerungsfeatures in einem geprüften Meister-Postprozessor.
2. **Im Haupt-Postprozessor:**  
   [`src/mein_erster_post.cps`](file:///C:/Projekte/CNC/src/mein_erster_post.cps)

### 🖥️ Schritt-für-Schritt: So öffnen, starten und simulieren Sie Übung 16 in Visual Studio Code (VSC)

#### Schritt 1: Datei in Visual Studio Code öffnen
1. Drücken Sie in VS Code `Strg + P`.
2. Tippen Sie ein: `uebung_16_endabnahme_meister_post.cps` und drücken Sie `Enter`.

#### Schritt 2: Programm im Terminal ausführen & testen
1. Öffnen Sie das Terminal mit ``Strg + ` ``.
2. Führen Sie aus:
   ```powershell
   node tests/simuliere_post.js uebungen/uebung_16_endabnahme_meister_post.cps
   ```
3. Der Meister-Postprozessor führt alle Sicherheitschecks (Drehzahl, Z-Kollision, Späneförderer) durch und erzeugt den perfekten Produktions-Code.

#### Schritt 3: Den erzeugten G-Code ansehen
* Öffnen Sie [`tests/mein_generierter_gcode.nc`](file:///C:/Projekte/CNC/tests/mein_generierter_gcode.nc) mit `Strg + P`.
* Kontrollieren Sie alle 5 Punkte der Meisterprüfung in den Zeilen des G-Codes.

#### Schritt 4: 3D-Simulation visuell prüfen
* Kopieren Sie den G-Code in [https://ncviewer.com](https://ncviewer.com) und lassen Sie die gesamte Fertigung vom Schruppen bis zum Entgraten und sicheren Rückzug durchlaufen.

---

### 🛠️ Wie prüft der Meister-Postprozessor die 5 Sicherheitspunkte in JavaScript?

```javascript
// Meister-Pruefung in onSection() & onClose():
// 1. Pruefung: Spindeldrehzahl und Drehrichtung gesetzt?
if (spindleSpeed <= 0) {
  error("MEISTER-CHECK FEHLER: Keine Spindeldrehzahl S angegeben!");
}

// 2. Pruefung: Z-MIN Tiefe berechnen und Schraubstock-Abstand pruefen
var zMin = currentSection.getGlobalZRange().getMinimum();
if (zMin < -25.0) {
  warning("MEISTER-CHECK WARNUNG: Z-Tiefe sehr gross (" + zMin + "mm). Schraubstockbacken pruefen!");
}

// 3. Pruefung: Kuehlmittel sicherstellen
if (!tool.coolant || tool.coolant == COOLANT_OFF) {
  writeComment("MEISTER-HINWEIS: Trockenbearbeitung aktiv.");
}
```

### ✅ So sieht das vollständige Meisterprüfungs-G-Code-Programm aus:

```gcode
%
O1001 (MEISTERSTUECK - FERTIGUNGSPROGRAMM MIT 5-PUNKTE-SICHERHEITSCHECK)
(==================================================)
(BENOETIGTE WERKZEUGE - TOOL TABLE)
(T01 | D=10.000MM | ECKE R=0.000 | Z-MIN=-5.000MM  | SCHAFTFRAESER 10MM VHM)
(T02 | D=6.000MM  | ECKE R=0.000 | Z-MIN=-12.000MM | SPIRALBOHRER 6MM VHM)
(T04 | D=10.000MM | 90-GRAD FASE | Z-MIN=-2.300MM  | FASENFRAESER 90 GRAD)
(==================================================)
N10 G90 G17 G40 G49 G80 G21 (SICHERHEITSZEILE: G90 ABSOLUT | G17 XY-EBENE | G40 RADIUSKORREKTUR AUS | G49 LAENGENKORREKTUR AUS | G80 BOHRZYKLEN AUS | G21 METRISCH MM)
(PUNKT 1: NULLPUNKT-CHECK G54)
N20 T01 M06 (T01 SCHAFTFRAESER D10 | M06 AUTOMATISCHER WERKZEUGWECHSEL)
N30 G54 (G54 WERKSTUECK-NULLPUNKT AKTIVIEREN - ECKE VORNE LINKS OBEN)
(PUNKT 4: TECHNOLOGIE-CHECK S8000 M03 M08)
N40 S8000 M03 (S8000 DREHZAHL 8000 U/MIN FUER ALU | M03 SPINDEL RECHTSLAUF)
N50 G43 H01 Z15.000 M08 (G43 LAENGENKORREKTUR | H01 SPEICHER 1 | Z15 FREIFAHRHOEHE | M08 KUEHLMITTEL AN)
(PUNKT 3: EILGANG-CHECK G00 NUR UEBER Z > 0)
N60 G00 X-10.000 Y-10.000 (G00 EILGANG VOR DAS TEIL BEI SICHERER HOEHE Z15)
N70 G00 Z2.000 (G00 EILGANG BIS 2MM UEBER OBERFLAECHE)
(PUNKT 2: TIEFEN- UND SCHRAUBSTOCK-CHECK Z-MIN)
N80 G01 Z-5.000 F500 (G01 EINTAUCHEN AUF FRAESTIEFE Z-5 - UEBER SCHRAUBSTOCKBACKEN)
N90 G01 X80.000 Y0.000 F1200 (G01 AUSSENKONTUR FRAESEN MIT VORSCHUB 1200 MM/MIN)
N100 G00 Z15.000 (G00 FREIFAHREN AUF SICHERHEITSHOEHE)
(PUNKT 5: SICHERES PROGRAMMENDE - SAFE FOOTER)
N110 M09 (M09 KUEHLWASSER AUSSCHALTEN)
N120 G53 G00 Z0.000 (G53 MASCHINENKOORDINATEN | G00 EILGANG | Z0 SPINDEL ZUERST GANZ NACH OBEN)
N130 M05 (M05 SPINDELSTOPP)
N140 G53 G00 Y0.000 (G53 MASCHINENKOORDINATEN | G00 EILGANG | Y0 TISCH VOR ZUR TUER)
N150 M30 (M30 HAUPTPROGRAMMENDE, RESET UND SPEICHER AUF ZEILE 1 ZURUECKSETZEN)
%
```

### 🛡️ Prüfliste dieser Übung: Wann ist die Meisterprüfung (Übung 16) zu 100 % bestanden?

| Prüfpunkt | Was du im Simulator & Code kontrollierst | Bestanden? |
| :--- | :--- | :---: |
| **1. Nullpunkt-Check (`G54`)** | Liegt der Koordinatenursprung `(X0, Y0, Z0)` im Simulator exakt an der Stelle, die du auf dem Einrichteblatt für den Kunden eingezeichnet hast? | [ ] |
| **2. Tiefen- & Schraubstock-Check (`Z-MIN`)** | Schau im Header auf den berechneten `Z-MIN`-Wert jedes Werkzeugs: Ist genug Platz zu den Schraubstockbacken UND ist das Werkzeug lang genug eingespannt ($L_{\text{min}} > |Z_{\text{min}}| + 5\,\text{mm}$)? | [ ] |
| **3. Eilgang-Check (`G00` / `FMAX`)** | Findet jede schnelle `G00`-Bewegung in $X$ und $Y$ garantiert **oberhalb des Bauteils ($Z > 0$)** in der Luft statt? | [ ] |
| **4. Technologie-Check (`S`, `F`, `M03`, `M08`)** | Dreht sich die Spindel (`M03`) mit plausibler Drehzahl (`S`) für das Material (Alu vs. Stahl) und ist beim Gewindebohren `F = S × Steigung` eingehalten? | [ ] |
| **5. Sicheres Programmende (`Safe Footer`)** | Zieht das Programm am Ende **zuerst** die $Z$-Achse ganz nach oben (`G53 G00 Z0` bzw. `L Z+250 R0 FMAX M91`), bevor der Tisch zur Tür fährt und `M30` stoppt? | [ ] |

Wenn du alle 5 Haken setzen kannst, speicherst du das Programm zusammen mit dem **Einrichteblatt** und einem kurzen **Simulationsvideo** ab – und dein Online-Auftrag ist abgabebereit!

> [!TIP]
> **Offizielle Kundenabgabe & Haftungsschutz:**  
> Für die finale Freigabe beim Kunden nutzt du an dieser Stelle die druckbare Abnahme-Checkliste mit Unterschriftenfeldern aus **[`SICHERHEITS_UND_QUALITAETS_PRUEFLISTE_GCODE.md`](file:///c:/Projekte/CNC/SICHERHEITS_UND_QUALITAETS_PRUEFLISTE_GCODE.md)**. Damit überreichst du dem Kunden ein lückenloses Qualitätszertifikat!


---

## 🎯 Konkrete Simulator-Prüfanleitung für die Profi-Übungen 9 bis 16 (Stufe 11 bis Stufe 18)

Damit du auch die fortgeschrittenen **Profi-Übungen 9 bis 16** sofort praktisch auf deinem Laptop testen und im Simulator überprüfen kannst, findest du hier die genauen Testschritte:

### 🔹 Test für Übung 9 (Schnittdaten-Kontrolle $v_c$, `S` & `F` im Postprozessor):
1. Füge die `vc`-Berechnung aus Übung 9 in [`src/mein_erster_post.cps`](file:///C:/Projekte/CNC/src/mein_erster_post.cps) in die Funktion `onSection()` ein und speichere (`Strg + S`).
2. Führe im Terminal `node tests/simuliere_post.js` aus.
3. **Prüfung:** Im erzeugten G-Code steht jetzt vor jeder Operation automatisch die berechnete Schnittgeschwindigkeit `(TECHNOLOGIE-CHECK: SCHNITTGESCHWINDIGKEIT VC = 251 M/MIN)`.

### 🔹 Test für Übung 10 (2. Aufspannung `G55` / `OP20` im Online-Simulator `NCViewer.com` testen):
1. Kopiere den Beispiel-G-Code aus **Übung 10** (`N500 M00` bis `N570 G01 X90.000`) ans Ende deiner Datei `tests/mein_generierter_gcode.nc` (direkt vor den Safe Footer `N370 M09`).
2. Füge den Code in **`https://ncviewer.com`** ein und klicke auf **`Plot`**.
3. **Prüfung:** Klicke auf Zeile `N560 G01 Z0.000 F1500` und `N570 G01 X90.000`: Du siehst im 3D-Fenster, wie der Fräser einmal sauber plan über die Oberseite (`Z0`) fährt!

### 🔹 Test für Übung 11 (Gewindebohren `G84` mit `F = S × Steigung`):
1. Prüfe im G-Code oder mit unserem Analyse-Tool `python GitHub_Projekte/cnc_setup_sheet_extractor.py Portfolio/Projekt_01_25D_Praezisionsfraesteil/Fertigungspaket_Projekt_01.md`:
   Bei einem `M8`-Gewinde (Steigung $1{,}25\,\text{mm}$) und `S600` muss im `G84`-Satz zwingend `F750` stehen.

### 🔹 Test für Übung 12 (Werkzeugradiuskorrektur `G41` / `G40` im Simulator prüfen):
1. Kopiere den `G41`-Codeblock aus **Übung 12** (`N200` bis `N250`) in **`https://ncviewer.com`**.
2. **Prüfung:** Klicke im NCViewer nacheinander auf `N200` (Start in der Kreismitte `X40 Y25`), `N220` (Anfahren an den Kreisrand `X55 Y25` mit aktivem `G41`), `N230` (Vollkreis `G03`) und `N240` (Zurückfahren zur Mitte mit `G40`).

### 🔹 Test für Übung 13 & 14 (3D-Freiformflächen & Heidenhain Klartext `.H` mit unserem Python-Extractor testen!):
1. Öffne das Terminal (`Strg + Ö`) in `C:\Projekte\CNC` und führe unser neues Python-Tool direkt auf dein Heidenhain-Referenzprojekt aus:
   ```powershell
   python GitHub_Projekte/cnc_setup_sheet_extractor.py Portfolio/Projekt_01_25D_Praezisionsfraesteil/Fertigungspaket_Projekt_01.md
   ```
2. **Prüfung:** Das Skript erkennt sofort automatisch `Heidenhain Klartext (TNC)`, liest das Rohteil (`BLK FORM`) von `150.0 x 100.0 x 45.0 mm` aus und listet die Heidenhain-Werkzeuge (`TOOL CALL 3`, `TOOL CALL 6`) inklusive Mindest-Auskraglänge ($L_{\text{min}}$) in einer fertigen Tabelle auf!

### 🔹 Test für Übung 15 (Kanten entgraten `2D-Fase` im 3D-Simulator):
1. Kopiere den Entgrat-Codeblock (`N350` bis `N450`) aus **Übung 15** in **`https://ncviewer.com`**.
2. **Prüfung:** Du siehst, wie der $90^\circ$-Fasenfräser (`T04`) exakt auf Tiefe `Z-2.300 mm` einmal sauber um das gesamte `80 x 50 mm` Rechteck herumfährt, um alle 4 Außenkanten zu brechen.

### 🔹 Test für Übung 16 (5-Punkte-Meisterprüfung):
Nimm dir die Checkliste aus **Übung 16** und prüfe damit die Datei [`tests/output_expected.nc`](file:///C:/Projekte/CNC/tests/output_expected.nc) in [3d_auftrag_simulator.html](file:///C:/Projekte/CNC/kundenauftrag_01_flanschplatte/3d_auftrag_simulator.html) – alle 5 Prüfpunkte werden dort zu 100 % erfüllt!


---

## 🤖 WANN und WIE du deine 4 KI-Agenten verwendest (Goldene Regel für die Übungen & Praxisanleitung nach Übung 16)

Viele fragen sich: *„Soll ich die 4 KI-Agenten schon während der 16 Übungen benutzen oder erst später?“*  
Hier ist die klare Regel und die genaue Anleitung, **wann** und **wie** jeder Agent zum Einsatz kommt:

---

### 1. WANN verwendest du die KI-Agenten? (Die 2-Phasen-Regel)

* **❌ WÄHREND der Übungen 1 bis 15 (Lernphase): Noch KEINE KI-Agenten benutzen!**
  * **Warum?** Während du die **Basis-Übungen A & B** sowie **Übung 1 bis 15** in diesem Handbuch durcharbeitest, sollst du **mit deinen eigenen Händen und Augen** verstehen, wie `onOpen()`, `onSection()`, `Z-MIN`, `G54/G55`, `G84`, `G41` und Heidenhain Klartext funktionieren.
  * Nur wenn du die Grundlagen einmal selbst gemacht hast, kannst du später als **Diplom-Ingenieur & Software Engineer** in 30 Sekunden erkennen, ob der Code, den dir der KI-Agent vorschlägt, zu 100 % sicher ist!
* **✅ AB Übung 16 & bei jedem echten Kundenauftrag: JETZT schaltest du alle 4 KI-Agenten ein!**
  * Sobald du bei **Übung 16 (5-Punkte-Endabnahme)** angekommen bist und deine ersten echten **100 % Online-Aufträge** *(über Upwork, Fiverr, Malt.de oder CAM-Systemhäuser)* abwickelst, überlässt du **80 % der Tipp- und Fleißarbeit** deinen 4 KI-Agenten aus **[KI_Agenten_System_und_Bauplan.md](file:///c:/Projekte/CNC/KI_Agenten_System_und_Bauplan.md)**.

---

### 2. WIE verwendest du die 4 KI-Agenten bei welcher Aufgabe? (Zuordnung zu deinen 16 Übungen)

Jeder deiner 4 KI-Agenten übernimmt später genau die Aufgaben, die du in diesen 16 Übungen von Hand gelernt hast:

| Welcher KI-Agent? | Welche Übungen aus diesem Handbuch übernimmt er später automatisch für dich? | WIE rufst du ihn auf? (Dein Befehl im Chat) |
| :--- | :--- | :--- |
| **🕵️‍♂️ Agent 1:<br>`Lead-Scout-Agent`**<br>*(Kunden-Sucher)* | **Nach Übung 16:**<br>Sucht dir im Internet passende **100 % Online-Aufträge** für genau die Themen aus Übung 1–16 *(Postprozessoren & 3D-CAM)* und schreibt das Bewerbungsanschreiben. | Du schreibst im Chat:<br>*„Starte **Agent 1 (`Lead-Scout-Agent`)** aus `KI_Agenten_System_und_Bauplan.md` und schreibe ein kurzes Angebotsschreiben für diese Kunden-Anfrage: [Text der Anzeige einfügen]“* |
| **💻 Agent 2:<br>`Postprocessor-Coder-Agent`**<br>*(Programmier-Roboter)* | **Übernimmt die Arbeit aus Übung 1, 2, 3, 6, 7, 8, 9 & 14:**<br>Schreibt für dich den JavaScript- (`.cps`), Python- oder Tcl-Code für Header (`onOpen`), Werkzeuglisten, `Z-MIN`-Schutz, `Safe Retract`, Schalter (`Properties`), Sinumerik und Heidenhain Klartext. | Du schreibst im Chat:<br>*„Starte **Agent 2 (`Postprocessor-Coder-Agent`)**. Hier ist der Postprozessor des Kunden und sein Wunsch-NC-Code. Programmiere mir die Funktion für [z. B. Heidenhain Werkzeugliste & sicheren Z-Rückzug].“* |
| **🛡️ Agent 3:<br>`NC-Safety- & Setup-Agent`**<br>*(Crash-Prüfer & Einrichteblatt-Schreiber)* | **Übernimmt die Arbeit aus Übung 4, 5, 10, 11, 12, 13, 15 & 16:**<br>Prüft deinen fertigen G-Code auf alle **5 Punkte der Meisterprüfung (Übung 16)** *(Kühlmittel `M08`, Gewindevorschub `G84`, Radiuskorrektur `G41`, Rückzug)* und füllt mit **[cnc_setup_sheet_extractor.py](file:///c:/Projekte/CNC/GitHub_Projekte/cnc_setup_sheet_extractor.py)** automatisch die Vorlage **[Vorlage_Einrichteblatt_und_Werkzeugliste.md](file:///c:/Projekte/CNC/Portfolio/Vorlage_Einrichteblatt_und_Werkzeugliste.md)** aus! | Du schreibst im Chat:<br>*„Starte **Agent 3 (`NC-Safety- & Setup-Agent`)** für die Datei `[Dateiname.nc / .H]`. Prüfe alle 5 Sicherheitspunkte aus Übung 16 und erstelle das fertige Einrichteblatt.“* |
| **💶 Agent 4:<br>`Backoffice-Ingenieur-Agent`**<br>*(Büro- & Finanzamts-Sekretär)* | **Vor und nach jedem Auftrag:**<br>Füllt dir in 5 Sekunden deine **[Vorlage_Angebot_und_Rechnung_Ingenieurbuero.md](file:///c:/Projekte/CNC/Vorlagen_Vertraege_Rechnungen/Vorlage_Angebot_und_Rechnung_Ingenieurbuero.md)** aus – inklusive **§ 18 EStG Ingenieur-Formulierung (für das Finanzamt Hanau)**, **50 % Anzahlung & Video-Vorabfreigabe** sowie den **4 Haftungsschutz-Klauseln**. | Du schreibst im Chat:<br>*„Starte **Agent 4 (`Backoffice-Ingenieur-Agent`)** und erstelle ein Angebot / eine Rechnung für Kunde [Name, Ort], Projekt [Name], Preis [Betrag €].“* |

---

### 3. Wo findest du alle Details zu den 4 KI-Agenten in deinen anderen Dokumenten?

Damit du jederzeit sofort nachschlagen kannst, stehen die Beschreibungen an diesen **3 Orten**:
1. **Hier im Übungshandbuch ([ALLE_UEBUNGEN_HANDBUCH.md](file:///c:/Projekte/CNC/ALLE_UEBUNGEN_HANDBUCH.md#L935-L975)):** Direkt in diesem Abschnitt am Ende von Übung 16 *(wann während/nach den Übungen nutzen + Zuordnungstabelle zu Übung 1–16)*.
2. **Im Hauptdokument ([CAM_Nebentaetigkeit_und_Gewerbe_Leitfaden.md – Abschnitt 15, Zeilen 815–900](file:///c:/Projekte/CNC/CAM_Nebentaetigkeit_und_Gewerbe_Leitfaden.md#L815-L900)):** Kompletter Ablaufplan für dein 5–8-Stunden-Wochenende *(wie du 80 % der Zeit sparst)* sowie oben auf Seite 1 in der **Lese- & Umschalt-Anleitung (Phase 5)**.
3. **Im technischen Bauplan ([KI_Agenten_System_und_Bauplan.md](file:///c:/Projekte/CNC/KI_Agenten_System_und_Bauplan.md)):** Alle 4 fertigen **System-Prompts (Programmier-Befehle)** in grauen Kopier-Boxen sowie die Stundensatz- und Festpreis-Tabelle (`65 € bis 135 € / Std.`).


---

### 4. Ganz konkret erklärt: WIE machen Agent 2 und Agent 3 das technisch auf deinem Laptop? (Klick-für-Klick-Ablauf)

Damit du dir genau vorstellen kannst, wie die Zusammenarbeit zwischen dir und den Agenten hier am Computer abläuft, ist hier der genaue technische Ablauf:

#### 💻 Wie Agent 2 (`Postprocessor-Coder-Agent`) deine JavaScript-Arbeit (Übung 1, 2, 3, 6, 7, 8, 9, 14) übernimmt:
* **In den Übungen (Lernphase):** Du öffnest selbst die Datei [`src/mein_erster_post.cps`](file:///C:/Projekte/CNC/src/mein_erster_post.cps) und tippst den JavaScript-Code Zeile für Zeile selbst ein.
* **Später beim echten Kundenauftrag (mit Agent 2):**
  1. Der Kunde schickt dir per E-Mail seine Postprozessor-Datei *(z. B. `kunde_maschine.cps`)* und sagt: *„Ich brauche oben eine automatische Werkzeugliste mit `Z-MIN` (wie in Übung 2 & 3), Heidenhain-Formatierung (wie in Übung 14) und am Ende den sicheren Rückzug (wie in Übung 6).“*
  2. Du speicherst die Datei `kunde_maschine.cps` einfach in deinem Ordner `c:\Projekte\CNC\src\` ab.
  3. Du tippst hier im Chat **nur einen einzigen Satz**:
     > *„Agent 2: Öffne `src/kunde_maschine.cps` und programmiere dort die Werkzeugliste, `Z-MIN` und den sicheren Rückzug am Programmende hinein!“*
  4. **Was passiert dann automatisch?** Ich (als dein Agent 2) habe direkten Lese- und Schreibzugriff auf deinen Ordner `c:\Projekte\CNC\`. Ich öffne die Datei `kunde_maschine.cps` selbstständig, suche die richtigen Funktionen (`onOpen`, `onSection`, `onClose`), schreibe den kompletten JavaScript-Code direkt in die Datei hinein, speichere sie ab und teste sie sofort mit `node tests/simuliere_post.js`!

#### 🛡️ Wie Agent 3 (`NC-Safety- & Setup-Agent`) deine Prüf- und Dokumentationsarbeit (Übung 4, 5, 10, 11, 12, 13, 15, 16) übernimmt:
* **Wichtige Aufteilung (20 % Du / 80 % Agent 3):**
  * **Deine 20 % am 3D-Modell (Übung 4, 10, 13, 15):** Wenn dir ein Kunde ein 3D-Bauteil (`.step`-Datei) schickt, öffnest du es in deinem 3D-CAM-Programm *(z. B. Fusion 360)*, klickst mit der Maus kurz die Flächen an (*Nullpunkt `G54` setzen, Schruppen, Schlichten, Bohren, Entgraten*) und drückst auf **„G-Code exportieren“**. Dadurch entsteht auf deiner Festplatte die fertige G-Code-Datei *(z. B. `Kunde_Ventilblock.nc`, `.H` oder `.MPF`)*.
  * **Die 80 % von Agent 3 (Übung 5, 11, 12, 16 – vollautomatisch!):**
    1. Du speicherst die erzeugte G-Code-Datei im Ordner `c:\Projekte\CNC\`.
    2. Du tippst hier im Chat **nur einen einzigen Satz**:
       > *„Agent 3: Prüfe die Datei `Kunde_Ventilblock.nc` nach allen Regeln aus Übung 16 und erstelle mir das fertige Einrichteblatt!“*
    3. **Was macht Agent 3 dann vollautomatisch auf deiner Festplatte?**
       * Er startet im Hintergrund unser Python-Werkzeug **[cnc_setup_sheet_extractor.py](file:///c:/Projekte/CNC/GitHub_Projekte/cnc_setup_sheet_extractor.py)** und liest alle tausend Zeilen deines G-Codes in 1 Sekunde durch.
       * **Automatischer Check aus Übung 10 (`G54` / `G55`):** Er prüft, ob vor dem Wechsel auf die 2. Aufspannung (`G55`) ein sicherer Stopp (`M00`) und ein Z-Rückzug steht.
       * **Automatischer Check aus Übung 11 (Gewindebohren `G84`):** Er rechnet nach, ob beim Gewindebohren der Vorschub `F` exakt zu `Drehzahl S × Steigung` passt, damit kein Gewindebohrer abbricht.
       * **Automatischer Check aus Übung 12 (`G41` / `G40`):** Er prüft, ob jede eingeschaltete Werkzeugradiuskorrektur (`G41`/`G42`) vor dem nächsten Werkzeugwechsel wieder sauber mit `G40` ausgeschaltet wurde.
       * **Automatischer Check aus Übung 16 (5-Punkte-Meisterprüfung):** Er prüft Kühlmittel (`M08`), Spindeldrehzahl (`S > 0`), Eilganghöhen (`G00`) und den tiefsten Punkt (`Z-MIN`).
       * **Automatisches Ausfüllen von Übung 5 (Einrichteblatt):** Zum Schluss nimmt Agent 3 automatisch deine Vorlage **[Vorlage_Einrichteblatt_und_Werkzeugliste.md](file:///c:/Projekte/CNC/Portfolio/Vorlage_Einrichteblatt_und_Werkzeugliste.md)**, trägt alle Werkzeuge (`T1`, `T2`...), Drehzahlen, Vorschübe, `Z-MIN`-Tiefen und Mindest-Auskraglängen ($L_{\text{min}}$) in die Tabelle ein und speichert dir das komplett fertige Einrichteblatt inkl. **Haftungs-Freigabeprotokoll** als neue Datei ab!

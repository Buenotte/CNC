# CNC-Postprozessor-Entwicklung (Entwicklung von Übersetzungsprogrammen für computergesteuerte Werkzeugmaschinen)

Willkommen in Ihrem Entwicklungs-Workspace (Arbeitsbereich) unter `C:\Projekte\CNC`. Dieses Projekt dient als professionelle Entwicklungsumgebung für **Autodesk Fusion Postprozessoren (JavaScript-basierte `.cps`-Übersetzungsskripte, die neutrale CAM-Werkzeugwege in maschinenspezifischen G-Code umwandeln)**.

---

## 📂 Ordnerstruktur (Verzeichnisaufbau des Projekts)

```text
C:\Projekte\CNC\
├── doc.txt                                              # Ursprüngliche Anforderungs- und Einstiegsnotiz
├── ANLEITUNG_BERUFSEINSTIEG_UND_IMPLEMENTATION_PLAN.md  # Vollständiger Leitfaden für Berufseinstieg & Implementierungsplan (Umsetzungsplan)
├── SICHERHEITS_UND_QUALITAETS_PRUEFLISTE_GCODE.md       # Umfassendes Sicherheits- und Qualitätsprüfprotokoll (Null-Kollisions-Garantie vor Auslieferung)
├── README.md                                            # Diese Projekt-Dokumentation (Übersicht und Bedienungsanleitung)
├── docs/                                                # Wissensdatenbank & Handbücher (Dokumentation für Entwickler und KI)
│   └── API_KURZREFERENZ.md                              # Nachschlagewerk der wichtigsten Autodesk Post-API-Funktionen (Programmierschnittstellen)
├── src/                                                 # Quellcode-Verzeichnis (Source Code)
│   ├── mein_erster_post.cps                             # Ihr erster CNC-Postprozessor (JavaScript-Datei mit erweitertem onOpen()-Header)
│   └── config.json                                      # Optionale Konfigurationsdatei (JSON-Format – JavaScript Object Notation)
├── uebungen/                                            # Einzelne Source-Dateien (.cps) für alle 16 Übungen
│   ├── uebung_00b_hallo_welt.cps                        # Basis-Übung B: Hallo Welt
│   ├── uebung_01_entwickler_header.cps                  # Übung 01: Entwickler-Infoblock onOpen()
│   ├── uebung_02_werkzeugliste.cps                      # Übung 02: Werkzeugliste getToolTable()
│   ├── uebung_03_z_min_berechnung.cps                   # Übung 03: Z-MIN Berechnung
│   ├── uebung_04_3d_modell_cam.cps                      # Übung 04/05: CAM-Operationen
│   ├── uebung_06_sicherer_rueckzug.cps                  # Übung 06: Sicherer Rückzug Z/Y
│   ├── uebung_07_spaenefoerderer_schalter.cps           # Übung 07: Späneförderer Schalter M31/M33
│   ├── uebung_08_fanuc_siemens_dialekt.cps              # Übung 08: Fanuc vs. Siemens Umschaltung
│   ├── uebung_09_schnittdaten_check.cps                 # Übung 09: Drehzahl- und Vorschubprüfung
│   ├── uebung_10_zweite_aufspannung_g55.cps             # Übung 10: 2. Aufspannung G55
│   ├── uebung_11_gewindebohren_g84.cps                  # Übung 11: Gewindebohren G84
│   ├── uebung_12_radiuskorrektur_g41.cps                # Übung 12: Radiuskorrektur G41/G42/G40
│   ├── uebung_13_3d_freiformflaechen.cps                # Übung 13: 3D-Freiformflächen
│   ├── uebung_14_heidenhain_klartext_4achse.cps         # Übung 14: Heidenhain Klartext & 4. Achse
│   ├── uebung_15_fasenfraesen_entgraten.cps             # Übung 15: Fasenfräsen & Entgraten 45°
│   └── uebung_16_endabnahme_meister_post.cps            # Übung 16: Meister-Post Endabnahme
└── tests/                                               # Test- und Simulationsumgebung (Qualitätssicherung)
    ├── simuliere_post.js                                # Lokaler Simulator (führt jede beliebige .cps-Datei aus)
    ├── mein_generierter_gcode.nc                        # Zuletzt generierter G-Code
    └── output_expected.nc                               # Beispiel-Ausgabe (G-Code-Maschinenprogramm) zum direkten Testen im 3D-Simulator
```

---

## 🚀 Schnellstart: So testen Sie Ihren ersten Postprozessor

### 1. Code ansehen und anpassen
Öffnen Sie die Datei [src/mein_erster_post.cps](file:///C:/Projekte/CNC/src/mein_erster_post.cps).
Dort finden Sie in der Funktion [`onOpen()`](file:///C:/Projekte/CNC/src/mein_erster_post.cps#L125-L215) (Start-Funktion beim Öffnen der Ausgabedatei) bereits Ihren fertig programmierten **Entwickler-Infoblock (Header-Kommentar)** mit:
- Entwickler-Name (`developerName`)
- Automatischem Datum & Uhrzeit (`new Date()`)
- Automatischer **Werkzeugliste (Tool Table – Übersicht aller im Programm verwendeten Fräser und Bohrer)**
- Sicherheits-Startbefehlen (`G90 G21 G17 G40 G49 G80` – **Sicherheitszeile / Safe Start Block zur Grundinitialisierung der CNC-Steuerung**)

### 2. Simulation in Antigravity IDE (Integrierte Entwicklungsumgebung)
1. Installieren Sie im Bereich **Extensions (Erweiterungen)** (`Strg + Umschalt + X`) das offizielle Plugin **`Autodesk Fusion Post Processor Utility`**.
2. Öffnen Sie [src/mein_erster_post.cps](file:///C:/Projekte/CNC/src/mein_erster_post.cps).
3. Öffnen Sie die **Command Palette (Befehlspalette)** mit `Strg + Umschalt + P` und wählen Sie **`Autodesk Fusion Post Processor: Post Process`** (oder drücken Sie die vom Plugin angezeigte Tastenkombination).
4. Wählen Sie eine der mitgelieferten **Benchmark-Dateien (`.cnc` Testdateien)** aus – sofort erscheint rechts daneben der frisch generierte **G-Code (Maschinencode)**!

### 3. Visuelle 3D-Prüfung im Simulator (Backplotter)
1. Öffnen Sie die Datei [tests/output_expected.nc](file:///C:/Projekte/CNC/tests/output_expected.nc) (diese enthält genau den **G-Code**, den `mein_erster_post.cps` erzeugt).
2. Kopieren Sie den gesamten Inhalt (`Strg + A`, dann `Strg + C`).
3. Öffnen Sie im Browser **NCViewer** (`https://ncviewer.com`), fügen Sie den Text im linken Fenster ein und klicken Sie auf **Plot (Zeichnen)** bzw. **Play (Abspielen)**.
4. Sie sehen nun live in 3D (dreidimensional), wie der Fräser das Werkstück bearbeitet!

---

## 📘 Zentrales Übungshandbuch & 3D-Kundenauftrag-Simulation

Alle praktischen Übungen (sowohl für **JavaScript-Postprozessoren** als auch für **3D-Modelle als Kundenauftrag**) sind in einfacher Sprache und mit Schritt-für-Schritt-Erklärungen in dieser zentralen Datei zusammengefasst:

* **[ALLE_UEBUNGEN_HANDBUCH.md](file:///C:/Projekte/CNC/ALLE_UEBUNGEN_HANDBUCH.md)** – Das komplette Übungshandbuch (Übung 1 bis Übung 8), in dem auch alle zukünftigen Übungen gesammelt werden.
* **[kundenauftrag_01_flanschplatte/KUNDEN_AUFTRAG_UND_KLICK_ANLEITUNG.md](file:///C:/Projekte/CNC/kundenauftrag_01_flanschplatte/KUNDEN_AUFTRAG_UND_KLICK_ANLEITUNG.md)** – Komplette Simulation eines echten **3D-Modell-Kundenauftrags (`80 x 50 x 12 mm` Aluminium-Platte)** mit Klick-für-Klick-Anleitung für **Autodesk Fusion (CAD/CAM-Software)**.
* **[kundenauftrag_01_flanschplatte/bauteil_1001.stl](file:///C:/Projekte/CNC/kundenauftrag_01_flanschplatte/bauteil_1001.stl)** – Das echte **3D-Modell (im STL-Format – Standard Tessellation Language)** zum Öffnen in **Autodesk Fusion**, **FreeCAD** oder dem **Windows 3D-Viewer**.
* **[kundenauftrag_01_flanschplatte/3d_auftrag_simulator.html](file:///C:/Projekte/CNC/kundenauftrag_01_flanschplatte/3d_auftrag_simulator.html)** – Interaktiver **3D-Browser-Simulator (per Doppelklick im Browser startbar)**, der das 3D-Bauteil, den **Nullpunkt (`G54`)**, die Werkzeuge (`T01` und `T02`) und den **G-Code (`O1001`)** live animiert darstellt.
* **[kundenauftrag_01_flanschplatte/EINRICHTEBLATT_SETUP_SHEET.md](file:///C:/Projekte/CNC/kundenauftrag_01_flanschplatte/EINRICHTEBLATT_SETUP_SHEET.md)** – Das fertige **Einrichteblatt (`Setup Sheet` – Rüstplan für den Maschinenbediener)** zur Übergabe an den Kunden.
* **[SICHERHEITS_UND_QUALITAETS_PRUEFLISTE_GCODE.md](file:///C:/Projekte/CNC/SICHERHEITS_UND_QUALITAETS_PRUEFLISTE_GCODE.md)** – Das **Sicherheits- und Qualitätsprüfprotokoll für CNC-G-Code** (Null-Kollisions-Garantie, 5-Stufen-Prüfkette und druckbare Checkliste für den Kundenauftrag).

* **Aktualisierter Umfang in [ALLE_UEBUNGEN_HANDBUCH.md](file:///C:/Projekte/CNC/ALLE_UEBUNGEN_HANDBUCH.md):** Enthält jetzt vollständig **alle 16 Haupt-Übungen (`Übung 1` bis `Übung 16`)** sowie die **2 Einsteiger-Vorübungen (`Basis-Übung A` und `Basis-Übung B`)** inklusive direkter Simulator-Prüfanleitungen unter jeder einzelnen Übung!


---

## 🖥️ Wo starte und teste ich die Programme? (Direkt hier in VSC / Antigravity IDE & im Browser)

1. **JavaScript-Code bearbeiten (Oben im VSC / Antigravity IDE Editor):**
   - Öffnen Sie [src/mein_erster_post.cps](file:///C:/Projekte/CNC/src/mein_erster_post.cps), ändern Sie eine Zeile und speichern Sie mit **`Strg + S`**.
2. **Programm ausführen & G-Code erzeugen (Unten im VSC / Antigravity IDE Terminal):**
   - Öffnen Sie das Terminal über das Menü **`Terminal` $\rightarrow$ `New Terminal`** (oder mit **`Strg + Ö`**).
   - Starten Sie den lokalen Simulator-Lauf mit:
     ```powershell
     node tests/simuliere_post.js
     ```
   - Der frisch generierte **G-Code (Maschinencode)** erscheint sofort im Terminal und wird in `tests/mein_generierter_gcode.nc` gespeichert!
3. **3D-Bewegung im Browser anschauen:**
   - **Fertiger 3D-Kundenauftrag-Simulator:** Doppelklick auf [kundenauftrag_01_flanschplatte/3d_auftrag_simulator.html](file:///C:/Projekte/CNC/kundenauftrag_01_flanschplatte/3d_auftrag_simulator.html).
   - **Online-3D-Simulator (`NCViewer`):** Text aus `tests/mein_generierter_gcode.nc` kopieren, auf **`https://ncviewer.com`** links einfügen und auf **`Plot`** klicken.

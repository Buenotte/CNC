# 🚀 CNC-Ingenieurbüro Dipl.-Ing. Buenotte – Zentrale Projekt-Steuerung & Dashboard

Willkommen in der organisierten Entwicklungsumgebung und dem digitalen Ingenieurbüro von **Dipl.-Ing. Buenotte** unter `C:\Projekte\CNC`. 

Dieses Projekt vereint die **Software-Entwicklung von CNC-Postprozessoren *(JavaScript-basierte `.cps`-Übersetzungsskripte für Autodesk Fusion, Python/Tcl für Siemens NX und Heidenhain)*, automatisierte G-Code-Sicherheitsprüfungen** sowie die **vollständig digitale Abwicklung von B2B-Kundenaufträgen *(100 % Remote-Engineering nach § 18 EStG)***.

---

## 🏛️ Die 4 Kernbereiche der Projektstruktur

Das gesamte Workspace ist in **4 logische, streng voneinander getrennte Säulen** unterteilt:

```
c:\Projekte\CNC\
│
├── 📂 01_Kundenauftraege/             ◄── Operatives Kundengeschäft & Auftragsakten
│   ├── 📁 auftragsakten_00b_bis_16/    (Alle 17 abgeschlossenen Kundenakten mit Angebot, Code & Setup Sheet)
│   ├── 📁 test_ubungen/                (Interaktive Testordner: test_auftrag_ubung_03, test_auftrag_ubung_04)
│   └── 📁 referenz_auftrag_flanschplatte/ (Ursprüngliches 3D-Referenzbauteil 1001)
│
├── 📂 02_Software_und_Tools/          ◄── Postprozessor-Entwicklung, Test-Suite & Generatoren
│   ├── 📁 src/                         (Haupt-Postprozessor mein_erster_post.cps)
│   ├── 📁 tests/                       (Lokaler Test-Runner simuliere_post.js & .nc-Outputs)
│   ├── 📁 scripts/                     (Python- & JS-Generatoren, Video-Renderer)
│   ├── 📁 web_tools/                   (Web-Interfaces: Universal 3D CAD/CAM Viewer, CPS- & Video-Generator)
│   └── 📁 GitHub_Projekte/             (cnc_setup_sheet_extractor.py)
│
├── 📂 03_Fachdokumentation_und_Wissen/ ◄── Ingenieurwissen, Handbücher & Sicherheit
│   ├── 📘 ALLE_UEBUNGEN_HANDBUCH.md    (Großes Praxishandbuch aller 17 Übungen)
│   ├── 🛡️ SICHERHEITS_UND_QUALITAETS_PRUEFLISTE_GCODE.md (5-Stufen-Cockpit-Sicherheitscheck)
│   ├── 🔧 FRAESER_UND_BOHRER_PRAXISGUIDE.md (Werkzeuggeometrien, Schneidstoffe, vc-Werte)
│   ├── 🏗️ BAUINGENIEUR_WISSEN_FUER_CNC_GUIDE.md (Transferwissen Statik/Dynamik zu Zerspanung)
│   ├── 📁 docs/                        (Bilder, CAD-Zeichnungen, Renderings & Simulationsvideos)
│   └── 📁 uebungen/                    (Originale Quellcode-Dateien .cps & .nc)
│
└── 📂 04_Recht_Steuern_und_Backoffice/ ◄── Freiberufler-Status, Steuern & KI-Agenten
    ├── 📑 CAM_Nebentaetigkeit_und_Gewerbe_Leitfaden.md (Rechtssicher nach § 18 EStG, FA Hanau)
    ├── 💼 PROFIL_POSITIONIERUNG_UND_KUNDENGESPRAECHE_LEITFADEN.md (LinkedIn/XING-Texte, Einwandbehandlung)
    ├── 🤖 KI_Agenten_System_und_Bauplan.md (System-Prompts & Bauplan deiner 4 KI-Agenten)
    ├── 📁 Vorlagen_Vertraege_Rechnungen/ (Muster-Angebote & § 14 UStG Rechnungen)
    └── 📁 Portfolio/                   (Kunden-Einrichteblätter & Referenz-Präsentationen)
```

---

## 🧭 Schnelleinstieg & Direkte Links zu den wichtigsten Werkzeugen

### 1. Kundengeschäft & Aufträge (Säule 1)
* 👉 **[Zentrale Auftrags-Übersicht (Alle 17 Kundenaufträge)](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/UEBERSICHT_ALLE_KUNDENAUFTRAEGE.md):** Tabelle aller Firmen, Budgets und Direktlinks zu den Auftragsordnern.
* 👉 **[Aktiver Test-Ordner zum Selbermachen (Übung 3)](file:///c:/Projekte/CNC/01_Kundenauftraege/test_ubungen/test_auftrag_ubung_03/WORKFLOW_UND_PROMPTS.md):** Schritt-für-Schritt-Anleitung mit den 4 fertigen Prompts für deine KI-Agenten.
* 👉 **[Neuer Test-Ordner zum Selbermachen (Übung 4)](file:///c:/Projekte/CNC/01_Kundenauftraege/test_ubungen/test_auftrag_ubung_04/KUNDENAUFTRAG.md):** Unberührter Testauftrag für 3D-Lagerplatte (nur Briefing und 3D-Modell).
* 👉 **[Vollständiger Prozessablauf von A bis Z](file:///c:/Projekte/CNC/01_Kundenauftraege/KUNDENAUFTRAG_VOLLSTAENDIGER_PROZESSABLAUF_A_BIS_Z.md):** Wie ein Kundenauftrag von der ersten E-Mail bis zum Geldeingang abläuft.

### 2. Software-Entwicklung & Lokale Test-Suite (Säule 2)
* 👉 **[Haupt-Postprozessor (`src/mein_erster_post.cps`)](file:///c:/Projekte/CNC/02_Software_und_Tools/src/mein_erster_post.cps):** Basis-Postprozessor mit Sicherheitszeile und Werkzeugliste.
* 👉 **[Lokaler Simulator-Runner (`tests/simuliere_post.js`)](file:///c:/Projekte/CNC/02_Software_und_Tools/tests/simuliere_post.js):** Führt jede `.cps`-Datei lokal mit Node.js in unter 1 Sekunde ohne Fusion 360 aus:
  ```powershell
  node 02_Software_und_Tools/tests/simuliere_post.js
  ```
* 👉 **[Python Rüstblatt-Extractor (`cnc_setup_sheet_extractor.py`)](file:///c:/Projekte/CNC/02_Software_und_Tools/GitHub_Projekte/cnc_setup_sheet_extractor.py):** Statische G-Code-Analyse und Einrichteblatt-Erzeugung.
* 👉 **[Web-Interface Postprozessor-Generator](file:///c:/Projekte/CNC/02_Software_und_Tools/web_tools/kunden_cps_generator_web.html):** Grafische Oberfläche zur Konfiguration von Postprozessoren.
* 👉 **[Universal 3D CAD/CAM Viewer & Messwerkzeug](file:///c:/Projekte/CNC/02_Software_und_Tools/web_tools/universal_3d_viewer.html):** Universeller browserbasierter 3D-Viewer mit Drag & Drop für beliebige Kunden-STLs, automatischer 3D-Bemaßung (Länge, Breite, Dicke), Volumen-, Oberflächen- und Bauteilgewichtsberechnung (Aluminium/Stahl) sowie scharfen CAD-Kantenlinien.

### 3. Fachwissen & Qualitätssicherung (Säule 3)
* 👉 **[Großes Praxis-Übungshandbuch (`ALLE_UEBUNGEN_HANDBUCH.md`)](file:///c:/Projekte/CNC/03_Fachdokumentation_und_Wissen/ALLE_UEBUNGEN_HANDBUCH.md):** 17 detaillierte Übungen von *Hallo Welt* bis zur *5-Punkte-Meisterprüfung*.
* 👉 **[Sicherheits- & Qualitätsprüfliste (`SICHERHEITS_UND_QUALITAETS_PRUEFLISTE_GCODE.md`)](file:///c:/Projekte/CNC/03_Fachdokumentation_und_Wissen/SICHERHEITS_UND_QUALITAETS_PRUEFLISTE_GCODE.md):** 5-Stufen-Prüfkette wie im Flugzeugcockpit zur 100 % Null-Kollisions-Garantie.
* 👉 **[Fräser & Bohrer Praxisguide](file:///c:/Projekte/CNC/03_Fachdokumentation_und_Wissen/FRAESER_UND_BOHRER_PRAXISGUIDE.md):** Schnittgeschwindigkeiten $v_c$, Zahnvorschübe $f_z$ und Werkzeugarten.
* 👉 **[Bauingenieur-Wissen für CNC](file:///c:/Projekte/CNC/03_Fachdokumentation_und_Wissen/BAUINGENIEUR_WISSEN_FUER_CNC_GUIDE.md):** Elastizitätstheorie, Schnittkräfte und Schwingungsdämpfung beim Fräsen.

### 4. Recht, Steuern & Backoffice (Säule 4)
* 👉 **[Freiberufler-Leitfaden (§ 18 EStG)](file:///c:/Projekte/CNC/04_Recht_Steuern_und_Backoffice/CAM_Nebentaetigkeit_und_Gewerbe_Leitfaden.md):** Nebentätigkeit, Finanzamt Hanau, Befreiung von Gewerbesteuer und IHK.
* 👉 **[Leitfaden: Profil-Positionierung & Kundengespräche](file:///c:/Projekte/CNC/04_Recht_Steuern_und_Backoffice/PROFIL_POSITIONIERUNG_UND_KUNDENGESPRAECHE_LEITFADEN.md):** Schlüsselfertige Profiltexte für LinkedIn/XING, Argumentationsleitfaden für Telefonate (wie man auch ohne Werkstatterfahrung souverän auftritt) und Haftungsabsicherung.
* 👉 **[KI-Agenten Bauplan & System-Prompts](file:///c:/Projekte/CNC/04_Recht_Steuern_und_Backoffice/KI_Agenten_System_und_Bauplan.md):** Rollen und Prompts für deine 4 KI-Agenten (`Lead-Scout`, `Post-Coder`, `NC-Safety`, `Backoffice`).
* 👉 **[Vorlagen für Angebote & Rechnungen](file:///c:/Projekte/CNC/04_Recht_Steuern_und_Backoffice/Vorlagen_Vertraege_Rechnungen/):** Rechtssichere B2B-Muster mit technischer Haftungsbegrenzung.

---

## 🤖 So steuerst du deine 4 KI-Agenten im Chat:

Schreibe mir hier im Chat einfach einen kurzen Satz, um einen der 4 registrierten Agenten zu aktivieren:
1. **Agent 1 (Akquise):** *„Starte Agent 1: Suche 5 CNC-Fräsereien mit Heidenhain-Steuerung im Raum Hanau/Aschaffenburg.“*
2. **Agent 2 (Software):** *„Starte Agent 2: Passe den Postprozessor an das Referenzprogramm im Ordner XY an.“*
3. **Agent 3 (Sicherheit):** *„Starte Agent 3: Führe den 5-Stufen-Crashcheck für das NC-Programm durch und erstelle das Einrichteblatt.“*
4. **Agent 4 (Backoffice):** *„Starte Agent 4: Erstelle ein B2B-Angebot über 480 € netto nach § 18 EStG für Kunde XY.“*

---

*Inhaber: Dipl.-Ing. Buenotte | Freiberufliches Ingenieurbüro für CAD/CAM-Fertigungstechnik | 63526 Erlensee*

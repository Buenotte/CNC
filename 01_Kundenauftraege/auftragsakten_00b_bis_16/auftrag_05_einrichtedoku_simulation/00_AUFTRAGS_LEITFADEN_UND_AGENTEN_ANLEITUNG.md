# 📘 Auftrags-Leitfaden & Agenten-Bedienungsanleitung
**Auftrags-Ordner:** `auftrag_05_einrichtedoku_simulation`  
**Projekt / Übung:** Übung 05: Einrichteblatt-Extraktion & Simulationsprüfung  
**Auftraggeber:** Thomas Kuhn (Inhaber, Kuhn Medizintechnik & CNC-Fräszentrum)  
**Vereinbartes Budget:** **280,00 € netto**  
**Auftragnehmer:** Dipl.-Ing. Bujanovski – Freiberufliches Ingenieurbüro für CAD/CAM-Fertigungstechnik (§ 18 EStG)  
**Status:** In Bearbeitung / Systematische Abwicklung

---

## 🎯 1. Technisches Ziel dieses Auftrags
Automatisierte Extraktion aller Rüstparameter aus NC-Code via cnc_setup_sheet_extractor.py und visuelle Prüfung im Simulator.

---

## 📂 2. Verbindliche Liste aller Artefakte (Was muss in diesem Ordner stehen?)

Damit dieser Auftrag zu 100 % erledigt ist, müssen **alle folgenden Artefakte direkt in diesem Ordner `auftrag_05_einrichtedoku_simulation` liegen**:

| Artefakt-Name | Dateityp | Zuständiger KI-Agent | Zweck & Inhalt |
| :--- | :---: | :---: | :--- |
| **`00_AUFTRAGS_LEITFADEN_UND_AGENTEN_ANLEITUNG.md`** | Doku | *System* | Diese verbindliche Schritt-für-Schritt-Anleitung. |
| **`KUNDENAUFTRAG_BRIEFING.md`** | Briefing | `Agent 1` / Kunde | Original-Auftrag mit Maschinenpark, Werkzeugen und Vorgaben. |
| **`ANGEBOT_DIPL_ING_BUJANOVSKI.md`** | Vertrag | **`Agent 4`** | Rechtssicheres B2B-Angebot nach § 18 EStG inkl. Haftungsausschluss. |
| **`output_expected.nc (vom Kunden beigestellt)`** | JavaScript | **`Agent 2`** | Maschinenspezifischer Postprozessor-Quellcode. |
| **`06_EINRICHTEBLATT_SETUP_SHEET.md`** | G-Code / Klartext | **`Agent 2`** | Fertig generiertes NC-Maschinenprogramm für die Kundenmaschine. |
| **`05_SICHERHEITS_CRASH_PRUEFBERICHT.md`** | Prüfbericht | **`Agent 3`** | 5-Stufen-Sicherheitsbericht (Crash-Check & Z-MIN Verifikation). |
| **`06_EINRICHTEBLATT_SETUP_SHEET.md`** | Werkstatt-Doku | **`Agent 3`** | Rüst- und Werkzeugdatenblatt für den Maschinenbediener. |
| **`07_RECHNUNG_NACH_PARAGRAPH_18_ESTG.md`** | Abrechnung | **`Agent 4`** | Revisionssichere Honorarabrechnung für das Finanzamt Hanau. |

---

## 🤖 3. Schritt-für-Schritt-Anleitung: So wickelst du diesen Auftrag mit den 4 KI-Agenten ab

Du musst die Arbeit nicht selbst programmieren. Nutze einfach die 4 spezialisierten KI-Agenten:

### Schritt 1: Angebot erstellen & kalkulieren (Agent 4)
* **Aufgabe:** Prüft die Kundenanfrage in `KUNDENAUFTRAG_BRIEFING.md`, kalkuliert den Festpreis von **280,00 € netto** und erstellt das B2B-Angebot.
* **Befehl im Chat:**
  > *„Starte bitte **Agent 4**: Überprüfe das Briefing im Ordner `auftrag_05_einrichtedoku_simulation` und erstelle das formelle Angebot `ANGEBOT_DIPL_ING_BUJANOVSKI.md` inklusive der Klausel zum Einfahren des ersten Bauteils im Einzelsatz.“*

### Schritt 2: Code & Postprozessor umsetzen (Agent 2)
* **Aufgabe:** Stelle sicher, dass alle relevanten Kommentarfelder für den Python-Extractor im NC-Code hinterlegt sind.
* **Befehl im Chat:**
  > *„Starte bitte **Agent 2**: Bearbeite den Postprozessor `output_expected.nc (vom Kunden beigestellt)` im Ordner `auftrag_05_einrichtedoku_simulation`. Automatisierte Extraktion aller Rüstparameter aus NC-Code via cnc_setup_sheet_extractor.py und visuelle Prüfung im Simulator. Generiere im Anschluss das NC-Programm `06_EINRICHTEBLATT_SETUP_SHEET.md`.“*

### Schritt 3: Crash-Prüfung & Einrichteblatt (Agent 3)
* **Aufgabe:** Führe cnc_setup_sheet_extractor.py aus und erstelle das druckfertige Rüstdatenblatt für den Maschinenbediener.
* **Befehl im Chat:**
  > *„Starte bitte **Agent 3**: Führe die 5-Stufen-Sicherheitsprüfung für `06_EINRICHTEBLATT_SETUP_SHEET.md` im Ordner `auftrag_05_einrichtedoku_simulation` durch. Erstelle `05_SICHERHEITS_CRASH_PRUEFBERICHT.md` und das druckfertige Rüstdatenblatt `06_EINRICHTEBLATT_SETUP_SHEET.md`.“*

### Schritt 4: Honorarrechnung stellen (Agent 4)
* **Aufgabe:** Nach erfolgreicher Simulation und Prüfung erstellt Agent 4 die steuersichere Rechnung über **280,00 € netto** nach § 14 UStG und § 18 EStG.
* **Befehl im Chat:**
  > *„Starte bitte **Agent 4**: Der Auftrag `auftrag_05_einrichtedoku_simulation` ist abgeschlossen. Erstelle die steuerlich korrekte Honorarrechnung `07_RECHNUNG_NACH_PARAGRAPH_18_ESTG.md` an Thomas Kuhn (Inhaber, Kuhn Medizintechnik & CNC-Fräszentrum).“*

---

## 🛡️ 4. Abnahme-Kriterien (Wann ist der Auftrag zu 100 % fertig?)
Ein Auftrag gilt erst dann als vollständig abgeschlossen und lieferbereit, wenn:
1. [ ] Alle oben gelisteten Dateien physisch in diesem Ordner `auftrag_05_einrichtedoku_simulation` existieren.
2. [ ] Der Postprozessor `output_expected.nc (vom Kunden beigestellt)` im Simulator fehlerfrei durchläuft.
3. [ ] Im Sicherheitsbericht `05_SICHERHEITS_CRASH_PRUEFBERICHT.md` der Status **BESTANDEN (GRÜN)** dokumentiert ist.
4. [ ] Das Einrichteblatt `06_EINRICHTEBLATT_SETUP_SHEET.md` alle Werkzeuge, Nullpunkte und Drehmomente enthält.
5. [ ] Das Rechnungsdokument `07_RECHNUNG_NACH_PARAGRAPH_18_ESTG.md` für das Finanzamt Hanau abgelegt ist.

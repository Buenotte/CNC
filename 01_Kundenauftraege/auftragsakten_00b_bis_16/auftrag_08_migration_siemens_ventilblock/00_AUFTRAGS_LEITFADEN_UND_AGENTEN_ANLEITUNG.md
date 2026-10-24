# 📘 Auftrags-Leitfaden & Agenten-Bedienungsanleitung
**Auftrags-Ordner:** `auftrag_08_migration_siemens_ventilblock`  
**Projekt / Übung:** Übung 08: Migration auf Siemens Sinumerik Dialekt  
**Auftraggeber:** Jürgen Meier (Fertigungsleiter, Franken Zerspanung GmbH)  
**Vereinbartes Budget:** **650,00 € netto**  
**Auftragnehmer:** Dipl.-Ing. Bujanovski – Freiberufliches Ingenieurbüro für CAD/CAM-Fertigungstechnik (§ 18 EStG)  
**Status:** In Bearbeitung / Systematische Abwicklung

---

## 🎯 1. Technisches Ziel dieses Auftrags
Übersetzung eines Haas/Fanuc-Postprozessors auf Siemens Sinumerik 840D (WORKPIECE, CYCLE800, SUPA G0 Z0 D0).

---

## 📂 2. Verbindliche Liste aller Artefakte (Was muss in diesem Ordner stehen?)

Damit dieser Auftrag zu 100 % erledigt ist, müssen **alle folgenden Artefakte direkt in diesem Ordner `auftrag_08_migration_siemens_ventilblock` liegen**:

| Artefakt-Name | Dateityp | Zuständiger KI-Agent | Zweck & Inhalt |
| :--- | :---: | :---: | :--- |
| **`00_AUFTRAGS_LEITFADEN_UND_AGENTEN_ANLEITUNG.md`** | Doku | *System* | Diese verbindliche Schritt-für-Schritt-Anleitung. |
| **`KUNDENAUFTRAG_BRIEFING.md`** | Briefing | `Agent 1` / Kunde | Original-Auftrag mit Maschinenpark, Werkzeugen und Vorgaben. |
| **`ANGEBOT_DIPL_ING_BUJANOVSKI.md`** | Vertrag | **`Agent 4`** | Rechtssicheres B2B-Angebot nach § 18 EStG inkl. Haftungsausschluss. |
| **`uebung_08_fanuc_siemens_dialekt.cps`** | JavaScript | **`Agent 2`** | Maschinenspezifischer Postprozessor-Quellcode. |
| **`siemens_ventilblock_post.nc`** | G-Code / Klartext | **`Agent 2`** | Fertig generiertes NC-Maschinenprogramm für die Kundenmaschine. |
| **`05_SICHERHEITS_CRASH_PRUEFBERICHT.md`** | Prüfbericht | **`Agent 3`** | 5-Stufen-Sicherheitsbericht (Crash-Check & Z-MIN Verifikation). |
| **`06_EINRICHTEBLATT_SETUP_SHEET.md`** | Werkstatt-Doku | **`Agent 3`** | Rüst- und Werkzeugdatenblatt für den Maschinenbediener. |
| **`07_RECHNUNG_NACH_PARAGRAPH_18_ESTG.md`** | Abrechnung | **`Agent 4`** | Revisionssichere Honorarabrechnung für das Finanzamt Hanau. |

---

## 🤖 3. Schritt-für-Schritt-Anleitung: So wickelst du diesen Auftrag mit den 4 KI-Agenten ab

Du musst die Arbeit nicht selbst programmieren. Nutze einfach die 4 spezialisierten KI-Agenten:

### Schritt 1: Angebot erstellen & kalkulieren (Agent 4)
* **Aufgabe:** Prüft die Kundenanfrage in `KUNDENAUFTRAG_BRIEFING.md`, kalkuliert den Festpreis von **650,00 € netto** und erstellt das B2B-Angebot.
* **Befehl im Chat:**
  > *„Starte bitte **Agent 4**: Überprüfe das Briefing im Ordner `auftrag_08_migration_siemens_ventilblock` und erstelle das formelle Angebot `ANGEBOT_DIPL_ING_BUJANOVSKI.md` inklusive der Klausel zum Einfahren des ersten Bauteils im Einzelsatz.“*

### Schritt 2: Code & Postprozessor umsetzen (Agent 2)
* **Aufgabe:** Passe die Ausgabe an den Siemens-Steuerungsstandard an (Rohteildefinition WORKPIECE, Zyklenaufrufe, Satznummern).
* **Befehl im Chat:**
  > *„Starte bitte **Agent 2**: Bearbeite den Postprozessor `uebung_08_fanuc_siemens_dialekt.cps` im Ordner `auftrag_08_migration_siemens_ventilblock`. Übersetzung eines Haas/Fanuc-Postprozessors auf Siemens Sinumerik 840D (WORKPIECE, CYCLE800, SUPA G0 Z0 D0). Generiere im Anschluss das NC-Programm `siemens_ventilblock_post.nc`.“*

### Schritt 3: Crash-Prüfung & Einrichteblatt (Agent 3)
* **Aufgabe:** Prüfe den Sinumerik-Code auf korrekte D-Korrekturaufrufe (D1) und SUPA-Sicherheitsrückzüge.
* **Befehl im Chat:**
  > *„Starte bitte **Agent 3**: Führe die 5-Stufen-Sicherheitsprüfung für `siemens_ventilblock_post.nc` im Ordner `auftrag_08_migration_siemens_ventilblock` durch. Erstelle `05_SICHERHEITS_CRASH_PRUEFBERICHT.md` und das druckfertige Rüstdatenblatt `06_EINRICHTEBLATT_SETUP_SHEET.md`.“*

### Schritt 4: Honorarrechnung stellen (Agent 4)
* **Aufgabe:** Nach erfolgreicher Simulation und Prüfung erstellt Agent 4 die steuersichere Rechnung über **650,00 € netto** nach § 14 UStG und § 18 EStG.
* **Befehl im Chat:**
  > *„Starte bitte **Agent 4**: Der Auftrag `auftrag_08_migration_siemens_ventilblock` ist abgeschlossen. Erstelle die steuerlich korrekte Honorarrechnung `07_RECHNUNG_NACH_PARAGRAPH_18_ESTG.md` an Jürgen Meier (Fertigungsleiter, Franken Zerspanung GmbH).“*

---

## 🛡️ 4. Abnahme-Kriterien (Wann ist der Auftrag zu 100 % fertig?)
Ein Auftrag gilt erst dann als vollständig abgeschlossen und lieferbereit, wenn:
1. [ ] Alle oben gelisteten Dateien physisch in diesem Ordner `auftrag_08_migration_siemens_ventilblock` existieren.
2. [ ] Der Postprozessor `uebung_08_fanuc_siemens_dialekt.cps` im Simulator fehlerfrei durchläuft.
3. [ ] Im Sicherheitsbericht `05_SICHERHEITS_CRASH_PRUEFBERICHT.md` der Status **BESTANDEN (GRÜN)** dokumentiert ist.
4. [ ] Das Einrichteblatt `06_EINRICHTEBLATT_SETUP_SHEET.md` alle Werkzeuge, Nullpunkte und Drehmomente enthält.
5. [ ] Das Rechnungsdokument `07_RECHNUNG_NACH_PARAGRAPH_18_ESTG.md` für das Finanzamt Hanau abgelegt ist.

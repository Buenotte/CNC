# 📋 Workflow-Beschreibung & Prompts: Auftrag 06: Sicherer Rückzug (Safe Retract) & Tisch zur Tür

Mit dieser Anleitung wickelst du den Kundenauftrag aus [`KUNDENAUFTRAG.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_06_sicherer_rueckzug_arbeitsschutz/KUNDENAUFTRAG.md) Schritt für Schritt mit deinen 4 KI-Agenten ab.

Kopiere nacheinander die folgenden **4 Prompts** in unseren Chat. Die Agenten erzeugen dann alle geforderten Artefakte direkt in diesem Ordner [`auftrag_06_sicherer_rueckzug_arbeitsschutz`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_06_sicherer_rueckzug_arbeitsschutz).

---

## 🗂️ 1. Welche Artefakte werden erzeugt und wo genau stehen sie?

| Artefakt-Dateiname | Was ist das? | Wo steht die Datei? *(Speicherort)* | Wer erzeugt sie? |
| :--- | :--- | :--- | :---: |
| **`02_ANGEBOT_DIPL_ING_BUENOTTE.md`** | Rechtssicheres B2B-Angebot (420,00 € netto) | [`02_ANGEBOT_DIPL_ING_BUENOTTE.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_06_sicherer_rueckzug_arbeitsschutz/02_ANGEBOT_DIPL_ING_BUENOTTE.md) | **Agent 4** *(Backoffice)* |
| **`uebung_06_sicherer_rueckzug.nc`** | Fertiger Maschinencode für Mazak VTC-800/30SR (Mazatrol Matrix 2) | [`uebung_06_sicherer_rueckzug.nc`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_06_sicherer_rueckzug_arbeitsschutz/uebung_06_sicherer_rueckzug.nc) | **Agent 2** *(Post-Coder)* |
| **`05_SICHERHEITS_CRASH_PRUEFBERICHT.md`** | 5-Stufen-Sicherheitsprüfbericht *(Null-Kollisions-Garantie)* | [`05_SICHERHEITS_CRASH_PRUEFBERICHT.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_06_sicherer_rueckzug_arbeitsschutz/05_SICHERHEITS_CRASH_PRUEFBERICHT.md) | **Agent 3** *(NC-Safety)* |
| **`06_EINRICHTEBLATT_SETUP_SHEET.md`** | Rüstdatenblatt für den Maschinenbediener vor Ort | [`06_EINRICHTEBLATT_SETUP_SHEET.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_06_sicherer_rueckzug_arbeitsschutz/06_EINRICHTEBLATT_SETUP_SHEET.md) | **Agent 3** *(NC-Safety)* |
| **`07_RECHNUNG_NACH_PARAGRAPH_18_ESTG.md`** | Revisionssichere Honorarrechnung (499,80 € brutto) | [`07_RECHNUNG_NACH_PARAGRAPH_18_ESTG.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_06_sicherer_rueckzug_arbeitsschutz/07_RECHNUNG_NACH_PARAGRAPH_18_ESTG.md) | **Agent 4** *(Backoffice)* |

---

## 🧭 2. Der 4-Stufen-Workflow im Überblick:

```
                  1. KUNDENAUFTRAG.md (Liegt bereits im Ordner)
                             │
                             ▼
 ┌────────────────────────────────────────────────────────────────────────┐
 │ SCHRITT 1: ANGEBOT ERSTELLEN (Agent 4: Backoffice-Agent)              │
 │ Prompt 1 ausführen ──► Erzeugt: 02_ANGEBOT_DIPL_ING_BUENOTTE.md        │
 └───────────────────────────┬────────────────────────────────────────────┘
                             │
                             ▼
 ┌────────────────────────────────────────────────────────────────────────┐
 │ SCHRITT 2: NC-MASCHINENCODE GENERIEREN (Agent 2: Postprocessor-Coder)  │
 │ Prompt 2 ausführen ──► Erzeugt: uebung_06_sicherer_rueckzug.nc
 └───────────────────────────┬────────────────────────────────────────────┘
                             │
                             ▼
 ┌────────────────────────────────────────────────────────────────────────┐
 │ SCHRITT 3: SICHERHEIT & EINRICHTEBLATT (Agent 3: NC-Safety-Agent)      │
 │ Prompt 3 ausführen ──► Erzeugt: 05_SICHERHEITS_CRASH_PRUEFBERICHT.md   │
 │                    ──► Erzeugt: 06_EINRICHTEBLATT_SETUP_SHEET.md       │
 └───────────────────────────┬────────────────────────────────────────────┘
                             │
                             ▼
 ┌────────────────────────────────────────────────────────────────────────┐
 │ SCHRITT 4: RECHNUNG STELLEN (Agent 4: Backoffice-Agent)                │
 │ Prompt 4 ausführen ──► Erzeugt: 07_RECHNUNG_NACH_PARAGRAPH_18_ESTG.md  │
 └────────────────────────────────────────────────────────────────────────┘
```

---

## 💬 3. Die 4 fertigen Prompts & wie du jedes Artefakt testest:

### 🟢 SCHRITT 1: Angebot erstellen (Agent 4)
#### Prompt zum Kopieren in den Chat:
```text
Starte bitte Agent 4 (Backoffice-Agent):
Lies die Kundenanfrage in c:\Projekte\CNC\01_Kundenauftraege\auftragsakten_00b_bis_16\auftrag_06_sicherer_rueckzug_arbeitsschutz\KUNDENAUFTRAG.md.
Erstelle direkt im Ordner c:\Projekte\CNC\01_Kundenauftraege\auftragsakten_00b_bis_16\auftrag_06_sicherer_rueckzug_arbeitsschutz\ das formelle B2B-Angebot "02_ANGEBOT_DIPL_ING_BUENOTTE.md" für Andreas Eder (Betriebsleiter) (Süd-Zerspanung GmbH) über 420,00 € netto. Verwende ausschließlich ingenieurmäßige Leistungsbeschreibungen nach § 18 EStG und binde die verbindliche Haftungsausschluss-Klausel für das Einfahren des ersten Werkstücks im Einzelsatz ein.
```

#### 🔍 Wie wird das Angebot getestet und geprüft?
1. **Honorar:** Steht exakt der Festpreis von **420,00 € netto** drin?
2. **Freiberufler-Status:** Enthält die Leistungsbeschreibung ingenieurmäßige Begriffe nach § 18 EStG *(keine Einstufung als Gewerbe durch das Finanzamt Hanau)*?
3. **Haftungsausschluss:** Verpflichtung des Kunden zum Einfahren des ersten Werkstücks im Einzelsatz *(Single Block)* an der Mazak VTC-800/30SR (Mazatrol Matrix 2) enthalten?

---

### 🔵 SCHRITT 2: NC-Maschinencode generieren (Agent 2)
#### Prompt zum Kopieren in den Chat:
```text
Starte bitte Agent 2 (Postprocessor-Coder-Agent):
Generiere für die Mazak VTC-800/30SR (Mazatrol Matrix 2) im Ordner c:\Projekte\CNC\01_Kundenauftraege\auftragsakten_00b_bis_16\auftrag_06_sicherer_rueckzug_arbeitsschutz\ das fertige NC-Programm "uebung_06_sicherer_rueckzug.nc".
Anforderung: Zwingende sequentielle Trennung in onClose(): Zuerst Z-Achse absolut sicher auf Maschinenhöhe (G53 G0 Z0 / M91), erst danach Tisch Y nach vorne zur Bedienertür.
Stelle sicher, dass alle Werkzeugaufrufe, Sicherheitszeilen und Programmabschlüsse fehlerfrei implementiert sind.
```

#### 🔍 Wie wird der generierte NC-Code getestet und geprüft?
1. **Syntax-Check:** Satz-für-Satz Kontrolle am Programmende: G53 Z0 muss zwingend vor G53 Y0 stehen (keine Diagonalbewegung!).
2. **Simulation:** Lade den Code in [NCViewer.com](https://ncviewer.com) oder führe ihn lokal aus. Fahren alle Achsen kollisionsfrei ab?

---

### 🛡️ SCHRITT 3: Sicherheitsbericht & Einrichteblatt erstellen (Agent 3)
#### Prompt zum Kopieren in den Chat:
```text
Starte bitte Agent 3 (NC-Safety- & Setup-Agent):
Führe für die Datei "uebung_06_sicherer_rueckzug.nc" im Ordner c:\Projekte\CNC\01_Kundenauftraege\auftragsakten_00b_bis_16\auftrag_06_sicherer_rueckzug_arbeitsschutz\ die 5-Stufen-Sicherheitsprüfung nach SICHERHEITS_UND_QUALITAETS_PRUEFLISTE_GCODE.md durch.
Erstelle im selben Ordner:
1. "05_SICHERHEITS_CRASH_PRUEFBERICHT.md" mit Freigabestatus BESTANDEN.
2. "06_EINRICHTEBLATT_SETUP_SHEET.md" als druckfertiges Rüstblatt für den Bediener an der Mazak VTC-800/30SR (Mazatrol Matrix 2) inklusive Werkzeugliste.
```

#### 🔍 Wie werden Sicherheitsbericht und Einrichteblatt getestet und geprüft?
1. **Sicherheitsbericht:** Ergonomie-Check: Steht der Maschinentisch am Programmende ergonomisch optimal zur Tür für schnellen Werkstückwechsel? Status muss **BESTANDEN (GRÜN)** sein.
2. **Einrichteblatt:** Sind alle Werkzeuge mit Mindest-Auskraglängen $L_{min}$, Drehzahlen und Nullpunktlagen vollständig gelistet?

---

### 💰 SCHRITT 4: Rechnungsstellung nach § 18 EStG (Agent 4)
#### Prompt zum Kopieren in den Chat:
```text
Starte bitte Agent 4 (Backoffice-Agent):
Der Auftrag im Ordner c:\Projekte\CNC\01_Kundenauftraege\auftragsakten_00b_bis_16\auftrag_06_sicherer_rueckzug_arbeitsschutz\ ist technisch erfolgreich abgeschlossen und freigegeben.
Erstelle jetzt im selben Ordner die steuersichere Honorarrechnung "07_RECHNUNG_NACH_PARAGRAPH_18_ESTG.md" über 420,00 € netto (499,80 € brutto) an Süd-Zerspanung GmbH mit allen Pflichtangaben nach § 14 UStG und freiberuflicher Leistungsabgrenzung für das Finanzamt Hanau.
```

#### 🔍 Wie wird die Rechnung getestet und geprüft?
1. **Betrag:** Netto-Honorar 420,00 € netto zzgl. 19 % USt. = **499,80 € brutto**.
2. **Steuerliche Pflichtangaben:** Eindeutige Rechnungsnummer, Leistungszeitraum, USt-Ausweis nach § 14 UStG und § 18 EStG Vermerk.

---

## 🛡️ 4. Abnahme-Kriterien (Checkliste für 100 % Erledigung)
* [ ] [`02_ANGEBOT_DIPL_ING_BUENOTTE.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_06_sicherer_rueckzug_arbeitsschutz/02_ANGEBOT_DIPL_ING_BUENOTTE.md) existiert und wurde geprüft.
* [ ] [`uebung_06_sicherer_rueckzug.nc`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_06_sicherer_rueckzug_arbeitsschutz/uebung_06_sicherer_rueckzug.nc) existiert und lief fehlerfrei im Simulator.
* [ ] [`05_SICHERHEITS_CRASH_PRUEFBERICHT.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_06_sicherer_rueckzug_arbeitsschutz/05_SICHERHEITS_CRASH_PRUEFBERICHT.md) bescheinigt Status **BESTANDEN (GRÜN)**.
* [ ] [`06_EINRICHTEBLATT_SETUP_SHEET.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_06_sicherer_rueckzug_arbeitsschutz/06_EINRICHTEBLATT_SETUP_SHEET.md) liegt vor.
* [ ] [`07_RECHNUNG_NACH_PARAGRAPH_18_ESTG.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_06_sicherer_rueckzug_arbeitsschutz/07_RECHNUNG_NACH_PARAGRAPH_18_ESTG.md) ist für das Finanzamt Hanau abgelegt.

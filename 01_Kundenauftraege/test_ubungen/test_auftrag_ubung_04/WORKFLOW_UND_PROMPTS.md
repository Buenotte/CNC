# 📋 Workflow-Beschreibung & Prompts: Auftrag 04: 3D-CAD-Modellbearbeitung (Lagerplatte)

Mit dieser Anleitung wickelst du den Kundenauftrag aus [`KUNDENAUFTRAG.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/test_auftrag_ubung_04/KUNDENAUFTRAG.md) Schritt für Schritt mit deinen 4 KI-Agenten ab.

Kopiere nacheinander die folgenden **4 Prompts** in unseren Chat. Die Agenten erzeugen dann alle geforderten Artefakte direkt in diesem Ordner [`test_auftrag_ubung_04`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/test_auftrag_ubung_04).

---

## 🗂️ 1. Welche Artefakte werden erzeugt und wo genau stehen sie?

| Artefakt-Dateiname | Was ist das? | Wo steht die Datei? *(Speicherort)* | Wer erzeugt sie? |
| :--- | :--- | :--- | :---: |
| **`02_ANGEBOT_DIPL_ING_BUENOTTE.md`** | Rechtssicheres B2B-Angebot (380,00 € netto) | [`02_ANGEBOT_DIPL_ING_BUENOTTE.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/test_auftrag_ubung_04/02_ANGEBOT_DIPL_ING_BUENOTTE.md) | **Agent 4** *(Backoffice)* |
| **`kunden_auftrag_04.nc`** | Fertiger Maschinencode für Haas VF-2 (Haas NGC Steuerung) | [`kunden_auftrag_04.nc`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/test_auftrag_ubung_04/kunden_auftrag_04.nc) | **Agent 2** *(Post-Coder)* |
| **`05_SICHERHEITS_CRASH_PRUEFBERICHT.md`** | 5-Stufen-Sicherheitsprüfbericht *(Null-Kollisions-Garantie)* | [`05_SICHERHEITS_CRASH_PRUEFBERICHT.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/test_auftrag_ubung_04/05_SICHERHEITS_CRASH_PRUEFBERICHT.md) | **Agent 3** *(NC-Safety)* |
| **`06_EINRICHTEBLATT_SETUP_SHEET.md`** | Rüstdatenblatt für den Maschinenbediener vor Ort | [`06_EINRICHTEBLATT_SETUP_SHEET.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/test_auftrag_ubung_04/06_EINRICHTEBLATT_SETUP_SHEET.md) | **Agent 3** *(NC-Safety)* |
| **`07_RECHNUNG_NACH_PARAGRAPH_18_ESTG.md`** | Revisionssichere Honorarrechnung (452,20 € brutto) | [`07_RECHNUNG_NACH_PARAGRAPH_18_ESTG.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/test_auftrag_ubung_04/07_RECHNUNG_NACH_PARAGRAPH_18_ESTG.md) | **Agent 4** *(Backoffice)* |

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
 │ Prompt 2 ausführen ──► Erzeugt: kunden_auftrag_04.nc
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
Lies die Kundenanfrage in c:\Projekte\CNC\01_Kundenauftraege\auftragsakten_00b_bis_16\test_auftrag_ubung_04\KUNDENAUFTRAG.md.
Erstelle direkt im Ordner c:\Projekte\CNC\01_Kundenauftraege\auftragsakten_00b_bis_16\test_auftrag_ubung_04\ das formelle B2B-Angebot "02_ANGEBOT_DIPL_ING_BUENOTTE.md" für Michael Brandner (Fertigungsleiter) (Franken Präzisionsteile GmbH) über 380,00 € netto. Verwende ausschließlich ingenieurmäßige Leistungsbeschreibungen nach § 18 EStG und binde die verbindliche Haftungsausschluss-Klausel für das Einfahren des ersten Werkstücks im Einzelsatz ein.
```

#### 🔍 Wie wird das Angebot getestet und geprüft?
1. **Honorar:** Steht exakt der Festpreis von **380,00 € netto** drin?
2. **Freiberufler-Status:** Enthält die Leistungsbeschreibung ingenieurmäßige Begriffe nach § 18 EStG *(keine Einstufung als Gewerbe durch das Finanzamt Hanau)*?
3. **Haftungsausschluss:** Verpflichtung des Kunden zum Einfahren des ersten Werkstücks im Einzelsatz *(Single Block)* an der Haas VF-2 (Haas NGC Steuerung) enthalten?

---

### 🔵 SCHRITT 2: NC-Maschinencode generieren (Agent 2)
#### Prompt zum Kopieren in den Chat:
```text
Starte bitte Agent 2 (Postprocessor-Coder-Agent):
Generiere für die Haas VF-2 (Haas NGC Steuerung) im Ordner c:\Projekte\CNC\01_Kundenauftraege\auftragsakten_00b_bis_16\test_auftrag_ubung_04\ das fertige NC-Programm "kunden_auftrag_04.nc".
Anforderung: Komplette 2,5D-Auslegung der Lagerplatte aus 3D-Modell (Planfräsen, 2D-Kontur Z -5 mm, Kreistasche Z -3 mm, 4 Bohrungen D=6 mm Z -12 mm).
Stelle sicher, dass alle Werkzeugaufrufe, Sicherheitszeilen und Programmabschlüsse fehlerfrei implementiert sind.
```

#### 🔍 Wie wird der generierte NC-Code getestet und geprüft?
1. **Syntax-Check:** Simulation in NCViewer: Prüfung, dass Bohrer T02 die Bohrungen vollständig durchbohrt (Z -12.0 mm), aber nicht in den Schraubstock sticht.
2. **Simulation:** Lade den Code in [NCViewer.com](https://ncviewer.com) oder führe ihn lokal aus. Fahren alle Achsen kollisionsfrei ab?

---

### 🛡️ SCHRITT 3: Sicherheitsbericht & Einrichteblatt erstellen (Agent 3)
#### Prompt zum Kopieren in den Chat:
```text
Starte bitte Agent 3 (NC-Safety- & Setup-Agent):
Führe für die Datei "kunden_auftrag_04.nc" im Ordner c:\Projekte\CNC\01_Kundenauftraege\auftragsakten_00b_bis_16\test_auftrag_ubung_04\ die 5-Stufen-Sicherheitsprüfung nach SICHERHEITS_UND_QUALITAETS_PRUEFLISTE_GCODE.md durch.
Erstelle im selben Ordner:
1. "05_SICHERHEITS_CRASH_PRUEFBERICHT.md" mit Freigabestatus BESTANDEN.
2. "06_EINRICHTEBLATT_SETUP_SHEET.md" als druckfertiges Rüstblatt für den Bediener an der Haas VF-2 (Haas NGC Steuerung) inklusive Werkzeugliste.
```

#### 🔍 Wie werden Sicherheitsbericht und Einrichteblatt getestet und geprüft?
1. **Sicherheitsbericht:** Prüfung der Tiefenstaffelung im Einrichteblatt mit Mindest-Auskraglängen L_min >= 25 mm. Status muss **BESTANDEN (GRÜN)** sein.
2. **Einrichteblatt:** Sind alle Werkzeuge mit Mindest-Auskraglängen $L_{min}$, Drehzahlen und Nullpunktlagen vollständig gelistet?

---

### 💰 SCHRITT 4: Rechnungsstellung nach § 18 EStG (Agent 4)
#### Prompt zum Kopieren in den Chat:
```text
Starte bitte Agent 4 (Backoffice-Agent):
Der Auftrag im Ordner c:\Projekte\CNC\01_Kundenauftraege\auftragsakten_00b_bis_16\test_auftrag_ubung_04\ ist technisch erfolgreich abgeschlossen und freigegeben.
Erstelle jetzt im selben Ordner die steuersichere Honorarrechnung "07_RECHNUNG_NACH_PARAGRAPH_18_ESTG.md" über 380,00 € netto (452,20 € brutto) an Franken Präzisionsteile GmbH mit allen Pflichtangaben nach § 14 UStG und freiberuflicher Leistungsabgrenzung für das Finanzamt Hanau.
```

#### 🔍 Wie wird die Rechnung getestet und geprüft?
1. **Betrag:** Netto-Honorar 380,00 € netto zzgl. 19 % USt. = **452,20 € brutto**.
2. **Steuerliche Pflichtangaben:** Eindeutige Rechnungsnummer, Leistungszeitraum, USt-Ausweis nach § 14 UStG und § 18 EStG Vermerk.

---

## 🛡️ 4. Abnahme-Kriterien (Checkliste für 100 % Erledigung)
* [ ] [`02_ANGEBOT_DIPL_ING_BUENOTTE.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/test_auftrag_ubung_04/02_ANGEBOT_DIPL_ING_BUENOTTE.md) existiert und wurde geprüft.
* [ ] [`kunden_auftrag_04.nc`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/test_auftrag_ubung_04/kunden_auftrag_04.nc) existiert und lief fehlerfrei im Simulator.
* [ ] [`05_SICHERHEITS_CRASH_PRUEFBERICHT.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/test_auftrag_ubung_04/05_SICHERHEITS_CRASH_PRUEFBERICHT.md) bescheinigt Status **BESTANDEN (GRÜN)**.
* [ ] [`06_EINRICHTEBLATT_SETUP_SHEET.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/test_auftrag_ubung_04/06_EINRICHTEBLATT_SETUP_SHEET.md) liegt vor.
* [ ] [`07_RECHNUNG_NACH_PARAGRAPH_18_ESTG.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/test_auftrag_ubung_04/07_RECHNUNG_NACH_PARAGRAPH_18_ESTG.md) ist für das Finanzamt Hanau abgelegt.

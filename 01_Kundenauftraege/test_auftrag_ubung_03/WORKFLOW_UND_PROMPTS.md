# 📋 Workflow-Beschreibung & Prompts zur Erledigung des Auftrags

Mit dieser Anleitung kannst du den Kundenauftrag aus [`KUNDENAUFTRAG.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/test_auftrag_ubung_03/KUNDENAUFTRAG.md) Schritt für Schritt mithilfe deiner 4 KI-Agenten bearbeiten.

Kopiere einfach nacheinander die folgenden **4 Prompts** in unseren Chat. Die Agenten erzeugen dann alle geforderten Artefakte direkt in diesem Ordner [`c:\Projekte\CNC\01_Kundenauftraege\test_auftrag_ubung_03\`](file:///c:/Projekte/CNC/01_Kundenauftraege/test_auftrag_ubung_03).

---

## 🧭 Der 4-Stufen-Workflow im Überblick:

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
 │ Prompt 2 ausführen ──► Erzeugt: uebung_03_z_min_berechnung.nc          │
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

## 💬 Die 4 fertigen Prompts zum Kopieren:

### 🟢 Prompt 1: Angebot erstellen (Agent 4)
Kopiere diesen Text in den Chat:
```text
Starte bitte Agent 4 (Backoffice-Agent):
Lies die Kundenanfrage in c:\Projekte\CNC\01_Kundenauftraege\test_auftrag_ubung_03\KUNDENAUFTRAG.md.
Erstelle direkt im Ordner c:\Projekte\CNC\01_Kundenauftraege\test_auftrag_ubung_03\ das formelle B2B-Angebot "02_ANGEBOT_DIPL_ING_BUENOTTE.md" für Markus Weber (Schmidt Präzisionstechnik GmbH) über 480,00 € netto. Verwende ausschließlich ingenieurmäßige Leistungsbeschreibungen nach § 18 EStG und binde die verbindliche Haftungsausschluss-Klausel für das Einfahren des ersten Werkstücks im Einzelsatz ein.
```

---

### 🔵 Prompt 2: NC-Maschinencode mit Z-MIN Berechnung erstellen (Agent 2)
Kopiere diesen Text in den Chat:
```text
Starte bitte Agent 2 (Postprocessor-Coder-Agent):
Generiere für die Haas VF-2 Fräsmaschine im Ordner c:\Projekte\CNC\01_Kundenauftraege\test_auftrag_ubung_03\ das fertige NC-Programm "uebung_03_z_min_berechnung.nc" für die Flanschplatte aus dem 3D-Modell bauteil_1001.stl.
Integriere im Header die exakte Z-MIN Tiefenberechnung für Werkzeug T01 (Außenkontur Z -5.0 mm, Kreistasche Z -3.0 mm) und den Nullpunkt G54 vorne links oben, damit der Maschinenbediener vor Crashs mit den Schraubstockbacken gewarnt wird.
```

---

### 🛡️ Prompt 3: Sicherheitsbericht & Einrichteblatt erstellen (Agent 3)
Kopiere diesen Text in den Chat:
```text
Starte bitte Agent 3 (NC-Safety- & Setup-Agent):
Führe für die Datei "uebung_03_z_min_berechnung.nc" im Ordner c:\Projekte\CNC\01_Kundenauftraege\test_auftrag_ubung_03\ die 5-Stufen-Sicherheitsprüfung nach SICHERHEITS_UND_QUALITAETS_PRUEFLISTE_GCODE.md durch.
Prüfe insbesondere den Z-MIN Abstand von Z = -5.0 mm zu den Schraubstockbacken bei Z = -12.0 mm (Spannrand 3.0 mm).
Erstelle im selben Ordner:
1. "05_SICHERHEITS_CRASH_PRUEFBERICHT.md" mit Freigabestatus BESTANDEN.
2. "06_EINRICHTEBLATT_SETUP_SHEET.md" als druckfertiges Rüstblatt für den Werkstattbediener inklusive Werkzeugliste und Nullpunkt G54.
```

---

### 💰 Prompt 4: Rechnungsstellung nach § 18 EStG (Agent 4)
Kopiere diesen Text in den Chat:
```text
Starte bitte Agent 4 (Backoffice-Agent):
Der Auftrag im Ordner c:\Projekte\CNC\01_Kundenauftraege\test_auftrag_ubung_03\ ist technisch erfolgreich abgeschlossen.
Erstelle jetzt im selben Ordner die steuersichere Honorarrechnung "07_RECHNUNG_NACH_PARAGRAPH_18_ESTG.md" über 480,00 € netto (571,20 € brutto) an die Schmidt Präzisionstechnik GmbH mit allen Pflichtangaben nach § 14 UStG und freiberuflicher Leistungsabgrenzung für das Finanzamt Hanau.
```

---

## 🛡️ Abnahmekriterien (Wann ist der Test abgeschlossen?)

Sobald du die 4 Prompts ausgeführt hast, befinden sich alle geforderten Artefakte in deinem Test-Ordner:
* [ ] [`02_ANGEBOT_DIPL_ING_BUENOTTE.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/test_auftrag_ubung_03/02_ANGEBOT_DIPL_ING_BUENOTTE.md) existiert.
* [ ] [`uebung_03_z_min_berechnung.nc`](file:///c:/Projekte/CNC/01_Kundenauftraege/test_auftrag_ubung_03/uebung_03_z_min_berechnung.nc) existiert mit Z-MIN Header.
* [ ] [`05_SICHERHEITS_CRASH_PRUEFBERICHT.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/test_auftrag_ubung_03/05_SICHERHEITS_CRASH_PRUEFBERICHT.md) bescheinigt Status **BESTANDEN (GRÜN)**.
* [ ] [`06_EINRICHTEBLATT_SETUP_SHEET.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/test_auftrag_ubung_03/06_EINRICHTEBLATT_SETUP_SHEET.md) liegt vor.
* [ ] [`07_RECHNUNG_NACH_PARAGRAPH_18_ESTG.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/test_auftrag_ubung_03/07_RECHNUNG_NACH_PARAGRAPH_18_ESTG.md) ist abgelegt.

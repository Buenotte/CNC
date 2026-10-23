# 📘 Auftrags-Leitfaden & Agenten-Bedienungsanleitung
**Auftrags-Ordner:** `test_auftrag_ubung_04`  
**Projekt / Übung:** Übung 04: 3D-CAD-Modellbearbeitung (Lagerplatte)  
**Auftraggeber:** Michael Brandner (Fertigungsleiter, Franken Präzisionsteile GmbH)  
**Vereinbartes Budget:** **380,00 € netto**  
**Auftragnehmer:** Dipl.-Ing. Buenotte – Freiberufliches Ingenieurbüro für CAD/CAM-Fertigungstechnik (§ 18 EStG)  
**Status:** In Bearbeitung / Systematische Abwicklung

---

## 🎯 1. Technisches Ziel dieses Auftrags
Komplette 2,5D- und 3D-Bearbeitung eines Bauteils (Planfräsen, 2D-Kontur, Kreistasche und Bohrbild) aus 3D-STEP/STL.

---

## 📂 2. Verbindliche Liste aller Artefakte (Was muss in diesem Ordner stehen?)

Damit dieser Auftrag zu 100 % erledigt ist, müssen **alle folgenden Artefakte direkt in diesem Ordner `test_auftrag_ubung_04` liegen**:

| Artefakt-Name | Dateityp | Zuständiger KI-Agent | Zweck & Inhalt |
| :--- | :---: | :---: | :--- |
| **`00_AUFTRAGS_LEITFADEN_UND_AGENTEN_ANLEITUNG.md`** | Doku | *System* | Diese verbindliche Schritt-für-Schritt-Anleitung. |
| **`KUNDENAUFTRAG_BRIEFING.md`** | Briefing | `Agent 1` / Kunde | Original-Auftrag mit Maschinenpark, Werkzeugen und Vorgaben. |
| **`02_ANGEBOT_DIPL_ING_BUENOTTE.md`** | Vertrag | **`Agent 4`** | Rechtssicheres B2B-Angebot nach § 18 EStG inkl. Haftungsausschluss. |
| **`kunden_auftrag_04.cps`** | JavaScript | **`Agent 2`** | Maschinenspezifischer Postprozessor-Quellcode. |
| **`kunden_auftrag_04.nc`** | G-Code / Klartext | **`Agent 2`** | Fertig generiertes NC-Maschinenprogramm für die Kundenmaschine. |
| **`05_SICHERHEITS_CRASH_PRUEFBERICHT.md`** | Prüfbericht | **`Agent 3`** | 5-Stufen-Sicherheitsbericht (Crash-Check & Z-MIN Verifikation). |
| **`06_EINRICHTEBLATT_SETUP_SHEET.md`** | Werkstatt-Doku | **`Agent 3`** | Rüst- und Werkzeugdatenblatt für den Maschinenbediener. |
| **`07_RECHNUNG_NACH_PARAGRAPH_18_ESTG.md`** | Abrechnung | **`Agent 4`** | Revisionssichere Honorarabrechnung für das Finanzamt Hanau. |

---

## 🤖 3. Schritt-für-Schritt-Anleitung: So wickelst du diesen Auftrag mit den 4 KI-Agenten ab

Du musst die Arbeit nicht selbst programmieren. Nutze einfach die 4 spezialisierten KI-Agenten:

### Schritt 1: Angebot erstellen & kalkulieren (Agent 4)
* **Aufgabe:** Prüft die Kundenanfrage in `KUNDENAUFTRAG_BRIEFING.md`, kalkuliert den Festpreis von **380,00 € netto** und erstellt das B2B-Angebot.
* **Befehl im Chat:**
  > *„Starte bitte **Agent 4**: Überprüfe das Briefing im Ordner `test_auftrag_ubung_04` und erstelle das formelle Angebot `02_ANGEBOT_DIPL_ING_BUENOTTE.md` inklusive der Klausel zum Einfahren des ersten Bauteils im Einzelsatz.“*

### Schritt 2: Code & Postprozessor umsetzen (Agent 2)
* **Aufgabe:** Generiere die optimierten Werkzeugbahnen für die Lagerplatte und passe die Schnittparameter an.
* **Befehl im Chat:**
  > *„Starte bitte **Agent 2**: Bearbeite den Postprozessor `kunden_auftrag_04.cps` im Ordner `test_auftrag_ubung_04`. Komplette 2,5D- und 3D-Bearbeitung eines Bauteils (Planfräsen, 2D-Kontur, Kreistasche und Bohrbild) aus 3D-STEP/STL. Generiere im Anschluss das NC-Programm `kunden_auftrag_04.nc`.“*

### Schritt 3: Crash-Prüfung & Einrichteblatt (Agent 3)
* **Aufgabe:** Prüfe die Bahnübergänge und stelle sicher, dass kein Werkzeug im Eilgang ins Rohteil eintaucht.
* **Befehl im Chat:**
  > *„Starte bitte **Agent 3**: Führe die 5-Stufen-Sicherheitsprüfung für `kunden_auftrag_04.nc` im Ordner `test_auftrag_ubung_04` durch. Erstelle `05_SICHERHEITS_CRASH_PRUEFBERICHT.md` und das druckfertige Rüstdatenblatt `06_EINRICHTEBLATT_SETUP_SHEET.md`.“*

### Schritt 4: Honorarrechnung stellen (Agent 4)
* **Aufgabe:** Nach erfolgreicher Simulation und Prüfung erstellt Agent 4 die steuersichere Rechnung über **380,00 € netto** nach § 14 UStG und § 18 EStG.
* **Befehl im Chat:**
  > *„Starte bitte **Agent 4**: Der Auftrag `test_auftrag_ubung_04` ist abgeschlossen. Erstelle die steuerlich korrekte Honorarrechnung `07_RECHNUNG_NACH_PARAGRAPH_18_ESTG.md` an Michael Brandner (Fertigungsleiter, Franken Präzisionsteile GmbH).“*

---

## 🛡️ 4. Abnahme-Kriterien (Wann ist der Auftrag zu 100 % fertig?)
Ein Auftrag gilt erst dann als vollständig abgeschlossen und lieferbereit, wenn:
1. [ ] Alle oben gelisteten Dateien physisch in diesem Ordner `test_auftrag_ubung_04` existieren.
2. [ ] Der Postprozessor `kunden_auftrag_04.cps` im Simulator fehlerfrei durchläuft.
3. [ ] Im Sicherheitsbericht `05_SICHERHEITS_CRASH_PRUEFBERICHT.md` der Status **BESTANDEN (GRÜN)** dokumentiert ist.
4. [ ] Das Einrichteblatt `06_EINRICHTEBLATT_SETUP_SHEET.md` alle Werkzeuge, Nullpunkte und Drehmomente enthält.
5. [ ] Das Rechnungsdokument `07_RECHNUNG_NACH_PARAGRAPH_18_ESTG.md` für das Finanzamt Hanau abgelegt ist.

# 📩 Kundenauftrag: Übung 5: 3D-Simulation im Browser & Einrichteblatt (`Setup Sheet`) für den Kunden erstellen
**Auftrags-Kategorie:** 5 (Einrichtedokumentation & Simulationsprüfung)
**Auftragnehmer:** Dipl.-Ing. Bujanovski – Freiberufliches Ingenieurbüro für CAD/CAM-Fertigungstechnik & Postprozessor-Entwicklung  
**Status:** Aktiv / Bereit zur Bearbeitung

---

## 1. Das Original-Auftragsbriefing des Kunden

So sieht eine typische Anfrage aus, wenn ein Kunde das CAM-Programm bereits hat, aber ein rechtssicheres Einrichteblatt und einen Simulationscheck für seine Werkstattmitarbeiter braucht:

> **Von:** Thomas Kuhn *(Inhaber & Werkstattleiter)* `<t.kuhn@kuhn-medizintechnik.de>`  
> **An:** Dipl.-Ing. Bujanovski `<kontakt@ingenieurbuero-bujanovski.de>`  
> **Datum:** 19. Oktober 2026, 16:05 Uhr  
> **Betreff:** Erstellung Einrichteblatt (PDF) & 3D-Simulationsbericht für Lagerplatte  
>
> Sehr geehrter Herr Dipl.-Ing. Bujanovski,  
> 
> wir bilden in unserer Werkstatt aktuell zwei neue Zerspanungsmechaniker-Auszubildende aus. Um Rüstfehler an der CNC-Maschine auszuschließen, dürfen Programme nur noch gerüstet werden, wenn ein vollständiges, bebildertes Einrichteblatt (`Setup Sheet`) und eine freigegebene 3D-Simulation vorliegen.  
> 
> **Aufgabenstellung:**  
> 1. Analysieren Sie das beiliegende G-Code-Programm `output_expected.nc`.  
> 2. Führen Sie eine vollständige 3D-Simulation zur visuellen Kollisionskontrolle durch.  
> 3. Erstellen Sie ein druckfertiges **Einrichteblatt (PDF)** mit Nullpunktdaten `G54`, exakten Werkzeugnummern (`T01`/`T02`), Auskraglängen $L_{\text{min}}$ und Rohteilabmessungen ($85 \times 55 \times 15\,\text{mm}$).  
> 
> **Vergütung:**  
> Pauschal **280,00 € netto** gegen Rechnung.  
> 
> Mit freundlichen Grüßen  
> **Thomas Kuhn** – Kuhn Medizintechnik & Feinmechanik, Tuttlingen

---

## 2. Bearbeitungshinweise für diesen Auftrag
* **Zuständiger Agent für Angebot & Honorar:** `Agent 4` (Backoffice-Agent) – siehe `ANGEBOT_DIPL_ING_BUJANOVSKI.md` in diesem Ordner.
* **Zuständiger Haupt-Agent für die Auftragsabwicklung:** `Agent 3` (NC-Safety- & Setup-Agent) – führt die 3D-Kollisionssimulation im Browser durch und extrahiert das normgerechte Werkstatt-Einrichteblatt (`06_EINRICHTEBLATT_SETUP_SHEET.md`) aus dem beigestellten Kunden-G-Code `output_expected.nc`.
* **Rolle von Agent 2 (Postprocessor-Coder-Agent):** Bereitschafts-Agent für Code-Korrekturen (wird in diesem Auftrag nur aufgerufen, falls Agent 3 bei der Analyse des beigestellten Kunden-G-Codes Syntaxfehler, fehlende Sicherheitszeilen oder Kollisionen detektiert; es wird keine neue `.cps`-Datei programmiert).
* **Zuständiger Agent für Endabrechnung:** `Agent 4` (Backoffice-Agent) – Erstellung der Honorarrechnung nach § 18 EStG.

# 📩 Kundenauftrag: Übung 5: 3D-Simulation im Browser & Einrichteblatt (`Setup Sheet`) für den Kunden erstellen
**Auftrags-Kategorie:** 5 (Einrichtedokumentation & Simulationsprüfung)
**Auftragnehmer:** Dipl.-Ing. Buenotte – Freiberufliches Ingenieurbüro für CAD/CAM-Fertigungstechnik & Postprozessor-Entwicklung  
**Status:** Aktiv / Bereit zur Bearbeitung

---

## 1. Das Original-Auftragsbriefing des Kunden

So sieht eine typische Anfrage aus, wenn ein Kunde das CAM-Programm bereits hat, aber ein rechtssicheres Einrichteblatt und einen Simulationscheck für seine Werkstattmitarbeiter braucht:

> **Von:** Thomas Kuhn *(Inhaber & Werkstattleiter)* `<t.kuhn@kuhn-medizintechnik.de>`  
> **An:** Dipl.-Ing. Buenotte `<kontakt@ingenieurbuero-buenotte.de>`  
> **Datum:** 19. Oktober 2026, 16:05 Uhr  
> **Betreff:** Erstellung Einrichteblatt (PDF) & 3D-Simulationsbericht für Lagerplatte  
>
> Sehr geehrter Herr Dipl.-Ing. Buenotte,  
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
* **Zuständiger Agent für Angebot:** `Agent 4` (Backoffice-Agent) – siehe `ANGEBOT_DIPL_ING_BUENOTTE.md` in diesem Ordner.
* **Zuständiger Agent für Umsetzung:** `Agent 2` (Postprocessor-Coder-Agent) für Code- & .cps-Modifikationen.
* **Zuständiger Agent für Prüfung & Freigabe:** `Agent 3` (NC-Safety- & Setup-Agent) für Crash-Prüfung und Einrichteblatt.

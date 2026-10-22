# 📩 Kundenauftrag: Übung 4: Ein 3D-Modell als Kundenauftrag bearbeiten (Vom 3D-Bauteil zum G-Code)
**Auftrags-Kategorie:** 4 (CAM-Programmierauftrag Lagerplatte)
**Auftragnehmer:** Dipl.-Ing. Buenotte – Freiberufliches Ingenieurbüro für CAD/CAM-Fertigungstechnik & Postprozessor-Entwicklung  
**Status:** Aktiv / Bereit zur Bearbeitung

---

## 1. Das Original-Auftragsbriefing des Kunden

So sieht ein typischer vollständiger Programmierauftrag aus, den ein Fertigungsbetrieb mit Engpässen an dein Ingenieurbüro vergibt:

> **Von:** Michael Brandner *(Fertigungsleiter)* `<m.brandner@franken-praezision.de>`  
> **An:** Dipl.-Ing. Buenotte `<kontakt@ingenieurbuero-buenotte.de>`  
> **Datum:** 18. Oktober 2026, 10:15 Uhr  
> **Betreff:** Eilauftrag CAM-Programmierung: Lagerplatte Alu (50 Stück) – 3D-STEP anbei  
>
> Sehr geehrter Herr Dipl.-Ing. Buenotte,  
> 
> wir haben in unserer Fräserei einen kurzfristigen Programmier-Engpass. Anbei senden wir Ihnen das 3D-CAD-Modell `bauteil_1001.step` für eine Lagerplatte aus Aluminium EN AW-6082 (Stückzahl: 50).  
> 
> **Maschine & Spannsituation:**  
> * Maschine: Haas VF-2 *(3-Achs-Fräszentrum)*  
> * Fertigmaß: $80 \times 50 \times 12\,\text{mm}$ *(mit Kreistasche $\varnothing 30\,\text{mm}$, Tiefe $3\,\text{mm}$ und 4 Eckbohrungen $\varnothing 6\,\text{mm}$)*  
> * Rohteil: $85 \times 55 \times 15\,\text{mm}$ im Maschinenschraubstock auf $3\,\text{mm}$ Spannrand gespannt.  
> * Nullpunkt `G54`: Vorne links oben auf dem Fertigteil.  
> 
> **Lieferumfang:**  
> 1. Fertige, kollisionsgeprüfte `.nc`-Maschinendatei für Haas NGC.  
> 2. Werkzeugzuordnung: `T01` Schaftfräser $\varnothing 10\,\text{mm}$, `T02` Spiralbohrer $\varnothing 6\,\text{mm}$.  
> 
> **Honorar:**  
> Festpreis **380,00 € netto** *(Zahlung: 50 % Anzahlung sofort, 50 % nach Vorlage des Freigabevideos)*.  
> 
> Mit besten Grüßen  
> **Michael Brandner** – Franken Präzisionsteile GmbH, Schweinfurt

---

## 2. Bearbeitungshinweise für diesen Auftrag
* **Zuständiger Agent für Angebot:** `Agent 4` (Backoffice-Agent) – siehe `ANGEBOT_DIPL_ING_BUENOTTE.md` in diesem Ordner.
* **Zuständiger Agent für Umsetzung:** `Agent 2` (Postprocessor-Coder-Agent) für Code- & .cps-Modifikationen.
* **Zuständiger Agent für Prüfung & Freigabe:** `Agent 3` (NC-Safety- & Setup-Agent) für Crash-Prüfung und Einrichteblatt.

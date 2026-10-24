# 📩 Kundenauftrag: Übung 15: Kanten entgraten am 3D-Modell (`2D-Fase / Chamfer Milling`) mit einem 45°-Fasenfräser (`T04`)
**Auftrags-Kategorie:** 15 (Automatisiertes Entgraten & Spitzenversatz)
**Auftragnehmer:** Dipl.-Ing. Bujanovski – Freiberufliches Ingenieurbüro für CAD/CAM-Fertigungstechnik & Postprozessor-Entwicklung  
**Status:** Aktiv / Bereit zur Bearbeitung

---

## 1. Das Original-Auftragsbriefing des Kunden

So sieht eine typische Anfrage aus, wenn ein Kunde Bauteile nicht mehr mühsam von Hand entgraten will und saubere $0{,}5 \times 45^\circ$ Fasen auf der CNC-Maschine verlangt:

> **Von:** Matthias Kunz *(Geschäftsführer)* `<m.kunz@kunz-feinwerktechnik.de>`  
> **An:** Dipl.-Ing. Bujanovski `<kontakt@ingenieurbuero-bujanovski.de>`  
> **Datum:** 29. Oktober 2026, 13:40 Uhr  
> **Betreff:** CAM-Optimierung: Kanten entgraten mit 45°-Fasenfräser & Spitzenversatz  
>
> Sehr geehrter Herr Dipl.-Ing. Bujanovski,  
> 
> in unserer Fertigung in Villingen-Schwenningen müssen unsere Mitarbeiter nach dem Fräsen jedes Bauteil mit Dreikantschaber und Schleifvlies von Hand entgraten. Das kostet uns pro Schicht über 2 Stunden teure Handarbeit!  
> 
> Wenn unser Programmierer die Fase im CAM anlegt, fräst die Maschine mit der äußersten Werkzeugspitze. Weil an der Spitze die Schnittgeschwindigkeit $v_c = 0\,\text{m/min}$ ist, schneidet das Werkzeug nicht, sondern drückt das Aluminium nur platt und erzeugt einen noch größeren Grat!  
> 
> **Aufgabenstellung:**  
> Binden Sie in das Fertigungsprogramm eine automatisierte Entgrat-Operation ein:  
> 1. Werkzeug `T04`: $90^\circ$-Fasenfräser $\varnothing 12\,\text{mm}$ *(45°-Flanken)*.  
> 2. Saubere $0{,}5 \times 45^\circ$ Fase an allen Außenkanten und an der Kreistasche.  
> 3. Zwingende Berücksichtigung eines **Spitzenversatzes *(Tip Offset)*** von $2{,}0\,\text{mm}$, damit die Schneide im optimalen Schnittgeschwindigkeitsbereich arbeitet.  
> 
> **Honorar:**  
> Festpreis **380,00 € netto** gegen Rechnung.  
> 
> Mit besten Grüßen  
> **Matthias Kunz** – Kunz Feinwerktechnik, Villingen-Schwenningen

---

## 2. Bearbeitungshinweise für diesen Auftrag
* **Zuständiger Agent für Angebot:** `Agent 4` (Backoffice-Agent) – siehe `ANGEBOT_DIPL_ING_BUJANOVSKI.md` in diesem Ordner.
* **Zuständiger Agent für Umsetzung:** `Agent 2` (Postprocessor-Coder-Agent) für Code- & .cps-Modifikationen.
* **Zuständiger Agent für Prüfung & Freigabe:** `Agent 3` (NC-Safety- & Setup-Agent) für Crash-Prüfung und Einrichteblatt.

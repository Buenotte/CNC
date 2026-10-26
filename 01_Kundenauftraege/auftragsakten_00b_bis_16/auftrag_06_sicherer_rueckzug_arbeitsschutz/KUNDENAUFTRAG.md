# 📩 Auftrag 06: Sicherer Maschinen-Rückzug (G53 Z0 / Y0) & Arbeitsschutz — Süd-Zerspanung GmbH

**Auftraggeber:** Andreas Eder (Betriebsleiter)  
**Unternehmen:** Süd-Zerspanung GmbH  
**Empfänger:** Dipl.-Ing. Bujanovski `<kontakt@ingenieurbuero-bujanovski.de>`  
**Zielmaschine:** **Haas VF-2 (Haas NGC Steuerung)**  
**Vereinbartes Budget:** **420,00 € netto** (499,80 € brutto)  

---

## Auftrags-Briefing des Kunden:

**Auftrags-Kategorie:** 6 (Arbeitssicherheit & Ergonomie am Programmende)
**Auftragnehmer:** Dipl.-Ing. Bujanovski – Freiberufliches Ingenieurbüro für CAD/CAM-Fertigungstechnik & Postprozessor-Entwicklung  
**Status:** Aktiv / Bereit zur Bearbeitung

---

## 1. Das Original-Auftragsbriefing des Kunden

So sieht eine typische Anfrage aus, wenn ein Betrieb die Sicherheit und Ergonomie an der Fräsmaschine verbessern will:

> **Von:** Andreas Eder *(Betriebsleiter)* `<a.eder@sued-zerspanung.de>`  
> **An:** Dipl.-Ing. Bujanovski `<kontakt@ingenieurbuero-bujanovski.de>`  
> **Datum:** 20. Oktober 2026, 13:10 Uhr  
> **Betreff:** Postprozessor-Änderung onClose: Tischrückzug zur Schiebetür & Spindel hoch  
>
> Sehr geehrter Herr Kollege Bujanovski,  
> 
> unsere Zerspanungsmechaniker beschweren sich seit Wochen über den Standard-Postprozessor unserer neuen Haas-Fräse.  
> 
> Nach Programmende bleibt der schwere Maschinentisch hinten in der Kabine stehen und der Fräser bleibt auf Werkstückhöhe stehen. Die Werker müssen sich tief in die nasse Maschine beugen, um das Teil zu entnehmen *(Rückenschmerzen & Verletzungsgefahr an der scharfen Fräserspitze!)*.  
> 
> **Aufgabenstellung:**  
> Programmieren Sie in der Funktion `onClose()` unseres Postprozessors einen zwingenden Sicherheitsablauf:  
> 1. Kühlmittel mit `M09` sofort abschalten.  
> 2. Frässpindel mit `G53 G00 Z0.` im Eilgang senkrecht an die Kabinendecke fahren *(Crash-Schutz)*.  
> 3. Spindel mit `M05` abschalten.  
> 4. Maschinentisch mit `G53 G00 Y0.` vollautomatisch ganz nach vorne an die geöffnete Schiebetür fahren.  
> 5. Erst dann mit `M30` beenden.  
> 
> **Honorar:**  
> Festpreis **420,00 € netto** bei sofortiger Freigabe.  
> 
> Mit besten Grüßen  
> **Andreas Eder** – Zerspanungstechnik Süd GmbH, Augsburg

---

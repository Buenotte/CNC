# 📩 Auftrag 01: ISO-9001 Entwickler-Header & Metadatenblock — Klausner Formenbau & Zerspanung

**Auftraggeber:** Stefan Klausner (Geschäftsführer)  
**Unternehmen:** Klausner Formenbau & Zerspanung  
**Empfänger:** Dipl.-Ing. Bujanovski `<kontakt@ingenieurbuero-bujanovski.de>`  
**Zielmaschine:** **3-Achs-Bearbeitungszentrum Hermle C400 (ISO/Fanuc-Modus)**  
**Vereinbartes Budget:** **350,00 € netto** (416,50 € brutto)  

---

## Auftrags-Briefing des Kunden:

**Auftrags-Kategorie:** 1 (Qualitäts-Rückverfolgbarkeit für Werkzeugbau)
**Auftragnehmer:** Dipl.-Ing. Bujanovski – Freiberufliches Ingenieurbüro für CAD/CAM-Fertigungstechnik & Postprozessor-Entwicklung  
**Status:** Aktiv / Bereit zur Bearbeitung

---

## 1. Das Original-Auftragsbriefing des Kunden

So sieht eine typische Anfrage aus, wenn ein Fertigungsbetrieb Qualitätsprobleme bei Schichtwechseln hat und Programme lückenlos nachvollziehbar machen muss:

> **Von:** Stefan Klausner *(Geschäftsführer)* `<s.klausner@klausner-formenbau.de>`  
> **An:** Dipl.-Ing. Bujanovski `<kontakt@ingenieurbuero-bujanovski.de>`  
> **Datum:** 14. Oktober 2026, 14:40 Uhr  
> **Betreff:** Anpassung Programmkopf Fusion 360 Postprozessor – ISO 9001 Dokumentation  
>
> Sehr geehrter Herr Kollege Bujanovski,  
> 
> in unserem Formenbau in Stuttgart fertigen wir mit 8 CNC-Fräszentren im 3-Schicht-Betrieb. Bei unserer letzten ISO 9001 Qualitäts-Audits wurde bemängelt, dass auf den Steuerungsmonitoren unserer Maschinen nicht sofort ersichtlich ist, wann ein G-Code-Programm erzeugt wurde und wer dafür die Verantwortung trägt.  
> 
> Oft werden ältere Versionen aus dem Netzwerk aufgespielt, was letzte Woche zu Ausschuss bei einer teuren Spritzgussform geführt hat.  
> 
> **Aufgabenstellung:**  
> Passen Sie unseren Postprozessor in der Funktion `onOpen()` so an, dass ganz oben vor dem ersten Frässatz automatisch folgende Daten in genormter Kommentarsyntax ausgegeben werden:  
> 1. Entwickler-Name *(Dipl.-Ing. Bujanovski / CAM-Büro)*  
> 2. Firmenname des Kunden *(Klausner Formenbau & CNC-Technik GmbH)*  
> 3. Generierungsdatum und exakte Uhrzeit  
> 4. Programm-Kommentar mit Bauteilbezeichnung  
> 
> **Budget:**  
> Wir vergüten diese Anpassung mit **350,00 € netto** gegen ordentliche Ingenieurrechnung.  
> 
> Mit freundlichen Grüßen  
> **Stefan Klausner** – Klausner Formenbau GmbH, Stuttgart

---

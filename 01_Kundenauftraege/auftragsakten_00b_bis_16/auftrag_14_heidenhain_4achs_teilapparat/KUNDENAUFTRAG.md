# 📩 Auftrag 14: Heidenhain TNC 640 Klartext-Postprozessor (4-Achs-Indexierung A-Achse) — Alps Precision AG (Schweiz)

**Auftraggeber:** Urs Hodel (Produktionsleiter)  
**Unternehmen:** Alps Precision AG (Schweiz)  
**Empfänger:** Dipl.-Ing. Bujanovski `<kontakt@ingenieurbuero-bujanovski.de>`  
**Zielmaschine:** **Hermle C400 (Heidenhain TNC 640 Steuerung mit 4. Achse / A-Achse)**  
**Vereinbartes Budget:** **850,00 € netto** (1.011,50 € brutto)  

---

## Auftrags-Briefing des Kunden:

**Auftrags-Kategorie:** 14 (Heidenhain TNC 640 & 4-Achs-Teilapparat)
**Auftragnehmer:** Dipl.-Ing. Bujanovski – Freiberufliches Ingenieurbüro für CAD/CAM-Fertigungstechnik & Postprozessor-Entwicklung  
**Status:** Aktiv / Bereit zur Bearbeitung

---

## 1. Das Original-Auftragsbriefing des Kunden

So sieht der lukrativste Auftragstyp aus der Schweiz oder Süddeutschland aus, wo Werkstätten strikt Heidenhain Klartext verlangen:

> **Von:** Urs Hodel *(Produktionsleiter)* `<u.hodel@alps-precision.ch>`  
> **An:** Dipl.-Ing. Bujanovski `<kontakt@ingenieurbuero-bujanovski.de>`  
> **Datum:** 28. Oktober 2026, 09:20 Uhr  
> **Betreff:** Postprozessor-Entwicklung: Nativer Heidenhain Klartext mit A-Achsen-Teilapparat  
>
> Sehr geehrter Herr Kollege Bujanovski,  
> 
> wir betreiben in St. Gallen (Schweiz) drei Hermle C400 Bearbeitungszentren mit Heidenhain TNC 640 Steuerung. Zusätzlich haben wir einen CNC-Teilapparat (4. Drehachse / A-Achse) montiert, um Bauteile von vier Seiten in einer einzigen Aufspannung zu bearbeiten.  
> 
> Unsere Schweizer Zerspaner lehnen ISO-G-Code (`G01`, `G00`, `M06`) kategorisch ab – wir programmieren und optimieren ausschließlich in gewohntem **Heidenhain Klartext (`.H`-Dateien)**!  
> 
> **Aufgabenstellung:**  
> Entwickeln Sie für uns einen maßgeschneiderten Fusion 360 Postprozessor für Heidenhain Klartext:  
> 1. Korrekter Header mit `BEGIN PGM ... MM` und `BLK FORM 0.1 / 0.2` Rohteilgitter.  
> 2. Nativer Werkzeugaufruf: `TOOL CALL <T> Z S...` *(ohne separates M06!)*.  
> 3. Fahrbefehle im Klartext: `L X.. Y.. Z.. R0 F...` und Eilgang mit `FMAX`.  
> 4. Ansteuerung der 4. Achse: Automatisches Lösen der Klemmung mit `M11`, Schwenken auf `L A+90.000 FMAX`, erneutes Klemmen mit `M10` vor dem Schnitt.  
> 5. Sicherer Z-Rückzug am Programmende mit `M91` (`L Z+250 R0 FMAX M91`).  
> 
> **Vergütung:**  
> Festpreis **850,00 € netto** *(entspricht ca. 820 CHF)* gegen offizielle Rechnung.  
> 
> Mit freundlichen Grüßen aus der Schweiz  
> **Urs Hodel** – Alps Precision CNC AG, St. Gallen

---

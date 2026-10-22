# 📩 Kundenauftrag: Übung 14: Heidenhain Klartext-Steuerung (`TOOL CALL`, `L ... FMAX`) & 4. Drehachse (`A-Achse`) für Aufträge im deutschsprachigen Raum
**Auftrags-Kategorie:** 14 (Heidenhain TNC 640 & 4-Achs-Teilapparat)
**Auftragnehmer:** Dipl.-Ing. Buenotte – Freiberufliches Ingenieurbüro für CAD/CAM-Fertigungstechnik & Postprozessor-Entwicklung  
**Status:** Aktiv / Bereit zur Bearbeitung

---

## 1. Das Original-Auftragsbriefing des Kunden

So sieht der lukrativste Auftragstyp aus der Schweiz oder Süddeutschland aus, wo Werkstätten strikt Heidenhain Klartext verlangen:

> **Von:** Urs Hodel *(Produktionsleiter)* `<u.hodel@alps-precision.ch>`  
> **An:** Dipl.-Ing. Buenotte `<kontakt@ingenieurbuero-buenotte.de>`  
> **Datum:** 28. Oktober 2026, 09:20 Uhr  
> **Betreff:** Postprozessor-Entwicklung: Nativer Heidenhain Klartext mit A-Achsen-Teilapparat  
>
> Sehr geehrter Herr Kollege Buenotte,  
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

## 2. Bearbeitungshinweise für diesen Auftrag
* **Zuständiger Agent für Angebot:** `Agent 4` (Backoffice-Agent) – siehe `ANGEBOT_DIPL_ING_BUENOTTE.md` in diesem Ordner.
* **Zuständiger Agent für Umsetzung:** `Agent 2` (Postprocessor-Coder-Agent) für Code- & .cps-Modifikationen.
* **Zuständiger Agent für Prüfung & Freigabe:** `Agent 3` (NC-Safety- & Setup-Agent) für Crash-Prüfung und Einrichteblatt.

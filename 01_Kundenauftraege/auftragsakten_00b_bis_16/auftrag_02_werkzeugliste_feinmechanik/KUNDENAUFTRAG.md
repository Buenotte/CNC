# 📩 Kundenauftrag: Bavaria Feinmechanik GmbH (Auftrag 02: Automatische Werkzeugliste (Tool Table))

**Auftraggeber:** Dr.-Ing. Sabine Hofmann (Produktionsleiterin)  
**Unternehmen:** Bavaria Feinmechanik GmbH  
**Empfänger:** Dipl.-Ing. Bujanovski `<kontakt@ingenieurbuero-bujanovski.de>`  
**Zielmaschine:** **Chiron FZ 15W High-Speed Fräszentrum (Fanuc 31i)**  
**Vereinbartes Budget:** **450,00 € netto** (535,50 € brutto)  

---

## Auftrags-Briefing des Kunden:

# 📩 Kundenauftrag: Übung 2: Automatische Werkzeugliste (`Tool Table`) ganz oben im Programm ausgeben
**Auftrags-Kategorie:** 2 (Rüstzeit-Optimierung für Feinmechanik)
**Auftragnehmer:** Dipl.-Ing. Bujanovski – Freiberufliches Ingenieurbüro für CAD/CAM-Fertigungstechnik & Postprozessor-Entwicklung  
**Status:** Aktiv / Bereit zur Bearbeitung

---

## 1. Das Original-Auftragsbriefing des Kunden

So sieht eine typische Anfrage aus, wenn ein Betrieb teure Maschinen-Stillstandszeiten beim Rüsten eliminieren will:

> **Von:** Dr.-Ing. Sabine Hofmann *(Produktionsleiterin)* `<s.hofmann@bavaria-feinmechanik.de>`  
> **An:** Dipl.-Ing. Bujanovski `<kontakt@ingenieurbuero-bujanovski.de>`  
> **Datum:** 16. Oktober 2026, 08:30 Uhr  
> **Betreff:** Postprozessor-Optimierung: Automatische Werkzeugtabelle im Programmkopf  
>
> Sehr geehrter Herr Dipl.-Ing. Bujanovski,  
> 
> in unserer Serienfertigung in Nürnberg rüsten unsere Zerspanungsmechaniker täglich bis zu 5 verschiedene Bauteile auf unseren Bearbeitungszentren.  
> 
> Aktuell verlieren die Werker bei jedem neuen Auftrag 15 bis 20 Minuten wertvolle Maschinenzeit, weil sie das mehrere tausend Zeilen lange G-Code-Programm am Steuerungsbildschirm durchblättern müssen, um alle `T.. M06` Werkzeugwechsel herauszuschreiben.  
> 
> **Aufgabenstellung:**  
> Wir möchten, dass unser Fusion 360 Postprozessor über die interne Funktion `getToolTable()` ganz oben im Programmkopf eine übersichtliche Werkzeugliste ausgibt:  
> 1. Werkzeugnummer (`T01`, `T02` usw.)  
> 2. Fräser-/Bohrerdurchmesser in mm (`D=10.000MM`)  
> 3. Eckenradius (`ECKE R=0.000`)  
> 4. Klartext-Bezeichnung des Werkzeugs *(z. B. SCHAFTFRAESER 10MM VHM)*  
> 
> **Vergütung:**  
> Für diese Programmierung in der Datei `.cps` bieten wir Ihnen ein Festhonorar von **450,00 € netto**.  
> 
> Bei schneller Umsetzung stellen wir die Zahlung sofort nach Testlauf frei.  
> 
> Mit besten Grüßen  
> **Dr.-Ing. Sabine Hofmann** – Bavaria Feinmechanik GmbH, Nürnberg

---

## 2. Bearbeitungshinweise für diesen Auftrag
* **Zuständiger Agent für Angebot:** `Agent 4` (Backoffice-Agent) – siehe `ANGEBOT_DIPL_ING_BUJANOVSKI.md` in diesem Ordner.
* **Zuständiger Agent für Umsetzung:** `Agent 2` (Postprocessor-Coder-Agent) für Code- & .cps-Modifikationen.
* **Zuständiger Agent für Prüfung & Freigabe:** `Agent 3` (NC-Safety- & Setup-Agent) für Crash-Prüfung und Einrichteblatt.


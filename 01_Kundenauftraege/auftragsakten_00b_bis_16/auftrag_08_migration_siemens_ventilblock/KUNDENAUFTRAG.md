# 📩 Kundenauftrag: Franken Zerspanung GmbH (Auftrag 08: Migration auf Siemens Sinumerik Dialekt)

**Auftraggeber:** Jürgen Meier (Fertigungsleiter)  
**Unternehmen:** Franken Zerspanung GmbH  
**Empfänger:** Dipl.-Ing. Buenotte `<kontakt@ingenieurbuero-buenotte.de>`  
**Zielmaschine:** **DMG MORI DMU 50 (Siemens Sinumerik 840D sl)**  
**Vereinbartes Budget:** **650,00 € netto** (773,50 € brutto)  

---

## Auftrags-Briefing des Kunden:

# 📩 Kundenauftrag: Übung 8: Zwei Steuerungs-Sprachen vergleichen (Haas/Fanuc vs. Siemens Sinumerik)
**Auftrags-Kategorie:** 8 (Migration von Haas auf Siemens Sinumerik)
**Auftragnehmer:** Dipl.-Ing. Buenotte – Freiberufliches Ingenieurbüro für CAD/CAM-Fertigungstechnik & Postprozessor-Entwicklung  
**Status:** Aktiv / Bereit zur Bearbeitung

---

## 1. Das Original-Auftragsbriefing des Kunden

So sieht eine typische Anfrage aus, wenn ein Betrieb eine neue Maschine mit einer völlig anderen Steuerungs-Sprache kauft:

> **Von:** Jürgen Meier *(Fertigungsleiter)* `<j.meier@franken-zerspanung.de>`  
> **An:** Dipl.-Ing. Buenotte `<kontakt@ingenieurbuero-buenotte.de>`  
> **Datum:** 22. Oktober 2026, 11:00 Uhr  
> **Betreff:** Postprozessor-Umstellung: Haas NGC Code auf Siemens Sinumerik 840D sl  
>
> Sehr geehrter Herr Dipl.-Ing. Buenotte,  
> 
> wir haben in unserer Werkhalle in Erlangen bisher ausschließlich auf Haas-Maschinen mit ISO/Fanuc-G-Code gefräst. Letzte Woche haben wir ein gebrauchtes 5-Achs-Bearbeitungszentrum von DMG MORI mit **Siemens Sinumerik 840D sl** Steuerung übernommen.  
> 
> Als unser Fräser ein gewohntes Haas-Programm auf die Siemens-Maschine geladen hat, blieb die Steuerung mit Fehlermeldungen stehen:  
> * Siemens kennt `G53 Z0` nicht so wie Haas, sondern verlangt `SUPA G0 Z0 D0`.  
> * Bei Tiefbohren verlangt Siemens den parametrischen Zyklus `CYCLE83(...)` statt `G83`.  
> * Statt `G43 H01` erwartet Siemens den Schneidenaufruf `D1`.  
> 
> **Aufgabenstellung:**  
> Passen Sie unseren Postprozessor so an, dass er sauberen, nativen Siemens Sinumerik Code erzeugt, der auf unserer neuen DMG MORI fehlerfrei startet.  
> 
> **Honorar:**  
> Festpreis **650,00 € netto** bei erfolgreicher Abnahme auf unserer Maschine.  
> 
> Mit besten Grüßen  
> **Jürgen Meier** – Lohnfertigung Franken GmbH, Erlangen

---

## 2. Bearbeitungshinweise für diesen Auftrag
* **Zuständiger Agent für Angebot:** `Agent 4` (Backoffice-Agent) – siehe `ANGEBOT_DIPL_ING_BUENOTTE.md` in diesem Ordner.
* **Zuständiger Agent für Umsetzung:** `Agent 2` (Postprocessor-Coder-Agent) für Code- & .cps-Modifikationen.
* **Zuständiger Agent für Prüfung & Freigabe:** `Agent 3` (NC-Safety- & Setup-Agent) für Crash-Prüfung und Einrichteblatt.


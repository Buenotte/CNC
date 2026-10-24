# 📩 Kundenauftrag: Übung 00b: Hallo Welt (Erste eigene Zeile im Postprozessor)
**Auftrags-Kategorie:** 00b (Kennenlern-Auftrag vom CAM-Systemhaus)
**Auftragnehmer:** Dipl.-Ing. Bujanovski – Freiberufliches Ingenieurbüro für CAD/CAM-Fertigungstechnik & Postprozessor-Entwicklung  
**Status:** Aktiv / Bereit zur Bearbeitung

---

## 1. Das Original-Auftragsbriefing des Kunden

So sieht eine typische Anfrage von einem großen CAM-Systemhaus aus, das einen fähigen externen Software-Ingenieur für Postprozessor-Aufträge sucht:

> **Von:** Jens Becker *(Leiter CAM-Postprozessor-Services)* `<j.becker@mum-systemhaus.de>`  
> **An:** Dipl.-Ing. Bujanovski `<kontakt@ingenieurbuero-bujanovski.de>`  
> **Datum:** 12. Oktober 2026, 11:20 Uhr  
> **Betreff:** Freelance-Kooperation: Qualifikations-Test Auftrag Postprozessor Autodesk Fusion (.cps)  
>
> Sehr geehrter Herr Dipl.-Ing. Bujanovski,  
> 
> als autorisiertes CAM-Systemhaus für Autodesk Fusion 360 haben wir aktuell mehr Kundenanfragen für Postprozessoren, als unsere interne Abteilung bewältigen kann. Wir suchen daher verlässliche freiberufliche Software-Ingenieure auf Honorarbasis.  
> 
> Um Ihre Arbeitsweise und die JavaScript-Schnittstelle zu testen, möchten wir Ihnen einen ersten kleinen Kennenlern-Auftrag erteilen:  
> 
> **Aufgabenstellung:**  
> Erstellen Sie ein sauberes, schlankes Basis-Postprozessor-Skript (`.cps`), das für eine Standard-3-Achs-Fräsmaschine (Haas/Fanuc-kompatibel) folgendes leistet:  
> 1. Korrekte Ausgabe der ISO-Sicherheitszeile (`G90 G17 G21 G94 G40 G80`).  
> 2. Ausgabe eines Begrüßungs- und Versionskommentars mit `writeComment()` im Programmkopf.  
> 3. Saubere Beendigung mit Spindel-Stopp `M05`, Kühlmittel-Aus `M09` und `M30`.  
> 
> **Vergütung:**  
> Für diesen ersten Schnittstellentest zahlen wir pauschal **250,00 € netto** bei erfolgreichem Testlauf in unserem Simulator. Nach erfolgreicher Abnahme listen wir Ihr Ingenieurbüro als festen Subunternehmer für Folgeaufträge.  
> 
> Bitte senden Sie uns Ihr Angebot zu!  
> 
> Mit freundlichen Grüßen  
> **Dipl.-Ing. Jens Becker** – Mensch und Maschine Systemhaus GmbH

---

## 2. Bearbeitungshinweise für diesen Auftrag
* **Zuständiger Agent für Angebot:** `Agent 4` (Backoffice-Agent) – siehe `ANGEBOT_DIPL_ING_BUJANOVSKI.md` in diesem Ordner.
* **Zuständiger Agent für Umsetzung:** `Agent 2` (Postprocessor-Coder-Agent) für Code- & .cps-Modifikationen.
* **Zuständiger Agent für Prüfung & Freigabe:** `Agent 3` (NC-Safety- & Setup-Agent) für Crash-Prüfung und Einrichteblatt.

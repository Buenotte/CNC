# 📩 Kundenauftrag: Übung 13: Echte 3D-Freiformflächen – `3D Adaptive Clearing` (Wirbelfräsen) & `3D-Schlichten` mit Kugelfräser (`Ball End Mill`)
**Auftrags-Kategorie:** 13 (3D-Freiformflächen & Kugelfräser-Schlichten)
**Auftragnehmer:** Dipl.-Ing. Buenotte – Freiberufliches Ingenieurbüro für CAD/CAM-Fertigungstechnik & Postprozessor-Entwicklung  
**Status:** Aktiv / Bereit zur Bearbeitung

---

## 1. Das Original-Auftragsbriefing des Kunden

So sieht eine typische hochdotierte Anfrage aus, wenn ein Formen- oder Prototypenbauer komplexe 3D-Geometrien ohne sichtbare Facetten fräsen muss:

> **Von:** Dr. Elena Rost *(Leiterin Prototypenbau)* `<e.rost@aerotech-bremen.de>`  
> **An:** Dipl.-Ing. Buenotte `<kontakt@ingenieurbuero-buenotte.de>`  
> **Datum:** 27. Oktober 2026, 11:30 Uhr  
> **Betreff:** Postprozessor-Optimierung für 3D-Freiformflächen & Hochgeschwindigkeits-Schlichten  
>
> Sehr geehrter Herr Dipl.-Ing. Buenotte,  
> 
> wir fertigen in Bremen aerodynamische Strömungskanäle und Windkanalmodelle aus hochfestem Aluminium.  
> 
> Bisherige NC-Programme, die unser Postprozessor erzeugt, ruckeln auf der Maschine bei Freiformflächen extrem: Die Steuerung bremst an jeder Zwischenkoordinate ab *(stotternde Fräsbewegung)*, und auf den geschwungenen Oberflächen entstehen hässliche Rattermarken und sichtbare Facetten.  
> 
> **Aufgabenstellung:**  
> 1. Optimieren Sie den Postprozessor für High-Speed-Machining (HSM) von 3D-Freiformflächen: Unterstützung von feinsten Sehnen-Toleranzen ($0{,}005\,\text{mm}$) mit simultanen $X/Y/Z$-Bahnen.  
> 2. Korrekte Werkzeugidentifikation für Kugelfräser *(Ball End Mill `TOOL_MILLING_END_BALL`)* mit Halbkugel-Mittelpunktsausgabe im Header.  
> 3. Aktivierung der Glättungsfunktion *(Look-Ahead)* der Maschinensteuerung.  
> 
> **Honorar:**  
> Festpreis **750,00 € netto** gegen Rechnung.  
> 
> Mit besten Grüßen  
> **Dr. Elena Rost** – AeroTech Turbinen- & Modellbau GmbH, Bremen

---

## 2. Bearbeitungshinweise für diesen Auftrag
* **Zuständiger Agent für Angebot:** `Agent 4` (Backoffice-Agent) – siehe `ANGEBOT_DIPL_ING_BUENOTTE.md` in diesem Ordner.
* **Zuständiger Agent für Umsetzung:** `Agent 2` (Postprocessor-Coder-Agent) für Code- & .cps-Modifikationen.
* **Zuständiger Agent für Prüfung & Freigabe:** `Agent 3` (NC-Safety- & Setup-Agent) für Crash-Prüfung und Einrichteblatt.

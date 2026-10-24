# 📩 Kundenauftrag: Meyer Hydraulikkomponenten GmbH (Auftrag 11: Starres Gewindebohren (G84 Rigid Tapping))

**Auftraggeber:** Christian Meyer (Fertigungsleiter)  
**Unternehmen:** Meyer Hydraulikkomponenten GmbH  
**Empfänger:** Dipl.-Ing. Bujanovski `<kontakt@ingenieurbuero-bujanovski.de>`  
**Zielmaschine:** **Haas VF-4SS (Haas NGC)**  
**Vereinbartes Budget:** **460,00 € netto** (547,40 € brutto)  

---

## Auftrags-Briefing des Kunden:

# 📩 Kundenauftrag: Übung 11: Gewindebohren (`G84` Rigid Tapping) – `M6`- und `M8`-Schraubengewinde ohne Werkzeugbruch programmieren (`F = S × Steigung`)
**Auftrags-Kategorie:** 11 (Gewindebohrerbruch bei M8-Serienfertigung)
**Auftragnehmer:** Dipl.-Ing. Bujanovski – Freiberufliches Ingenieurbüro für CAD/CAM-Fertigungstechnik & Postprozessor-Entwicklung  
**Status:** Aktiv / Bereit zur Bearbeitung

---

## 1. Das Original-Auftragsbriefing des Kunden

So sieht eine typische Anfrage aus, wenn in der Fertigung ständig Gewindebohrer abbrechen und die Synchronisation zwischen Spindel und Z-Achse nicht stimmt:

> **Von:** Christian Meyer *(Fertigungsleiter)* `<c.meyer@meyer-hydraulik.de>`  
> **An:** Dipl.-Ing. Bujanovski `<kontakt@ingenieurbuero-bujanovski.de>`  
> **Datum:** 25. Oktober 2026, 09:10 Uhr  
> **Betreff:** DRINGEND: Postprozessor-Korrektur G84 Rigid Tapping – Gewindebohrer brechen ab  
>
> Sehr geehrter Herr Dipl.-Ing. Bujanovski,  
> 
> wir fertigen in Hannover Hydraulikblöcke mit jeweils 8 M8-Gewindebohrungen. Seit gestern haben wir auf unserer CNC-Fräse bereits vier hochwertige Maschinengewindebohrer zerstört:  
> Die Werkzeuge brechen unten im Sackloch beim Reversieren *(Umschalten von Rechtslauf auf Linkslauf)* explosionsartig ab und zerstören das teure Bauteil!  
> 
> Unser CAM-System gibt fälschlicherweise einen willkürlichen Vorschub `F500` aus, anstatt die Steigung exakt mit der Drehzahl zu koppeln.  
> 
> **Aufgabenstellung:**  
> Passen Sie den Zyklusaufruf im Postprozessor so an, dass:  
> 1. Starres Gewindebohren *(Rigid Tapping)* mit `M29 S...` aktiviert wird.  
> 2. Der Vorschub $F$ für jedes Gewinde zwingend nach der Formel $F = S \times \text{Steigung}$ berechnet wird *(bei M8 mit Steigung $P=1{,}25\,\text{mm}$ und $S=600\,\text{U/min}$ muss exakt $F=750\,\text{mm/min}$ ausgegeben werden!)*.  
> 3. Am Zyklusende mit `G80` sicher entkoppelt wird.  
> 
> **Vergütung:**  
> Festpreis **460,00 € netto** gegen Rechnung.  
> 
> Mit besten Grüßen  
> **Christian Meyer** – Meyer Hydraulik KG, Hannover

---

## 2. Bearbeitungshinweise für diesen Auftrag
* **Zuständiger Agent für Angebot:** `Agent 4` (Backoffice-Agent) – siehe `ANGEBOT_DIPL_ING_BUJANOVSKI.md` in diesem Ordner.
* **Zuständiger Agent für Umsetzung:** `Agent 2` (Postprocessor-Coder-Agent) für Code- & .cps-Modifikationen.
* **Zuständiger Agent für Prüfung & Freigabe:** `Agent 3` (NC-Safety- & Setup-Agent) für Crash-Prüfung und Einrichteblatt.


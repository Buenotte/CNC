# 📩 Kundenauftrag: AluTech Gehäusebau GmbH (Auftrag 10: 2. Aufspannung (OP20) & WCS G55)

**Auftraggeber:** Robert Schneider (Fertigungsleiter)  
**Unternehmen:** AluTech Gehäusebau GmbH  
**Empfänger:** Dipl.-Ing. Bujanovski `<kontakt@ingenieurbuero-bujanovski.de>`  
**Zielmaschine:** **Hermle C42 U MT**  
**Vereinbartes Budget:** **520,00 € netto** (618,80 € brutto)  

---

## Auftrags-Briefing des Kunden:

# 📩 Kundenauftrag: Übung 10: Die 2. Aufspannung (`G55` / `OP20`) – Wie das 3D-Bauteil umgedreht und der Restboden auf der Rückseite plangefräst wird
**Auftrags-Kategorie:** 10 (Restboden-Planfräsen in der 2. Aufspannung)
**Auftragnehmer:** Dipl.-Ing. Bujanovski – Freiberufliches Ingenieurbüro für CAD/CAM-Fertigungstechnik & Postprozessor-Entwicklung  
**Status:** Aktiv / Bereit zur Bearbeitung

---

## 1. Das Original-Auftragsbriefing des Kunden

So sieht eine typische Anfrage aus, wenn ein Bauteil nach der ersten Aufspannung noch den Spannrand am Boden hat und komplett auf Fertigmaß gebracht werden muss:

> **Von:** Robert Schneider *(Fertigungsleiter)* `<r.schneider@alutech-gehaeuse.de>`  
> **An:** Dipl.-Ing. Bujanovski `<kontakt@ingenieurbuero-bujanovski.de>`  
> **Datum:** 24. Oktober 2026, 10:30 Uhr  
> **Betreff:** CAM-Programmierung OP20: Umdrehen & Planfräsen auf Fertigdicke 12.0 mm  
>
> Sehr geehrter Herr Dipl.-Ing. Bujanovski,  
> 
> wir fertigen in unserem Werk in Friedrichshafen 200 Elektronik-Gehäuse. Die 1. Aufspannung *(OP10: Kontur, Taschen und Bohrungen)* läuft bereits.  
> 
> Das Bauteil hat jetzt am Boden jedoch noch die überstehenden $3\,\text{mm}$ Rohmaterial *(den ursprünglichen Spannrand aus $15\,\text{mm}$ Rohteil auf $12\,\text{mm}$ Fertigmaß)*.  
> 
> **Aufgabenstellung:**  
> Programmieren Sie die 2. Aufspannung (`OP20`):  
> 1. Programmierter Bediener-Stopp (`M00`) nach OP10 mit Kommentar: `(TEIL UMDREHEN UND AUF PARALLELUNTERLAGEN SPANNEN)`.  
> 2. Umschalten auf den zweiten Werkstück-Nullpunkt `G55` *(liegt auf der neu gewendeten Oberseite)*.  
> 3. Planfräsen der Rückseite mit Messerkopf `T03` ($\varnothing 50\,\text{mm}$) auf Fertigdicke exakt $12{,}0\,\text{mm}$.  
> 4. Sauberes Entgraten der Unterkanten.  
> 
> **Honorar:**  
> Festpreis **520,00 € netto** gegen Rechnung.  
> 
> Mit besten Grüßen  
> **Robert Schneider** – AluTech Gehäusebau GmbH, Friedrichshafen

---

## 2. Bearbeitungshinweise für diesen Auftrag
* **Zuständiger Agent für Angebot:** `Agent 4` (Backoffice-Agent) – siehe `ANGEBOT_DIPL_ING_BUJANOVSKI.md` in diesem Ordner.
* **Zuständiger Agent für Umsetzung:** `Agent 2` (Postprocessor-Coder-Agent) für Code- & .cps-Modifikationen.
* **Zuständiger Agent für Prüfung & Freigabe:** `Agent 3` (NC-Safety- & Setup-Agent) für Crash-Prüfung und Einrichteblatt.


# 📩 Kundenauftrag: Wagner Getriebebau GmbH (Auftrag 12: Werkzeugradiuskorrektur (G41 / G40) für H7-Passungen)

**Auftraggeber:** Alexander Wagner (Werkstattleiter)  
**Unternehmen:** Wagner Getriebebau GmbH  
**Empfänger:** Dipl.-Ing. Bujanovski `<kontakt@ingenieurbuero-bujanovski.de>`  
**Zielmaschine:** **DMG MORI NVX 5080**  
**Vereinbartes Budget:** **580,00 € netto** (690,20 € brutto)  

---

## Auftrags-Briefing des Kunden:

# 📩 Kundenauftrag: Übung 12: Werkzeugradiuskorrektur (`G41` / `G42` / `G40`) – Wie der Kunde an der Maschine `0,01 mm` Genauigkeit für Passungen einstellt
**Auftrags-Kategorie:** 12 (H7-Passungstoleranz über Steuerungskorrektur)
**Auftragnehmer:** Dipl.-Ing. Bujanovski – Freiberufliches Ingenieurbüro für CAD/CAM-Fertigungstechnik & Postprozessor-Entwicklung  
**Status:** Aktiv / Bereit zur Bearbeitung

---

## 1. Das Original-Auftragsbriefing des Kunden

So sieht eine typische Anfrage aus, wenn ein Kunde Passungen fertigen muss und Maßkorrekturen direkt am Steuerungsdisplay vornehmen will:

> **Von:** Alexander Wagner *(Werkstattleiter)* `<a.wagner@wagner-getriebe.de>`  
> **An:** Dipl.-Ing. Bujanovski `<kontakt@ingenieurbuero-bujanovski.de>`  
> **Datum:** 26. Oktober 2026, 14:15 Uhr  
> **Betreff:** Postprozessor-Anforderung: G41 Radiuskorrektur für Kugellager-Passung Ø 30 H7  
>
> Sehr geehrter Herr Dipl.-Ing. Bujanovski,  
> 
> wir fertigen Getriebegehäuse mit einer Kugellagersitz-Passung $\varnothing 30\,\text{H7}$ *(Toleranz: $+0{,}021 / 0\,\text{mm}$)*.  
> 
> Aktuell gibt unser Postprozessor nur fest berechnete Fräsermittelpunktsbahnen ohne Radiuskorrektur aus (`G40`). Wenn unsere Schaftfräser nach 30 Teilen um nur $0{,}015\,\text{mm}$ verschleißen, wird die Bohrung sofort zu klein und das Gehäuse ist unbrauchbarer Ausschuss!  
> 
> Unsere Bediener müssen in der Lage sein, den Verschleiß am Bedienpult im Werkzeugkorrekturspeicher *(Register `D01`)* um z. B. `-0.01 mm` nachzustellen, ohne dass wir jedes Mal das CAM-Modell neu berechnen müssen!  
> 
> **Aufgabenstellung:**  
> Passen Sie den Postprozessor für Schlichtkonturen an:  
> 1. Saubere Ausgabe von `G41 D..` *(Gleichlaufkorrektur links der Kontur)* mit linearem Anfahrweg.  
> 2. Fräsen des Vollkreises mit `G03`.  
> 3. Sicheres Aufheben der Korrektur mit `G40` bei der linearen Abfahrbewegung.  
> 
> **Honorar:**  
> Festpreis **580,00 € netto** gegen Rechnung.  
> 
> Mit freundlichen Grüßen  
> **Alexander Wagner** – Präzisions-Getriebebau Wagner GmbH, Schweinfurt

---

## 2. Bearbeitungshinweise für diesen Auftrag
* **Zuständiger Agent für Angebot:** `Agent 4` (Backoffice-Agent) – siehe `ANGEBOT_DIPL_ING_BUJANOVSKI.md` in diesem Ordner.
* **Zuständiger Agent für Umsetzung:** `Agent 2` (Postprocessor-Coder-Agent) für Code- & .cps-Modifikationen.
* **Zuständiger Agent für Prüfung & Freigabe:** `Agent 3` (NC-Safety- & Setup-Agent) für Crash-Prüfung und Einrichteblatt.


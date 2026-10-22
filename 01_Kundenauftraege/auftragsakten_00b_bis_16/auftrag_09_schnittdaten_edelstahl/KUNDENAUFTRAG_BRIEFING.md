# 📩 Kundenauftrag: Übung 9: Schnittdaten (`S` Drehzahl & `F` Vorschub) berechnen – Warum Aluminium, Baustahl und Edelstahl völlig andere Werte brauchen
**Auftrags-Kategorie:** 9 (Werkzeugbruch-Verhütung bei Edelstahl-Umstellung)
**Auftragnehmer:** Dipl.-Ing. Buenotte – Freiberufliches Ingenieurbüro für CAD/CAM-Fertigungstechnik & Postprozessor-Entwicklung  
**Status:** Aktiv / Bereit zur Bearbeitung

---

## 1. Das Original-Auftragsbriefing des Kunden

So sieht eine typische Anfrage aus, wenn ein Kunde beim Wechsel von Aluminium auf zähen Edelstahl teuren Werkzeugbruch erleidet:

> **Von:** Frank Lehmann *(Produktionsleiter)* `<f.lehmann@krupp-maschinenteile.de>`  
> **An:** Dipl.-Ing. Buenotte `<kontakt@ingenieurbuero-buenotte.de>`  
> **Datum:** 23. Oktober 2026, 08:45 Uhr  
> **Betreff:** EILIGE ANFRAGE: Schnittdaten-Optimierung Edelstahl V4A 1.4571 – Fräser brennen ab  
>
> Sehr geehrter Herr Dipl.-Ing. Buenotte,  
> 
> wir haben ein massives Fertigungsproblem in Duisburg: Wir fertigen seit Jahren ein Gehäuse aus Aluminium mit $8.000\,\text{U/min}$ und $1.200\,\text{mm/min}$ Vorschub. Jetzt hat unser Großkunde das Material auf hochlegierten Edelstahl V4A *(Werkstoff 1.4571 / X6CrNiMoTi17-12-2)* umgestellt.  
> 
> Unser CAM-Programmierer hat die bisherigen Schnittdaten übernommen – gestern sind innerhalb von zwei Stunden drei brandneue VHM-Schaftfräser $\varnothing 10\,\text{mm}$ (Stückpreis: 85 €) rotglühend abgebrannt und zersplittert!  
> 
> **Aufgabenstellung:**  
> Berechnen Sie die physikalisch korrekten, standzeit-optimierten Schnittdaten für:  
> 1. Werkstoff Aluminium EN AW-6082 ($v_c = 300\,\text{m/min}$, $f_z = 0{,}06\,\text{mm}$)  
> 2. Werkstoff Baustahl S235JR ($v_c = 160\,\text{m/min}$, $f_z = 0{,}05\,\text{mm}$)  
> 3. Werkstoff Edelstahl V4A 1.4571 ($v_c = 80\,\text{m/min}$, $f_z = 0{,}035\,\text{mm}$)  
> Passen Sie das NC-Programm an und dokumentieren Sie die Formeln für Spindeldrehzahl $S$ und Vorschub $F$.  
> 
> **Honorar:**  
> Festpreis **480,00 € netto** gegen Rechnung.  
> 
> Mit besten Grüßen  
> **Frank Lehmann** – Krupp Maschinenteile GmbH, Duisburg

---

## 2. Bearbeitungshinweise für diesen Auftrag
* **Zuständiger Agent für Angebot:** `Agent 4` (Backoffice-Agent) – siehe `ANGEBOT_DIPL_ING_BUENOTTE.md` in diesem Ordner.
* **Zuständiger Agent für Umsetzung:** `Agent 2` (Postprocessor-Coder-Agent) für Code- & .cps-Modifikationen.
* **Zuständiger Agent für Prüfung & Freigabe:** `Agent 3` (NC-Safety- & Setup-Agent) für Crash-Prüfung und Einrichteblatt.

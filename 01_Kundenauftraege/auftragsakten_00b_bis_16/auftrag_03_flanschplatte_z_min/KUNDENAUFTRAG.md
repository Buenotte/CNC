# 📩 Kundenauftrag: Schmidt Präzisionstechnik GmbH (Auftrag 03: Z-MIN Tiefenberechnung & Schraubstock-Crashschutz)

**Auftraggeber:** Markus Weber (Fertigungsleiter)  
**Unternehmen:** Schmidt Präzisionstechnik GmbH  
**Empfänger:** Dipl.-Ing. Buenotte `<kontakt@ingenieurbuero-buenotte.de>`  
**Zielmaschine:** **Haas VF-2 (Haas NGC Steuerung)**  
**Vereinbartes Budget:** **480,00 € netto** (571,20 € brutto)  

---

## Auftrags-Briefing des Kunden:

# 📩 Kundenauftrag: Übung 3: Sicherheits-Schutz gegen Maschinencrash – Tiefste Frästiefe (`Z-MIN`) berechnen
**Auftrags-Kategorie:** 3 (Original-Anfrage an dein Ingenieurbüro)
**Auftragnehmer:** Dipl.-Ing. Buenotte – Freiberufliches Ingenieurbüro für CAD/CAM-Fertigungstechnik & Postprozessor-Entwicklung  
**Status:** Aktiv / Bereit zur Bearbeitung

---

## 1. Das Original-Auftragsbriefing des Kunden

So sieht eine typische, hochbezahlte E-Mail aus, die ein Zerspanungsbetrieb an dein freiberufliches Ingenieurbüro schickt, wenn es in der Werkstatt brennt:

> **Von:** Markus Weber *(Fertigungsleiter)* `<m.weber@schmidt-praezision.de>`  
> **An:** Dipl.-Ing. Buenotte `<kontakt@ingenieurbuero-buenotte.de>`  
> **Datum:** 22. Oktober 2026, 09:15 Uhr  
> **Betreff:** EIL-ANFRAGE: Postprozessor-Anpassung & Z-MIN Sicherheitsprüfung für Haas VF-2 (Projekt: Flanschplatte 1001)  
>
> Sehr geehrter Herr Kollege Dipl.-Ing. Buenotte,  
> 
> ich wende mich mit einer dringenden technischen Aufgabenstellung an Ihr Ingenieurbüro.  
> 
> Wir haben in unserer Fertigungshalle in Kassel seit zwei Wochen ein neues 3-Achs-Bearbeitungszentrum *(Haas VF-2 mit NextGen Control)* im Einsatz. Für die CAM-Programmierung nutzen wir Autodesk Fusion 360.  
> 
> Aktuell haben wir einen Serienauftrag über **150 Stück Flanschplatten (Aluminium EN AW-6082)** auf der Maschine. Gestern kam es beim Einrichten beinahe zu einer schweren Kollision mit den Schraubstockbacken, weil der Standard-Postprozessor von Autodesk die tiefste Frästiefe nicht im Programmkopf anzeigt und der Tisch am Programmende hinten stehen bleibt.  
> 
> Da wir von Ihrer Spezialisierung auf maschinenspezifische Postprozessor-Entwicklung und CNC-Kollisionsschutz erfahren haben, möchten wir Sie mit folgendem Gesamtpaket beauftragen:  
> 
> #### 📋 Technische Auftragsdaten (Projekt: Flanschplatte 1001):
> 1. **Bauteil-Geometrie (Zeichnung Teil 1001 im Anhang):**  
>    * **Fertigmaß:** $80 \times 50 \times 12\,\text{mm}$  
>    * **Rohteil aus der Säge:** $85 \times 55 \times 15\,\text{mm}$ *(Aufmaß: $2{,}5\,\text{mm}$ seitlich rundherum, $3\,\text{mm}$ am Boden)*  
>    * **Bearbeitung Oberseite (OP10):**  
>      * Außenkontur: $5\,\text{mm}$ Stufe absetzen *(Schnitttiefe $Z = -5{,}0\,\text{mm}$)*  
>      * Kreistasche im Zentrum: $\varnothing 30\,\text{mm}$, Tiefe $3\,\text{mm}$ *(Schnitttiefe $Z = -3{,}0\,\text{mm}$)*  
>      * 4 Befestigungsbohrungen: $\varnothing 6\,\text{mm}$ komplett durchbohren *(Schnitttiefe $Z = -12{,}0\,\text{mm}$)*  
> 2. **Spannsituation im Maschinenschraubstock:**  
>    * Maschinenschraubstock mit gehärteten Stahlbacken.  
>    * Das Werkstück wird unten an den untersten $3\,\text{mm}$ gespannt *(Spannrand $Z = -12\,\text{mm}$ bis $Z = -15\,\text{mm}$)*.  
>    * **Kritische Sicherheitsgrenze:** Die Stahlbacken liegen bei $Z = -12{,}5\,\text{mm}$. Ein Eintauchen tiefer als $Z = -12{,}0\,\text{mm}$ führt zum Crash!  
> 3. **Werkzeuge im Magazin:**  
>    * `T01`: VHM-Schaftfräser $\varnothing 10\,\text{mm}$ *(Schnittdaten: $S=8000\,\text{U/min}$, $F=1200\,\text{mm/min}$)*  
>    * `T02`: VHM-Spiralbohrer $\varnothing 6\,\text{mm}$ *(Tiefbohrzyklus G83 mit $Q=3\,\text{mm}$ Spanbruch, $S=3500\,\text{U/min}$, $F=300\,\text{mm/min}$)*  
> 
> #### 🎯 Unser Anforderungskatalog an Ihr Ingenieurbüro:
> 1. **Postprozessor-Anpassung (`schmidt_haas_vf2.cps`):**  
>    * Automatische Berechnung und gut sichtbare Ausgabe der absolut tiefsten Frästiefe **`Z-MIN`** ganz oben im Programmkopf.  
>    * Sicherheitswarnung im G-Code, falls $Z_{\text{min}}$ tiefer als $-12{,}0\,\text{mm}$ programmiert werden sollte.  
>    * Am Programmende soll der Frästisch automatisch mit `G53 G00 Y0.` ganz nach vorne an die Schiebetür fahren, damit der Werker bequem entladen kann.  
> 2. **Crash-Prüfung & Freigabe-Video:**  
>    * Wir benötigen vorab ein kurzes **30-Sekunden-Simulationsvideo** aus dem Maschinencode, damit mein Schichtleiter sieht, dass die Werkzeugwege kollisionsfrei über den Spannbacken bleiben.  
> 3. **Einrichteblatt (PDF):**  
>    * Ausdruckbare Werkzeugliste für den Bediener an der Maschine mit Drehzahlen, Vorschüben und Nullpunkt `G54` (oben links).  
> 
> #### 💰 Konditionen & Vergütung:
> * Für dieses Gesamtpaket bieten wir ein Festhonorar von **480,00 € netto**.  
> * Zahlungsbedingung: **50 % Anzahlung (240,00 €) sofort** nach Erhalt Ihrer Auftragsbestätigung, restliche **50 % (240,00 €)** vor Code-Übergabe.  
> * Lieferzeit: Innerhalb von 24 bis 48 Stunden.  
> 
> Bitte senden Sie uns Ihre offizielle Auftragsbestätigung nach § 18 EStG zu, damit unsere Buchhaltung die Anzahlung heute noch anweisen kann.  
> 
> Mit freundlichen Grüßen aus Kassel  
> **Dipl.-Ing. (FH) Markus Weber**  
> *Leiter Fertigung & Zerspanungstechnik* – Schmidt Präzisionsteile GmbH & Co. KG  
> Industriestraße 14, 34123 Kassel

---

## 2. Bearbeitungshinweise für diesen Auftrag
* **Zuständiger Agent für Angebot:** `Agent 4` (Backoffice-Agent) – siehe `ANGEBOT_DIPL_ING_BUENOTTE.md` in diesem Ordner.
* **Zuständiger Agent für Umsetzung:** `Agent 2` (Postprocessor-Coder-Agent) für Code- & .cps-Modifikationen.
* **Zuständiger Agent für Prüfung & Freigabe:** `Agent 3` (NC-Safety- & Setup-Agent) für Crash-Prüfung und Einrichteblatt.


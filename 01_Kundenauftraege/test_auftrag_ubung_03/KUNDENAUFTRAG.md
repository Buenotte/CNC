# 📩 Kundenauftrag: Schmidt Präzisionstechnik GmbH (Übung 3)

**Auftraggeber:** Markus Weber *(Fertigungsleiter)* `<m.weber@schmidt-praezision.de>`  
**Unternehmen:** Schmidt Präzisionstechnik GmbH  
**Empfänger:** Dipl.-Ing. Buenotte `<kontakt@ingenieurbuero-buenotte.de>`  
**Datum:** 14. Oktober 2026, 08:45 Uhr  
**Betreff:** EIL-AUFTRAG: Postprozessor-Crashschutz Z-MIN & Einrichteblatt für Haas VF-2  

---

## Die Kunden-E-Mail (Das Briefing):

> Sehr geehrter Herr Dipl.-Ing. Buenotte,  
> 
> wir hatten gestern an unserer neuen **Haas VF-2 *(3-Achs-CNC-Bearbeitungszentrum mit Haas NGC-Steuerung)*** beinahe einen massiven Maschinencrash: Ein Mitarbeiter hat bei einer Kleinserie vergessen, die Auskraglänge des Schaftfräsers zu prüfen. Der Werkzeughalter ist nur um Haaresbreite an den gehärteten Stahlbacken unseres Maschinenschraubstocks vorbeigeschrammt!  
> 
> Uns wurde Ihr freiberufliches Ingenieurbüro als Spezialist für CAM-Postprozessor-Sicherheit und automatisierte G-Code-Prüfung empfohlen.  
> 
> **Wir möchten Sie mit folgendem Eilauftrag beauftragen:**  
> 
> 1. **Postprozessor-Anpassung *(JavaScript `.cps` für Autodesk Fusion)***:  
>    Der Postprozessor muss für jedes eingewechselte Fräs- und Bohrwerkzeug die **absolut tiefste Frästiefe (`Z-MIN`) berechnen** und direkt oben im NC-Header in die Werkzeugliste hineinschreiben *(z. B. `(T01 D=10.0 CR=0.0 - Z-MIN: -5.000 MM - VORSICHT TIEFE)`)*.  
> 
> 2. **Konkretes Testbauteil („Flanschplatte OP10“):**  
>    Als Referenzteil für den Abnahmetest nutzen wir unser 3D-Modell [`bauteil_1001.stl`](file:///c:/Projekte/CNC/01_Kundenauftraege/test_auftrag_ubung_03/bauteil_1001.stl):  
>    * **Fertigmaß des Werkstücks:** `80 mm` lang $\times$ `50 mm` breit $\times$ `12 mm` hoch *(Material: Aluminium EN AW-6082 / AlSi1MgMn)*.  
>    * **Rohteil im Schraubstock:** `85 mm` $\times$ `55 mm` $\times$ `15 mm`. Der Maschinenschraubstock klemmt das Rohteil an der Unterseite mit einem **Spannrand *(Einspanntiefe)* von exakt `3,0 mm`** *(von `Z = -12,0 mm` bis `Z = -15,0 mm`)*.  
>    * **Kollisionsgrenze:** Jeder Frässchnitt tiefer als `Z = -12,0 mm` rammt die gehärteten Stahlbacken des Schraubstocks!  
>    * **Geplante Zerspanungs-Operationen:**  
>      - Stufe 1: Außenkontur auf Tiefe `Z = -5,0 mm` mit VHM-Schaftfräser $\varnothing 10\text{ mm}$ (`T01`).  
>      - Stufe 2: Kreistasche im Zentrum $\varnothing 30\text{ mm}$ auf Tiefe `Z = -3,0 mm` (`T01`).  
>      - Stufe 3: 4x Durchgangsbohrungen $\varnothing 6\text{ mm}$ mit VHM-Spiralbohrer (`T02`).  
>    * **Werkstück-Nullpunkt (`G54`):** Vorne links oben auf der Fertigteil-Oberkante (`X0, Y0, Z0`).  
> 
> 3. **Geforderter Lieferumfang:**  
>    * Ein formelles Ingenieur-Angebot vorab.  
>    * Das fertig generierte und geprüfte NC-Programm (`.nc`) für unsere Haas VF-2 mit Z-MIN Berechnung im Programmkopf.  
>    * Einen schriftlichen Sicherheits- und Crash-Prüfbericht.  
>    * Das fertige Rüstdatenblatt / Einrichteblatt als Arbeitsanweisung für unseren Fräser an der Maschine.  
>    * Die abschließende Honorarabrechnung.  
> 
> **Budget & Konditionen:**  
> Wir vergüten diese Auslegung und Postprozessor-Anpassung mit einem **Festpreis von 480,00 € netto**. Bitte senden Sie uns vorab Ihr formelles Ingenieur-Angebot zu.  
> 
> Mit freundlichen Grüßen  
> **Markus Weber**  
> Fertigungsleitung – Schmidt Präzisionstechnik GmbH  

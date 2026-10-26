# 📩 Auftrag 07: Konfigurierbare Postprozessor-Properties (Späneförderer M31/M33) — Vogtland Zerspanungstechnik GmbH

**Auftraggeber:** Karsten Wolf (Technischer Leiter)  
**Unternehmen:** Vogtland Zerspanungstechnik GmbH  
**Empfänger:** Dipl.-Ing. Bujanovski `<kontakt@ingenieurbuero-bujanovski.de>`  
**Zielmaschine:** **Alzmetall CS 1200 (ISO G-Code-Modus)**  
**Vereinbartes Budget:** **390,00 € netto** (464,10 € brutto)  

---

## Auftrags-Briefing des Kunden:

**Auftrags-Kategorie:** 7 (Konfigurierbare Schalter für verschiedene Materialien)
**Auftragnehmer:** Dipl.-Ing. Bujanovski – Freiberufliches Ingenieurbüro für CAD/CAM-Fertigungstechnik & Postprozessor-Entwicklung  
**Status:** Aktiv / Bereit zur Bearbeitung

---

## 1. Das Original-Auftragsbriefing des Kunden

So sieht eine typische Anfrage aus, wenn ein Betrieb verschiedene Werkstoffe zerspant und dafür benutzerdefinierte Schalter im CAM-Dialog braucht:

> **Von:** Karsten Wolf *(Technischer Leiter)* `<k.wolf@vogtland-zerspanung.de>`  
> **An:** Dipl.-Ing. Bujanovski `<kontakt@ingenieurbuero-bujanovski.de>`  
> **Datum:** 21. Oktober 2026, 09:45 Uhr  
> **Betreff:** Postprozessor-Erweiterung: Konfigurierbare Schalter (Properties) im Fusion-Dialog  
>
> Sehr geehrter Herr Dipl.-Ing. Bujanovski,  
> 
> wir fertigen auf derselben CNC-Maschine sowohl Aluminiumteile als auch POM- und PEEK-Kunststoffe.  
> * Bei Aluminium brauchen wir Flutkühlung (`M08`).  
> * Bei Kunststoff dürfen wir jedoch kein Wasser nutzen, sondern benötigen trockene Druckluft (`M07` Blasluft), weil der Kunststoff sonst quillt.  
> 
> Bisher müssen unsere Programmierer den G-Code nach dem Postprozessieren mühsam im Texteditor öffnen und `M08` von Hand durch `M07` ersetzen – das führt immer wieder zu Fehlern!  
> 
> **Aufgabenstellung:**  
> Bauen Sie in den Einstellungs-Bereich `properties` unseres Postprozessors zwei neue Schalter ein, die direkt im Fusion 360 Exportfenster als Checkbox erscheinen:  
> 1. Schalter 1: `useAirBlow` *(Blasluft M07 statt Flutkühlung M08 aktivieren)*.  
> 2. Schalter 2: `chipConveyor` *(Späneförderer automatisch mit M31 beim Start einschalten und bei M33 am Ende stoppen)*.  
> 
> **Vergütung:**  
> Festpreis **390,00 € netto** gegen Rechnung.  
> 
> Mit freundlichen Grüßen  
> **Karsten Wolf** – Vogtland Zerspanungs-GmbH, Plauen

---

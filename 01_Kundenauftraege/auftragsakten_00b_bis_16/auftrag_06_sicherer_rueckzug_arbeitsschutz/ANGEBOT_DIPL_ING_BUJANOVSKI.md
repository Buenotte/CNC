# 📄 Ingenieur-Angebot: Auftrag 06: Sicherer Maschinen-Rückzug (G53 Z0 / Y0) & Arbeitsschutz

* **Auftragnehmer:** Ingenieurbüro Dipl.-Ing. (FH) Alexander Bujanovski *(Freiberuflicher Beratender Ingenieur nach § 18 Abs. 1 Nr. 1 EStG [Einkommensteuergesetz])*
* **Auftraggeber:** **Süd-Zerspanung GmbH**, z. Hd. Andreas Eder (Betriebsleiter), Gewerbering 7, 83022 Rosenheim
* **Angebot-Nr.:** `ANG-2026-06`
* **Projekt / Bauteil:** Gehäusedeckel-Serie (Ergonomie- & Rückzugs-Update onClose)
* **Zielmaschine & Steuerung:** Haas VF-2 (Haas NGC Steuerung) — Haas NGC (Next Generation Control / ISO G-Code)

---

## 1. Technische Ausgangslage & Aufgabenstellung

Sehr geehrte(r) Andreas Eder (Betriebsleiter),

vielen Dank für Ihre Projektanfrage bezüglich der ingenieurtechnischen Auslegung und Programmierung für Ihre **Haas VF-2 (Haas NGC Steuerung)**. Ziel des Auftrags ist die Entwicklung und mathematische Verifikation von `uebung_06_sicherer_rueckzug.nc` (sowie `uebung_06_sicherer_rueckzug.cps`) für das Bauteil **Gehäusedeckel-Serie (Ergonomie- & Rückzugs-Update onClose)** aus dem Werkstoff **Baustahl S355J2 (1.0577)** unter strikter Einhaltung aller Kollisions- und Arbeitsschutzvorgaben.

---

## 2. Ingenieurtechnischer Leistungsumfang *(Freie Ingenieurleistung nach § 18 EStG)*

1. **Algorithmische Postprozessor- & NC-Architektur *(Agent 2 — Postprocessor-Coder-Agent)*:**
   - Implementierung und Validierung der steuerungsspezifischen Ausgabelogik für **Haas NGC (Next Generation Control / ISO G-Code)**.
   - Ausgabe eines eindeutigen Sicherheits-Startblocks *(Safe Start Block)* sowie exakter Werkzeuglängenkompensation (`H01`).
2. **Mathematische Z-MIN-Kollisionsanalyse & Einrichtedokumentation *(Agent 3 — NC-Safety- & Setup-Agent)*:**
   - Statische Überprüfung aller Verfahrwege in `uebung_06_sicherer_rueckzug.nc` auf Einhaltung der tiefsten Zustellung $Z_{\text{min}} = -5.000\,\text{mm}$ gegenüber der Spannmittel-Oberkante bei $Z = -15.000\,\text{mm}$.
   - Erstellung des formalen Prüfberichts [`05_SICHERHEITS_CRASH_PRUEFBERICHT.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_06_sicherer_rueckzug_arbeitsschutz/05_SICHERHEITS_CRASH_PRUEFBERICHT.md), des Einrichteblatts [`06_EINRICHTEBLATT_SETUP_SHEET.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_06_sicherer_rueckzug_arbeitsschutz/06_EINRICHTEBLATT_SETUP_SHEET.md) sowie des 3D-Simulationsvideos [`uebung_06_sicherer_rueckzug_simulation_video.mp4`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_06_sicherer_rueckzug_arbeitsschutz/uebung_06_sicherer_rueckzug_simulation_video.mp4).

---

## 3. Honorarkalkulation *(Festpreis nach § 18 EStG)*

| Pos. | Leistungsbeschreibung *(Ingenieurtechnische Entwicklung)* | Aufwand | Stundensatz | Gesamtpreis (Netto) |
| :---: | :--- | :---: | :---: | :---: |
| **1** | Ingenieurtechnische Analyse, Postprozessor-/CAM-Entwicklung (`uebung_06_sicherer_rueckzug.nc`), statische Z-MIN-Kollisionsprüfung & Werkstatteinrichteblatt | 4,20 Std. | 100,00 € | **420,00 €** |
| | **Summe Netto** | | | **420,00 €** |
| | zzgl. 19 % Umsatzsteuer *(gemäß § 14 UStG [Umsatzsteuergesetz])* | | | 79,80 € |
| | **Gesamtbetrag (Brutto)** | | | **499,80 €** |

---

## 4. Abwicklungsmodalitäten & Sicherheitshinweis *(Mitwirkungspflicht)*

* **Lieferzeit:** Sofortige digitale Bereitstellung aller 6 Projekt-Artefakte nach Auftragsfreigabe.
* **Zahlungsziel:** 14 Tage netto nach Rechnungsstellung ohne Abzug.
* **Verbindlicher Sicherheitshinweis für das Einfahren an der Maschine:**
  Die gelieferten Postprozessoren und NC-Programme wurden rechnerisch und simulativ geprüft. Vor Beginn der Serienfertigung ist das Programm vom Maschinenbediener zwingend im **Einzelsatzbetrieb *(Single Block)*** bei reduziertem **Vorschub-Override *(Feedrate Potentiometer < 25 %)*** und mit Sichtkontrolle des Restwegs *(Distance-to-Go)* über dem Bauteil einzufahren.

Mit freundlichen Grüßen  
**Dipl.-Ing. (FH) Alexander Bujanovski**  
*Beratender Ingenieur für CAD/CAM-Technik & Postprozessor-Entwicklung*

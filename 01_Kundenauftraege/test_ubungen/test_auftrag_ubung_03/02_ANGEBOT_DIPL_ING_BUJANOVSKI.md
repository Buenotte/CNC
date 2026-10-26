# 📄 Ingenieur-Angebot: Auftrag 03: Automatischer Z-MIN-Kollisionsschutz (Flanschplatte)

* **Auftragnehmer:** Ingenieurbüro Dipl.-Ing. (FH) Alexander Bujanovski *(Freiberuflicher Beratender Ingenieur nach § 18 Abs. 1 Nr. 1 EStG [Einkommensteuergesetz])*
* **Auftraggeber:** **Schmidt Präzisionsteile GmbH & Co. KG**, z. Hd. Dipl.-Ing. (FH) Markus Weber (Leiter Fertigung & Zerspanungstechnik), Industriestraße 14, 34123 Kassel
* **Angebot-Nr.:** `ANG-2026-03`
* **Projekt / Bauteil:** Flanschplatte 80 x 50 x 12 mm (Serienauftrag 150 Stück, OP10)
* **Zielmaschine & Steuerung:** Haas VF-2 (Haas NextGen Control) — Haas NGC (Next Generation Control / Fanuc-ISO-Modus)

---

## 1. Technische Ausgangslage & Aufgabenstellung

Sehr geehrte(r) Dipl.-Ing. (FH) Markus Weber (Leiter Fertigung & Zerspanungstechnik),

vielen Dank für Ihre Projektanfrage bezüglich der ingenieurtechnischen Auslegung und Programmierung für Ihre **Haas VF-2 (Haas NextGen Control)**. Ziel des Auftrags ist die Entwicklung und mathematische Verifikation von `uebung_03_z_min_berechnung.nc` (sowie `uebung_03_z_min_berechnung.cps`) für das Bauteil **Flanschplatte 80 x 50 x 12 mm (Serienauftrag 150 Stück, OP10)** aus dem Werkstoff **Aluminium EN AW-6082 T6 (Rohteil 85 x 55 x 15 mm)** unter strikter Einhaltung aller Kollisions- und Arbeitsschutzvorgaben.

---

## 2. Ingenieurtechnischer Leistungsumfang *(Freie Ingenieurleistung nach § 18 EStG)*

1. **Algorithmische Postprozessor- & NC-Architektur *(Agent 2 — Postprocessor-Coder-Agent)*:**
   - Implementierung und Validierung der steuerungsspezifischen Ausgabelogik für **Haas NGC (Next Generation Control / Fanuc-ISO-Modus)**.
   - Ausgabe eines eindeutigen Sicherheits-Startblocks *(Safe Start Block)* sowie exakter Werkzeuglängenkompensation (`H01`).
2. **Mathematische Z-MIN-Kollisionsanalyse & Einrichtedokumentation *(Agent 3 — NC-Safety- & Setup-Agent)*:**
   - Statische Überprüfung aller Verfahrwege in `uebung_03_z_min_berechnung.nc` auf Einhaltung der tiefsten Zustellung $Z_{\text{min}} = -12.000\,\text{mm}$ gegenüber der Spannmittel-Oberkante bei $Z = -12.500\,\text{mm}$.
   - Erstellung des formalen Prüfberichts [`05_SICHERHEITS_CRASH_PRUEFBERICHT.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/test_ubungen/test_auftrag_ubung_03/05_SICHERHEITS_CRASH_PRUEFBERICHT.md), des Einrichteblatts [`06_EINRICHTEBLATT_SETUP_SHEET.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/test_ubungen/test_auftrag_ubung_03/06_EINRICHTEBLATT_SETUP_SHEET.md) sowie des 3D-Simulationsvideos [`uebung_03_simulation_video.mp4`](file:///c:/Projekte/CNC/01_Kundenauftraege/test_ubungen/test_auftrag_ubung_03/uebung_03_simulation_video.mp4).

---

## 3. Honorarkalkulation *(Festpreis nach § 18 EStG)*

| Pos. | Leistungsbeschreibung *(Ingenieurtechnische Entwicklung)* | Aufwand | Stundensatz | Gesamtpreis (Netto) |
| :---: | :--- | :---: | :---: | :---: |
| **1** | Ingenieurtechnische Analyse, Postprozessor-/CAM-Entwicklung (`uebung_03_z_min_berechnung.nc`), statische Z-MIN-Kollisionsprüfung & Werkstatteinrichteblatt | 5,00 Std. | 96,00 € | **480,00 €** |
| | **Summe Netto** | | | **480,00 €** |
| | zzgl. 19 % Umsatzsteuer *(gemäß § 14 UStG [Umsatzsteuergesetz])* | | | 91,20 € |
| | **Gesamtbetrag (Brutto)** | | | **571,20 €** |

---

## 4. Abwicklungsmodalitäten & Sicherheitshinweis *(Mitwirkungspflicht)*

* **Lieferzeit:** Sofortige digitale Bereitstellung aller 6 Projekt-Artefakte nach Auftragsfreigabe.
* **Zahlungsziel:** 14 Tage netto nach Rechnungsstellung ohne Abzug.
* **Verbindlicher Sicherheitshinweis für das Einfahren an der Maschine:**
  Die gelieferten Postprozessoren und NC-Programme wurden rechnerisch und simulativ geprüft. Vor Beginn der Serienfertigung ist das Programm vom Maschinenbediener zwingend im **Einzelsatzbetrieb *(Single Block)*** bei reduziertem **Vorschub-Override *(Feedrate Potentiometer < 25 %)*** und mit Sichtkontrolle des Restwegs *(Distance-to-Go)* über dem Bauteil einzufahren.

Mit freundlichen Grüßen  
**Dipl.-Ing. (FH) Alexander Bujanovski**  
*Beratender Ingenieur für CAD/CAM-Technik & Postprozessor-Entwicklung*

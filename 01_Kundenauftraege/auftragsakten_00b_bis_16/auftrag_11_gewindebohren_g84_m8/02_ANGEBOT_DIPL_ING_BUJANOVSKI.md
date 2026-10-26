# 📄 Ingenieur-Angebot: Auftrag 11: Synchron-Gewindebohren (Rigid Tapping M29 + G84 für M8x1,25)

* **Auftragnehmer:** Ingenieurbüro Dipl.-Ing. (FH) Alexander Bujanovski *(Freiberuflicher Beratender Ingenieur nach § 18 Abs. 1 Nr. 1 EStG [Einkommensteuergesetz])*
* **Auftraggeber:** **Meyer Hydraulikkomponenten GmbH**, z. Hd. Christian Meyer (Fertigungsleiter), Dieselstraße 9, 86154 Augsburg
* **Angebot-Nr.:** `ANG-2026-11`
* **Projekt / Bauteil:** Getriebeflanschplatte mit 4x Befestigungsgewinde M8 (Steigung P = 1,25 mm)
* **Zielmaschine & Steuerung:** Haas VF-4SS (Haas NGC Steuerung) — Haas NGC / Fanuc ISO (Synchron-Gewindebohren M29 S500 + G84 F625)

---

## 1. Technische Ausgangslage & Aufgabenstellung

Sehr geehrte(r) Christian Meyer (Fertigungsleiter),

vielen Dank für Ihre Projektanfrage bezüglich der ingenieurtechnischen Auslegung und Programmierung für Ihre **Haas VF-4SS (Haas NGC Steuerung)**. Ziel des Auftrags ist die Entwicklung und mathematische Verifikation von `uebung_11_gewindebohren_g84.nc` (sowie `uebung_11_gewindebohren_g84.cps`) für das Bauteil **Getriebeflanschplatte mit 4x Befestigungsgewinde M8 (Steigung P = 1,25 mm)** aus dem Werkstoff **Baustahl S235JR / C45 (1.0503)** unter strikter Einhaltung aller Kollisions- und Arbeitsschutzvorgaben.

---

## 2. Ingenieurtechnischer Leistungsumfang *(Freie Ingenieurleistung nach § 18 EStG)*

1. **Algorithmische Postprozessor- & NC-Architektur *(Agent 2 — Postprocessor-Coder-Agent)*:**
   - Implementierung und Validierung der steuerungsspezifischen Ausgabelogik für **Haas NGC / Fanuc ISO (Synchron-Gewindebohren M29 S500 + G84 F625)**.
   - Ausgabe eines eindeutigen Sicherheits-Startblocks *(Safe Start Block)* sowie exakter Werkzeuglängenkompensation (`H01`).
2. **Mathematische Z-MIN-Kollisionsanalyse & Einrichtedokumentation *(Agent 3 — NC-Safety- & Setup-Agent)*:**
   - Statische Überprüfung aller Verfahrwege in `uebung_11_gewindebohren_g84.nc` auf Einhaltung der tiefsten Zustellung $Z_{\text{min}} = -12.000\,\text{mm}$ gegenüber der Spannmittel-Oberkante bei $Z = -16.000\,\text{mm}$.
   - Erstellung des formalen Prüfberichts [`05_SICHERHEITS_CRASH_PRUEFBERICHT.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_11_gewindebohren_g84_m8/05_SICHERHEITS_CRASH_PRUEFBERICHT.md), des Einrichteblatts [`06_EINRICHTEBLATT_SETUP_SHEET.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_11_gewindebohren_g84_m8/06_EINRICHTEBLATT_SETUP_SHEET.md) sowie des 3D-Simulationsvideos [`uebung_11_gewindebohren_g84_simulation_video.mp4`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_11_gewindebohren_g84_m8/uebung_11_gewindebohren_g84_simulation_video.mp4).

---

## 3. Honorarkalkulation *(Festpreis nach § 18 EStG)*

| Pos. | Leistungsbeschreibung *(Ingenieurtechnische Entwicklung)* | Aufwand | Stundensatz | Gesamtpreis (Netto) |
| :---: | :--- | :---: | :---: | :---: |
| **1** | Ingenieurtechnische Analyse, Postprozessor-/CAM-Entwicklung (`uebung_11_gewindebohren_g84.nc`), statische Z-MIN-Kollisionsprüfung & Werkstatteinrichteblatt | 4,60 Std. | 100,00 € | **460,00 €** |
| | **Summe Netto** | | | **460,00 €** |
| | zzgl. 19 % Umsatzsteuer *(gemäß § 14 UStG [Umsatzsteuergesetz])* | | | 87,40 € |
| | **Gesamtbetrag (Brutto)** | | | **547,40 €** |

---

## 4. Abwicklungsmodalitäten & Sicherheitshinweis *(Mitwirkungspflicht)*

* **Lieferzeit:** Sofortige digitale Bereitstellung aller 6 Projekt-Artefakte nach Auftragsfreigabe.
* **Zahlungsziel:** 14 Tage netto nach Rechnungsstellung ohne Abzug.
* **Verbindlicher Sicherheitshinweis für das Einfahren an der Maschine:**
  Die gelieferten Postprozessoren und NC-Programme wurden rechnerisch und simulativ geprüft. Vor Beginn der Serienfertigung ist das Programm vom Maschinenbediener zwingend im **Einzelsatzbetrieb *(Single Block)*** bei reduziertem **Vorschub-Override *(Feedrate Potentiometer < 25 %)*** und mit Sichtkontrolle des Restwegs *(Distance-to-Go)* über dem Bauteil einzufahren.

Mit freundlichen Grüßen  
**Dipl.-Ing. (FH) Alexander Bujanovski**  
*Beratender Ingenieur für CAD/CAM-Technik & Postprozessor-Entwicklung*

# 📄 Ingenieur-Angebot: Auftrag 14: Heidenhain TNC 640 Klartext-Postprozessor (4-Achs-Indexierung A-Achse)

* **Auftragnehmer:** Ingenieurbüro Dipl.-Ing. (FH) Alexander Bujanovski *(Freiberuflicher Beratender Ingenieur nach § 18 Abs. 1 Nr. 1 EStG [Einkommensteuergesetz])*
* **Auftraggeber:** **Alps Precision AG (Schweiz)**, z. Hd. Urs Hodel (Produktionsleiter), Industriestrasse 18, CH-9015 St. Gallen (Schweiz)
* **Angebot-Nr.:** `ANG-2026-14`
* **Projekt / Bauteil:** 4-Seiten-Steuerwelle auf Teilapparat (Indexierung A+0 / A+90 / A+180 / A+270)
* **Zielmaschine & Steuerung:** Hermle C400 (Heidenhain TNC 640 Steuerung mit 4. Achse / A-Achse) — Heidenhain TNC 640 (Klartext-Dialogprogrammierung .H mit M126 & CYCL DEF 200)

---

## 1. Technische Ausgangslage & Aufgabenstellung

Sehr geehrte(r) Urs Hodel (Produktionsleiter),

vielen Dank für Ihre Projektanfrage bezüglich der ingenieurtechnischen Auslegung und Programmierung für Ihre **Hermle C400 (Heidenhain TNC 640 Steuerung mit 4. Achse / A-Achse)**. Ziel des Auftrags ist die Entwicklung und mathematische Verifikation von `uebung_14_heidenhain_klartext_4achse.nc` (sowie `uebung_14_heidenhain_klartext_4achse.cps`) für das Bauteil **4-Seiten-Steuerwelle auf Teilapparat (Indexierung A+0 / A+90 / A+180 / A+270)** aus dem Werkstoff **Edelstahl 1.4404 (X2CrNiMo17-12-2 / V4A)** unter strikter Einhaltung aller Kollisions- und Arbeitsschutzvorgaben.

---

## 2. Ingenieurtechnischer Leistungsumfang *(Freie Ingenieurleistung nach § 18 EStG)*

1. **Algorithmische Postprozessor- & NC-Architektur *(Agent 2 — Postprocessor-Coder-Agent)*:**
   - Implementierung und Validierung der steuerungsspezifischen Ausgabelogik für **Heidenhain TNC 640 (Klartext-Dialogprogrammierung .H mit M126 & CYCL DEF 200)**.
   - Ausgabe eines eindeutigen Sicherheits-Startblocks *(Safe Start Block)* sowie exakter Werkzeuglängenkompensation (`TOOL CALL 1 Z`).
2. **Mathematische Z-MIN-Kollisionsanalyse & Einrichtedokumentation *(Agent 3 — NC-Safety- & Setup-Agent)*:**
   - Statische Überprüfung aller Verfahrwege in `uebung_14_heidenhain_klartext_4achse.nc` auf Einhaltung der tiefsten Zustellung $Z_{\text{min}} = -12.000\,\text{mm}$ gegenüber der Spannmittel-Oberkante bei $Z = -18.000\,\text{mm}$.
   - Erstellung des formalen Prüfberichts [`05_SICHERHEITS_CRASH_PRUEFBERICHT.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_14_heidenhain_4achs_teilapparat/05_SICHERHEITS_CRASH_PRUEFBERICHT.md), des Einrichteblatts [`06_EINRICHTEBLATT_SETUP_SHEET.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_14_heidenhain_4achs_teilapparat/06_EINRICHTEBLATT_SETUP_SHEET.md) sowie des 3D-Simulationsvideos [`uebung_14_heidenhain_klartext_4achse_simulation_video.mp4`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_14_heidenhain_4achs_teilapparat/uebung_14_heidenhain_klartext_4achse_simulation_video.mp4).

---

## 3. Honorarkalkulation *(Festpreis nach § 18 EStG)*

| Pos. | Leistungsbeschreibung *(Ingenieurtechnische Entwicklung)* | Aufwand | Stundensatz | Gesamtpreis (Netto) |
| :---: | :--- | :---: | :---: | :---: |
| **1** | Ingenieurtechnische Analyse, Postprozessor-/CAM-Entwicklung (`uebung_14_heidenhain_klartext_4achse.nc`), statische Z-MIN-Kollisionsprüfung & Werkstatteinrichteblatt | 8,50 Std. | 100,00 € | **850,00 €** |
| | **Summe Netto** | | | **850,00 €** |
| | zzgl. 19 % Umsatzsteuer *(gemäß § 14 UStG [Umsatzsteuergesetz])* | | | 161,50 € |
| | **Gesamtbetrag (Brutto)** | | | **1.011,50 €** |

---

## 4. Abwicklungsmodalitäten & Sicherheitshinweis *(Mitwirkungspflicht)*

* **Lieferzeit:** Sofortige digitale Bereitstellung aller 6 Projekt-Artefakte nach Auftragsfreigabe.
* **Zahlungsziel:** 14 Tage netto nach Rechnungsstellung ohne Abzug.
* **Verbindlicher Sicherheitshinweis für das Einfahren an der Maschine:**
  Die gelieferten Postprozessoren und NC-Programme wurden rechnerisch und simulativ geprüft. Vor Beginn der Serienfertigung ist das Programm vom Maschinenbediener zwingend im **Einzelsatzbetrieb *(Single Block)*** bei reduziertem **Vorschub-Override *(Feedrate Potentiometer < 25 %)*** und mit Sichtkontrolle des Restwegs *(Distance-to-Go)* über dem Bauteil einzufahren.

Mit freundlichen Grüßen  
**Dipl.-Ing. (FH) Alexander Bujanovski**  
*Beratender Ingenieur für CAD/CAM-Technik & Postprozessor-Entwicklung*

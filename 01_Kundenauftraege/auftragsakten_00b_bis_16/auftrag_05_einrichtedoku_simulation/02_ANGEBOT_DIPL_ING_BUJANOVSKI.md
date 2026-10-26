# 📄 Ingenieur-Angebot: Auftrag 05: Einrichtedokumentation, G-Code-Verifikation & 3D-Simulation

* **Auftragnehmer:** Ingenieurbüro Dipl.-Ing. (FH) Alexander Bujanovski *(Freiberuflicher Beratender Ingenieur nach § 18 Abs. 1 Nr. 1 EStG [Einkommensteuergesetz])*
* **Auftraggeber:** **Kuhn Medizintechnik & CNC-Fräszentrum**, z. Hd. Thomas Kuhn (Inhaber & Werkstattleiter), Medizinalring 11, 78532 Tuttlingen
* **Angebot-Nr.:** `ANG-2026-05`
* **Projekt / Bauteil:** Referenz-Trägerplatte O1001 (80 x 50 x 12 mm)
* **Zielmaschine & Steuerung:** Haas VF-2 (Haas NGC Steuerung) — Haas NGC (Next Generation Control / ISO G-Code)

---

## 1. Technische Ausgangslage & Aufgabenstellung

Sehr geehrte(r) Thomas Kuhn (Inhaber & Werkstattleiter),

vielen Dank für Ihre Projektanfrage bezüglich der ingenieurtechnischen Auslegung und Programmierung für Ihre **Haas VF-2 (Haas NGC Steuerung)**. Ziel des Auftrags ist die Entwicklung und mathematische Verifikation von `output_expected.nc` (sowie Bestands-Postprozessor (Verifikationslauf)) für das Bauteil **Referenz-Trägerplatte O1001 (80 x 50 x 12 mm)** aus dem Werkstoff **Aluminium EN AW-6082 T6** unter strikter Einhaltung aller Kollisions- und Arbeitsschutzvorgaben.

---

## 2. Ingenieurtechnischer Leistungsumfang *(Freie Ingenieurleistung nach § 18 EStG)*

1. **Algorithmische Postprozessor- & NC-Architektur *(Agent 2 — Postprocessor-Coder-Agent)*:**
   - Implementierung und Validierung der steuerungsspezifischen Ausgabelogik für **Haas NGC (Next Generation Control / ISO G-Code)**.
   - Ausgabe eines eindeutigen Sicherheits-Startblocks *(Safe Start Block)* sowie exakter Werkzeuglängenkompensation (`H01`).
2. **Mathematische Z-MIN-Kollisionsanalyse & Einrichtedokumentation *(Agent 3 — NC-Safety- & Setup-Agent)*:**
   - Statische Überprüfung aller Verfahrwege in `output_expected.nc` auf Einhaltung der tiefsten Zustellung $Z_{\text{min}} = -12.000\,\text{mm}$ gegenüber der Spannmittel-Oberkante bei $Z = -15.000\,\text{mm}$.
   - Erstellung des formalen Prüfberichts [`05_SICHERHEITS_CRASH_PRUEFBERICHT.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_05_einrichtedoku_simulation/05_SICHERHEITS_CRASH_PRUEFBERICHT.md), des Einrichteblatts [`06_EINRICHTEBLATT_SETUP_SHEET.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_05_einrichtedoku_simulation/06_EINRICHTEBLATT_SETUP_SHEET.md) sowie des 3D-Simulationsvideos [`output_expected_simulation_video.mp4`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_05_einrichtedoku_simulation/output_expected_simulation_video.mp4).

---

## 3. Honorarkalkulation *(Festpreis nach § 18 EStG)*

| Pos. | Leistungsbeschreibung *(Ingenieurtechnische Entwicklung)* | Aufwand | Stundensatz | Gesamtpreis (Netto) |
| :---: | :--- | :---: | :---: | :---: |
| **1** | Ingenieurtechnische Analyse, Postprozessor-/CAM-Entwicklung (`output_expected.nc`), statische Z-MIN-Kollisionsprüfung & Werkstatteinrichteblatt | 2,80 Std. | 100,00 € | **280,00 €** |
| | **Summe Netto** | | | **280,00 €** |
| | zzgl. 19 % Umsatzsteuer *(gemäß § 14 UStG [Umsatzsteuergesetz])* | | | 53,20 € |
| | **Gesamtbetrag (Brutto)** | | | **333,20 €** |

---

## 4. Abwicklungsmodalitäten & Sicherheitshinweis *(Mitwirkungspflicht)*

* **Lieferzeit:** Sofortige digitale Bereitstellung aller 6 Projekt-Artefakte nach Auftragsfreigabe.
* **Zahlungsziel:** 14 Tage netto nach Rechnungsstellung ohne Abzug.
* **Verbindlicher Sicherheitshinweis für das Einfahren an der Maschine:**
  Die gelieferten Postprozessoren und NC-Programme wurden rechnerisch und simulativ geprüft. Vor Beginn der Serienfertigung ist das Programm vom Maschinenbediener zwingend im **Einzelsatzbetrieb *(Single Block)*** bei reduziertem **Vorschub-Override *(Feedrate Potentiometer < 25 %)*** und mit Sichtkontrolle des Restwegs *(Distance-to-Go)* über dem Bauteil einzufahren.

Mit freundlichen Grüßen  
**Dipl.-Ing. (FH) Alexander Bujanovski**  
*Beratender Ingenieur für CAD/CAM-Technik & Postprozessor-Entwicklung*

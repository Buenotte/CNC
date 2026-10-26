# 📄 Ingenieur-Angebot: Auftrag 12: Fräserradiuskorrektur G41/G42 für H7-Lagersitzpassung (Ø 30 H7)

* **Auftragnehmer:** Ingenieurbüro Dipl.-Ing. (FH) Alexander Bujanovski *(Freiberuflicher Beratender Ingenieur nach § 18 Abs. 1 Nr. 1 EStG [Einkommensteuergesetz])*
* **Auftraggeber:** **Wagner Getriebebau GmbH**, z. Hd. Alexander Wagner (Werkstattleiter), Hafenstraße 44, 24103 Kiel
* **Angebot-Nr.:** `ANG-2026-12`
* **Projekt / Bauteil:** Lagerschild mit Kugellagersitz Ø 30 H7 (+0,000 / +0,021 mm)
* **Zielmaschine & Steuerung:** DMG MORI NVX 5080 (Fanuc 31i Steuerung) — Fanuc 31i / ISO (G41 D01 Anfahrtsatz + G40 Abwahl vor Z-Rückzug)

---

## 1. Technische Ausgangslage & Aufgabenstellung

Sehr geehrte(r) Alexander Wagner (Werkstattleiter),

vielen Dank für Ihre Projektanfrage bezüglich der ingenieurtechnischen Auslegung und Programmierung für Ihre **DMG MORI NVX 5080 (Fanuc 31i Steuerung)**. Ziel des Auftrags ist die Entwicklung und mathematische Verifikation von `uebung_12_radiuskorrektur_g41.nc` (sowie `uebung_12_radiuskorrektur_g41.cps`) für das Bauteil **Lagerschild mit Kugellagersitz Ø 30 H7 (+0,000 / +0,021 mm)** aus dem Werkstoff **Einsatzstahl 16MnCr5 (1.7131)** unter strikter Einhaltung aller Kollisions- und Arbeitsschutzvorgaben.

---

## 2. Ingenieurtechnischer Leistungsumfang *(Freie Ingenieurleistung nach § 18 EStG)*

1. **Algorithmische Postprozessor- & NC-Architektur *(Agent 2 — Postprocessor-Coder-Agent)*:**
   - Implementierung und Validierung der steuerungsspezifischen Ausgabelogik für **Fanuc 31i / ISO (G41 D01 Anfahrtsatz + G40 Abwahl vor Z-Rückzug)**.
   - Ausgabe eines eindeutigen Sicherheits-Startblocks *(Safe Start Block)* sowie exakter Werkzeuglängenkompensation (`H01`).
2. **Mathematische Z-MIN-Kollisionsanalyse & Einrichtedokumentation *(Agent 3 — NC-Safety- & Setup-Agent)*:**
   - Statische Überprüfung aller Verfahrwege in `uebung_12_radiuskorrektur_g41.nc` auf Einhaltung der tiefsten Zustellung $Z_{\text{min}} = -5.000\,\text{mm}$ gegenüber der Spannmittel-Oberkante bei $Z = -15.000\,\text{mm}$.
   - Erstellung des formalen Prüfberichts [`05_SICHERHEITS_CRASH_PRUEFBERICHT.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_12_radiuskorrektur_g41_h7/05_SICHERHEITS_CRASH_PRUEFBERICHT.md), des Einrichteblatts [`06_EINRICHTEBLATT_SETUP_SHEET.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_12_radiuskorrektur_g41_h7/06_EINRICHTEBLATT_SETUP_SHEET.md) sowie des 3D-Simulationsvideos [`uebung_12_radiuskorrektur_g41_simulation_video.mp4`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_12_radiuskorrektur_g41_h7/uebung_12_radiuskorrektur_g41_simulation_video.mp4).

---

## 3. Honorarkalkulation *(Festpreis nach § 18 EStG)*

| Pos. | Leistungsbeschreibung *(Ingenieurtechnische Entwicklung)* | Aufwand | Stundensatz | Gesamtpreis (Netto) |
| :---: | :--- | :---: | :---: | :---: |
| **1** | Ingenieurtechnische Analyse, Postprozessor-/CAM-Entwicklung (`uebung_12_radiuskorrektur_g41.nc`), statische Z-MIN-Kollisionsprüfung & Werkstatteinrichteblatt | 5,80 Std. | 100,00 € | **580,00 €** |
| | **Summe Netto** | | | **580,00 €** |
| | zzgl. 19 % Umsatzsteuer *(gemäß § 14 UStG [Umsatzsteuergesetz])* | | | 110,20 € |
| | **Gesamtbetrag (Brutto)** | | | **690,20 €** |

---

## 4. Abwicklungsmodalitäten & Sicherheitshinweis *(Mitwirkungspflicht)*

* **Lieferzeit:** Sofortige digitale Bereitstellung aller 6 Projekt-Artefakte nach Auftragsfreigabe.
* **Zahlungsziel:** 14 Tage netto nach Rechnungsstellung ohne Abzug.
* **Verbindlicher Sicherheitshinweis für das Einfahren an der Maschine:**
  Die gelieferten Postprozessoren und NC-Programme wurden rechnerisch und simulativ geprüft. Vor Beginn der Serienfertigung ist das Programm vom Maschinenbediener zwingend im **Einzelsatzbetrieb *(Single Block)*** bei reduziertem **Vorschub-Override *(Feedrate Potentiometer < 25 %)*** und mit Sichtkontrolle des Restwegs *(Distance-to-Go)* über dem Bauteil einzufahren.

Mit freundlichen Grüßen  
**Dipl.-Ing. (FH) Alexander Bujanovski**  
*Beratender Ingenieur für CAD/CAM-Technik & Postprozessor-Entwicklung*

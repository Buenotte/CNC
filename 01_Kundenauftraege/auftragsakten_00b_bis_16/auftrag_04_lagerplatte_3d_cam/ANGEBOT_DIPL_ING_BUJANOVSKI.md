# 📄 Ingenieur-Angebot: Auftrag 04: 3D-CAD-Modell zu komplettem NC-Programm (Lagerplatte)

* **Auftragnehmer:** Ingenieurbüro Dipl.-Ing. (FH) Alexander Bujanovski *(Freiberuflicher Beratender Ingenieur nach § 18 Abs. 1 Nr. 1 EStG [Einkommensteuergesetz])*
* **Auftraggeber:** **Franken Präzisionsteile GmbH**, z. Hd. Michael Brandner (Fertigungsleiter), Industriestraße 28, 97424 Schweinfurt
* **Angebot-Nr.:** `ANG-2026-04`
* **Projekt / Bauteil:** Lagerplatte 80 x 50 x 12 mm mit Passungstasche Ø 30 mm (3D-CAD-Auftrag)
* **Zielmaschine & Steuerung:** DMG MORI CMX 600 V (3-Achs-Bearbeitungszentrum) — Fanuc 31i / Siemens ISO-Modus (DIN 66025)

---

## 1. Technische Ausgangslage & Aufgabenstellung

Sehr geehrte(r) Michael Brandner (Fertigungsleiter),

vielen Dank für Ihre Projektanfrage bezüglich der ingenieurtechnischen Auslegung und Programmierung für Ihre **DMG MORI CMX 600 V (3-Achs-Bearbeitungszentrum)**. Ziel des Auftrags ist die Entwicklung und mathematische Verifikation von `uebung_04_3d_modell_cam.nc` (sowie `uebung_04_3d_modell_cam.cps`) für das Bauteil **Lagerplatte 80 x 50 x 12 mm mit Passungstasche Ø 30 mm (3D-CAD-Auftrag)** aus dem Werkstoff **Aluminium EN AW-6082 T6** unter strikter Einhaltung aller Kollisions- und Arbeitsschutzvorgaben.

---

## 2. Ingenieurtechnischer Leistungsumfang *(Freie Ingenieurleistung nach § 18 EStG)*

1. **Algorithmische Postprozessor- & NC-Architektur *(Agent 2 — Postprocessor-Coder-Agent)*:**
   - Implementierung und Validierung der steuerungsspezifischen Ausgabelogik für **Fanuc 31i / Siemens ISO-Modus (DIN 66025)**.
   - Ausgabe eines eindeutigen Sicherheits-Startblocks *(Safe Start Block)* sowie exakter Werkzeuglängenkompensation (`H01`).
2. **Mathematische Z-MIN-Kollisionsanalyse & Einrichtedokumentation *(Agent 3 — NC-Safety- & Setup-Agent)*:**
   - Statische Überprüfung aller Verfahrwege in `uebung_04_3d_modell_cam.nc` auf Einhaltung der tiefsten Zustellung $Z_{\text{min}} = -12.000\,\text{mm}$ gegenüber der Spannmittel-Oberkante bei $Z = -15.000\,\text{mm}$.
   - Erstellung des formalen Prüfberichts [`05_SICHERHEITS_CRASH_PRUEFBERICHT.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_04_lagerplatte_3d_cam/05_SICHERHEITS_CRASH_PRUEFBERICHT.md), des Einrichteblatts [`06_EINRICHTEBLATT_SETUP_SHEET.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_04_lagerplatte_3d_cam/06_EINRICHTEBLATT_SETUP_SHEET.md) sowie des 3D-Simulationsvideos [`uebung_04_3d_modell_cam_simulation_video.mp4`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_04_lagerplatte_3d_cam/uebung_04_3d_modell_cam_simulation_video.mp4).

---

## 3. Honorarkalkulation *(Festpreis nach § 18 EStG)*

| Pos. | Leistungsbeschreibung *(Ingenieurtechnische Entwicklung)* | Aufwand | Stundensatz | Gesamtpreis (Netto) |
| :---: | :--- | :---: | :---: | :---: |
| **1** | Ingenieurtechnische Analyse, Postprozessor-/CAM-Entwicklung (`uebung_04_3d_modell_cam.nc`), statische Z-MIN-Kollisionsprüfung & Werkstatteinrichteblatt | 4,00 Std. | 95,00 € | **380,00 €** |
| | **Summe Netto** | | | **380,00 €** |
| | zzgl. 19 % Umsatzsteuer *(gemäß § 14 UStG [Umsatzsteuergesetz])* | | | 72,20 € |
| | **Gesamtbetrag (Brutto)** | | | **452,20 €** |

---

## 4. Abwicklungsmodalitäten & Sicherheitshinweis *(Mitwirkungspflicht)*

* **Lieferzeit:** Sofortige digitale Bereitstellung aller 6 Projekt-Artefakte nach Auftragsfreigabe.
* **Zahlungsziel:** 14 Tage netto nach Rechnungsstellung ohne Abzug.
* **Verbindlicher Sicherheitshinweis für das Einfahren an der Maschine:**
  Die gelieferten Postprozessoren und NC-Programme wurden rechnerisch und simulativ geprüft. Vor Beginn der Serienfertigung ist das Programm vom Maschinenbediener zwingend im **Einzelsatzbetrieb *(Single Block)*** bei reduziertem **Vorschub-Override *(Feedrate Potentiometer < 25 %)*** und mit Sichtkontrolle des Restwegs *(Distance-to-Go)* über dem Bauteil einzufahren.

Mit freundlichen Grüßen  
**Dipl.-Ing. (FH) Alexander Bujanovski**  
*Beratender Ingenieur für CAD/CAM-Technik & Postprozessor-Entwicklung*

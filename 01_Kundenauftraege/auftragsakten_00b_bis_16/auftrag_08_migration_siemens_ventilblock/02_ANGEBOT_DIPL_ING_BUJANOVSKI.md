# 📄 Ingenieur-Angebot: Auftrag 08: Steuerungsmigration Fanuc ISO auf Siemens Sinumerik 840D sl (Ventilblock)

* **Auftragnehmer:** Ingenieurbüro Dipl.-Ing. (FH) Alexander Bujanovski *(Freiberuflicher Beratender Ingenieur nach § 18 Abs. 1 Nr. 1 EStG [Einkommensteuergesetz])*
* **Auftraggeber:** **Franken Zerspanung GmbH**, z. Hd. Jürgen Meier (Fertigungsleiter), Nürnberger Straße 55, 90762 Fürth
* **Angebot-Nr.:** `ANG-2026-08`
* **Projekt / Bauteil:** Hydraulik-Ventilblock OP10 (80 x 50 x 12 mm)
* **Zielmaschine & Steuerung:** DMG MORI DMU 50 (Siemens Sinumerik 840D sl) — Siemens Sinumerik 840D sl (DIN/ISO & Siemens-Zyklen SUPA / D1 / M88)

---

## 1. Technische Ausgangslage & Aufgabenstellung

Sehr geehrte(r) Jürgen Meier (Fertigungsleiter),

vielen Dank für Ihre Projektanfrage bezüglich der ingenieurtechnischen Auslegung und Programmierung für Ihre **DMG MORI DMU 50 (Siemens Sinumerik 840D sl)**. Ziel des Auftrags ist die Entwicklung und mathematische Verifikation von `siemens_ventilblock_post.nc` (sowie `siemens_ventilblock_post.cps`) für das Bauteil **Hydraulik-Ventilblock OP10 (80 x 50 x 12 mm)** aus dem Werkstoff **Vergütungsstahl 42CrMo4 (1.7225)** unter strikter Einhaltung aller Kollisions- und Arbeitsschutzvorgaben.

---

## 2. Ingenieurtechnischer Leistungsumfang *(Freie Ingenieurleistung nach § 18 EStG)*

1. **Algorithmische Postprozessor- & NC-Architektur *(Agent 2 — Postprocessor-Coder-Agent)*:**
   - Implementierung und Validierung der steuerungsspezifischen Ausgabelogik für **Siemens Sinumerik 840D sl (DIN/ISO & Siemens-Zyklen SUPA / D1 / M88)**.
   - Ausgabe eines eindeutigen Sicherheits-Startblocks *(Safe Start Block)* sowie exakter Werkzeuglängenkompensation (`D1`).
2. **Mathematische Z-MIN-Kollisionsanalyse & Einrichtedokumentation *(Agent 3 — NC-Safety- & Setup-Agent)*:**
   - Statische Überprüfung aller Verfahrwege in `siemens_ventilblock_post.nc` auf Einhaltung der tiefsten Zustellung $Z_{\text{min}} = -12.000\,\text{mm}$ gegenüber der Spannmittel-Oberkante bei $Z = -18.000\,\text{mm}$.
   - Erstellung des formalen Prüfberichts [`05_SICHERHEITS_CRASH_PRUEFBERICHT.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_08_migration_siemens_ventilblock/05_SICHERHEITS_CRASH_PRUEFBERICHT.md), des Einrichteblatts [`06_EINRICHTEBLATT_SETUP_SHEET.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_08_migration_siemens_ventilblock/06_EINRICHTEBLATT_SETUP_SHEET.md) sowie des 3D-Simulationsvideos [`siemens_ventilblock_post_simulation_video.mp4`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_08_migration_siemens_ventilblock/siemens_ventilblock_post_simulation_video.mp4).

---

## 3. Honorarkalkulation *(Festpreis nach § 18 EStG)*

| Pos. | Leistungsbeschreibung *(Ingenieurtechnische Entwicklung)* | Aufwand | Stundensatz | Gesamtpreis (Netto) |
| :---: | :--- | :---: | :---: | :---: |
| **1** | Ingenieurtechnische Analyse, Postprozessor-/CAM-Entwicklung (`siemens_ventilblock_post.nc`), statische Z-MIN-Kollisionsprüfung & Werkstatteinrichteblatt | 6,50 Std. | 100,00 € | **650,00 €** |
| | **Summe Netto** | | | **650,00 €** |
| | zzgl. 19 % Umsatzsteuer *(gemäß § 14 UStG [Umsatzsteuergesetz])* | | | 123,50 € |
| | **Gesamtbetrag (Brutto)** | | | **773,50 €** |

---

## 4. Abwicklungsmodalitäten & Sicherheitshinweis *(Mitwirkungspflicht)*

* **Lieferzeit:** Sofortige digitale Bereitstellung aller 6 Projekt-Artefakte nach Auftragsfreigabe.
* **Zahlungsziel:** 14 Tage netto nach Rechnungsstellung ohne Abzug.
* **Verbindlicher Sicherheitshinweis für das Einfahren an der Maschine:**
  Die gelieferten Postprozessoren und NC-Programme wurden rechnerisch und simulativ geprüft. Vor Beginn der Serienfertigung ist das Programm vom Maschinenbediener zwingend im **Einzelsatzbetrieb *(Single Block)*** bei reduziertem **Vorschub-Override *(Feedrate Potentiometer < 25 %)*** und mit Sichtkontrolle des Restwegs *(Distance-to-Go)* über dem Bauteil einzufahren.

Mit freundlichen Grüßen  
**Dipl.-Ing. (FH) Alexander Bujanovski**  
*Beratender Ingenieur für CAD/CAM-Technik & Postprozessor-Entwicklung*

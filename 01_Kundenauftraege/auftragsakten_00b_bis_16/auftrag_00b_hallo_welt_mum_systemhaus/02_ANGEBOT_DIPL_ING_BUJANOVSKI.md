# 📄 Ingenieur-Angebot: Auftrag 00b: Hallo-Welt & Systemhaus-Eignungstest

* **Auftragnehmer:** Ingenieurbüro Dipl.-Ing. (FH) Alexander Bujanovski *(Freiberuflicher Beratender Ingenieur nach § 18 Abs. 1 Nr. 1 EStG [Einkommensteuergesetz])*
* **Auftraggeber:** **Mensch und Maschine Systemhaus GmbH**, z. Hd. Jens Becker (Leiter CAM-Postprozessor-Services), Argelsrieder Feld 5, 82234 Weßling
* **Angebot-Nr.:** `ANG-2026-00B`
* **Projekt / Bauteil:** Kalibrier-Prüfkörper 80 x 50 x 12 mm (Systemhaus-Eignungstest)
* **Zielmaschine & Steuerung:** Standard 3-Achs-Fräsmaschine (Haas/Fanuc-kompatibel) — Haas NGC / Fanuc ISO G-Code (DIN 66025)

---

## 1. Technische Ausgangslage & Aufgabenstellung

Sehr geehrte(r) Jens Becker (Leiter CAM-Postprozessor-Services),

vielen Dank für Ihre Projektanfrage bezüglich der ingenieurtechnischen Auslegung und Programmierung für Ihre **Standard 3-Achs-Fräsmaschine (Haas/Fanuc-kompatibel)**. Ziel des Auftrags ist die Entwicklung und mathematische Verifikation von `uebung_00b_hallo_welt.nc` (sowie `uebung_00b_hallo_welt.cps`) für das Bauteil **Kalibrier-Prüfkörper 80 x 50 x 12 mm (Systemhaus-Eignungstest)** aus dem Werkstoff **Aluminium EN AW-6082 (AlSi1MgMn)** unter strikter Einhaltung aller Kollisions- und Arbeitsschutzvorgaben.

---

## 2. Ingenieurtechnischer Leistungsumfang *(Freie Ingenieurleistung nach § 18 EStG)*

1. **Algorithmische Postprozessor- & NC-Architektur *(Agent 2 — Postprocessor-Coder-Agent)*:**
   - Implementierung und Validierung der steuerungsspezifischen Ausgabelogik für **Haas NGC / Fanuc ISO G-Code (DIN 66025)**.
   - Ausgabe eines eindeutigen Sicherheits-Startblocks *(Safe Start Block)* sowie exakter Werkzeuglängenkompensation (`H01`).
2. **Mathematische Z-MIN-Kollisionsanalyse & Einrichtedokumentation *(Agent 3 — NC-Safety- & Setup-Agent)*:**
   - Statische Überprüfung aller Verfahrwege in `uebung_00b_hallo_welt.nc` auf Einhaltung der tiefsten Zustellung $Z_{\text{min}} = -5.000\,\text{mm}$ gegenüber der Spannmittel-Oberkante bei $Z = -12.000\,\text{mm}$.
   - Erstellung des formalen Prüfberichts [`05_SICHERHEITS_CRASH_PRUEFBERICHT.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_00b_hallo_welt_mum_systemhaus/05_SICHERHEITS_CRASH_PRUEFBERICHT.md), des Einrichteblatts [`06_EINRICHTEBLATT_SETUP_SHEET.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_00b_hallo_welt_mum_systemhaus/06_EINRICHTEBLATT_SETUP_SHEET.md) sowie des 3D-Simulationsvideos [`uebung_00b_hallo_welt_simulation_video.mp4`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_00b_hallo_welt_mum_systemhaus/uebung_00b_hallo_welt_simulation_video.mp4).

---

## 3. Honorarkalkulation *(Festpreis nach § 18 EStG)*

| Pos. | Leistungsbeschreibung *(Ingenieurtechnische Entwicklung)* | Aufwand | Stundensatz | Gesamtpreis (Netto) |
| :---: | :--- | :---: | :---: | :---: |
| **1** | Ingenieurtechnische Analyse, Postprozessor-/CAM-Entwicklung (`uebung_00b_hallo_welt.nc`), statische Z-MIN-Kollisionsprüfung & Werkstatteinrichteblatt | 2,50 Std. | 100,00 € | **250,00 €** |
| | **Summe Netto** | | | **250,00 €** |
| | zzgl. 19 % Umsatzsteuer *(gemäß § 14 UStG [Umsatzsteuergesetz])* | | | 47,50 € |
| | **Gesamtbetrag (Brutto)** | | | **297,50 €** |

---

## 4. Abwicklungsmodalitäten & Sicherheitshinweis *(Mitwirkungspflicht)*

* **Lieferzeit:** Sofortige digitale Bereitstellung aller 6 Projekt-Artefakte nach Auftragsfreigabe.
* **Zahlungsziel:** 14 Tage netto nach Rechnungsstellung ohne Abzug.
* **Verbindlicher Sicherheitshinweis für das Einfahren an der Maschine:**
  Die gelieferten Postprozessoren und NC-Programme wurden rechnerisch und simulativ geprüft. Vor Beginn der Serienfertigung ist das Programm vom Maschinenbediener zwingend im **Einzelsatzbetrieb *(Single Block)*** bei reduziertem **Vorschub-Override *(Feedrate Potentiometer < 25 %)*** und mit Sichtkontrolle des Restwegs *(Distance-to-Go)* über dem Bauteil einzufahren.

Mit freundlichen Grüßen  
**Dipl.-Ing. (FH) Alexander Bujanovski**  
*Beratender Ingenieur für CAD/CAM-Technik & Postprozessor-Entwicklung*

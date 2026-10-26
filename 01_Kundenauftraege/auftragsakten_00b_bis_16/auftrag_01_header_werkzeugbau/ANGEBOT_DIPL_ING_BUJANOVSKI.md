# 📄 Ingenieur-Angebot: Auftrag 01: ISO-9001 Entwickler-Header & Metadatenblock

* **Auftragnehmer:** Ingenieurbüro Dipl.-Ing. (FH) Alexander Bujanovski *(Freiberuflicher Beratender Ingenieur nach § 18 Abs. 1 Nr. 1 EStG [Einkommensteuergesetz])*
* **Auftraggeber:** **Klausner Formenbau & Zerspanung**, z. Hd. Stefan Klausner (Geschäftsführer), Dornierstraße 14, 71034 Böblingen
* **Angebot-Nr.:** `ANG-2026-01`
* **Projekt / Bauteil:** Führungssäulen-Aufnahmeplatte (ISO-9001 Audit-Pflichtkopf)
* **Zielmaschine & Steuerung:** 3-Achs-Bearbeitungszentrum Hermle C400 (ISO/Fanuc-Modus) — ISO G-Code (DIN 66025 mit Pflicht-Header)

---

## 1. Technische Ausgangslage & Aufgabenstellung

Sehr geehrte(r) Stefan Klausner (Geschäftsführer),

vielen Dank für Ihre Projektanfrage bezüglich der ingenieurtechnischen Auslegung und Programmierung für Ihre **3-Achs-Bearbeitungszentrum Hermle C400 (ISO/Fanuc-Modus)**. Ziel des Auftrags ist die Entwicklung und mathematische Verifikation von `uebung_01_entwickler_header.nc` (sowie `uebung_01_entwickler_header.cps`) für das Bauteil **Führungssäulen-Aufnahmeplatte (ISO-9001 Audit-Pflichtkopf)** aus dem Werkstoff **Werkzeugstahl 1.2312 (40CrMnMoS8-6)** unter strikter Einhaltung aller Kollisions- und Arbeitsschutzvorgaben.

---

## 2. Ingenieurtechnischer Leistungsumfang *(Freie Ingenieurleistung nach § 18 EStG)*

1. **Algorithmische Postprozessor- & NC-Architektur *(Agent 2 — Postprocessor-Coder-Agent)*:**
   - Implementierung und Validierung der steuerungsspezifischen Ausgabelogik für **ISO G-Code (DIN 66025 mit Pflicht-Header)**.
   - Ausgabe eines eindeutigen Sicherheits-Startblocks *(Safe Start Block)* sowie exakter Werkzeuglängenkompensation (`H01`).
2. **Mathematische Z-MIN-Kollisionsanalyse & Einrichtedokumentation *(Agent 3 — NC-Safety- & Setup-Agent)*:**
   - Statische Überprüfung aller Verfahrwege in `uebung_01_entwickler_header.nc` auf Einhaltung der tiefsten Zustellung $Z_{\text{min}} = -5.000\,\text{mm}$ gegenüber der Spannmittel-Oberkante bei $Z = -15.000\,\text{mm}$.
   - Erstellung des formalen Prüfberichts [`05_SICHERHEITS_CRASH_PRUEFBERICHT.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_01_header_werkzeugbau/05_SICHERHEITS_CRASH_PRUEFBERICHT.md), des Einrichteblatts [`06_EINRICHTEBLATT_SETUP_SHEET.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_01_header_werkzeugbau/06_EINRICHTEBLATT_SETUP_SHEET.md) sowie des 3D-Simulationsvideos [`uebung_01_entwickler_header_simulation_video.mp4`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_01_header_werkzeugbau/uebung_01_entwickler_header_simulation_video.mp4).

---

## 3. Honorarkalkulation *(Festpreis nach § 18 EStG)*

| Pos. | Leistungsbeschreibung *(Ingenieurtechnische Entwicklung)* | Aufwand | Stundensatz | Gesamtpreis (Netto) |
| :---: | :--- | :---: | :---: | :---: |
| **1** | Ingenieurtechnische Analyse, Postprozessor-/CAM-Entwicklung (`uebung_01_entwickler_header.nc`), statische Z-MIN-Kollisionsprüfung & Werkstatteinrichteblatt | 3,50 Std. | 100,00 € | **350,00 €** |
| | **Summe Netto** | | | **350,00 €** |
| | zzgl. 19 % Umsatzsteuer *(gemäß § 14 UStG [Umsatzsteuergesetz])* | | | 66,50 € |
| | **Gesamtbetrag (Brutto)** | | | **416,50 €** |

---

## 4. Abwicklungsmodalitäten & Sicherheitshinweis *(Mitwirkungspflicht)*

* **Lieferzeit:** Sofortige digitale Bereitstellung aller 6 Projekt-Artefakte nach Auftragsfreigabe.
* **Zahlungsziel:** 14 Tage netto nach Rechnungsstellung ohne Abzug.
* **Verbindlicher Sicherheitshinweis für das Einfahren an der Maschine:**
  Die gelieferten Postprozessoren und NC-Programme wurden rechnerisch und simulativ geprüft. Vor Beginn der Serienfertigung ist das Programm vom Maschinenbediener zwingend im **Einzelsatzbetrieb *(Single Block)*** bei reduziertem **Vorschub-Override *(Feedrate Potentiometer < 25 %)*** und mit Sichtkontrolle des Restwegs *(Distance-to-Go)* über dem Bauteil einzufahren.

Mit freundlichen Grüßen  
**Dipl.-Ing. (FH) Alexander Bujanovski**  
*Beratender Ingenieur für CAD/CAM-Technik & Postprozessor-Entwicklung*

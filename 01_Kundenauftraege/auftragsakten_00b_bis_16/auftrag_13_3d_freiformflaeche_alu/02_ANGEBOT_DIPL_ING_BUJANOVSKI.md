# 📄 Ingenieur-Angebot: Auftrag 13: 3D-Freiformflächen-Schlichten & High-Speed-Glättung (G187 / G64)

* **Auftragnehmer:** Ingenieurbüro Dipl.-Ing. (FH) Alexander Bujanovski *(Freiberuflicher Beratender Ingenieur nach § 18 Abs. 1 Nr. 1 EStG [Einkommensteuergesetz])*
* **Auftraggeber:** **AeroTech Prototypenbau Bremen**, z. Hd. Dr. Elena Rost (Leiterin Prototypenbau), Flugplatzstraße 12, 28199 Bremen
* **Angebot-Nr.:** `ANG-2026-13`
* **Projekt / Bauteil:** CFK-Laminierform mit doppelt gekrümmter 3D-Freiformfläche
* **Zielmaschine & Steuerung:** Hermle C32 U 5-Achs (ISO/Haas-Highspeed-Modus) — ISO G-Code (mit G187 P3 E0.005 Hochgeschwindigkeits-Bahnverschleifung)

---

## 1. Technische Ausgangslage & Aufgabenstellung

Sehr geehrte(r) Dr. Elena Rost (Leiterin Prototypenbau),

vielen Dank für Ihre Projektanfrage bezüglich der ingenieurtechnischen Auslegung und Programmierung für Ihre **Hermle C32 U 5-Achs (ISO/Haas-Highspeed-Modus)**. Ziel des Auftrags ist die Entwicklung und mathematische Verifikation von `uebung_13_3d_freiformflaechen.nc` (sowie `uebung_13_3d_freiformflaechen.cps`) für das Bauteil **CFK-Laminierform mit doppelt gekrümmter 3D-Freiformfläche** aus dem Werkstoff **Hochfestes Flugzeugaluminium EN AW-7075 T651** unter strikter Einhaltung aller Kollisions- und Arbeitsschutzvorgaben.

---

## 2. Ingenieurtechnischer Leistungsumfang *(Freie Ingenieurleistung nach § 18 EStG)*

1. **Algorithmische Postprozessor- & NC-Architektur *(Agent 2 — Postprocessor-Coder-Agent)*:**
   - Implementierung und Validierung der steuerungsspezifischen Ausgabelogik für **ISO G-Code (mit G187 P3 E0.005 Hochgeschwindigkeits-Bahnverschleifung)**.
   - Ausgabe eines eindeutigen Sicherheits-Startblocks *(Safe Start Block)* sowie exakter Werkzeuglängenkompensation (`H01`).
2. **Mathematische Z-MIN-Kollisionsanalyse & Einrichtedokumentation *(Agent 3 — NC-Safety- & Setup-Agent)*:**
   - Statische Überprüfung aller Verfahrwege in `uebung_13_3d_freiformflaechen.nc` auf Einhaltung der tiefsten Zustellung $Z_{\text{min}} = -5.000\,\text{mm}$ gegenüber der Spannmittel-Oberkante bei $Z = -15.000\,\text{mm}$.
   - Erstellung des formalen Prüfberichts [`05_SICHERHEITS_CRASH_PRUEFBERICHT.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_13_3d_freiformflaeche_alu/05_SICHERHEITS_CRASH_PRUEFBERICHT.md), des Einrichteblatts [`06_EINRICHTEBLATT_SETUP_SHEET.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_13_3d_freiformflaeche_alu/06_EINRICHTEBLATT_SETUP_SHEET.md) sowie des 3D-Simulationsvideos [`uebung_13_3d_freiformflaechen_simulation_video.mp4`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_13_3d_freiformflaeche_alu/uebung_13_3d_freiformflaechen_simulation_video.mp4).

---

## 3. Honorarkalkulation *(Festpreis nach § 18 EStG)*

| Pos. | Leistungsbeschreibung *(Ingenieurtechnische Entwicklung)* | Aufwand | Stundensatz | Gesamtpreis (Netto) |
| :---: | :--- | :---: | :---: | :---: |
| **1** | Ingenieurtechnische Analyse, Postprozessor-/CAM-Entwicklung (`uebung_13_3d_freiformflaechen.nc`), statische Z-MIN-Kollisionsprüfung & Werkstatteinrichteblatt | 7,50 Std. | 100,00 € | **750,00 €** |
| | **Summe Netto** | | | **750,00 €** |
| | zzgl. 19 % Umsatzsteuer *(gemäß § 14 UStG [Umsatzsteuergesetz])* | | | 142,50 € |
| | **Gesamtbetrag (Brutto)** | | | **892,50 €** |

---

## 4. Abwicklungsmodalitäten & Sicherheitshinweis *(Mitwirkungspflicht)*

* **Lieferzeit:** Sofortige digitale Bereitstellung aller 6 Projekt-Artefakte nach Auftragsfreigabe.
* **Zahlungsziel:** 14 Tage netto nach Rechnungsstellung ohne Abzug.
* **Verbindlicher Sicherheitshinweis für das Einfahren an der Maschine:**
  Die gelieferten Postprozessoren und NC-Programme wurden rechnerisch und simulativ geprüft. Vor Beginn der Serienfertigung ist das Programm vom Maschinenbediener zwingend im **Einzelsatzbetrieb *(Single Block)*** bei reduziertem **Vorschub-Override *(Feedrate Potentiometer < 25 %)*** und mit Sichtkontrolle des Restwegs *(Distance-to-Go)* über dem Bauteil einzufahren.

Mit freundlichen Grüßen  
**Dipl.-Ing. (FH) Alexander Bujanovski**  
*Beratender Ingenieur für CAD/CAM-Technik & Postprozessor-Entwicklung*

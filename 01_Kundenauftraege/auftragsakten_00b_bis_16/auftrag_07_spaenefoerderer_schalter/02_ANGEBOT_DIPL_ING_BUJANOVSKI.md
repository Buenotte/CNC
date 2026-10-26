# 📄 Ingenieur-Angebot: Auftrag 07: Konfigurierbare Postprozessor-Properties (Späneförderer M31/M33)

* **Auftragnehmer:** Ingenieurbüro Dipl.-Ing. (FH) Alexander Bujanovski *(Freiberuflicher Beratender Ingenieur nach § 18 Abs. 1 Nr. 1 EStG [Einkommensteuergesetz])*
* **Auftraggeber:** **Vogtland Zerspanungstechnik GmbH**, z. Hd. Karsten Wolf (Technischer Leiter), Plauener Straße 22, 08523 Plauen
* **Angebot-Nr.:** `ANG-2026-07`
* **Projekt / Bauteil:** Hochvolumen-Aluminiumgehäuse (90 % Zerspanungsvolumen)
* **Zielmaschine & Steuerung:** Alzmetall CS 1200 (ISO G-Code-Modus) — ISO G-Code (mit M31/M33 Späneförderer-Ansteuerung)

---

## 1. Technische Ausgangslage & Aufgabenstellung

Sehr geehrte(r) Karsten Wolf (Technischer Leiter),

vielen Dank für Ihre Projektanfrage bezüglich der ingenieurtechnischen Auslegung und Programmierung für Ihre **Alzmetall CS 1200 (ISO G-Code-Modus)**. Ziel des Auftrags ist die Entwicklung und mathematische Verifikation von `uebung_07_spaenefoerderer_schalter.nc` (sowie `uebung_07_spaenefoerderer_schalter.cps`) für das Bauteil **Hochvolumen-Aluminiumgehäuse (90 % Zerspanungsvolumen)** aus dem Werkstoff **Aluminium EN AW-6060 (AlMgSi0,5)** unter strikter Einhaltung aller Kollisions- und Arbeitsschutzvorgaben.

---

## 2. Ingenieurtechnischer Leistungsumfang *(Freie Ingenieurleistung nach § 18 EStG)*

1. **Algorithmische Postprozessor- & NC-Architektur *(Agent 2 — Postprocessor-Coder-Agent)*:**
   - Implementierung und Validierung der steuerungsspezifischen Ausgabelogik für **ISO G-Code (mit M31/M33 Späneförderer-Ansteuerung)**.
   - Ausgabe eines eindeutigen Sicherheits-Startblocks *(Safe Start Block)* sowie exakter Werkzeuglängenkompensation (`H01`).
2. **Mathematische Z-MIN-Kollisionsanalyse & Einrichtedokumentation *(Agent 3 — NC-Safety- & Setup-Agent)*:**
   - Statische Überprüfung aller Verfahrwege in `uebung_07_spaenefoerderer_schalter.nc` auf Einhaltung der tiefsten Zustellung $Z_{\text{min}} = -5.000\,\text{mm}$ gegenüber der Spannmittel-Oberkante bei $Z = -15.000\,\text{mm}$.
   - Erstellung des formalen Prüfberichts [`05_SICHERHEITS_CRASH_PRUEFBERICHT.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_07_spaenefoerderer_schalter/05_SICHERHEITS_CRASH_PRUEFBERICHT.md), des Einrichteblatts [`06_EINRICHTEBLATT_SETUP_SHEET.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_07_spaenefoerderer_schalter/06_EINRICHTEBLATT_SETUP_SHEET.md) sowie des 3D-Simulationsvideos [`uebung_07_spaenefoerderer_schalter_simulation_video.mp4`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_07_spaenefoerderer_schalter/uebung_07_spaenefoerderer_schalter_simulation_video.mp4).

---

## 3. Honorarkalkulation *(Festpreis nach § 18 EStG)*

| Pos. | Leistungsbeschreibung *(Ingenieurtechnische Entwicklung)* | Aufwand | Stundensatz | Gesamtpreis (Netto) |
| :---: | :--- | :---: | :---: | :---: |
| **1** | Ingenieurtechnische Analyse, Postprozessor-/CAM-Entwicklung (`uebung_07_spaenefoerderer_schalter.nc`), statische Z-MIN-Kollisionsprüfung & Werkstatteinrichteblatt | 3,90 Std. | 100,00 € | **390,00 €** |
| | **Summe Netto** | | | **390,00 €** |
| | zzgl. 19 % Umsatzsteuer *(gemäß § 14 UStG [Umsatzsteuergesetz])* | | | 74,10 € |
| | **Gesamtbetrag (Brutto)** | | | **464,10 €** |

---

## 4. Abwicklungsmodalitäten & Sicherheitshinweis *(Mitwirkungspflicht)*

* **Lieferzeit:** Sofortige digitale Bereitstellung aller 6 Projekt-Artefakte nach Auftragsfreigabe.
* **Zahlungsziel:** 14 Tage netto nach Rechnungsstellung ohne Abzug.
* **Verbindlicher Sicherheitshinweis für das Einfahren an der Maschine:**
  Die gelieferten Postprozessoren und NC-Programme wurden rechnerisch und simulativ geprüft. Vor Beginn der Serienfertigung ist das Programm vom Maschinenbediener zwingend im **Einzelsatzbetrieb *(Single Block)*** bei reduziertem **Vorschub-Override *(Feedrate Potentiometer < 25 %)*** und mit Sichtkontrolle des Restwegs *(Distance-to-Go)* über dem Bauteil einzufahren.

Mit freundlichen Grüßen  
**Dipl.-Ing. (FH) Alexander Bujanovski**  
*Beratender Ingenieur für CAD/CAM-Technik & Postprozessor-Entwicklung*

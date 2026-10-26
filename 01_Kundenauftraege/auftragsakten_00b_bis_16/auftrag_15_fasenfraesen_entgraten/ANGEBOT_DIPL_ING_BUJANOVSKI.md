# 📄 Ingenieur-Angebot: Auftrag 15: Vollautomatisches 2D-Fasenfräsen & Entgraten (90°-NC-Anbohrer/Fasenfräser)

* **Auftragnehmer:** Ingenieurbüro Dipl.-Ing. (FH) Alexander Bujanovski *(Freiberuflicher Beratender Ingenieur nach § 18 Abs. 1 Nr. 1 EStG [Einkommensteuergesetz])*
* **Auftraggeber:** **Kunz Feinwerktechnik**, z. Hd. Matthias Kunz (Geschäftsführer), Aesculap-Platz 4, 78532 Tuttlingen
* **Angebot-Nr.:** `ANG-2026-15`
* **Projekt / Bauteil:** Chirurgische Instrumenten-Halteplatte 80 x 50 x 12 mm (100 % gratfrei direkt von der Maschine)
* **Zielmaschine & Steuerung:** Hedelius Tiltenta 7 (ISO G-Code-Modus) — Fanuc / Haas ISO G-Code (mit geometrischem Spitzenversatz für 45°-Fase)

---

## 1. Technische Ausgangslage & Aufgabenstellung

Sehr geehrte(r) Matthias Kunz (Geschäftsführer),

vielen Dank für Ihre Projektanfrage bezüglich der ingenieurtechnischen Auslegung und Programmierung für Ihre **Hedelius Tiltenta 7 (ISO G-Code-Modus)**. Ziel des Auftrags ist die Entwicklung und mathematische Verifikation von `uebung_15_fasenfraesen_entgraten.nc` (sowie `uebung_15_fasenfraesen_entgraten.cps`) für das Bauteil **Chirurgische Instrumenten-Halteplatte 80 x 50 x 12 mm (100 % gratfrei direkt von der Maschine)** aus dem Werkstoff **Medizinal-Edelstahl 1.4441 / Aluminium EN AW-6082** unter strikter Einhaltung aller Kollisions- und Arbeitsschutzvorgaben.

---

## 2. Ingenieurtechnischer Leistungsumfang *(Freie Ingenieurleistung nach § 18 EStG)*

1. **Algorithmische Postprozessor- & NC-Architektur *(Agent 2 — Postprocessor-Coder-Agent)*:**
   - Implementierung und Validierung der steuerungsspezifischen Ausgabelogik für **Fanuc / Haas ISO G-Code (mit geometrischem Spitzenversatz für 45°-Fase)**.
   - Ausgabe eines eindeutigen Sicherheits-Startblocks *(Safe Start Block)* sowie exakter Werkzeuglängenkompensation (`H01`).
2. **Mathematische Z-MIN-Kollisionsanalyse & Einrichtedokumentation *(Agent 3 — NC-Safety- & Setup-Agent)*:**
   - Statische Überprüfung aller Verfahrwege in `uebung_15_fasenfraesen_entgraten.nc` auf Einhaltung der tiefsten Zustellung $Z_{\text{min}} = -12.000\,\text{mm}$ gegenüber der Spannmittel-Oberkante bei $Z = -15.000\,\text{mm}$.
   - Erstellung des formalen Prüfberichts [`05_SICHERHEITS_CRASH_PRUEFBERICHT.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_15_fasenfraesen_entgraten/05_SICHERHEITS_CRASH_PRUEFBERICHT.md), des Einrichteblatts [`06_EINRICHTEBLATT_SETUP_SHEET.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_15_fasenfraesen_entgraten/06_EINRICHTEBLATT_SETUP_SHEET.md) sowie des 3D-Simulationsvideos [`uebung_15_fasenfraesen_entgraten_simulation_video.mp4`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_15_fasenfraesen_entgraten/uebung_15_fasenfraesen_entgraten_simulation_video.mp4).

---

## 3. Honorarkalkulation *(Festpreis nach § 18 EStG)*

| Pos. | Leistungsbeschreibung *(Ingenieurtechnische Entwicklung)* | Aufwand | Stundensatz | Gesamtpreis (Netto) |
| :---: | :--- | :---: | :---: | :---: |
| **1** | Ingenieurtechnische Analyse, Postprozessor-/CAM-Entwicklung (`uebung_15_fasenfraesen_entgraten.nc`), statische Z-MIN-Kollisionsprüfung & Werkstatteinrichteblatt | 3,80 Std. | 100,00 € | **380,00 €** |
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

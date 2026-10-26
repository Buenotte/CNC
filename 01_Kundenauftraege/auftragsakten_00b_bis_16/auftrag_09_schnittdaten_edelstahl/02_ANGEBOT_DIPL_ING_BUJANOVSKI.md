# 📄 Ingenieur-Angebot: Auftrag 09: Automatische Schnittdaten-Wächter-Logik für Edelstahl 1.4301 (V2A)

* **Auftragnehmer:** Ingenieurbüro Dipl.-Ing. (FH) Alexander Bujanovski *(Freiberuflicher Beratender Ingenieur nach § 18 Abs. 1 Nr. 1 EStG [Einkommensteuergesetz])*
* **Auftraggeber:** **Krupp & Partner Maschinenteile**, z. Hd. Frank Lehmann (Produktionsleiter), Kruppstraße 31, 45128 Essen
* **Angebot-Nr.:** `ANG-2026-09`
* **Projekt / Bauteil:** Lebensmittel-Pumpenflansch 80 x 50 x 12 mm (Edelstahl V2A)
* **Zielmaschine & Steuerung:** Haas VF-2 (Haas NGC Steuerung) — Haas NGC (mit automatischer Drehzahl-Deckelung maxRPM = 4500 U/min)

---

## 1. Technische Ausgangslage & Aufgabenstellung

Sehr geehrte(r) Frank Lehmann (Produktionsleiter),

vielen Dank für Ihre Projektanfrage bezüglich der ingenieurtechnischen Auslegung und Programmierung für Ihre **Haas VF-2 (Haas NGC Steuerung)**. Ziel des Auftrags ist die Entwicklung und mathematische Verifikation von `uebung_09_schnittdaten_check.nc` (sowie `uebung_09_schnittdaten_check.cps`) für das Bauteil **Lebensmittel-Pumpenflansch 80 x 50 x 12 mm (Edelstahl V2A)** aus dem Werkstoff **Edelstahl X5CrNi18-10 / 1.4301 (V2A — Kaltverfestigungsgefahr!)** unter strikter Einhaltung aller Kollisions- und Arbeitsschutzvorgaben.

---

## 2. Ingenieurtechnischer Leistungsumfang *(Freie Ingenieurleistung nach § 18 EStG)*

1. **Algorithmische Postprozessor- & NC-Architektur *(Agent 2 — Postprocessor-Coder-Agent)*:**
   - Implementierung und Validierung der steuerungsspezifischen Ausgabelogik für **Haas NGC (mit automatischer Drehzahl-Deckelung maxRPM = 4500 U/min)**.
   - Ausgabe eines eindeutigen Sicherheits-Startblocks *(Safe Start Block)* sowie exakter Werkzeuglängenkompensation (`H01`).
2. **Mathematische Z-MIN-Kollisionsanalyse & Einrichtedokumentation *(Agent 3 — NC-Safety- & Setup-Agent)*:**
   - Statische Überprüfung aller Verfahrwege in `uebung_09_schnittdaten_check.nc` auf Einhaltung der tiefsten Zustellung $Z_{\text{min}} = -12.000\,\text{mm}$ gegenüber der Spannmittel-Oberkante bei $Z = -15.000\,\text{mm}$.
   - Erstellung des formalen Prüfberichts [`05_SICHERHEITS_CRASH_PRUEFBERICHT.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_09_schnittdaten_edelstahl/05_SICHERHEITS_CRASH_PRUEFBERICHT.md), des Einrichteblatts [`06_EINRICHTEBLATT_SETUP_SHEET.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_09_schnittdaten_edelstahl/06_EINRICHTEBLATT_SETUP_SHEET.md) sowie des 3D-Simulationsvideos [`uebung_09_schnittdaten_check_simulation_video.mp4`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_09_schnittdaten_edelstahl/uebung_09_schnittdaten_check_simulation_video.mp4).

---

## 3. Honorarkalkulation *(Festpreis nach § 18 EStG)*

| Pos. | Leistungsbeschreibung *(Ingenieurtechnische Entwicklung)* | Aufwand | Stundensatz | Gesamtpreis (Netto) |
| :---: | :--- | :---: | :---: | :---: |
| **1** | Ingenieurtechnische Analyse, Postprozessor-/CAM-Entwicklung (`uebung_09_schnittdaten_check.nc`), statische Z-MIN-Kollisionsprüfung & Werkstatteinrichteblatt | 5,00 Std. | 96,00 € | **480,00 €** |
| | **Summe Netto** | | | **480,00 €** |
| | zzgl. 19 % Umsatzsteuer *(gemäß § 14 UStG [Umsatzsteuergesetz])* | | | 91,20 € |
| | **Gesamtbetrag (Brutto)** | | | **571,20 €** |

---

## 4. Abwicklungsmodalitäten & Sicherheitshinweis *(Mitwirkungspflicht)*

* **Lieferzeit:** Sofortige digitale Bereitstellung aller 6 Projekt-Artefakte nach Auftragsfreigabe.
* **Zahlungsziel:** 14 Tage netto nach Rechnungsstellung ohne Abzug.
* **Verbindlicher Sicherheitshinweis für das Einfahren an der Maschine:**
  Die gelieferten Postprozessoren und NC-Programme wurden rechnerisch und simulativ geprüft. Vor Beginn der Serienfertigung ist das Programm vom Maschinenbediener zwingend im **Einzelsatzbetrieb *(Single Block)*** bei reduziertem **Vorschub-Override *(Feedrate Potentiometer < 25 %)*** und mit Sichtkontrolle des Restwegs *(Distance-to-Go)* über dem Bauteil einzufahren.

Mit freundlichen Grüßen  
**Dipl.-Ing. (FH) Alexander Bujanovski**  
*Beratender Ingenieur für CAD/CAM-Technik & Postprozessor-Entwicklung*

# 📄 Ingenieur-Angebot: Auftrag 16: Meister-Endabnahme & Komplett-Postprozessor-Zertifizierung

* **Auftragnehmer:** Ingenieurbüro Dipl.-Ing. (FH) Alexander Bujanovski *(Freiberuflicher Beratender Ingenieur nach § 18 Abs. 1 Nr. 1 EStG [Einkommensteuergesetz])*
* **Auftraggeber:** **Hessen Automotive GmbH**, z. Hd. Dipl.-Ing. Bernd Schäfer (Leiter Qualitätssicherung), Automobilring 10, 34225 Baunatal
* **Angebot-Nr.:** `ANG-2026-16`
* **Projekt / Bauteil:** Zertifizierungs-Referenzbauteil O1001 (Komplett-Audit aller Sicherheitsmodule)
* **Zielmaschine & Steuerung:** Haas VF-2 / Grob G550 (Komplett-Zertifizierung ISO G-Code) — Haas NGC / ISO (Vollständiger Kunden-Postprozessor inkl. Tool-Table, Z-MIN-Sperre & G53 Y0)

---

## 1. Technische Ausgangslage & Aufgabenstellung

Sehr geehrte(r) Dipl.-Ing. Bernd Schäfer (Leiter Qualitätssicherung),

vielen Dank für Ihre Projektanfrage bezüglich der ingenieurtechnischen Auslegung und Programmierung für Ihre **Haas VF-2 / Grob G550 (Komplett-Zertifizierung ISO G-Code)**. Ziel des Auftrags ist die Entwicklung und mathematische Verifikation von `kunden_post_generiert.nc` (sowie `kunden_post_generiert.cps`) für das Bauteil **Zertifizierungs-Referenzbauteil O1001 (Komplett-Audit aller Sicherheitsmodule)** aus dem Werkstoff **Aluminium EN AW-6082 T6 (80 x 50 x 12 mm)** unter strikter Einhaltung aller Kollisions- und Arbeitsschutzvorgaben.

---

## 2. Ingenieurtechnischer Leistungsumfang *(Freie Ingenieurleistung nach § 18 EStG)*

1. **Algorithmische Postprozessor- & NC-Architektur *(Agent 2 — Postprocessor-Coder-Agent)*:**
   - Implementierung und Validierung der steuerungsspezifischen Ausgabelogik für **Haas NGC / ISO (Vollständiger Kunden-Postprozessor inkl. Tool-Table, Z-MIN-Sperre & G53 Y0)**.
   - Ausgabe eines eindeutigen Sicherheits-Startblocks *(Safe Start Block)* sowie exakter Werkzeuglängenkompensation (`H01`).
2. **Mathematische Z-MIN-Kollisionsanalyse & Einrichtedokumentation *(Agent 3 — NC-Safety- & Setup-Agent)*:**
   - Statische Überprüfung aller Verfahrwege in `kunden_post_generiert.nc` auf Einhaltung der tiefsten Zustellung $Z_{\text{min}} = -12.000\,\text{mm}$ gegenüber der Spannmittel-Oberkante bei $Z = -15.000\,\text{mm}$.
   - Erstellung des formalen Prüfberichts [`05_SICHERHEITS_CRASH_PRUEFBERICHT.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_16_meister_endabnahme_audit/05_SICHERHEITS_CRASH_PRUEFBERICHT.md), des Einrichteblatts [`06_EINRICHTEBLATT_SETUP_SHEET.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_16_meister_endabnahme_audit/06_EINRICHTEBLATT_SETUP_SHEET.md) sowie des 3D-Simulationsvideos [`kunden_post_generiert_simulation_video.mp4`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_16_meister_endabnahme_audit/kunden_post_generiert_simulation_video.mp4).

---

## 3. Honorarkalkulation *(Festpreis nach § 18 EStG)*

| Pos. | Leistungsbeschreibung *(Ingenieurtechnische Entwicklung)* | Aufwand | Stundensatz | Gesamtpreis (Netto) |
| :---: | :--- | :---: | :---: | :---: |
| **1** | Ingenieurtechnische Analyse, Postprozessor-/CAM-Entwicklung (`kunden_post_generiert.nc`), statische Z-MIN-Kollisionsprüfung & Werkstatteinrichteblatt | 4,90 Std. | 100,00 € | **490,00 €** |
| | **Summe Netto** | | | **490,00 €** |
| | zzgl. 19 % Umsatzsteuer *(gemäß § 14 UStG [Umsatzsteuergesetz])* | | | 93,10 € |
| | **Gesamtbetrag (Brutto)** | | | **583,10 €** |

---

## 4. Abwicklungsmodalitäten & Sicherheitshinweis *(Mitwirkungspflicht)*

* **Lieferzeit:** Sofortige digitale Bereitstellung aller 6 Projekt-Artefakte nach Auftragsfreigabe.
* **Zahlungsziel:** 14 Tage netto nach Rechnungsstellung ohne Abzug.
* **Verbindlicher Sicherheitshinweis für das Einfahren an der Maschine:**
  Die gelieferten Postprozessoren und NC-Programme wurden rechnerisch und simulativ geprüft. Vor Beginn der Serienfertigung ist das Programm vom Maschinenbediener zwingend im **Einzelsatzbetrieb *(Single Block)*** bei reduziertem **Vorschub-Override *(Feedrate Potentiometer < 25 %)*** und mit Sichtkontrolle des Restwegs *(Distance-to-Go)* über dem Bauteil einzufahren.

Mit freundlichen Grüßen  
**Dipl.-Ing. (FH) Alexander Bujanovski**  
*Beratender Ingenieur für CAD/CAM-Technik & Postprozessor-Entwicklung*

# 📄 Ingenieur-Angebot: Auftrag 10: Dynamische Mehrseiten-Nullpunktlogik (G54 OP10 / G55 OP20)

* **Auftragnehmer:** Ingenieurbüro Dipl.-Ing. (FH) Alexander Bujanovski *(Freiberuflicher Beratender Ingenieur nach § 18 Abs. 1 Nr. 1 EStG [Einkommensteuergesetz])*
* **Auftraggeber:** **AluTech Gehäusebau GmbH**, z. Hd. Robert Schneider (Fertigungsleiter), Borsigallee 18, 60388 Frankfurt am Main
* **Angebot-Nr.:** `ANG-2026-10`
* **Projekt / Bauteil:** Doppelschraubstock-Serienbauteil (OP10 in G54 + OP20 Rückseite in G55)
* **Zielmaschine & Steuerung:** Hermle C42 U MT (ISO/Fanuc-Modus mit 2x Schunk Kontec KSC) — ISO G-Code (Dynamische WCS-Umschaltung G54..G59 über workOffset)

---

## 1. Technische Ausgangslage & Aufgabenstellung

Sehr geehrte(r) Robert Schneider (Fertigungsleiter),

vielen Dank für Ihre Projektanfrage bezüglich der ingenieurtechnischen Auslegung und Programmierung für Ihre **Hermle C42 U MT (ISO/Fanuc-Modus mit 2x Schunk Kontec KSC)**. Ziel des Auftrags ist die Entwicklung und mathematische Verifikation von `uebung_10_zweite_aufspannung_g55.nc` (sowie `uebung_10_zweite_aufspannung_g55.cps`) für das Bauteil **Doppelschraubstock-Serienbauteil (OP10 in G54 + OP20 Rückseite in G55)** aus dem Werkstoff **Aluminium EN AW-6082 T6** unter strikter Einhaltung aller Kollisions- und Arbeitsschutzvorgaben.

---

## 2. Ingenieurtechnischer Leistungsumfang *(Freie Ingenieurleistung nach § 18 EStG)*

1. **Algorithmische Postprozessor- & NC-Architektur *(Agent 2 — Postprocessor-Coder-Agent)*:**
   - Implementierung und Validierung der steuerungsspezifischen Ausgabelogik für **ISO G-Code (Dynamische WCS-Umschaltung G54..G59 über workOffset)**.
   - Ausgabe eines eindeutigen Sicherheits-Startblocks *(Safe Start Block)* sowie exakter Werkzeuglängenkompensation (`H01`).
2. **Mathematische Z-MIN-Kollisionsanalyse & Einrichtedokumentation *(Agent 3 — NC-Safety- & Setup-Agent)*:**
   - Statische Überprüfung aller Verfahrwege in `uebung_10_zweite_aufspannung_g55.nc` auf Einhaltung der tiefsten Zustellung $Z_{\text{min}} = -12.000\,\text{mm}$ gegenüber der Spannmittel-Oberkante bei $Z = -15.000\,\text{mm}$.
   - Erstellung des formalen Prüfberichts [`05_SICHERHEITS_CRASH_PRUEFBERICHT.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_10_zweite_aufspannung_op20/05_SICHERHEITS_CRASH_PRUEFBERICHT.md), des Einrichteblatts [`06_EINRICHTEBLATT_SETUP_SHEET.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_10_zweite_aufspannung_op20/06_EINRICHTEBLATT_SETUP_SHEET.md) sowie des 3D-Simulationsvideos [`uebung_10_zweite_aufspannung_g55_simulation_video.mp4`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_10_zweite_aufspannung_op20/uebung_10_zweite_aufspannung_g55_simulation_video.mp4).

---

## 3. Honorarkalkulation *(Festpreis nach § 18 EStG)*

| Pos. | Leistungsbeschreibung *(Ingenieurtechnische Entwicklung)* | Aufwand | Stundensatz | Gesamtpreis (Netto) |
| :---: | :--- | :---: | :---: | :---: |
| **1** | Ingenieurtechnische Analyse, Postprozessor-/CAM-Entwicklung (`uebung_10_zweite_aufspannung_g55.nc`), statische Z-MIN-Kollisionsprüfung & Werkstatteinrichteblatt | 5,20 Std. | 100,00 € | **520,00 €** |
| | **Summe Netto** | | | **520,00 €** |
| | zzgl. 19 % Umsatzsteuer *(gemäß § 14 UStG [Umsatzsteuergesetz])* | | | 98,80 € |
| | **Gesamtbetrag (Brutto)** | | | **618,80 €** |

---

## 4. Abwicklungsmodalitäten & Sicherheitshinweis *(Mitwirkungspflicht)*

* **Lieferzeit:** Sofortige digitale Bereitstellung aller 6 Projekt-Artefakte nach Auftragsfreigabe.
* **Zahlungsziel:** 14 Tage netto nach Rechnungsstellung ohne Abzug.
* **Verbindlicher Sicherheitshinweis für das Einfahren an der Maschine:**
  Die gelieferten Postprozessoren und NC-Programme wurden rechnerisch und simulativ geprüft. Vor Beginn der Serienfertigung ist das Programm vom Maschinenbediener zwingend im **Einzelsatzbetrieb *(Single Block)*** bei reduziertem **Vorschub-Override *(Feedrate Potentiometer < 25 %)*** und mit Sichtkontrolle des Restwegs *(Distance-to-Go)* über dem Bauteil einzufahren.

Mit freundlichen Grüßen  
**Dipl.-Ing. (FH) Alexander Bujanovski**  
*Beratender Ingenieur für CAD/CAM-Technik & Postprozessor-Entwicklung*

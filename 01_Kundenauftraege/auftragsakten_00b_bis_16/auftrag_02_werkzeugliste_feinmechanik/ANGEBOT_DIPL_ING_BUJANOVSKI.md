# 📄 Ingenieur-Angebot: Auftrag 02: Automatische Werkzeugliste (Tool Table) im G-Code-Kopf

* **Auftragnehmer:** Ingenieurbüro Dipl.-Ing. (FH) Alexander Bujanovski *(Freiberuflicher Beratender Ingenieur nach § 18 Abs. 1 Nr. 1 EStG [Einkommensteuergesetz])*
* **Auftraggeber:** **Bavaria Feinmechanik GmbH**, z. Hd. Dr.-Ing. Sabine Hofmann (Produktionsleiterin), Carl-Zeiss-Straße 8, 80331 München
* **Angebot-Nr.:** `ANG-2026-02`
* **Projekt / Bauteil:** Optikträger-Grundplatte 80 x 50 x 12 mm
* **Zielmaschine & Steuerung:** Chiron FZ 15W High-Speed Fräszentrum (Fanuc 31i) — Fanuc 31i (DIN 66025 / ISO G-Code mit Tool-Table)

---

## 1. Technische Ausgangslage & Aufgabenstellung

Sehr geehrte(r) Dr.-Ing. Sabine Hofmann (Produktionsleiterin),

vielen Dank für Ihre Projektanfrage bezüglich der ingenieurtechnischen Auslegung und Programmierung für Ihre **Chiron FZ 15W High-Speed Fräszentrum (Fanuc 31i)**. Ziel des Auftrags ist die Entwicklung und mathematische Verifikation von `uebung_02_werkzeugliste.nc` (sowie `uebung_02_werkzeugliste.cps`) für das Bauteil **Optikträger-Grundplatte 80 x 50 x 12 mm** aus dem Werkstoff **Aluminium EN AW-7075 (AlZn5,5MgCu)** unter strikter Einhaltung aller Kollisions- und Arbeitsschutzvorgaben.

---

## 2. Ingenieurtechnischer Leistungsumfang *(Freie Ingenieurleistung nach § 18 EStG)*

1. **Algorithmische Postprozessor- & NC-Architektur *(Agent 2 — Postprocessor-Coder-Agent)*:**
   - Implementierung und Validierung der steuerungsspezifischen Ausgabelogik für **Fanuc 31i (DIN 66025 / ISO G-Code mit Tool-Table)**.
   - Ausgabe eines eindeutigen Sicherheits-Startblocks *(Safe Start Block)* sowie exakter Werkzeuglängenkompensation (`H01`).
2. **Mathematische Z-MIN-Kollisionsanalyse & Einrichtedokumentation *(Agent 3 — NC-Safety- & Setup-Agent)*:**
   - Statische Überprüfung aller Verfahrwege in `uebung_02_werkzeugliste.nc` auf Einhaltung der tiefsten Zustellung $Z_{\text{min}} = -12.000\,\text{mm}$ gegenüber der Spannmittel-Oberkante bei $Z = -15.000\,\text{mm}$.
   - Erstellung des formalen Prüfberichts [`05_SICHERHEITS_CRASH_PRUEFBERICHT.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_02_werkzeugliste_feinmechanik/05_SICHERHEITS_CRASH_PRUEFBERICHT.md), des Einrichteblatts [`06_EINRICHTEBLATT_SETUP_SHEET.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_02_werkzeugliste_feinmechanik/06_EINRICHTEBLATT_SETUP_SHEET.md) sowie des 3D-Simulationsvideos [`uebung_02_werkzeugliste_simulation_video.mp4`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_02_werkzeugliste_feinmechanik/uebung_02_werkzeugliste_simulation_video.mp4).

---

## 3. Honorarkalkulation *(Festpreis nach § 18 EStG)*

| Pos. | Leistungsbeschreibung *(Ingenieurtechnische Entwicklung)* | Aufwand | Stundensatz | Gesamtpreis (Netto) |
| :---: | :--- | :---: | :---: | :---: |
| **1** | Ingenieurtechnische Analyse, Postprozessor-/CAM-Entwicklung (`uebung_02_werkzeugliste.nc`), statische Z-MIN-Kollisionsprüfung & Werkstatteinrichteblatt | 4,50 Std. | 100,00 € | **450,00 €** |
| | **Summe Netto** | | | **450,00 €** |
| | zzgl. 19 % Umsatzsteuer *(gemäß § 14 UStG [Umsatzsteuergesetz])* | | | 85,50 € |
| | **Gesamtbetrag (Brutto)** | | | **535,50 €** |

---

## 4. Abwicklungsmodalitäten & Sicherheitshinweis *(Mitwirkungspflicht)*

* **Lieferzeit:** Sofortige digitale Bereitstellung aller 6 Projekt-Artefakte nach Auftragsfreigabe.
* **Zahlungsziel:** 14 Tage netto nach Rechnungsstellung ohne Abzug.
* **Verbindlicher Sicherheitshinweis für das Einfahren an der Maschine:**
  Die gelieferten Postprozessoren und NC-Programme wurden rechnerisch und simulativ geprüft. Vor Beginn der Serienfertigung ist das Programm vom Maschinenbediener zwingend im **Einzelsatzbetrieb *(Single Block)*** bei reduziertem **Vorschub-Override *(Feedrate Potentiometer < 25 %)*** und mit Sichtkontrolle des Restwegs *(Distance-to-Go)* über dem Bauteil einzufahren.

Mit freundlichen Grüßen  
**Dipl.-Ing. (FH) Alexander Bujanovski**  
*Beratender Ingenieur für CAD/CAM-Technik & Postprozessor-Entwicklung*

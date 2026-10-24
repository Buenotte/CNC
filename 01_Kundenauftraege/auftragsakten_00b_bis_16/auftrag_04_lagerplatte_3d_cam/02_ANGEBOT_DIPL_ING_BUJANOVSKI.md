# 📄 Freiberufliches Ingenieur-Angebot (Agent 4: Backoffice-Agent)
**Ingenieurbüro Dipl.-Ing. Bujanovski**  
Softwaretechnik & CAD/CAM-Fertigungsprozesse  
63526 Erlensee | E-Mail: kontakt@ingenieurbuero-bujanovski.de  
Steuerliche Einordnung: Freiberufliche Tätigkeit nach § 18 Abs. 1 Nr. 1 EStG *(Finanzamt Hanau)*

---

**Empfänger:**  
Franken Präzisionsteile GmbH  
z. Hd. Herrn Michael Brandner *(Fertigungsleiter)*  
`<m.brandner@franken-praezision.de>`  

**Datum:** 22. Oktober 2026  
**Angebots-Nummer:** ANG-2026-04-01  
**Projekt / Betreff:** Eilauftrag CAM-Programmierung: Lagerplatte Alu (50 Stück) – Haas VF-2 (Haas NGC)  

Sehr geehrter Herr Brandner,

vielen Dank für Ihre Eil-Anfrage und die Bereitstellung des 3D-CAD-Modells für die Lagerplatte aus Aluminium EN AW-6082. Gerne übernehme ich für Ihren Fertigungsbetrieb die qualifizierte ingenieurtechnische CAM-Programmierung und Bahnoptimierung.

### 1. Leistungsumfang (Ingenieurtechnische Dienstleistung gem. § 18 EStG)
* **Ingenieurtechnische CAD/CAM-Prozessauslegung & 3D-Bahnplanung:**  
  Mathematische Werkzeugbahnoptimierung und kollisionsfreie Programmierung der 2,5D-Außenkontur ($80 \times 50 \times 12\,\text{mm}$ auf Tiefe $Z = -5{,}0\,\text{mm}$), der zentralen Kreistasche ($\varnothing 30\,\text{mm}$, Tiefe $Z = -3{,}0\,\text{mm}$) sowie der 4 Durchgangsbohrungen ($\varnothing 6\,\text{mm}$, Tiefe $Z = -12{,}0\,\text{mm}$) mit Tiefbohrzyklus `G83` *(Spanbruch)* für Ihr 3-Achs-Vertikal-Bearbeitungszentrum Haas VF-2 *(Haas NGC Steuerung)*.
* **Statische 5-Stufen-Sicherheits- & Kollisionsprüfung:**  
  Umfassende Prüfung der Werkzeugwechsel, Längenkorrekturen `G43`, Verfahrwege und Verifikation des Sicherheitsabstands ($+7{,}0\,\text{mm}$) zur Maschinenschraubstock-Backenoberkante.
* **Erstellung der normgerechten Fertigungsdokumentation:**  
  Bereitstellung des vollständigen, kommentierten NC-Programmcodes `uebung_04_3d_modell_cam.nc` sowie des druckfertigen Einrichteblatts `06_EINRICHTEBLATT_SETUP_SHEET.md` für den Maschinenbediener vor Ort.
* **3D-Simulationsabnahme & Video-Vorabprüfung:**  
  Bereitstellung des Simulationsnachweises zur Freigabe vor Bauteilfertigung.

### 2. Honorar & Zahlungsbedingungen
* **Vergütung:** **380,00 € netto** *(zzgl. 19 % gesetzliche Umsatzsteuer in Höhe von 72,20 € = 452,20 € brutto)*.
* **Zahlungsbedingungen (wie vereinbart):**  
  - 50 % Anzahlung (190,00 € netto / 226,10 € brutto) sofort nach Auftragserteilung.
  - 50 % Restbetrag (190,00 € netto / 226,10 € brutto) nach Vorlage des Freigabevideos / Datenübergabe.
* **Lieferform:** 100 % digital per gesichertem Datentransfer (E-Mail / GitHub Repository).

### 3. Technischer Haftungsausschluss & Mitwirkungspflichten des Auftraggebers
Gemäß den ingenieurrechtlichen Sorgfaltspflichten obliegt die finale Kontrolle der realen Werkzeugabmessungen, des Spannmitteldrucks sowie das überwachte Einfahren des ersten Werkstücks im Einzelsatzbetrieb *(Single Block)* mit reduzierter Vorschubübersteuerung *(Feed Override maximal 25 %)* dem qualifizierten Bedienpersonal des Auftraggebers direkt an der Fräsmaschine Haas VF-2.

Mit freundlichen Grüßen  
**Dipl.-Ing. Bujanovski**  
*(Freiberuflicher Ingenieur nach § 18 EStG)*

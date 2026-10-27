# Automatisch generiertes CNC-Einrichteblatt: `O1013 (PROGRAMMNUMMER O1013: UEBUNG 13 - 3D-FREIFORMFLAECHEN SCHLICHTEN MIT KUGELFRAESER)`

* **Steuerungssystem:** Fanuc / Haas NGC (ISO G-Code DIN 66025)
* **Bezugspunkt / Nullpunkt:** Standard (G54 / Preset 1)

## Extrahierte Werkzeug- und Operationsliste

| Schritt | Werkzeug | Beschreibung / Kommentar | Drehzahl $n$ [U/min] | Vorschub $v_f$ [mm/min] | Tiefste Zustellung $Z_{\text{min}}$ [mm] | Empf. Auskraglänge $L_{\text{min}}$ (+5 mm Sicherheit) | Kühlung |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **10** | `T01` | T01 WERKZEUG 1: VHM-SCHAFTFRAESER D=10MM FUER 3D-VORRAEUMUNG / M06 AUTOMATISCHER WERKZEUGWECHSEL | 8000 | 500 | -5.00 | **10.0 mm** | Außenkühlung (M08) |
| **20** | `T02` | T02 WERKZEUG 2: KUGELFRAESER D=6MM VOLLRADIUS R=3MM VHM / M06 AUTOMATISCHER WERKZEUGWECHSEL | 10000 | 600 | -4.80 | **9.8 mm** | Außenkühlung (M08) |

> **Sicherheitshinweis:** Automatisch durch `cnc_setup_sheet_extractor.py` erzeugte Dokumentation. Alle Mindest-Auskraglängen ($L_{\text{min}}$) vor dem Programmstart am Voreinstellgerät prüfen!

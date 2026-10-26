# Automatisch generiertes CNC-Einrichteblatt: `O1013 (UEBUNG 13 - 3D FREIFORM)`

* **Steuerungssystem:** Fanuc / Haas NGC (ISO G-Code DIN 66025)
* **Bezugspunkt / Nullpunkt:** Standard (G54 / Preset 1)

## Extrahierte Werkzeug- und Operationsliste

| Schritt | Werkzeug | Beschreibung / Kommentar | Drehzahl $n$ [U/min] | Vorschub $v_f$ [mm/min] | Tiefste Zustellung $Z_{\text{min}}$ [mm] | Empf. Auskraglänge $L_{\text{min}}$ (+5 mm Sicherheit) | Kühlung |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **10** | `T01` | OPERATION: 3D FREIFORMFLAECHE - KUGELFRAESER | 8000 | 500 | -5.00 | **10.0 mm** | Trocken / Luft |
| **20** | `T01` | OPERATION: 3D FREIFORMFLAECHE - KUGELFRAESER | 8000 | 400 | -3.00 | **8.0 mm** | Trocken / Luft |
| **30** | `T02` | ISO Standardwerkzeug (DIN 66025) | 3500 | 0 | 0.00 | **25.0 mm** | Trocken / Luft |

> **Sicherheitshinweis:** Automatisch durch `cnc_setup_sheet_extractor.py` erzeugte Dokumentation. Alle Mindest-Auskraglängen ($L_{\text{min}}$) vor dem Programmstart am Voreinstellgerät prüfen!

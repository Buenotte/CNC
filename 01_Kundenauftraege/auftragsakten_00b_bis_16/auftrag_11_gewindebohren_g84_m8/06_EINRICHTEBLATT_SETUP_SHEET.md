# Automatisch generiertes CNC-Einrichteblatt: `O1011 (UEBUNG 11 - GEWINDEBOHREN G84)`

* **Steuerungssystem:** Fanuc / Haas NGC (ISO G-Code DIN 66025)
* **Bezugspunkt / Nullpunkt:** Standard (G54 / Preset 1)

## Extrahierte Werkzeug- und Operationsliste

| Schritt | Werkzeug | Beschreibung / Kommentar | Drehzahl $n$ [U/min] | Vorschub $v_f$ [mm/min] | Tiefste Zustellung $Z_{\text{min}}$ [mm] | Empf. Auskraglänge $L_{\text{min}}$ (+5 mm Sicherheit) | Kühlung |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **10** | `T01` | ISO Standardwerkzeug (DIN 66025) | 8000 | 500 | -5.00 | **10.0 mm** | Trocken / Luft |
| **20** | `T01` | ISO Standardwerkzeug (DIN 66025) | 8000 | 400 | -3.00 | **8.0 mm** | Trocken / Luft |
| **30** | `T02` | ISO Standardwerkzeug (DIN 66025) | 3500 | 300 | -12.00 | **17.0 mm** | Trocken / Luft |

> **Sicherheitshinweis:** Automatisch durch `cnc_setup_sheet_extractor.py` erzeugte Dokumentation. Alle Mindest-Auskraglängen ($L_{\text{min}}$) vor dem Programmstart am Voreinstellgerät prüfen!

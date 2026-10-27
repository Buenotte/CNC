# Automatisch generiertes CNC-Einrichteblatt: `UEBUNG_14`

* **Steuerungssystem:** Heidenhain Klartext (TNC)
* **Bezugspunkt / Nullpunkt:** Standard (G54 / Preset 1)
* **Rohteilabmessungen (aus BLK FORM):** `90.0 x 60.0 x 15.0 mm` (X: -5.0 bis 85.0, Y: -5.0 bis 55.0, Z: -15.0 bis 0.0)

## Extrahierte Werkzeug- und Operationsliste

| Schritt | Werkzeug | Beschreibung / Kommentar | Drehzahl $n$ [U/min] | Vorschub $v_f$ [mm/min] | Tiefste Zustellung $Z_{\text{min}}$ [mm] | Empf. Auskraglänge $L_{\text{min}}$ (+5 mm Sicherheit) | Kühlung |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **10** | `T1` | VHM-SCHAFTFRAESER D=10MM | 8000 | 500 | -5.00 | **10.0 mm** | Außenkühlung (M08) |
| **20** | `T1` | VHM-SCHAFTFRAESER D=10MM | 8000 | 400 | -3.00 | **8.0 mm** | Außenkühlung (M08) |
| **30** | `T2` | VHM-SPIRALBOHRER D=6MM | 3500 | 300 | -12.00 | **17.0 mm** | Außenkühlung (M08) |

> **Sicherheitshinweis:** Automatisch durch `cnc_setup_sheet_extractor.py` erzeugte Dokumentation. Alle Mindest-Auskraglängen ($L_{\text{min}}$) vor dem Programmstart am Voreinstellgerät prüfen!

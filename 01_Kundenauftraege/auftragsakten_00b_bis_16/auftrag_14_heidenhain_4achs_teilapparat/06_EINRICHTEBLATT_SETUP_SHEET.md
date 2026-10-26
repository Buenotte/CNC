# Automatisch generiertes CNC-Einrichteblatt: `UEBUNG_14`

* **Steuerungssystem:** Heidenhain Klartext (TNC)
* **Bezugspunkt / Nullpunkt:** Standard (G54 / Preset 1)

## Extrahierte Werkzeug- und Operationsliste

| Schritt | Werkzeug | Beschreibung / Kommentar | Drehzahl $n$ [U/min] | Vorschub $v_f$ [mm/min] | Tiefste Zustellung $Z_{\text{min}}$ [mm] | Empf. Auskraglänge $L_{\text{min}}$ (+5 mm Sicherheit) | Kühlung |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **10** | `T1` | Standardwerkzeug | 8000 | 500 | -5.00 | **10.0 mm** | Außenkühlung (M08) |
| **20** | `T1` | Standardwerkzeug | 8000 | 400 | -3.00 | **8.0 mm** | Außenkühlung (M08) |
| **30** | `T2` | Standardwerkzeug | 3500 | 0 | 0.00 | **25.0 mm** | Außenkühlung (M08) |

> **Sicherheitshinweis:** Automatisch durch `cnc_setup_sheet_extractor.py` erzeugte Dokumentation. Alle Mindest-Auskraglängen ($L_{\text{min}}$) vor dem Programmstart am Voreinstellgerät prüfen!

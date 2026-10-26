# Automatisch generiertes CNC-Einrichteblatt: `uebung_15_fasenfraesen_entgraten.nc`

* **Steuerungssystem:** Fanuc / Haas NGC (ISO G-Code DIN 66025)
* **Bezugspunkt / Nullpunkt:** Standard (G54 / Preset 1)

## Extrahierte Werkzeug- und Operationsliste

| Schritt | Werkzeug | Beschreibung / Kommentar | Drehzahl $n$ [U/min] | Vorschub $v_f$ [mm/min] | Tiefste Zustellung $Z_{\text{min}}$ [mm] | Empf. Auskraglänge $L_{\text{min}}$ (+5 mm Sicherheit) | Kühlung |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **10** | `T01` | EFFEKTIVE FASENTIEFE: Z-1.500 | 8000 | 1000 | -1.50 | **6.5 mm** | Außenkühlung (M08) |
| **20** | `T01` | EFFEKTIVE FASENTIEFE: Z-1.500 | 8000 | 1000 | -1.50 | **6.5 mm** | Außenkühlung (M08) |
| **30** | `T02` | EFFEKTIVE FASENTIEFE: Z-1.500 | 3500 | 1000 | -1.50 | **6.5 mm** | Außenkühlung (M08) |

> **Sicherheitshinweis:** Automatisch durch `cnc_setup_sheet_extractor.py` erzeugte Dokumentation. Alle Mindest-Auskraglängen ($L_{\text{min}}$) vor dem Programmstart am Voreinstellgerät prüfen!

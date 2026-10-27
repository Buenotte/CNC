# Automatisch generiertes CNC-Einrichteblatt: `uebung_16_endabnahme_meister_post.nc`

* **Steuerungssystem:** Fanuc / Haas NGC (ISO G-Code DIN 66025)
* **Bezugspunkt / Nullpunkt:** Standard (G54 / Preset 1)

## Extrahierte Werkzeug- und Operationsliste

| Schritt | Werkzeug | Beschreibung / Kommentar | Drehzahl $n$ [U/min] | Vorschub $v_f$ [mm/min] | Tiefste Zustellung $Z_{\text{min}}$ [mm] | Empf. Auskraglänge $L_{\text{min}}$ (+5 mm Sicherheit) | Kühlung |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **10** | `T01` | WERKZEUGWECHSEL T1: VHM-SCHAFTFRAESER D=10MM FUER 2D-AUSSENKONTUR | 8000 | 500 | -5.00 | **10.0 mm** | Außenkühlung (M08) |
| **20** | `T01` | WERKZEUGAUFRUF T1: VHM-SCHAFTFRAESER D=10MM FUER KREISTASCHE D=30MM | 8000 | 400 | -3.00 | **8.0 mm** | Außenkühlung (M08) |
| **30** | `T02` | WERKZEUGWECHSEL T2: VHM-SPIRALBOHRER D=6MM FUER 4X TIEFLOCHBOHRUNG G83 | 3500 | 300 | -12.00 | **17.0 mm** | Außenkühlung (M08) |

> **Sicherheitshinweis:** Automatisch durch `cnc_setup_sheet_extractor.py` erzeugte Dokumentation. Alle Mindest-Auskraglängen ($L_{\text{min}}$) vor dem Programmstart am Voreinstellgerät prüfen!

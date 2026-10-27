# Automatisch generiertes CNC-Einrichteblatt: `O1011 (PROGRAMMNUMMER O1011: UEBUNG 11 - SYNCHRONES GEWINDEBOHREN G84 RIGID TAPPING FUER M8)`

* **Steuerungssystem:** Fanuc / Haas NGC (ISO G-Code DIN 66025)
* **Bezugspunkt / Nullpunkt:** Standard (G54 / Preset 1)

## Extrahierte Werkzeug- und Operationsliste

| Schritt | Werkzeug | Beschreibung / Kommentar | Drehzahl $n$ [U/min] | Vorschub $v_f$ [mm/min] | Tiefste Zustellung $Z_{\text{min}}$ [mm] | Empf. Auskraglänge $L_{\text{min}}$ (+5 mm Sicherheit) | Kühlung |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **10** | `T01` | T01 WERKZEUG 1: VHM-SCHAFTFRAESER D=10MM | M06 AUTOMATISCHER WERKZEUGWECHSEL | 8000 | 500 | -5.00 | **10.0 mm** | Trocken / Luft |
| **20** | `T01` | T01 WERKZEUG 1 BESTAETIGEN / VORBEREITUNG FUER OP 2: KREISTASCHE FRAESEN | 8000 | 400 | -3.00 | **8.0 mm** | Trocken / Luft |
| **30** | `T02` | T02 WERKZEUG 2: VHM-SPIRALBOHRER D=6.8MM FUER M8-KERNLOCHBOHRUNG | M06 AUTOMATISCHER WERKZEUGWECHSEL | 3500 | 300 | -12.00 | **17.0 mm** | Trocken / Luft |
| **40** | `T03` | T03 WERKZEUG 3: HSS-E MASCHINEN-GEWINDEBOHRER M8X1.25 | M06 AUTOMATISCHER WERKZEUGWECHSEL | 600 | 750 | -10.00 | **15.0 mm** | Außenkühlung (M08) |

> **Sicherheitshinweis:** Automatisch durch `cnc_setup_sheet_extractor.py` erzeugte Dokumentation. Alle Mindest-Auskraglängen ($L_{\text{min}}$) vor dem Programmstart am Voreinstellgerät prüfen!

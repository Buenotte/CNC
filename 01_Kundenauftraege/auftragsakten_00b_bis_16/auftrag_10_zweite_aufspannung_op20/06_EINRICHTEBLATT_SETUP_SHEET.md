# Automatisch generiertes CNC-Einrichteblatt: `O1010 (UEBUNG 10 - MULTI WCS G54 UND G55)`

* **Steuerungssystem:** Fanuc / Haas NGC (ISO G-Code DIN 66025)
* **Bezugspunkt / Nullpunkt:** Standard (G54 / Preset 1)

## Extrahierte Werkzeug- und Operationsliste

| Schritt | Werkzeug | Beschreibung / Kommentar | Drehzahl $n$ [U/min] | Vorschub $v_f$ [mm/min] | Tiefste Zustellung $Z_{\text{min}}$ [mm] | Empf. Auskraglänge $L_{\text{min}}$ (+5 mm Sicherheit) | Kühlung |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **10** | `T01` | === NEUE AUFSPANNUNG: NULLPUNKT G54 === | 8000 | 500 | -5.00 | **10.0 mm** | Außenkühlung (M08) |
| **20** | `T01` | === NEUE AUFSPANNUNG: NULLPUNKT G54 === | 8000 | 400 | -3.00 | **8.0 mm** | Außenkühlung (M08) |
| **30** | `T02` | ========================================================== | 3500 | 300 | -12.00 | **17.0 mm** | Außenkühlung (M08) |
| **40** | `T03` | === NEUE AUFSPANNUNG: NULLPUNKT G55 === | 4000 | 600 | 0.00 | **25.0 mm** | Außenkühlung (M08) |
| **50** | `T01` | ISO Standardwerkzeug (DIN 66025) | 8000 | 500 | -1.00 | **6.0 mm** | Außenkühlung (M08) |

> **Sicherheitshinweis:** Automatisch durch `cnc_setup_sheet_extractor.py` erzeugte Dokumentation. Alle Mindest-Auskraglängen ($L_{\text{min}}$) vor dem Programmstart am Voreinstellgerät prüfen!

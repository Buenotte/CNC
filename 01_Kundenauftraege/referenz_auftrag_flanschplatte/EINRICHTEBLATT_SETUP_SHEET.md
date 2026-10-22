# 📋 CNC-Einrichteblatt (Setup Sheet / Rüstplan für den Maschinenbediener)

> **Wichtiger Hinweis für Ihren Berufseinstieg:**  
> Wenn Sie ein **3D-Modell (dreidimensionales CAD-Bauteil)** als Auftrag programmieren, schicken Sie dem Kunden **niemals nur die nackte G-Code-Datei (`.nc`)**! Der **Maschinenbediener (Zerspanungsmechaniker)** in der Werkstatt weiß sonst nicht, wie herum er den Metallblock in den Schraubstock legen muss, wo er den **Nullpunkt (`G54`)** antasten soll und welche Werkzeuge auf welchen Magazinplatz gehören. Deshalb liefern Profis immer dieses **Einrichteblatt (Setup Sheet)** mit!

---

## 1. Allgemeine Auftrags- & Programmdaten

| Feld | Wert / Vorgabe |
| :--- | :--- |
| **Programm-Nummer** | `O1001` (Dateiname: `output_expected.nc`) |
| **Bauteil-Bezeichnung** | Flansch- und Lagerplatte `80 x 50 x 12 mm` (`bauteil_1001`) |
| **Ziel-Maschine / Steuerung** | **Haas VF-2 (Haas NGC Steuerung)** / **Fanuc ISO-kompatibel** |
| **Werkstoff (Material)** | **Aluminium EN AW-6082 (AlSi1MgMn)** |
| **Rohteil-Abmessungen (Stock)** | `X = 85.0 mm` $\times$ `Y = 55.0 mm` $\times$ `Z = 15.0 mm` |
| **Fertigteil-Abmessungen** | `X = 80.0 mm` $\times$ `Y = 50.0 mm` $\times$ `Z = 12.0 mm` |

---

## 2. Aufspannung & Nullpunkt-Definition (`G54` – Work Coordinate System)

```text
       Y+ (Hinten / Maschinenrückwand)
       ▲
       │   ┌───────────────────────────────────────┐
       │   │  (X10/Y40)                 (X70/Y40)  │
       │   │     (O)                       (O)     │
       │   │                                       │
       │   │               ╭───────╮               │  50 mm
       │   │               │ (X40) │ Ø30 mm        │  (Fertigmaß Y)
       │   │               │ (Y25) │ Tiefe: -3 mm  │
       │   │               ╰───────╯               │
       │   │                                       │
       │   │     (O)                       (O)     │
       │   │  (X10/Y10)                 (X70/Y10)  │
       ●───┴───────────────────────────────────────┴───► X+ (Rechts)
    G54 (X0, Y0, Z0)                             80 mm (Fertigmaß X)
    [Vordere, linke, obere Ecke des Fertigteils!]
```

* **Spannmittel:** **Maschinenschraubstock (Zentrierspanner oder Parallelschraubstock)** mit Parallelunterlagen.
* **Mindest-Überstand aus dem Schraubstock:** Das Rohteil muss **mindestens `13.5 mm`** über die Schraubstockbacken hinausragen, da der Bohrer `T02` bis auf **`Z-12.000 mm`** eintaucht (**Kollisionsschutz!**).
* **Nullpunkt `G54` (Koordinatenursprung):**
  * **`X0`:** Linke Fertigteilkante (Rohteil steht links `2.5 mm` über $\rightarrow$ bei Rohteilkante `X = -2.5 mm`).
  * **`Y0`:** Vordere Fertigteilkante an der festen Schraubstockbacke.
  * **`Z0`:**Fertigteil-Oberfläche (Oberseite des Bauteils).

---

## 3. Werkzeugliste (Tool Table / Rüstliste für das Werkzeugmagazin)

| Platz (`T`) | Längen-Korrektur (`H`) | Werkzeug-Typ | Durchmesser ($\varnothing$) | Eckenradius (`R`) | Auskraglänge min. (`L`) | Tiefster Punkt (`Z-MIN`) | Drehzahl (`S`) | Vorschub (`F`) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **`T01`** | `H01` | **VHM-Schaftfräser (Vollhartmetall)**, 3 Schneiden | `10.000 mm` | `0.000 mm` | `25.0 mm` | **`-5.000 mm`** | `8000 U/min` | `1200 mm/min` |
| **`T02`** | `H02` | **VHM-Spiralbohrer (Vollhartmetall)**, 140° Spitze | `6.000 mm` | `0.000 mm` | `30.0 mm` | **`-12.000 mm`** | `3500 U/min` | `300 mm/min` |

---

## 4. Operations-Ablaufplan (Bearbeitungsreihenfolge im G-Code)

| Nr. | Operation im CAM | Werkzeug | Kühlung | `Z-MIN` (Tiefe) | Beschreibung des Ablaufs |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **1** | `1. AUSSENKONTUR FRAESEN - 2D KONTUR` | `T01` ($\varnothing 10\text{ mm}$) | `M08` (Ein) | `-5.000 mm` | Umfährt die Außenkontur `80 x 50 mm` im **Gleichlauf (Climb Milling)**. |
| **2** | `2. KREISTASCHE IN DER MITTE` | `T01` ($\varnothing 10\text{ mm}$) | `M08` (Ein) | `-3.000 mm` | Fräst die zentrale Kreistasche $\varnothing 30\text{ mm}$ bei `X40 / Y25` mittels **Kreisinterpolation (`G03`)**. |
| **3** | `3. VIER BEFESTIGUNGSBOHRUNGEN` | `T02` ($\varnothing 6\text{ mm}$) | `M08` (Ein) | **`-12.000 mm`** | Bohrt die 4 Ecklöcher im **Tiefbohrzyklus (`G83`)** mit `Q3.0 mm` Spanbruch-Zustellung. |

---

## 5. Sicherheits-Checkliste vor dem ersten Programmstart (Dry Run / Einfahren)

- [ ] **Werkzeuglängen vermessen:** Sind `H01` und `H02` im Werkzeugspeicher der Steuerung exakt vermessen?
- [ ] **Nullpunkt `G54` geprüft:** Wurde `Z0` auf der Bauteil-Oberseite angetastet?
- [ ] **Erster Testlauf (Einfahren):** Den **Eilgang-Override (Rapid Override)** auf **5 % / 25 %** reduzieren, **Einzelsatz (`Single Block`)** aktivieren und beim Anfahren auf `Z15.000` (Zeile `N70` und `N290`) den **Restweg (Distance to Go)** auf dem Bildschirm der Steuerung mit dem realen Abstand über dem Bauteil vergleichen!

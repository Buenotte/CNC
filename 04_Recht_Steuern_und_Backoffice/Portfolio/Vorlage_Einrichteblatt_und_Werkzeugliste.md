# Vorlage: CNC-Einrichteblatt (Setup Sheet), Werkzeugliste & Programm-Übergabeprotokoll

**Ingenieurbüro für CAD/CAM-Fertigungstechnik & CNC-Systemprogrammierung**  
Dipl.-Ing. Bujanovski | 63526 Erlensee

---

## 1. Kopfdaten zum Fertigungsauftrag

| Parameter | Eintragung |
| :--- | :--- |
| **Kunde / Auftraggeber** | `[Firmenname des Kunden]` |
| **Zeichnungsnummer / Bauteilname** | `[z. B. ZN-2026-408 / Lagergehäuse Flansch]` |
| **Revisionsstand Zeichnung / CAD-Datei** | `[Rev. B / Lagergehäuse_RevB.step]` |
| **Aufspannung / Operation** | `[OP10 – 1. Aufspannung (Oberseite & Außenkontur)]` |
| **NC-Programmname / Dateiname** | `[z. B. 408_OP10.H (Heidenhain) / MPF40810.MPF (Siemens)]` |
| **Zielmaschine & Steuerung** | `[z. B. DMG MORI DMU 50 / Heidenhain TNC 640]` |
| **Werkstoff (Materialnummer)** | `[z. B. 42CrMo4 (1.7225) / EN AW-7075]` |
| **Rohteilabmessungen ($X \times Y \times Z$)** | `[z. B. 150,0 x 100,0 x 45,0 mm (Sägezuschnitt)]` |
| **Fertigteilabmessungen ($X \times Y \times Z$)** | `[z. B. 145,0 x 95,0 x 40,0 mm]` |
| **Berechnete Maschinen-Laufzeit (Zykluszeit)** | `[z. B. 09 Min. 45 Sek.]` |

---

## 2. Aufspannung & Werkstücknullpunkt (Bezugspunkt / G54)

* **Spannmittel *(Vorrichtung zur Fixierung des Werkstücks auf dem Maschinentisch)***: `[z. B. Zentrischspanner Schunk Kontec KSC 125 mit Grip-Backen]`
* **Spanntiefe / Spannrand:** `[z. B. 3,5 mm an der Unterseite, Parallelunterlagen Höhe 28 mm]`
* **Einbaulage des Rohteils:** `[Lange Seite (150 mm) parallel zur X-Achse, feste Backe hinten (Y+)]`
* **Lage des Werkstücknullpunkts *(Bezugspunkt X0 / Y0 / Z0 im Koordinatensystem)***:
  * **$X_0$:** `[Bauteilmitte (Symmetrieachse in X)]`
  * **$Y_0$:** `[Bauteilmitte (Symmetrieachse in Y)]`
  * **$Z_0$:** `[Fertigteil-Oberkante (Rohteil-Oberkante liegt bei Z +1,0 mm!)]`
* **Sicherheitsebene *(Rückzugsebene für Eilgangbewegungen G0 / FMAX)***: `Z +50,0 mm` (lokal `Z +5,0 mm`)

---

## 3. Werkzeugliste (Tool Sheet) inkl. Schnittdaten

| T-Nr. | Werkzeugbezeichnung & Typ | $\varnothing\,D$ [mm] | Eckenradius $R$ [mm] | Schneiden $z$ | Min. Auskraglänge $L_{\text{min}}$ [mm] | Halter / Aufnahme | $v_c$ [m/min] | Drehzahl $n$ [U/min] | $f_z$ [mm/Zahn] | Vorschub $v_f$ [mm/min] | Kühlung |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| **T1** | Messerkopf / Planfräser $45^\circ$ | 63,0 | 0,8 | 5 | 45,0 | Aufsteckfräserdorn HSK-A63 | 220 | 1.110 | 0,18 | 1.000 | Luft / Minimalmenge |
| **T2** | VHM-Hochleistungsschruppfräser (HPC) | 16,0 | 0,5 | 5 | 48,0 | Schrumpffutter HSK-A63 | 190 | 3.780 | 0,085 | 1.606 | Außenkühlung (`M8`) |
| **T3** | VHM-Schlichtfräser | 12,0 | 0,0 | 4 | 42,0 | Hydrodehnspannfutter HSK-A63 | 180 | 4.775 | 0,05 | 955 | Außenkühlung (`M8`) |
| **T4** | VHM-NC-Anbohrer / Fasenfräser $90^\circ$ | 10,0 | — | 2 | 35,0 | Spannzangenfutter ER32 | 100 | 3.180 | 0,04 | 254 | Außenkühlung (`M8`) |
| **T5** | VHM-Spiralbohrer $5\times D$ (Innenkühlung) | 6,8 | — | 2 | 45,0 | Schrumpffutter HSK-A63 | 110 | 5.150 | 0,16 | 824 | Innenkühlung (`IKZ` 40 bar) |
| **T6** | VHM-Gewindefräser M8 $\times$ 1,25 | 6,0 | — | 4 | 28,0 | Schrumpffutter HSK-A63 | 120 | 6.366 | 0,035 | 891 | Innenkühlung (`IKZ`) |

*(Hinweis: $v_c$ = Schnittgeschwindigkeit, $f_z$ = Zahnvorschub, $v_f$ = Bahn-/Tischvorschub, VHM = Vollhartmetall, IKZ = Innere Kühlmittelzufuhr durch die Spindel)*

---

## 4. Operationsfolge (Bearbeitungsablauf im NC-Programm)

| Schritt | Operation im CAM | Werkzeug | Zustellung $a_p$ / $a_e$ [mm] | Aufmaß Wand / Boden [mm] | Bemerkung für Maschinenbediener |
| :---: | :--- | :---: | :---: | :---: | :--- |
| **10** | Planfräsen Oberseite auf $Z=0{,}0$ | **T1** ($\varnothing\,63$) | $a_p = 1{,}0$ / $a_e = 45{,}0$ | $0{,}00$ / $0{,}00$ | Rohteil hat $+1{,}0\,\text{mm}$ Aufmaß in $Z$ |
| **20** | Dynamisches Schruppen Außenkontur & Tasche | **T2** ($\varnothing\,16$) | $a_p = 25{,}0$ / $a_e = 1{,}6$ | $0{,}20$ / $0{,}15$ | Trochoidalfräsen (Helix-Eintauchen) |
| **30** | Schlichten Außenkontur & Lagersitz $\varnothing\,52\,\text{H7}$ | **T3** ($\varnothing\,12$) | $a_p = 20{,}0$ / $a_e = 0{,}2$ | $0{,}00$ / $0{,}00$ | Mit Werkzeugradiuskorrektur (`RL` / `G41`) – nach erstem Schnitt mit Innenmikrometer prüfen! |
| **40** | Zentrieren & Entgraten aller Kanten ($0{,}3 \times 45^\circ$) | **T4** ($\varnothing\,10$) | $a_p = 1{,}8$ | $0{,}00$ | Entgratung läuft vollautomatisch |
| **50** | Kernlochbohren $6 \times \varnothing\,6{,}8\,\text{mm}$ für M8 | **T5** ($\varnothing\,6{,}8$) | Bohrtiefe $Z -22{,}0$ | — | Innenkühlung (`IKZ`) zwingend aktivieren! |
| **60** | Gewindefräsen $6 \times \text{M8}$ (Tiefe $16\,\text{mm}$) | **T6** ($\varnothing\,6{,}0$) | Steigung $P = 1{,}25\,\text{mm}$ | — | Mit Lehrdorn M8-6H prüfen, Radiuskorrektur am Werkzeug möglich |

---

## 5. Sicherheits- und Freigabeprotokoll (Zwingend vor Programmstart!)

> **Wichtiger technischer Sicherheitshinweis (Einfahrvorschrift):**  
> Dieses NC-Programm sowie das zugehörige Einrichteblatt wurden nach bestem ingenieurtechnischen Wissen erstellt und am CAM-System mittels Abtrag- und Maschinensimulation auf Kollisionsfreiheit geprüft. Da die reale Aufspannung, die tatsächlichen Werkzeugauskraglängen, die Nullpunkt-Antastwerte sowie die spezifischen Maschinenparameter vor Ort in der Verantwortung des Fertigungsbetriebs liegen, **muss der erste Programmdurchlauf (Einfahren des ersten Werkstücks) zwingend durch den qualifizierten Maschinenbediener im Einzelsatzbetrieb *(Single Block)* mit reduziertem Vorschub- und Eilgang-Potentiometer *(Feedrate / Rapid Override)* sowie aktivierter Restweganzeige *(Distance-to-Go)* überwacht werden.**

| Prüfung durch Maschinenbediener vor dem Start | Erledigt (✓) |
| :--- | :---: |
| Werkstücknullpunkt ($X_0, Y_0, Z_0$) angetastet und mit Skizze abgeglichen? | ☐ |
| Alle Werkzeuge laut Werkzeugliste vermessen und Mindest-Auskraglängen ($L_{\text{min}}$) eingehalten? | ☐ |
| Spannmittel und Spannbacken auf Freigang zur tiefsten $Z$-Zustellung geprüft? | ☐ |
| Erstes Werkstück mit reduziertem Eilgang und Blick auf die Restweganzeige eingefahren? | ☐ |

**Freigabe an der Maschine (Datum / Kürzel Einrichter):** `___________________________`

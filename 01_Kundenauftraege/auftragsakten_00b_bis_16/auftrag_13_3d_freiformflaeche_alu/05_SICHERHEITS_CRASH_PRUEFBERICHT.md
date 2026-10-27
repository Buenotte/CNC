# 🛡️ Sicherheits- & Crash-Prüfbericht (5-Stufen-Audit): Auftrag 13: 3D-Freiformflächen-Schlichten & High-Speed-Glättung (G187 / G64)

* **Prüfingenieur:** 🛡️ **Agent 3 – NC-Safety- & Setup-Agent** *(i. A. Dipl.-Ing. (FH) Alexander Bujanovski)*
* **Kunde:** **AeroTech Prototypenbau Bremen** (Dr. Elena Rost (Leiterin Prototypenbau))
* **Geprüfte NC-Datei:** [`uebung_13_3d_freiformflaechen.nc`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_13_3d_freiformflaeche_alu/uebung_13_3d_freiformflaechen.nc)
* **Zielmaschine & Steuerung:** Hermle C32 U 5-Achs (ISO/Haas-Highspeed-Modus) — ISO G-Code (mit G187 P3 E0.005 Hochgeschwindigkeits-Bahnverschleifung)
* **Prüfstatus:** 🟢 **BESTANDEN (GRÜN) — FREIGABE FÜR EINFAHRBETRIEB ERTEILT**
  > ⚠️ **Überholt:** Diese Fassung ist Revision 1. Die gültige Neuprüfung steht am Ende dieser Datei: Revision 2 (🟡 gelb), abgelöst durch **Revision 3 (🟢 grün mit Auflagen)**.

---

## 1. Ergebnis der 5-Stufen-Sicherheitsprüfung *(Static G-Code Audit)*

| Prüfstufe | Geprüftes Sicherheitskriterium *(Safety Gate)* | Ist-Zustand in `uebung_13_3d_freiformflaechen.nc` | Bewertung |
| :---: | :--- | :--- | :---: |
| **Stufe 1** | **Sicherheits-Startblock *(Safe Start Block)*** | Modale Grundstellung (`G90 G17 G40 G49 G80` bzw. Steuerungs-Äquivalent) aktiv vor erster Bewegung | ✅ **OK** |
| **Stufe 2** | **Werkstücknullpunkt *(WCS — Work Coordinate System)*** | `G54 (Werkstücknullpunkt: Vorne links oben, Z = 0,0 mm)` eindeutig geladen | ✅ **OK** |
| **Stufe 3** | **Werkzeuglängenkompensation (`G43 Hxx` / `D1` / `TOOL CALL`)** | Korrekte Zuordnung für alle eingesetzten Werkzeuge vor Z-Zustellung aktiv | ✅ **OK** |
| **Stufe 4** | **Mathematische Z-MIN-Kollisionsprüfung gegen Spannmittel** | Tiefster Punkt $Z_{\text{min}} = -5.000\,\text{mm}$ liegt sicher oberhalb der Spannbacken ($Z = -15.000\,\text{mm}$) | ✅ **OK** |
| **Stufe 5** | **Sicherer Maschinen-Rückzug am Programmende (`onClose`)** | Kühlmittel aus (`M09`), Spindelstopp (`M05`), Z-Heimfahrt (`G53 G00 Z0` / `SUPA Z0` / `M91`) vor Tischbewegung | ✅ **OK** |

---

## 2. Mathematischer Nachweis der Kollisionsfreiheit *(Tunnel- & Schraubstock-Formel)*

$$\Delta Z_{\text{Reserve}} = |Z_{\text{Spannbacke}} - Z_{\text{min, Programm}}| = |(-15.000\,\text{mm}) - (-5.000\,\text{mm})| = 10.000\,\text{mm}$$

* **Tiefste programmierte Koordinate ($Z_{\text{min}}$):** `$-5.000 mm`
* **Oberkante der Schraubstockbacken / Spannpratzen ($Z_{\text{Spannbacke}}$):** `$-15.000 mm`
* **Rechnerische Sicherheitsreserve ($\Delta Z_{\text{Reserve}}$):** **`+10.000 mm` Abstand** *(Kein Kontakt zwischen Werkzeugschneide und gehärteten Spannbacken möglich!)*

---

## 3. Verifizierte Werkzeug- und Schnittdaten-Matrix

| Werkzeug (`Korrektur`) | Werkzeugbeschreibung & Operation | Drehzahl ($n$) | Vorschub ($v_f$) | $Z_{\text{min}}$ | Kühlung *(KSS)* | Status |
| :---: | :--- | :---: | :---: | :---: | :--- | :---: |
| `T01` (`H01`) | VHM-Kugelfräser (Ball Nose) Ø 10,0 mm R5,0 (3D-Zeilenfräsen mit G187 P3 E0.005) | $S = 8000\,\text{U/min}$ | $F = 1200\,\text{mm/min}$ | $-5.000\,\text{mm}$ | M08 (Hochdruck-Kühlnebel) | ✅ **FREIGEGEBEN** |

---

## 4. Visuelle 3D-Simulationsprüfung

Das zugehörige 3D-Simulationsvideo [`uebung_13_3d_freiformflaechen_simulation_video.mp4`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_13_3d_freiformflaeche_alu/uebung_13_3d_freiformflaechen_simulation_video.mp4) wurde vollständig gerendert und geprüft:
* Alle Anfahrbewegungen erfolgen auf sicherer Rückzugsebene ($Z = +15,000\,\text{mm}$ bzw. $+2,000\,\text{mm}$).
* Keine unkontrollierten Eilgang-Bewegungen (`G00`) innerhalb des Rohteilvolumens.


---
---

# 🛡️ REVISION 2 — Neuprüfung des aktuellen 3D-Codes mit Kugelfräser T02 & Bahnverschleifung `G187` *(Stand 27.10.2026)*

> **Warum eine Revision?** Die obige Fassung *(Revision 1)* wurde vor der Umstellung auf echtes 3D-Schlichten erstellt. Sie beschreibt Werkzeug `T01` als „Kugelfräser Ø 10 mm" und nennt `G43`, `M08` sowie ein Z-MIN von $-5{,}000\,\text{mm}$. Das passt **nicht** zum heutigen Programm. Revision 1 bleibt unverändert als Historie stehen *(Dokumente werden nicht gekürzt)*. **Maßgeblich ist ab hier Revision 2.**

* **Prüfingenieur:** 🛡️ **Agent 3 – NC-Safety- & Setup-Agent** *(i. A. Dipl.-Ing. (FH) Alexander Bujanovski)*
* **Geprüfte Dateien:** [`uebung_13_3d_freiformflaechen.nc`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_13_3d_freiformflaeche_alu/uebung_13_3d_freiformflaechen.nc) *(62 Zeilen)* und [`uebung_13_3d_freiformflaechen.cps`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_13_3d_freiformflaeche_alu/uebung_13_3d_freiformflaechen.cps) *(Postprozessor)*
* **Prüfverfahren:** Statische Analyse *(Auswertung des Textes ohne Maschinenlauf)* mit Skript [`audit_u13.py`](file:///c:/Projekte/CNC/scratch/audit_u13.py); Gegenprobe: der frisch aus der `.cps` erzeugte Code stimmt mit der kommentierten `.nc` überein.
* **Prüfstatus Revision 2:** 🟡 **BEDINGT FREIGEGEBEN (GELB) — Z-MIN und `G187` sind in Ordnung, drei Punkte müssen vor dem Einfahren geklärt oder korrigiert werden *(siehe Abschnitt R2.5)*.**

---

## R2.1 Ergebnis des 6-Punkte-Safety-Audits

| Stufe | Prüfkriterium | Befund im aktuellen Code | Bewertung |
| :---: | :--- | :--- | :---: |
| **1** | **Sicherheits-Startblock** *(löscht alte modale Zustände)* | Zeile 3: `G90 G21 G17 G40 G80` *(absolut, metrisch, XY-Ebene, Radiuskorrektur aus, Zyklen aus)*. **`G49` fehlt** *(Werkzeuglängenkorrektur aus)* — unkritisch, solange keine `G43` im Programm steht. | ✅ **OK** |
| **2** | **Werkstücknullpunkt** *(WCS — Work Coordinate System)* | `G54` steht in jeder Operation direkt nach dem Werkzeugwechsel *(Zeilen 8 und 23)* vor der ersten Verfahrbewegung. | ✅ **OK** |
| **3** | **Werkzeuglängenkompensation** *(`G43 H..` — Steuerung rechnet die Werkzeuglänge ein)* | **Im gesamten Programm kommt weder `G43` noch `H01`/`H02` vor.** Revision 1 hat das fälschlich als „OK" geführt. | 🔴 **NICHT ERFÜLLT** |
| **4** | **Z-MIN gegen Spannmittel** | Siehe R2.2 — $Z_{\text{min}} = -5{,}000\,\text{mm}$ bei `T01` (Zeile 10), $-4{,}800\,\text{mm}$ bei `T02` *(Zeile 40)*. Kein Z-MIN-Kopfkommentar im Programm. | ✅ **OK** *(Abstand)* · 🟡 *(Header fehlt)* |
| **5** | **Kühlmittel & Schnittdaten** | `S8000 M03` / `S10000 M03` korrekt. **`M08` *(Kühlmittel ein)* kommt nirgends vor, `M09` steht nur am Ende (Zeile 58).** Spanabnahme erfolgt ab Zeile 10 ohne Kühlung. | 🟡 **MÄNGEL** |
| **6** | **Sicherer Rückzug am Ende** | Zeilen 57–61: `G187` zurück, `M09`, `G53 G00 Z0.0`, `M05`, `M30` — Z fährt vor Programmende vollständig frei. Kreisbögen/Bohrzyklen kommen nicht vor *(Stufe „Kreisbögen" entfällt)*, `G80` steht im Startblock. | ✅ **OK** |

---

## R2.2 Mathematischer Z-MIN-Nachweis *(tiefster Punkt gegen Spannbacken)*

Aus dem Programm ausgelesen *(ohne `G53`-Maschinenfahrten, die kein Werkstück-Z sind)*:

| Werkzeug | Operation | Tiefste Z-Koordinate | Fundstelle |
| :---: | :--- | :---: | :---: |
| `T01` | Außenkontur-Vorräumung, Schaftfräser Ø 10 mm | $-5{,}000\,\text{mm}$ | Zeile 10 |
| `T02` | 3D-Schlichten, Kugelfräser Ø 6 mm | **$-4{,}800\,\text{mm}$** *(Muldenmitte, Zeilen 40–41 bei $Y = 25\,\text{mm}$)* | Zeile 40 |

$$\Delta Z_{\text{Reserve, T02}} = \left|Z_{\text{Spannbacke}} - Z_{\text{min}}\right| = \left|(-15{,}000\,\text{mm}) - (-4{,}800\,\text{mm})\right| = 10{,}200\,\text{mm}$$

$$\Delta Z_{\text{Reserve, T01}} = \left|(-15{,}000\,\text{mm}) - (-5{,}000\,\text{mm})\right| = 10{,}000\,\text{mm}$$

**Restwandstärke unter der Mulde:** Das Fertigteil ist $12\,\text{mm}$ dick *(Unterseite bei $Z = -12\,\text{mm}$)*. Unter dem tiefsten Muldenpunkt bleiben also $12{,}0 - 4{,}8 = \mathbf{7{,}2\,\text{mm}}$ Material stehen — kein Durchbruch.

**Kugelspitze:** Beim Kugelfräser steht die *Spitze* auf $Z = -4{,}8\,\text{mm}$; der Kugelmittelpunkt liegt $R = 3{,}0\,\text{mm}$ höher bei $Z = -1{,}8\,\text{mm}$. Programmiert ist die Spitze, weil das CAM auf die Kugelspitze bezieht. Das ist konsistent mit `T02`-Länge an der Kugelspitze vermessen.

> [!IMPORTANT]
> **Annahme:** Die Spannbackenoberkante bei $Z = -15{,}000\,\text{mm}$ stammt aus Revision 1 bzw. dem Angebot und ist **nicht** in `KUNDENAUFTRAG.md` belegt. Der Bediener muss die tatsächliche Backenhöhe beim Einrichten messen. Liegt die Backe höher als $Z = -10{,}000\,\text{mm}$, schrumpft die Reserve unter die geforderten $5\,\text{mm}$.

---

## R2.3 Prüfung der Bahnverschleifung `G187 P3 E0.005`

| Prüfpunkt | Befund | Bewertung |
| :--- | :--- | :---: |
| **Syntax** *(Haas-Befehl `G187 Pn En`)* | Zeile 24: `G187 P3 E0.005` — `P3` = Genauigkeitsstufe *Finish* (`P1` Schruppen, `P2` Mittel, `P3` Schlichten), `E0.005` = max. Eckenverrundung $0{,}005\,\text{mm}$ *(in den Einheiten des Programms, hier mm wegen `G21`)*. | ✅ **OK** |
| **Position** | Steht erst **nach** Werkzeugwechsel `T02`, Drehzahl und `G54`, also vor der ersten 3D-Bewegung *(Zeile 25 `G00`)*. | ✅ **OK** |
| **Geltungsbereich** | Zwischen Zeile 24 und 57 verfährt nur der Kugelfräser. Das Schruppen mit `T01` *(Zeilen 4–16)* läuft **ohne** Glättung — gewollt, dort zählt Zeit, nicht Konturtreue. | ✅ **OK** |
| **Rücksetzen** | Zeile 57: `G187` ohne Parameter *(Maschinen-Standard)* **vor** `M09`/`M05`/`M30`. Das Folgeprogramm erbt keine Finish-Glättung. | ✅ **OK** |
| **Passung zur CAM-Toleranz** | `E0.005` = Sehnentoleranz `tolerance = spatial(0.005, MM)` der `.cps`. Die Steuerung rundet Ecken also nicht stärker als das CAM Sehnen bildet. | ✅ **OK** |
| **Steuerungs-Kompatibilität** | `G187` ist **Haas-spezifisch**. Bei Fanuc wäre `G05.1 Q1` bzw. `G05 P10000` nötig, bei Heidenhain `CYCL DEF 32`, bei Siemens `CYCLE832`. Kundenauftrag nennt „ISO/Haas-Highspeed-Modus". | 🟡 **Steuerung beim Kunden bestätigen** |

---

## R2.4 Verifizierte Werkzeug- und Schnittdaten-Matrix *(ersetzt die falsche Zeile aus Revision 1)*

| Werkzeug | Beschreibung | Operation | Drehzahl ($n$) | Vorschub ($v_f$) | $Z_{\text{min}}$ | Kühlung *(KSS)* | Status |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| `T01` | VHM-Schaftfräser *(Vollhartmetall)* Ø 10 mm | Außenkontur-Vorräumung | $S = 8000\,\text{U/min}$ | $F = 500$ *(Eintauchen)*, $1200\,\text{mm/min}$ | $-5{,}000\,\text{mm}$ | ❌ **kein `M08`** | 🟡 |
| `T02` | VHM-Kugelfräser Ø 6 mm, $R = 3{,}0\,\text{mm}$ | 3D-Zeilenschlichten, 5 Zeilen, $\Delta Y = 5\,\text{mm}$ | $S = 10000\,\text{U/min}$ | $F = 600$ *(Eintauchen)*, $1500\,\text{mm/min}$ | $-4{,}800\,\text{mm}$ | ❌ **kein `M08`** | 🟡 |

**Schnittgeschwindigkeit** $v_c = \dfrac{\pi \cdot d \cdot n}{1000}$:
* `T01`: $\dfrac{\pi \cdot 10 \cdot 8000}{1000} \approx 251\,\text{m/min}$ *(für Aluminium EN AW-7075 üblich: 200–500 m/min — plausibel)*.
* `T02`: $\dfrac{\pi \cdot 6 \cdot 10000}{1000} \approx 188\,\text{m/min}$ am vollen Durchmesser. An der Kugelspitze selbst geht $v_c \to 0$ *(siehe Handbuch-Tipp zu Übung 13)* — deshalb wird die Mulde mit der Kugelflanke geschlichtet und die Drehzahl hoch gewählt.

---

## R2.5 Offene Punkte vor der Freigabe zum Einfahren

| Nr. | Schwere | Befund | Empfohlene Korrektur |
| :---: | :---: | :--- | :--- |
| **1** | 🔴 **Hoch** | **Keine Werkzeuglängenkompensation** (`G43 H01` / `G43 H02`). Ohne sie rechnet die Steuerung nicht mit der Länge des eingewechselten Werkzeugs. Z0 des Werkstücks passt dann nur zufällig; ein Fräser, der länger ist als der Referenzwert, fährt tiefer als programmiert. Kollisionsgefahr bei `Z-5` / `Z-4.8`. | In `onSection()` nach `G54`: `G43 H` + Werkzeugnummer + `Z2.000` ausgeben; im Startblock `G49` ergänzen. |
| **2** | 🟡 **Mittel** | **Kein `M08`.** Das Programm schaltet die Kühlung nie ein, schaltet sie aber am Ende ab *(`M09`)*. Aluminium schmiert ohne KSS an den Schneiden an; bei $Z-5$ im Vollschnitt mit Ø 10 mm entsteht Spanstau. | In `onSection()` nach `G54`/`G43`: `M08` ausgeben *(oder bewusst Druckluft `M07` / Trockenbearbeitung mit Kunde festlegen)*. |
| **3** | 🟡 **Mittel** | **Außenkontur `T01`** fährt mit der **Werkzeugmitte** auf der Fertigteilkante *(Zeilen 11–15, $X0\ldots80$, $Y0\ldots50$)*, ohne Radiuskorrektur und ohne Versatz. Bei Ø 10 mm schneidet der Fräser damit $R = 5\,\text{mm}$ in das Fertigteil hinein. Das Rohteil ist $85 \times 55\,\text{mm}$ — es stehen nur $2{,}5\,\text{mm}$ Aufmaß je Seite. **Folge: Fertigteil wird zu klein.** | Entweder Bahn um $R = 5\,\text{mm}$ nach außen versetzen *(CAM: „Außen")* oder `G41 D01` ergänzen *(siehe Übung 12)*, oder bewusst als reines Vorräumen mit Schlichtaufmaß dokumentieren. |
| **4** | 🟢 **Niedrig** | Kein `Z-MIN`-Kommentar im Programmkopf. Skill-Vorgabe: Header-Wert soll mit tiefstem Z übereinstimmen. | In `onOpen()` Zeile `(Z-MIN=-5.000MM)` ausgeben *(aus `getGlobalZRange()`)*. |

---

## R2.6 Formale Freigabeentscheidung Revision 2

* **Z-MIN-Kollision:** 🟢 **freigegeben** — Reserve $10{,}2\,\text{mm}$, unter Vorbehalt der gemessenen Backenhöhe.
* **`G187`-Bahnverschleifung:** 🟢 **freigegeben** — unter Vorbehalt der Steuerung beim Kunden.
* **Gesamtstatus:** 🟡 **NICHT zum Einfahren freigegeben**, bis Punkt 1 *(`G43`)* behoben ist. Punkte 2 und 3 sind vor dem ersten Bauteil zu klären. Danach ist Revision 3 zu erstellen.

**Hinweis zur Maschinenfreigabe:** Auch nach Korrektur gilt: erstes Teil im Einzelsatzbetrieb *(Single Block)* mit Vorschubpoti auf 25 %, Werkzeuglängen im Speicher gegenprüfen, Z-Achse vor der ersten Mulden-Zeile mit Abstand $> 2\,\text{mm}$ antasten.


---
---

# 🛡️ REVISION 3 — Nachprüfung nach Korrektur des Postprozessors *(Stand 27.10.2026)*

> **Anlass:** Revision 2 hat drei Mängel gefunden *(fehlende Werkzeuglängenkorrektur, fehlende Kühlung, Konturbahn ohne Fräserradius-Versatz)*. Der Postprozessor [`uebung_13_3d_freiformflaechen.cps`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_13_3d_freiformflaeche_alu/uebung_13_3d_freiformflaechen.cps) wurde korrigiert, das Programm [`uebung_13_3d_freiformflaechen.nc`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_13_3d_freiformflaeche_alu/uebung_13_3d_freiformflaechen.nc) neu erzeugt *(jetzt 65 Zeilen, davon 61 aktive Sätze, jede Zeile kommentiert)*. Revision 1 und 2 bleiben als Historie stehen. **Maßgeblich ist ab hier Revision 3.**

* **Prüfingenieur:** 🛡️ **Agent 3 – NC-Safety- & Setup-Agent** *(i. A. Dipl.-Ing. (FH) Alexander Bujanovski)*
* **Prüfverfahren:** Statische Analyse mit [`audit_u13.py`](file:///c:/Projekte/CNC/scratch/audit_u13.py) und [`verify_u13.py`](file:///c:/Projekte/CNC/scratch/verify_u13.py). Gegenprobe: frisch aus der `.cps` erzeugter Code = kommentierte `.nc` = Simulator-Preset = Handbuch *(alle 61 aktiven Sätze identisch)*.
* **Prüfstatus Revision 3:** 🟢 **BESTANDEN (GRÜN) mit Auflagen für den Bediener *(siehe R3.4)* — Freigabe zum Einfahren im Einzelsatzbetrieb.**

---

## R3.1 Abarbeitung der Befunde aus Revision 2

| Nr. | Befund Rev. 2 | Korrektur | Fundstelle im neuen Programm | Status |
| :---: | :--- | :--- | :--- | :---: |
| **1** 🔴 | Keine Werkzeuglängenkorrektur | `G00 G43 H01 Z15.000` nach `T01`, `G00 G43 H02 Z15.000` nach `T02` *(Register `H` = Werkzeugnummer, Eilgang auf sichere Höhe $Z+15\,\text{mm}$ vor jeder Bewegung ins Material)*; `G49` im Startblock | Zeilen **3**, **9**, **26** | ✅ **behoben** |
| **2** 🟡 | Kein `M08` | `M08` direkt nach der ersten Längenkorrektur, **vor** dem ersten Spankontakt | Zeile **10** *(erster Schnitt Zeile 12)* | ✅ **behoben** |
| **3** 🟡 | Außenkontur mit Werkzeugmitte auf der Bauteilkante | Bahn um den Fräserradius $R = 5\,\text{mm}$ nach außen versetzt: $X-5 \ldots 85$, $Y-5 \ldots 55$ | Zeilen **13–17** | ✅ **behoben** |
| **4** 🟢 | Kein Z-MIN-Kommentar im Kopf | nicht umgesetzt *(rein informativ)* | — | ⚪ **offen, unkritisch** |

---

## R3.2 Erneute 6-Punkte-Prüfung

| Stufe | Prüfkriterium | Befund im aktuellen Code | Bewertung |
| :---: | :--- | :--- | :---: |
| **1** | Sicherheits-Startblock | Zeile 3: `G90 G21 G17 G40 G49 G80` — jetzt vollständig inkl. `G49` | ✅ **OK** |
| **2** | Werkstücknullpunkt | `G54` in Zeile 8 und Zeile 25, jeweils vor der ersten Bewegung | ✅ **OK** |
| **3** | Werkzeuglängenkompensation | `G43 H01` *(Zeile 9)* und `G43 H02` *(Zeile 26)* **vor** der ersten Z-Zustellung auf $Z-5$ bzw. $Z-2$. `T01 → H01`, `T02 → H02` stimmig. | ✅ **OK** |
| **4** | Z-MIN gegen Spannmittel | Siehe R3.3 | ✅ **OK** |
| **5** | Kühlmittel & Schnittdaten | `M08` Zeile 10 vor erstem Schnitt *(Zeile 12)*; `S8000 M03` / `S10000 M03` plausibel; `M09` Zeile 61 | ✅ **OK** |
| **6** | Sicherer Rückzug am Ende | Zeilen 59–64: `G00 Z15.000`, `G187`, `M09`, `G53 G00 Z0.0`, `M05`, `M30` | ✅ **OK** |

**Zusätzlicher Eilgang-Check:** Kein `G00`-Satz mit X/Y-Bewegung unterhalb $Z = +2\,\text{mm}$. Der Rückzug nach der Kontur erfolgt senkrecht *(`G00 Z15.000`, Zeile 18)* auf der Ecke $X-5\ Y-5$ — **nicht** diagonal über die Bauteilecke. Dieser Fehler wäre beim Konturversatz beinahe entstanden und wurde vor der Freigabe korrigiert.

---

## R3.3 Z-MIN-Nachweis *(neue Zeilennummern)*

| Werkzeug | Tiefste Z-Koordinate | Fundstelle | Reserve zur Spannbacke $Z = -15{,}000\,\text{mm}$ |
| :---: | :---: | :---: | :---: |
| `T01` Schaftfräser Ø 10 mm | $-5{,}000\,\text{mm}$ | Zeile 12 | $\left|-15{,}000 - (-5{,}000)\right| = 10{,}000\,\text{mm}$ |
| `T02` Kugelfräser Ø 6 mm | $-4{,}800\,\text{mm}$ | Zeile 43 | $\left|-15{,}000 - (-4{,}800)\right| = 10{,}200\,\text{mm}$ |

* **Restwandstärke unter der Mulde:** $12{,}0 - 4{,}8 = 7{,}2\,\text{mm}$ — kein Durchbruch.
* **3D-Sätze mit gleichzeitiger X/Z-Bewegung:** Zeilen **30 bis 58** *(fünf Schlichtzeilen im Abstand $\Delta Y = 5\,\text{mm}$)*.
* **`G187 P3 E0.005`:** Zeile 27 *(nach `G43 H02`, vor der ersten 3D-Bewegung)*, zurückgesetzt in Zeile 60 *(vor `M09`)* — unverändert gültig gegenüber R2.3.

---

## R3.4 Auflagen und Hinweise für den Bediener *(vor dem ersten Teil)*

1. **Backenhöhe messen:** Die Annahme „Spannbackenoberkante bei $Z = -15\,\text{mm}$" ist nicht belegt. Liegt die Backe höher als $Z = -10\,\text{mm}$, unterschreitet die Reserve $5\,\text{mm}$.
2. **Längenregister prüfen:** `H01` = Länge `T01`, `H02` = Länge `T02` *(Kugelfräser **bis zur Kugelspitze** messen!)*. Falsche Werte im Register sind jetzt die einzige Crash-Quelle in Z — die Steuerung vertraut dem Wert ungeprüft.
3. **Außenkontur ist nur Vorräumen:** Die Bahn fährt bis $Z-5\,\text{mm}$, das Fertigteil ist $12\,\text{mm}$ dick *(Unterseite bei $Z = -12$)*. Die Kontur ist also **nicht** fertig gefräst; weitere Zustellungen bis $Z-12$ sind nicht Teil dieses Programms *(Umfang laut Angebot: Postprozessor-Optimierung für 3D-Freiformflächen)*.
4. **Steuerung klären:** `G187` ist Haas-spezifisch. Bei Fanuc `G05.1 Q1`, Heidenhain `CYCL DEF 32`, Siemens `CYCLE832`. Vor Lieferung beim Kunden bestätigen.
5. **Einfahren:** Einzelsatzbetrieb *(Single Block)*, Vorschubpoti auf 25 %, vor der ersten Mulden-Zeile *(Zeile 29, `G01 Z-2.000`)* mit Abstand $> 2\,\text{mm}$ anhalten und Position prüfen.

---

## R3.5 Formale Freigabe Revision 3

* **Z-MIN-Kollision:** 🟢 freigegeben *(Reserve $10{,}0$ bzw. $10{,}2\,\text{mm}$, unter Vorbehalt der gemessenen Backenhöhe)*.
* **Werkzeuglängenkorrektur:** 🟢 freigegeben.
* **Kühlung:** 🟢 freigegeben.
* **Bahnverschleifung `G187`:** 🟢 freigegeben *(unter Vorbehalt der Kundensteuerung)*.
* **Gesamtstatus:** 🟢 **FREIGABE FÜR EINFAHRBETRIEB — unter den Auflagen R3.4.**

# 📋 Workflow-Beschreibung & Prompts zur Erledigung des Auftrags

Mit dieser Anleitung kannst du den Kundenauftrag aus [`KUNDENAUFTRAG.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/test_auftrag_ubung_03/KUNDENAUFTRAG.md) Schritt für Schritt mithilfe deiner 4 KI-Agenten bearbeiten.

Kopiere einfach nacheinander die folgenden **4 Prompts** in unseren Chat. Die Agenten erzeugen dann alle geforderten Artefakte direkt in diesem Ordner [`c:\Projekte\CNC\01_Kundenauftraege\test_auftrag_ubung_03\`](file:///c:/Projekte/CNC/01_Kundenauftraege/test_auftrag_ubung_03).

---

## 🗂️ 1. Welche Artefakte werden erzeugt und wo genau stehen sie?

Sobald du die Agenten beauftragst, entstehen direkt in diesem Ordner die folgenden **6 zentralen Ergebnis-Artefakte *(Ergebnis-Dokumente, Maschinencode & 3D-Video)***:

| Artefakt-Dateiname | Was ist das? | Wo steht die Datei? *(Speicherort)* | Wer erzeugt sie? |
| :--- | :--- | :--- | :---: |
| **`02_ANGEBOT_DIPL_ING_BUENOTTE.md`** | Rechtssicheres B2B-Ingenieurangebot *(Festpreis 480 € netto)* | [`c:\Projekte\CNC\01_Kundenauftraege\test_auftrag_ubung_03\02_ANGEBOT_DIPL_ING_BUENOTTE.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/test_auftrag_ubung_03/02_ANGEBOT_DIPL_ING_BUENOTTE.md) | **Agent 4** *(Backoffice)* |
| **`uebung_03_z_min_berechnung.nc`** | Fertiger Maschinencode für Haas VF-2 *(mit Z-MIN Header)* | [`c:\Projekte\CNC\01_Kundenauftraege\test_auftrag_ubung_03\uebung_03_z_min_berechnung.nc`](file:///c:/Projekte/CNC/01_Kundenauftraege/test_auftrag_ubung_03/uebung_03_z_min_berechnung.nc) | **Agent 2** *(Post-Coder)* |
| **`05_SICHERHEITS_CRASH_PRUEFBERICHT.md`** | 5-Stufen-Sicherheitsprüfbericht *(Null-Kollisions-Garantie)* | [`c:\Projekte\CNC\01_Kundenauftraege\test_auftrag_ubung_03\05_SICHERHEITS_CRASH_PRUEFBERICHT.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/test_auftrag_ubung_03/05_SICHERHEITS_CRASH_PRUEFBERICHT.md) | **Agent 3** *(NC-Safety)* |
| **`06_EINRICHTEBLATT_SETUP_SHEET.md`** | Werkstatt-Rüstdatenblatt für den Maschinenbediener vor Ort | [`c:\Projekte\CNC\01_Kundenauftraege\test_auftrag_ubung_03\06_EINRICHTEBLATT_SETUP_SHEET.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/test_auftrag_ubung_03/06_EINRICHTEBLATT_SETUP_SHEET.md) | **Agent 3** *(NC-Safety)* |
| **`uebung_03_simulation_video.mp4`** | **3D-Maschinensimulationsvideo *(MP4 zur Kundenfreigabe)*** | [`c:\Projekte\CNC\01_Kundenauftraege\test_auftrag_ubung_03\uebung_03_simulation_video.mp4`](file:///c:/Projekte/CNC/01_Kundenauftraege/test_auftrag_ubung_03/uebung_03_simulation_video.mp4) | **Agent 3** *(NC-Safety)* |
| **`07_RECHNUNG_NACH_PARAGRAPH_18_ESTG.md`** | Revisionssichere Honorarrechnung *(nach § 14 UStG & § 18 EStG)* | [`c:\Projekte\CNC\01_Kundenauftraege\test_auftrag_ubung_03\07_RECHNUNG_NACH_PARAGRAPH_18_ESTG.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/test_auftrag_ubung_03/07_RECHNUNG_NACH_PARAGRAPH_18_ESTG.md) | **Agent 4** *(Backoffice)* |

---

## 🧭 2. Der 4-Stufen-Workflow im Überblick:

```
                  1. KUNDENAUFTRAG.md (Liegt bereits im Ordner)
                             │
                             ▼
 ┌────────────────────────────────────────────────────────────────────────┐
 │ SCHRITT 1: ANGEBOT ERSTELLEN (Agent 4: Backoffice-Agent)              │
 │ Prompt 1 ausführen ──► Erzeugt: 02_ANGEBOT_DIPL_ING_BUENOTTE.md        │
 └───────────────────────────┬────────────────────────────────────────────┘
                             │
                             ▼
 ┌────────────────────────────────────────────────────────────────────────┐
 │ SCHRITT 2: NC-MASCHINENCODE GENERIEREN (Agent 2: Postprocessor-Coder)  │
 │ Prompt 2 ausführen ──► Erzeugt: uebung_03_z_min_berechnung.nc          │
 └───────────────────────────┬────────────────────────────────────────────┘
                             │
                             ▼
 ┌────────────────────────────────────────────────────────────────────────┐
 │ SCHRITT 3: SICHERHEIT, EINRICHTEBLATT & 3D-VIDEO (Agent 3: Safety)     │
 │ Prompt 3 ausführen ──► Erzeugt: 05_SICHERHEITS_CRASH_PRUEFBERICHT.md   │
 │                    ──► Erzeugt: 06_EINRICHTEBLATT_SETUP_SHEET.md       │
 │                    ──► Erzeugt: uebung_03_simulation_video.mp4 🎬       │
 └───────────────────────────┬────────────────────────────────────────────┘
                             │
                             ▼
 ┌────────────────────────────────────────────────────────────────────────┐
 │ SCHRITT 4: RECHNUNG STELLEN (Agent 4: Backoffice-Agent)                │
 │ Prompt 4 ausführen ──► Erzeugt: 07_RECHNUNG_NACH_PARAGRAPH_18_ESTG.md  │
 └────────────────────────────────────────────────────────────────────────┘
```

---

## 💬 3. Die 4 fertigen Prompts & wie du jedes Artefakt testest:

### 🟢 SCHRITT 1: Angebot erstellen (Agent 4)

#### Prompt zum Kopieren in den Chat:
```text
Starte bitte Agent 4 (Backoffice-Agent):
Lies die Kundenanfrage in c:\Projekte\CNC\01_Kundenauftraege\test_auftrag_ubung_03\KUNDENAUFTRAG.md.
Erstelle direkt im Ordner c:\Projekte\CNC\01_Kundenauftraege\test_auftrag_ubung_03\ das formelle B2B-Angebot "02_ANGEBOT_DIPL_ING_BUENOTTE.md" für Markus Weber (Schmidt Präzisionstechnik GmbH) über 480,00 € netto. Verwende ausschließlich ingenieurmäßige Leistungsbeschreibungen nach § 18 EStG und binde die verbindliche Haftungsausschluss-Klausel für das Einfahren des ersten Werkstücks im Einzelsatz ein.
```

#### 🔍 Wie wird das Angebot getestet und geprüft?
Öffne nach Erstellung die Datei `02_ANGEBOT_DIPL_ING_BUENOTTE.md` und prüfe folgende **3 Kriterien**:
1. **Honorar-Prüfung:** Steht dort exakt der Festpreis von **`480,00 € netto`** *(zzgl. 19 % USt.)*?
2. **Freiberufler-Prüfung:** Werden Begriffe wie *„Ingenieurtechnische CAD/CAM-Prozessauslegung“* verwendet *(Finanzamtssicher nach § 18 EStG, keine gewerbliche Einstufung als Lohnfertiger)*?
3. **Haftungsausschluss-Check:** Ist die Klausel enthalten, dass das erste Werkstück vom qualifizierten Personal des Kunden im Einzelsatz *(Single Block)* an der Haas VF-2 eingefahren werden muss?

---

### 🔵 SCHRITT 2: NC-Maschinencode mit Z-MIN Berechnung erstellen (Agent 2)

#### Prompt zum Kopieren in den Chat:
```text
Starte bitte Agent 2 (Postprocessor-Coder-Agent):
Generiere für die Haas VF-2 Fräsmaschine im Ordner c:\Projekte\CNC\01_Kundenauftraege\test_auftrag_ubung_03\ das fertige NC-Programm "uebung_03_z_min_berechnung.nc" für die Flanschplatte aus dem 3D-Modell bauteil_1001.stl.
Integriere im Header die exakte Z-MIN Tiefenberechnung für Werkzeug T01 (Außenkontur Z -5.0 mm, Kreistasche Z -3.0 mm) und den Nullpunkt G54 vorne links oben, damit der Maschinenbediener vor Crashs mit den Schraubstockbacken gewarnt wird.
```

#### 🔍 Wie wird der generierte NC-Code getestet und geprüft?
Es stehen dir **3 Test-Methoden** zur Verfügung:

1. **Visuelle Code-Prüfung (im Text-Editor):**
   * Öffne `uebung_03_z_min_berechnung.nc`.
   * Suche im Programmkopf nach dem Werkzeugaufruf von T01. Steht dort die Sicherheitszeile:
     `(T01 ... Z-MIN: -5.000 MM ...)`?
   * Steht in Zeile 5 der vollständige Steuerungs-Reset: `G90 G17 G21 G94 G40 G49 G80`?

2. **3D-Backplot-Simulation im Web-Simulator (NCViewer):**
   * Kopiere den gesamten Inhalt von `uebung_03_z_min_berechnung.nc`.
   * Öffne im Browser [https://ncviewer.com](https://ncviewer.com).
   * Füge den G-Code links ein und klicke auf **„Plot“** bzw. **„Play“**.
   * **Sichtprüfung:** Das Werkzeug muss zuerst die Außenstufe bei $Z = -5{,}0\,\text{mm}$ abfahren, danach im Eilgang auf $Z = +15{,}0\,\text{mm}$ in die Luft abheben, in die Mitte fahren und die Kreistasche bei $Z = -3{,}0\,\text{mm}$ ausfräsen.

3. **Interaktiver 3D-Simulator:**
   * Öffne die Datei [`c:\Projekte\CNC\01_Kundenauftraege\referenz_auftrag_flanschplatte\3d_auftrag_simulator.html`](file:///c:/Projekte/CNC/01_Kundenauftraege/referenz_auftrag_flanschplatte/3d_auftrag_simulator.html) per Doppelklick im Webbrowser *(Chrome oder Edge)*.
   * Wähle das Preset **„Übung 3: Flanschplatte Z-MIN“** und prüfe die kollisionsfreie Werkzeugbahn direkt im interaktiven 3D-Modell.

---

### 🛡️ SCHRITT 3: Sicherheitsbericht, Einrichteblatt & 3D-Video erstellen (Agent 3)

#### Prompt zum Kopieren in den Chat:
```text
Starte bitte Agent 3 (NC-Safety- & Setup-Agent):
Führe für die Datei "uebung_03_z_min_berechnung.nc" im Ordner c:\Projekte\CNC\01_Kundenauftraege\test_auftrag_ubung_03\ die 5-Stufen-Sicherheitsprüfung nach SICHERHEITS_UND_QUALITAETS_PRUEFLISTE_GCODE.md durch.
Prüfe insbesondere den Z-MIN Abstand von Z = -5.0 mm zu den Schraubstockbacken bei Z = -12.0 mm (Spannrand 3.0 mm).
Erstelle im selben Ordner:
1. "05_SICHERHEITS_CRASH_PRUEFBERICHT.md" mit Freigabestatus BESTANDEN.
2. "06_EINRICHTEBLATT_SETUP_SHEET.md" als druckfertiges Rüstblatt für den Werkstattbediener inklusive Werkzeugliste und Nullpunkt G54.
3. Rendere das 3D-Simulationsvideo "uebung_03_simulation_video.mp4" für die Kundenfreigabe mit unserem Python-Tool c:\Projekte\CNC\02_Software_und_Tools\scripts\render_simulation_video.py.
```

#### 🔍 Wie werden Sicherheitsbericht, Einrichteblatt & 3D-Video getestet?

1. **Prüfung von `05_SICHERHEITS_CRASH_PRUEFBERICHT.md`:**
   * Steht der Gesamtstatus auf **BESTANDEN (GRÜN)**?
   * Ist die rechnerische Sicherheitsreserve zu den Schraubstockbacken ausgewiesen?
     $$\text{Sicherheitsabstand} = Z_{\text{Backen}} - Z_{\text{min}} = (-12{,}0\,\text{mm}) - (-5{,}0\,\text{mm}) = \mathbf{+7{,}0\,\text{mm Puffer}}$$
2. **Prüfung von `06_EINRICHTEBLATT_SETUP_SHEET.md`:**
   * Sind die Werkzeuge `T01` (Schaftfräser $\varnothing 10\,\text{mm}$, $S=3800$, $F=1200$) und `T02` (Spiralbohrer $\varnothing 6\,\text{mm}$) vollständig mit Mindest-Auskraglängen aufgeführt?
   * Ist der Werkstücknullpunkt `G54` unmissverständlich auf **„Vorne links oben“** definiert?

3. **🎬 Prüfung des 3D-Simulationsvideos (`uebung_03_simulation_video.mp4`):**
   * **Wie anschauen?** Öffne die Datei `uebung_03_simulation_video.mp4` per Doppelklick in deinem Video-Player *(z. B. Windows Media Player, VLC)* oder ziehe sie direkt in ein Browserfenster von Google Chrome / Edge.
   * **Was wird im Video geprüft?**
     - **Frame 1–60:** Der Fräser T01 schwebt sicher auf Referenzhöhe $Z = +15\,\text{mm}$ über dem Rohteil.
     - **Frame 60–180:** Der Fräser taucht sanft im Vorschub ein und fräst die Außenstufe bei $Z = -5{,}0\,\text{mm}$.
     - **Frame 180–300:** Der Fräser hebt auf $Z = +15\,\text{mm}$ im Eilgang ab, fährt ins Zentrum und fräst die Kreistasche bei $Z = -3{,}0\,\text{mm}$.
     - **Schraubstock-Kontrolle:** Unten im Video siehst du die Schraubstockbacken *(rot schraffierte Gefahrenzone)* – der Fräser bleibt zu jeder Sekunde **mindestens $7\,\text{mm}$ weit über den Backen**.
   * **Kundennutzen:** Dieses Video sendest du per E-Mail oder Cloud-Link an Markus Weber. Er sieht in 15 Sekunden auf seinem Smartphone oder PC, dass der Code absolut crashfrei ist, bevor er an die echte 150.000-Euro-Maschine geht!

---

### 💰 SCHRITT 4: Rechnungsstellung nach § 18 EStG (Agent 4)

#### Prompt zum Kopieren in den Chat:
```text
Starte bitte Agent 4 (Backoffice-Agent):
Der Auftrag im Ordner c:\Projekte\CNC\01_Kundenauftraege\test_auftrag_ubung_03\ ist technisch erfolgreich abgeschlossen.
Erstelle jetzt im selben Ordner die steuersichere Honorarrechnung "07_RECHNUNG_NACH_PARAGRAPH_18_ESTG.md" über 480,00 € netto (571,20 € brutto) an die Schmidt Präzisionstechnik GmbH mit allen Pflichtangaben nach § 14 UStG und freiberuflicher Leistungsabgrenzung für das Finanzamt Hanau.
```

#### 🔍 Wie wird die Rechnung getestet und geprüft?
Öffne `07_RECHNUNG_NACH_PARAGRAPH_18_ESTG.md` und prüfe die **steuerlichen Pflichtangaben nach § 14 UStG**:
1. **Adressen:** Vollständige Firmenanschrift der Schmidt Präzisionstechnik GmbH und deines Ingenieurbüros *(Erlensee)*.
2. **Rechnungsbetrag:** Netto-Honorar $480{,}00\,\text{€} + 19\,\%\text{ USt. } (91{,}20\,\text{€}) = \mathbf{571{,}20\,\text{€ Brutto}}$.
3. **Freiberufler-Status:** Klare Benennung von **§ 18 Abs. 1 Nr. 1 EStG** zur steuerlichen Anerkennung durch das **Finanzamt Hanau**.
4. **Zahlungsziel & Bankverbindung:** 14 Tage Zahlungsziel ohne Abzug.

---

## 🛡️ 4. Abnahme-Kriterien (Checkliste für 100 % Erledigung)

Sobald du die 4 Prompts ausgeführt hast, befinden sich alle Artefakte in deinem Test-Ordner:
* [ ] [`02_ANGEBOT_DIPL_ING_BUENOTTE.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/test_auftrag_ubung_03/02_ANGEBOT_DIPL_ING_BUENOTTE.md) existiert und wurde geprüft.
* [ ] [`uebung_03_z_min_berechnung.nc`](file:///c:/Projekte/CNC/01_Kundenauftraege/test_auftrag_ubung_03/uebung_03_z_min_berechnung.nc) existiert mit Z-MIN Header und lief im Simulator.
* [ ] [`05_SICHERHEITS_CRASH_PRUEFBERICHT.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/test_auftrag_ubung_03/05_SICHERHEITS_CRASH_PRUEFBERICHT.md) bescheinigt Status **BESTANDEN (GRÜN)**.
* [ ] [`06_EINRICHTEBLATT_SETUP_SHEET.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/test_auftrag_ubung_03/06_EINRICHTEBLATT_SETUP_SHEET.md) liegt druckfertig vor.
* [ ] [`uebung_03_simulation_video.mp4`](file:///c:/Projekte/CNC/01_Kundenauftraege/test_auftrag_ubung_03/uebung_03_simulation_video.mp4) wurde gerendert und zeigt kollisionsfreie Fräsbahnen.
* [ ] [`07_RECHNUNG_NACH_PARAGRAPH_18_ESTG.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/test_auftrag_ubung_03/07_RECHNUNG_NACH_PARAGRAPH_18_ESTG.md) ist für das Finanzamt Hanau abgelegt.

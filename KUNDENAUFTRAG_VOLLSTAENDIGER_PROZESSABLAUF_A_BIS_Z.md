# 🗺️ Master-Leitfaden: Vollständiger Prozessablauf für jeden Kundenauftrag (Von A bis Z)

Dieses Dokument ist Ihre **zentrale Arbeitsanleitung**. Es beschreibt Schritt für Schritt den exakten, lückenlosen Ablauf, wie Sie als freiberuflicher CAM-Ingenieur einen Kundenauftrag bearbeiten – vom ersten E-Mail-Kontakt über die Software-Tools bis zum Geldeingang auf Ihrem Bankkonto.

---

## 🧭 Übersicht: Wo sind unsere neuen Tools im Projekt dokumentiert?

Falls Sie nach bestimmten Funktionen suchen, finden Sie diese an folgenden Stellen:

| Tool / Thema | Datei auf Ihrer Festplatte | Wo im Handbuch beschrieben? |
|:---|:---|:---|
| **Web-Postprozessor-Generator** | [`kunden_cps_generator_web.html`](file:///C:/Projekte/CNC/kunden_cps_generator_web.html) | [`ANLEITUNG_CPS_GENERATOR_UND_WEB_INTERFACE.md`](file:///C:/Projekte/CNC/ANLEITUNG_CPS_GENERATOR_UND_WEB_INTERFACE.md) & [`ALLE_UEBUNGEN_HANDBUCH.md#L2370`](file:///C:/Projekte/CNC/ALLE_UEBUNGEN_HANDBUCH.md#L2370) |
| **Web-Video-Generator (3D-Freigabe)** | [`cnc_video_generator_web.html`](file:///C:/Projekte/CNC/cnc_video_generator_web.html) | [`ALLE_UEBUNGEN_HANDBUCH.md#L2256`](file:///C:/Projekte/CNC/ALLE_UEBUNGEN_HANDBUCH.md#L2256) (Abschnitt 13) |
| **Fertiges MP4-Video zu Übung 3** | [`docs/videos/uebung_03_simulation_video.mp4`](file:///c:/Projekte/CNC/docs/videos/uebung_03_simulation_video.mp4) | Handbuch Übung 3 / Abschnitt 13 |
| **Klick-Anleitung 3D-Modell Fusion 360** | [`kundenauftrag_01_flanschplatte/KUNDEN_AUFTRAG_UND_KLICK_ANLEITUNG.md`](file:///C:/Projekte/CNC/kundenauftrag_01_flanschplatte/KUNDEN_AUFTRAG_UND_KLICK_ANLEITUNG.md) | Handbuch Übung 4 |
| **3D-Simulator mit Satz-Editor** | [`kundenauftrag_01_flanschplatte/3d_auftrag_simulator.html`](file:///c:/Projekte/CNC/kundenauftrag_01_flanschplatte/3d_auftrag_simulator.html) | Handbuch Übung 00b & Übung 5 |
| **Sicherheits- & Qualitätsprüfliste** | [`SICHERHEITS_UND_QUALITAETS_PRUEFLISTE_GCODE.md`](file:///c:/Projekte/CNC/SICHERHEITS_UND_QUALITAETS_PRUEFLISTE_GCODE.md) | Begleitendes Prüfhandbuch Phase 1 bis 5 |

---

## 🔄 Die 7 Phasen eines Kundenauftrags (Der vollständige Workflow)

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ DER 7-PHASEN-PRAXISABLAUF VOM BRIEFING BIS ZUR ENDZAHLUNG                              │
└────────────────────────────────────────────────────────────────────────────────────────┘
  PHASE 1: Kunden-E-Mail & Angebot (50 % Anzahlung anfordern)
      │
      ▼
  PHASE 2: Passenden Postprozessor wählen oder in 30 Sek. generieren (kunden_cps_generator_web.html)
      │
      ▼
  PHASE 3: 3D-CAM-Strategie in Autodesk Fusion 360 programmieren (Setup, Kontur, Tasche, Bohren)
      │
      ▼
  PHASE 4: Maschinencode (G-Code .NC) über den Postprozessor exportieren
      │
      ▼
  PHASE 5: 3D-Simulations-Video aufnehmen (cnc_video_generator_web.html)
      │
      ▼
  PHASE 6: Video an Kunden senden -> Vorab-Freigabe & 2. Teilzahlung (Restliche 50 %)
      │
      ▼
  PHASE 7: Auslieferung der finalen .NC-Datei & des Einrichteblatts (PDF)
```

---

### 📩 Phase 1: Die Kundenanfrage & das Angebot (10 Minuten)

1. **Die Kunden-E-Mail trifft ein:**  
   Der Kunde *(z. B. eine Fräserei)* schickt Ihnen:
   * Die 3D-CAD-Datei *(z. B. `bauteil.step` oder `flanschplatte.stl`)*.
   * Die Maschinenangabe *(z. B. „Haas VF-2“ oder „Hermle mit Heidenhain TNC 640“)*.
   * Die Stückzahl und das Material *(z. B. Aluminium EN AW-6082)*.
2. **Angebot schreiben:**  
   Sie öffnen unsere Vorlage [`Vorlagen_Vertraege_Rechnungen/Vorlage_Angebot_und_Rechnung_Ingenieurbuero.md`](file:///c:/Projekte/CNC/Vorlagen_Vertraege_Rechnungen/Vorlage_Angebot_und_Rechnung_Ingenieurbuero.md).
   * Typischer Preis: **180 € bis 350 €** für ein 3-Achs-Bauteil.
   * **Die goldene Zahlungsbedingung im Angebot:**  
     *„50 % Anzahlung bei Auftragserteilung. Restliche 50 % nach Vorlage des 3D-Simulations-Freigabevideos vor Code-Übergabe.“*
3. **Anzahlung abwarten:**  
   Sobald die 50 % Anzahlung eingegangen sind, starten Sie mit der Bearbeitung!

---

### ⚙️ Phase 2: Postprozessor vorbereiten (1 Minute)

Frage: Hat der Kunde eine Haas-, Siemens-, Fanuc- oder Heidenhain-Maschine?

1. Öffnen Sie per Doppelklick:  
   👉 [`kunden_cps_generator_web.html`](file:///C:/Projekte/CNC/kunden_cps_generator_web.html)
2. Tragen Sie den Kundennamen ein.
3. Klicken Sie auf die passende Maschinen-Kachel *(z. B. 🟡 Haas oder 🔵 Siemens)*.
4. Prüfen Sie, ob **`Z-MIN Tiefenprüfung`** und **`Tisch zur Tür fahren`** angehakt sind.
5. Klicken Sie auf **„📥 .cps-Datei herunterladen“**.
6. Sie haben nun Ihre maßgeschneiderte Postprozessor-Datei *(z. B. `schmidt_haas.cps`)* auf Ihrem Laptop!

---

### 🖱️ Phase 3: 3D-Modell im CAM programmieren (15–20 Minuten)

*(Die vollständige Klick-für-Klick-Anleitung finden Sie in [`kundenauftrag_01_flanschplatte/KUNDEN_AUFTRAG_UND_KLICK_ANLEITUNG.md`](file:///C:/Projekte/CNC/kundenauftrag_01_flanschplatte/KUNDEN_AUFTRAG_UND_KLICK_ANLEITUNG.md)).*

1. **3D-Modell in Autodesk Fusion 360 öffnen:**  
   `Datei` $\rightarrow$ `Öffnen` $\rightarrow$ Bauteildatei auswählen. Oben links auf **`Fertigen (Manufacture)`** umschalten.
2. **Setup anlegen:**  
   Nullpunkt `G54` auf die **vordere linke obere Bauteilecke** legen. Rohteilaufmaß eingeben *(z. B. seitlich $+2{,}5\,\text{mm}$)*.
3. **Fräsoperationen anklicken:**  
   * **Planfräsen / Face:** Oberseite schlichten.
   * **2D-Kontur:** Außenkanten mit Schaftfräser $\varnothing 10\,\text{mm}$ umfahren *(Lead-In aktiviert)*.
   * **2D-Tasche:** Innentaschen ausräumen.
   * **Bohren:** Bohrungen mit Tiefbohrzyklus `G83` anlegen.
4. **Interne Fusion-Simulation starten:**  
   Prüfen, ob der Zeitbalken unten grün bleibt *(keine roten Kollisionen)*.

---

### 📄 Phase 4: G-Code erzeugen (1 Minute)

1. In Fusion 360 oben auf **`NC-Programm / Postprozess (Strg + P)`** klicken.
2. Bei **„Post-Konfiguration“** Ihre in Phase 2 erzeugte `.cps`-Datei auswählen.
3. Auf **`Postprozessieren (Post)`** klicken.
4. Fusion 360 schreibt die fertige **`.nc`-Datei** auf Ihre Festplatte!

---

### 🎥 Phase 5: Das 3D-Kunden-Freigabevideo aufnehmen (2 Minuten)

Jetzt kommt der Schritt, der Ihnen volles Kundenvertrauen und sofortige Zahlung sichert:

1. Öffnen Sie in Ihrem Webbrowser:  
   👉 [`cnc_video_generator_web.html`](file:///C:/Projekte/CNC/cnc_video_generator_web.html)
2. Ziehen Sie Ihre in Phase 4 erzeugte `.nc`-Datei per Drag & Drop in das Fenster *(oder wählen Sie das Preset aus)*.
3. Tragen Sie den Kundennamen ein.
4. Klicken Sie auf den roten Button **„🔴 Video-Aufnahme starten“**.
5. Das Tool spielt die Fräsbewegungen mit 30 FPS im 3D-Raum ab, blendet Ihr Ingenieurbüro-Wasserzeichen ein und prüft live die Z-MIN Tiefe.
6. Nach Durchlauf öffnet sich das Vorschaufenster: Klicken Sie auf **„📥 Video herunterladen“** *(speichert z. B. `Freigabe_Simulation_Kunde.webm` oder `.mp4`)*.

---

### 💰 Phase 6: Vorab-Freigabe & 2. Teilzahlung anfordern (5 Minuten)

Sie schreiben eine kurze E-Mail an Ihren Kunden:

> **Betreff:** Ihr Bauteil [Name] – 3D-Simulationsvideo zur Vorab-Freigabe
> 
> Sehr geehrter Herr [Name],  
> die CAM-Programmierung für Ihr Bauteil wurde erfolgreich abgeschlossen.  
> 
> Im Anhang finden Sie ein **kurzes 30-Sekunden-Video unserer 3D-Simulation**:  
> • Nullpunkt `G54` liegt wie gewünscht vorne links oben.  
> • Kollisionsprüfung gegen Spannmittel: **Erfolgreich bestanden (Z-MIN = -12.0 mm)**.  
> • Bearbeitungszeit: ca. 4 Minuten 30 Sekunden.  
> 
> Bitte geben Sie das Video kurz frei. Nach Eingang der 2. Teilzahlung (Restbetrag: [Betrag] €) erhalten Sie umgehend die fertige `.NC`-Maschinendatei sowie das ausdruckbare Einrichteblatt für Ihren Fräser.  
> 
> Mit freundlichen Grüßen  
> [Ihr Name] – CAD/CAM Ingenieurbüro

👉 **Der psychologische Effekt:** Der Kunde sieht das Video, ist begeistert, weil er genau sieht, dass alles passt, gibt die Freigabe und überweist sofort das Geld!

---

### 📦 Phase 7: Finale Auslieferung & Projektabschluss

Sobald das Geld auf Ihrem Konto gutgeschrieben ist:

1. **Einrichteblatt exportieren:**  
   Sie füllen kurz die Vorlage [`Portfolio/Vorlage_Einrichteblatt_und_Werkzeugliste.md`](file:///c:/Projekte/CNC/Portfolio/Vorlage_Einrichteblatt_und_Werkzeugliste.md) aus *(Werkzeugliste, Nullpunkt, Spannbackenhöhe)* und speichern sie als PDF.
2. **Liefer-E-Mail an den Kunden senden:**  
   Sie hängen die fertige **`.nc`-Datei** und das **Einrichteblatt (PDF)** an.
3. **Schlussrechnung beilegen:**  
   Die bezahlte Gesamtrechnung beilegen.
4. **Auftrag zu 100 % erfolgreich und rechtssicher abgeschlossen!**

---

## 📌 Schnell-Spickzettel: Die 3 Web-Tools auf einen Blick

* ⚙️ **Postprozessor bauen / anpassen:** [`kunden_cps_generator_web.html`](file:///C:/Projekte/CNC/kunden_cps_generator_web.html)
* 🎥 **Kunden-Freigabevideo aufnehmen:** [`cnc_video_generator_web.html`](file:///C:/Projekte/CNC/cnc_video_generator_web.html)
* 🔍 **G-Code Satz für Satz im 3D-Detail analysieren:** [`kundenauftrag_01_flanschplatte/3d_auftrag_simulator.html`](file:///c:/Projekte/CNC/kundenauftrag_01_flanschplatte/3d_auftrag_simulator.html)

---

## 🎬 8. Vertiefung: Alles über das 3D-Freigabe-Video (Wann, Warum, Welche Datei?)

### ⏱️ WANN genau wird das Video an den Kunden geschickt?

Das Video wird zu einem ganz bestimmten, strategisch entscheidenden Zeitpunkt versendet:

> **👉 GENAU IN DER MITTE DES AUFTRAGS:**  
> Wenn Ihre Programmierarbeit fertig ist, aber **BEVOR** Sie dem Kunden die finale `.NC`-Datei aushändigen!

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ DER EXAKTE ZEITSTRAHL DER VIDEO-VERSENDUNG                                            │
└────────────────────────────────────────────────────────────────────────────────────────┘
  1. TAG 1:  Kunde schickt 3D-Modell  --> Sie verlangen 50 % Anzahlung.
                 │
                 ▼
  2. TAG 2:  Die 50 % Anzahlung ist auf Ihrem Bankkonto gutgeschrieben.
                 │
                 ▼
  3. TAG 2:  Sie programmieren das Teil im CAM, erzeugen den G-Code und
             nehmen das 30-Sekunden-Video im Web-Studio auf.
                 │
                 ▼
  4. JETZT:  👉 HIER SCHICKEN SIE DAS VIDEO AN DEN KUNDEN! 👈
             Sie schicken NUR das Video (KEINE .nc-Datei!).
             Text: „Hier ist Ihr Freigabe-Video. Bitte bestätigen & Schlussrechnung anweisen.“
                 │
                 ▼
  5. TAG 3:  Der Kunde sieht das Video, ist begeistert und überweist die restlichen 50 %.
                 │
                 ▼
  6. TAG 3:  Geld ist da  --> JETZT schicken Sie die .nc-Datei & das Einrichteblatt!
```

---

### 🚨 Warum darf die `.nc`-Datei NIEMALS zusammen mit dem Video geschickt werden?

Das ist die **wichtigste kaufmännische Schutzregel** für jeden selbstständigen Ingenieur:

1. **Die Gefahr bei vorzeitiger Übergabe:**  
   Wenn Sie die `.nc`-Datei zusammen mit dem Video per E-Mail mitschicken, hat der Kunde das fertige Fräsprogramm bereits auf seinem Computer. Ein unzuverlässiger Kunde könnte die Datei auf die Maschine spielen, seine Bauteile fräsen und Ihre Rechnung wochenlang ignorieren.
2. **Der Schutz durch das Video:**  
   * Das Video beweist: *„Meine Arbeit ist zu 100 % erledigt, fehlerfrei und kollisionsfrei geprüft.“*
   * Aber fräsen kann der Kunde mit dem Video **nicht** – dazu braucht er zwingend die `.nc`-Datei!
   * Er bezahlt also sofort und freiwillig die restlichen 50 %, um den Code schnellstmöglich auf seine Maschine laden zu können.

---

### ❓ Warum schickt man eine 3D-Simulation und kein „echtes Kamera-Video“?

Viele Einsteiger fragen: *„Muss ich das Werkstück nicht mit einer echten Kamera filmen, wie der Fräser Späne schneidet?“*

**Klare Antwort: NEIN, das ist unmöglich und wird in der Industrie niemals so gemacht!**

* **Warum unmöglich?**  
  Sie sind der externe Remote-Programmierer. Der Kunde ist die Fräserei mit der Maschine in der Werkhalle. Das Bauteil existiert auf der Maschine **noch gar nicht**! Würde das Teil schon fertig gefräst sein, bräuchte der Kunde Ihre Dienste gar nicht mehr.
* **Warum will der Kunde die 3D-Simulation?**  
  Auf einem echten Werkstatt-Video sieht man vor lauter weißem Spritzwasser *(Kühlschmiermittel)* und fliegenden Spänen überhaupt keine Details.  
  In unserer digitalen 3D-Simulation sieht der Fertigungsleiter dagegen mit Röntgenblick:
  1. Den exakten Nullpunkt `G54` an der Bauteilecke.
  2. Die Werkzeugwege und den sanften **Lead-In-Anschnitt**.
  3. Die Spannbacken des Schraubstocks und die Bestätigung: `Z-MIN = -12.0 mm -> SICHER!`
  
👉 **Die 3D-CAD/CAM-Simulation ist der weltweite Industriestandard** *(bei DMG MORI, Hermle, Haas, Siemens und Autodesk)*!

---

### 🔍 Warum wird das Video aus der `.nc`-Datei erzeugt und nicht nur aus dem 3D-Modell?

* **CAM-Simulation *(in Fusion 360)*:**  
  Simuliert die internen mathematischen Pfade der CAD-Software.
* **G-Code-Simulation *(in unserem Web-Studio `cnc_video_generator_web.html`)*:**  
  Liest Zeile für Zeile **den tatsächlichen Maschinencode (`G00`, `G01`, `G03`, `G83`)** ein, den die Steuerung später abarbeitet.
* **Der unschlagbare Vorteil für den Kunden:**  
  Ein Video aus der `.nc`-Datei beweist nicht nur, dass die 3D-Zeichnung stimmt, sondern beweist schwarz auf weiß: **Der Postprozessor hat fehlerfrei übersetzt und der Maschinencode ist zu 100 % crashsicher!**

---

## ✉️ 9. Die 3 fertigen E-Mail-Vorlagen für Ihren Kundenkontakt

### E-Mail 1: Angebot mit 50 % Anzahlung *(Vor Arbeitsbeginn)*

> **Betreff:** Angebot CAM-Programmierung – Bauteil [Name] (Projekt #[Nummer])
> 
> Sehr geehrter Herr [Name],
> 
> vielen Dank für Ihre Anfrage und die Zusendung der 3D-Daten für das Bauteil [Name].
> 
> Gerne übernehmen wir die vollständige CAM-Programmierung inklusive 3D-Kollisionsprüfung und Erstellung des Einrichteblatts für Ihre Maschine [z. B. Haas VF-2].
> 
> **Konditionen:**  
> • Festpreis: **[z. B. 240,00] €** *(zzgl. gesetzl. MwSt.)*  
> • Lieferumfang: Fertige `.NC`-Maschinendatei, druckbares Rüstblatt (PDF) sowie ein 3D-Simulations-Freigabevideo.  
> • Zahlungsbedingung: 50 % Anzahlung bei Auftragserteilung. Restbetrag nach Bereitstellung des 3D-Simulationsvideos vor Code-Übergabe.  
> 
> Bitte bestätigen Sie dieses Angebot kurz per E-Mail. Nach Eingang der Anzahlung beginnen wir umgehend mit der Programmierung.
> 
> Mit freundlichen Grüßen  
> [Ihr Name] – Diplom-Ingenieur & Senior Software Engineer

---

### E-Mail 2: Das Freigabe-Video *(Genau zur Halbzeit)*

> **Betreff:** Ihr Bauteil [Name] – 3D-Simulationsvideo zur Vorab-Freigabe
> 
> Sehr geehrter Herr [Name],
> 
> die CAM-Programmierung für Ihr Bauteil [Name] wurde erfolgreich fertiggestellt.
> 
> Im Anhang finden Sie ein **kurzes Video unserer 3D-Simulation direkt aus dem Maschinencode**:  
> • Nullpunkt `G54`: Vorne links oben wie vereinbart.  
> • Werkzeugwege & Schnittanfahrt: Geprüft und kollisionsfrei.  
> • Schraubstock-Prüfung: **Erfolgreich bestanden (Z-MIN = -12.0 mm)**.  
> 
> Bitte geben Sie das Video kurz frei. Nach Ausgleich der beiliegenden Schlussrechnung über [Restbetrag] € senden wir Ihnen umgehend die fertige `.NC`-Datei und das Einrichteblatt für Ihren Maschinenbediener zu.
> 
> Mit freundlichen Grüßen  
> [Ihr Name] – CAD/CAM Ingenieurbüro

---

### E-Mail 3: Finale Auslieferung *(Nach Zahlungseingang)*

> **Betreff:** Fertigungsdaten Bauteil [Name] – NC-Programm & Einrichteblatt
> 
> Sehr geehrter Herr [Name],
> 
> vielen Dank für die Freigabe und den schnellen Rechnungsausgleich!
> 
> Im Anhang erhalten Sie Ihre finalen Produktionsdaten:  
> 1. **`[Dateiname].nc`**: Das fertige CNC-Maschinenprogramm für Ihre Steuerung.  
> 2. **`Einrichteblatt_[Dateiname].pdf`**: Rüstplan mit Werkzeugliste, Auskraglängen und Nullpunktdaten.  
> 3. **Schlussrechnung (Quittung)** als bezahlter Beleg für Ihre Buchhaltung.  
> 
> Wir wünschen eine erfolgreiche und späneintensive Fertigung und freuen uns auf das nächste gemeinsame Projekt!
> 
> Mit freundlichen Grüßen  
> [Ihr Name] – CAD/CAM Ingenieurbüro


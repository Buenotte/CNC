# 🗺️ Master-Leitfaden: Vollständiger Prozessablauf für jeden Kundenauftrag (Von A bis Z)

Dieses Dokument ist Ihre **zentrale Arbeitsanleitung**. Es beschreibt Schritt für Schritt den exakten, lückenlosen Ablauf, wie Sie als freiberuflicher CAM-Ingenieur einen Kundenauftrag bearbeiten – vom ersten E-Mail-Kontakt über die Software-Tools bis zum Geldeingang auf Ihrem Bankkonto.

---

## 🧭 Übersicht: Wo sind unsere neuen Tools im Projekt dokumentiert?

Falls Sie nach bestimmten Funktionen suchen, finden Sie diese an folgenden Stellen:

| Tool / Thema | Datei auf Ihrer Festplatte | Wo im Handbuch beschrieben? |
|:---|:---|:---|
| **Web-Postprozessor-Generator** | [`kunden_cps_generator_web.html`](file:///C:/Projekte/CNC/02_Software_und_Tools/web_tools/kunden_cps_generator_web.html) | [`ANLEITUNG_CPS_GENERATOR_UND_WEB_INTERFACE.md`](file:///C:/Projekte/CNC/02_Software_und_Tools/ANLEITUNG_CPS_GENERATOR_UND_WEB_INTERFACE.md) & [`ALLE_UEBUNGEN_HANDBUCH.md#L2370`](file:///C:/Projekte/CNC/03_Fachdokumentation_und_Wissen/ALLE_UEBUNGEN_HANDBUCH.md#L2370) |
| **Web-Video-Generator (3D-Freigabe)** | [`cnc_video_generator_web.html`](file:///C:/Projekte/CNC/02_Software_und_Tools/web_tools/cnc_video_generator_web.html) | [`ALLE_UEBUNGEN_HANDBUCH.md#L2256`](file:///C:/Projekte/CNC/03_Fachdokumentation_und_Wissen/ALLE_UEBUNGEN_HANDBUCH.md#L2256) (Abschnitt 13) |
| **Fertiges MP4-Video zu Übung 3** | [`docs/videos/uebung_03_simulation_video.mp4`](file:///c:/Projekte/CNC/03_Fachdokumentation_und_Wissen/docs/videos/uebung_03_simulation_video.mp4) | Handbuch Übung 3 / Abschnitt 13 |
| **Klick-Anleitung 3D-Modell Fusion 360** | [`kundenauftrag_01_flanschplatte/KUNDEN_AUFTRAG_UND_KLICK_ANLEITUNG.md`](file:///C:/Projekte/CNC/01_Kundenauftraege/referenz_auftrag_flanschplatte/KUNDEN_AUFTRAG_UND_KLICK_ANLEITUNG.md) | Handbuch Übung 4 |
| **3D-Simulator mit Satz-Editor** | [`kundenauftrag_01_flanschplatte/3d_auftrag_simulator.html`](file:///c:/Projekte/CNC/01_Kundenauftraege/referenz_auftrag_flanschplatte/3d_auftrag_simulator.html) | Handbuch Übung 00b & Übung 5 |
| **Sicherheits- & Qualitätsprüfliste** | [`SICHERHEITS_UND_QUALITAETS_PRUEFLISTE_GCODE.md`](file:///c:/Projekte/CNC/03_Fachdokumentation_und_Wissen/SICHERHEITS_UND_QUALITAETS_PRUEFLISTE_GCODE.md) | Begleitendes Prüfhandbuch Phase 1 bis 5 |

---

## 🔄 Die 2 Geschäftswege deines Ingenieurbüros

Als **Diplom-Ingenieur & Senior Software Engineer** hast du zwei klare Wege, Aufträge anzunehmen. **Weg A ist dein absoluter Hauptfokus**, weil er deine Programmier-Stärken zu 100 % ausspielt:

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ DIE 2 GESCHÄFTSWEGE IM VERGLEICH                                                      │
└────────────────────────────────────────────────────────────────────────────────────────┘
  🚀 WEG A (DEIN HAUPTFOKUS): REINE POSTPROZESSOR- & CODE-ENTWICKLUNG
     • Du machst: JavaScript (.cps), Python & NC-Safety-Routinen für Systemhäuser & Fräsereien.
     • CAD/CAM-Klicks in Fusion 360: 0 % (KEIN Fräsbahn-Mausklicken erforderlich!).
     • Stundensatz: 100 € bis 150 € / Stunde (Feste Paketpreise: 400 € bis 900 € pro Postprozessor).
     • Zeitaufwand: Nur 2 bis 3 Stunden pro Auftrag – ideal für den Feierabend!
  
  📦 WEG B (OPTIONALER NEBENWEG): KOMPLETTE BAUTEIL-FERTIGUNG (CAM-KUNDENAUFTRAG)
     • Du machst: Kunde schickt 3D-STEP-Modell -> Du klickst die 4 Standard-Operationen
       nach unserer Klick-Anleitung in Fusion 360 ab (Setup, Planen, Kontur, Bohren).
     • CAD/CAM-Klicks: ca. 10 bis 15 Minuten pro Bauteil.
     • Stundensatz: 80 € bis 110 € / Stunde (ca. 180 € bis 350 € pro Bauteil).
```

---

## 🚀 WEG A (DEIN HAUPTWEG): Der vollständige Ablauf für Postprozessor-Aufträge (0 % CAD-Klicks)

Das ist der schnellste, lukrativste und eleganteste Weg für dich als Software-Ingenieur:

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ DER WEG-A-PRAXISABLAUF (REINE POSTPROZESSOR- & AUTOMATISIERUNGS-AUFTRÄGE)              │
└────────────────────────────────────────────────────────────────────────────────────────┘
  SCHRITT 1: Systemhaus oder Fräserei kontaktiert dich (oder über Agent 1 akquiriert)
             Kunde formuliert seine Anforderungen (z. B. Maschine, Steuerung, Sonderwünsche).
        │
        ▼
  SCHRITT 2: Schneller Anforderungs-Check (Die 4 goldenen Fragen)
             Kunde liefert die 2 Schlüsseldateien:
             1. Den bisherigen Postprozessor (z. B. eine alte .cps-Datei aus Fusion).
             2. Ein funktionierendes Referenz-NC-Programm von seiner Maschine.
        │
        ▼
  SCHRITT 3: Angebot mit 50 % Anzahlung versenden
             🤖 Übernimmt: AGENT 4 (Backoffice-Agent schreibt Angebot: z. B. 480 € Festpreis).
        │
        ▼
  SCHRITT 4: Postprozessor anpassen mit unseren Generatoren & Agent 2
             🤖 Übernimmt: AGENT 2 (Postprocessor-Coder-Agent) & kunden_cps_generator_web.html
             Du öffnest den Code in VS Code, Agent 2 schreibt die JavaScript-Funktionen hinein.
             --> 0 % Fusion-360-Klicks! Reine Software-Arbeit!
        │
        ▼
  SCHRITT 5: Automatische Sicherheitsprüfung mit Prüfliste
             🤖 Übernimmt: AGENT 3 (NC-Safety-Agent prüft Syntax, Modale Befehle, Z-MIN).
        │
        ▼
  SCHRITT 6: 2. Teilzahlung & Auslieferung der fertigen .cps-Datei
             🤖 Übernimmt: AGENT 4 (Schlussrechnung & Dokumentation der geänderten Zeilen).
```

---

### 📋 Wie sehen Kunden-Anforderungen in der Realität aus? (Der 4-Punkte-Check)

Zerspanungsbetriebe und CAM-Systemhäuser schreiben keine 50 Seiten langen Pflichtenhefte, sondern ganz pragmatische E-Mails oder Tickets. Hier erfährst du genau, was auf dich zukommt und wie du die Anforderungen in 2 Minuten glasklar ordnest:

#### 1. Ein reales Beispiel einer Kundenanfrage:
> *„Guten Tag Herr [Name],  
> wir haben eine neue 3-Achs-Fräsmaschine (Haas VF-2 mit NextGen-Steuerung) in unserer Werkstatt aufgestellt. Wir nutzen Autodesk Fusion 360.  
> Der Standard-Postprozessor von Autodesk passt für uns nicht optimal:  
> 1. Am Programmende soll der Frästisch ganz nach vorne an die Schiebetür fahren, damit der Werker bequem entladen kann.  
> 2. Bei Tieflochbohrern ab 50 mm Bohrtiefe benötigen wir automatisch Innenkühlung (M88) statt Standard-Kühlmittel (M08).  
> 3. Im Programmkopf soll die absolut tiefste Frästiefe (Z-MIN) angezeigt werden, damit vor dem Start kein Crash in den Maschinenschraubstock droht.  
> Können Sie uns den Postprozessor anpassen und was würde das kosten?  
> Anbei ein Musterprogramm, wie unsere Maschine den Code erwartet.  
> Viele Grüße, Werkstattleiter Müller“*

#### 2. Die 4 goldenen Fragen, die du immer brauchst:
Falls ein Kunde nur knapp schreibt *(„Hallo, wir brauchen einen Postprozessor für Hermle“)*, schickst du ihm (oder Agent 4) einfach diesen **1-Minuten-Fragebogen**:

| Frage | Warum wichtig? | Typische Kunden-Antwort |
|:---|:---|:---|
| **1. Genaue Maschine & Steuerung?** | Bestimmt den G-Code-Dialekt. | *„Hermle C400 mit Heidenhain TNC 640“* oder *„Haas VF-2 NGC“*. |
| **2. Welches CAM-System?** | Bestimmt die Dateiendung des Postprozessors. | *„Autodesk Fusion 360 (`.cps`-Datei)“*. |
| **3. Haben Sie ein Referenz-NC-Programm?** | **Der wichtigste Punkt überhaupt!** Anhand eines Musters, das auf seiner Maschine fehlerfrei läuft, siehst du sofort Header, Sicherheitszeilen und Zyklen! | *„Ja, siehe Anhang `teil_01.H` oder `muster.nc`“*. |
| **4. Welche konkreten Sonderfunktionen?** | Bestimmt die JavaScript-Funktionen, die geändert werden müssen. | *„Tisch zur Tür, Z-MIN Anzeige, Innenkühlung M88, Werkzeugbruchkontrolle“*. |

#### 3. Fertige E-Mail-Vorlage für fehlende Kunden-Anforderungen (Copy-Paste):

> **Betreff:** Re: Ihre Anfrage zur Postprozessor-Anpassung – Kurze Detailabstimmung
> 
> Sehr geehrter Herr [Name],
> 
> vielen Dank für Ihre Anfrage! Sehr gerne passe ich den Postprozessor für Ihre Fräsmaschine maßgeschneidert an.
> 
> Damit ich Ihnen heute noch ein verbindliches Festpreisangebot erstellen kann, bitte ich Sie um kurze Beantwortung von vier kurzen Punkten:
> 1. Welcher Maschinentyp und welche Steuerung *(z. B. Heidenhain TNC 640, Siemens 840D oder Haas NGC)* ist im Einsatz?
> 2. Nutzen Sie Autodesk Fusion 360 als CAM-System?
> 3. Bitte senden Sie mir ein kurzes **Referenz-NC-Programm**, das auf Ihrer Maschine bereits einwandfrei läuft *(z. B. ein Standard-Fräsprogramm aus Ihrer Werkstatt)*.
> 4. Welche konkreten Sonderfunktionen *(z. B. automatischer Tischrückzug zur Tür, Z-MIN Tiefenprüfung im Programmkopf, Innenkühlung)* wünschen Sie?
> 
> Nach Erhalt dieser Angaben erstelle ich Ihnen umgehend das Festpreisangebot und liefere den fertigen Postprozessor innerhalb von 24 bis 48 Stunden aus.
> 
> Mit freundlichen Grüßen  
> Dipl.-Ing. Bujanovski – Diplom-Ingenieur & Senior Software Engineer

#### 4. Wie gibst du die Kundenanforderungen an Agent 2 weiter?
Sobald der Kunde geantwortet hat, kopierst du die Anforderungen einfach in diesen Chat-Prompt:
```text
Starte AGENT 2 (Postprocessor-Coder-Agent):
Kunde: [z. B. Fa. Schmidt Zerspanung]
Maschine: [z. B. Haas VF-2 mit NextGen Control]
CAM-System: Autodesk Fusion 360 (.cps)
Anforderungen des Kunden:
1. Tischrückzug am Programmende ganz nach vorne zur Schiebetür (G53 Y0).
2. Automatische Innenkühlung M88 bei Werkzeugen mit IKZ-Kennzeichnung.
3. Z-MIN Tiefenprüfung im Programmkopf als gut sichtbaren Kommentar.
Hier ist das Referenz-NC-Programm des Kunden: [Code oder Dateipfad einfügen]
Passe den Postprozessor an und dokumentiere alle geänderten Zeilen!
```
Agent 2 nimmt die Anforderungen und baut die JavaScript-Routinen in Sekundenschnelle in die `.cps`-Datei ein!

#### 5. Wo gibst du diesen konkreten Haas VF-2 Kundenwunsch ein? (Die 2 Wege in der Praxis)

Wenn der Kunde dir genau diesen Text schreibt:  
> *„Wir haben eine neue Haas VF-2 Fräse mit NextGen-Steuerung und nutzen Fusion 360. Der Standard-Postprozessor fährt am Programmende den Tisch nicht an die Schiebetür, und wir brauchen Z-MIN im Programmkopf sowie M88 Innenkühlung. Können Sie uns den Postprozessor anpassen?“*

Hast du **zwei gleichwertige Möglichkeiten**, diesen Wunsch einzugeben:

##### 🌐 Weg 1: Im Web-Interface [`kunden_cps_generator_web.html`](file:///C:/Projekte/CNC/02_Software_und_Tools/web_tools/kunden_cps_generator_web.html) *(Visuell per 4 Klicks)*
1. Öffne per Doppelklick: [`kunden_cps_generator_web.html`](file:///C:/Projekte/CNC/02_Software_und_Tools/web_tools/kunden_cps_generator_web.html) *(im Browser)*.
2. Trage den Kundennamen ein *(z. B. `Schmidt Zerspanungstechnik`)*.
3. Klicke auf die gelbe Kachel **🟡 Haas (NGC / Classic)**.
4. Setze die **3 Häkchen gemäß Kundenwunsch**:
   * ☑️ **Z-MIN Tiefenprüfung im Header einbinden**
   * ☑️ **Tisch am Programmende zur Tür fahren (G53 G00 Y0.)**
   * ☑️ **Kühlmittel:** Klicke auf den Radio-Button **`M88 (IKZ / Hochdruck Innenkühlung)`** *(statt Standard M08)*.
5. Klicke unten auf **„📥 .cps-Datei herunterladen“**.
   * 👉 **Fertig in 30 Sekunden!** Die fertige `.cps`-Datei landet in deinem Download-Ordner.

##### 🤖 Weg 2: Direkt hier im Chat an KI-Agent 2 *(Per Copy-Paste des Kunden-Originaltexts)*
Du musst das Web-Tool gar nicht öffnen, sondern kopierst einfach den Originaltext des Kunden in den Chat:
```text
Starte AGENT 2 (Postprocessor-Coder-Agent):
Hier ist die Original-Anfrage des Kunden:
„Wir haben eine neue Haas VF-2 Fräse mit NextGen-Steuerung und nutzen Fusion 360. Der Standard-Postprozessor fährt am Programmende den Tisch nicht an die Schiebetür, und wir brauchen Z-MIN im Programmkopf sowie M88 Innenkühlung. Können Sie uns den Postprozessor anpassen?“

Erstelle mir den maßgeschneiderten Haas-Postprozessor für diesen Kunden!
```
* 👉 **Was Agent 2 tut:** Agent 2 liest die 3 Anforderungen automatisch heraus, aktualisiert die JavaScript-Funktionen `onOpen()` *(Z-MIN)*, `onSection()` *(M88)* und `onClose()` *(G53 Y0)* und speichert die Datei direkt in deinem Projektordner!

##### 🔍 Der Vorher-Nachher-Vergleich im erzeugten Maschinencode (G-Code):

| Was der Kunde wollte | VORHER (Standard-Postprozessor) | NACHHER (Mit unserem angepassten Postprozessor) |
|:---|:---|:---|
| **Z-MIN im Programmkopf** | *(Keine Tiefenangabe im Header)* | `(TIEFSTE FRAESTIEFE Z-MIN = -12.000 MM - SICHER!)` |
| **Innenkühlung M88** | `M08` *(Kühlmittel von außen)* | `M88` *(20 bar Hochdruck durch das Werkzeuginnere)* |
| **Tisch zur Tür fahren** | `G28 G91 Z0.` *(Tisch bleibt hinten stehen)* | `G53 G00 Y0.` *(Tisch fährt direkt vor die Schiebetür)* |

---

## 🔄 Die 8 Phasen eines Kundenauftrags (Der vollständige Workflow von A bis Z)

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ DER 8-PHASEN-PRAXISABLAUF VOM ERSTKONTAKT BIS ZUR ENDZAHLUNG                           │
│ (HAUPTFOKUS WEG A: REINE POSTPROZESSOR- & CODE-ENTWICKLUNG - 0 % CAD-KLICKS!)          │
└────────────────────────────────────────────────────────────────────────────────────────┘
  PHASE 0: Neukunden finden, Anzeigen erstellen & veröffentlichen
           🤖 Übernimmt: AGENT 1 (Lead-Scout-Agent) & fertige Anzeigen-Vorlagen
      │
      ▼
  PHASE 1: Kunden-E-Mail trifft ein & Angebot erstellen (50 % Anzahlung anfordern)
           🤖 Übernimmt: AGENT 4 (Backoffice-Ingenieur-Agent)
      │
      ▼
  PHASE 2: Kundenanforderungen & Referenz-NC einlesen (kunden_cps_generator_web.html)
           🤖 Übernimmt: AGENT 2 & 4-Punkte-Checkliste (Maschine, Steuerung, Sonderwünsche)
      │
      ▼
  PHASE 3: Postprozessor-Code anpassen & Funktionen einbinden (JavaScript .cps / Python)
           👤 Übernimmst DU (Deine 20 % Kernarbeit: 2-Minuten-Code-Review in VS Code / Freigabe)
           --> 0 % CAD-Mausklicks! Reine Software-Ingenieur-Arbeit!
      │
      ▼
  PHASE 4: Maschinencode gegen Kunden-Referenz prüfen & 5-Stufen-Sicherheitscheck
           🤖 Übernimmt: AGENT 3 (NC-Safety-Check & Crash-Prüfung)
      │
      ▼
  PHASE 5: Testlauf im 3D-Simulator / Verifikations-Prüfbericht erstellen
           🤖 Übernimmt: AGENT 3 & Web-Studio (cnc_video_generator_web.html / Simulator)
      │
      ▼
  PHASE 6: Vorab-Prüfbericht an Kunden senden -> Freigabe & 2. Teilzahlung anfordern
           🤖 Übernimmt: AGENT 4 (Backoffice-Agent: Freigabe-E-Mail & Rechnung Restbetrag)
      │
      ▼
  PHASE 7: Auslieferung der finalen .cps-Datei inklusive Dokumentation der Änderungen
           🤖 Übernimmt: AGENT 2 (Code-Doku) & AGENT 4 (quittierte Schlussrechnung)
```

---

## 🤖 Die Rollenverteilung: Die 80/20-Regel mit deinen 4 KI-Agenten

Als freiberuflicher Ingenieur mit **nur 5 bis 8 Stunden Zeit pro Woche** nebenberuflich musst du deine Zeit schützen:

* **In Weg A (Dein Hauptfokus: Postprozessoren & Automatisierung – 0 % CAD-Klicks):**
  * **Deine 20 % (Mensch / Senior Software Engineer):** Kundenanfrage überfliegen *(1 Minute)*, Referenz-NC-Programm des Kunden anschauen, Code-Änderungen in der `.cps`-Datei kurz prüfen und Endfreigabe erteilen. Du musst **kein einziges 3D-Modell mit der Maus anklicken**!
  * **Die 80 % der KI-Agenten:** `Agent 1` recherchiert Systemhäuser & Firmen, `Agent 4` schreibt Angebot & Rechnungen, `Agent 2` schreibt den JavaScript-Code für die Zyklen, `Agent 3` testet den Maschinencode!

* **In Weg B (Optionaler Nebenweg: Komplettes 3D-Bauteil von A bis Z):**
  * **Deine 20 % (Mensch / Ingenieur):** 3D-Modell in Fusion 360 öffnen und die 4 Standard-Operationen *(Setup, Planen, Kontur, Bohren)* streng nach unserer Klick-Anleitung [`kundenauftrag_01_flanschplatte/KUNDEN_AUFTRAG_UND_KLICK_ANLEITUNG.md`](file:///C:/Projekte/CNC/01_Kundenauftraege/referenz_auftrag_flanschplatte/KUNDEN_AUFTRAG_UND_KLICK_ANLEITUNG.md) kurz anklicken *(10 bis 15 Minuten)*.
  * **Die 80 % der KI-Agenten:** Postprozessor generieren, G-Code-Sicherheitscheck, Video aufnehmen, Rüstblatt extrahieren und Rechnungen versenden!

*(Ausführliche technische Baupläne und System-Prompts: Siehe [`KI_Agenten_System_und_Bauplan.md`](file:///c:/Projekte/CNC/04_Recht_Steuern_und_Backoffice/KI_Agenten_System_und_Bauplan.md)).*

---

### 💡 Grundsatzfrage: „Wir haben doch eigene Skripte & Web-Generatoren gebaut – wozu brauche ich überhaupt noch Fusion 360?“

Diese Frage ist absolut berechtigt! Um Missverständnisse zu vermeiden, ist hier die glasklare Abgrenzung, **welches Werkzeug welche Aufgabe übernimmt**:

#### 1. Was unsere Skripte & Web-Generatoren tun (und was sie NICHT tun)
Unsere selbst gebauten Werkzeuge sind hochspezialisierte Automatisierungs- und Sicherheits-Werkzeuge:

| Werkzeug | Was das Tool perfekt erledigt | Was das Tool **nicht** kann |
|:---|:---|:---|
| **[`kunden_cps_generator_web.html`](file:///C:/Projekte/CNC/02_Software_und_Tools/web_tools/kunden_cps_generator_web.html)** | Erzeugt per Klick maßgeschneiderte Postprozessoren *(Übersetzungsdateien `.cps`)* für Haas, Siemens, Heidenhain mit Z-MIN Check und Tisch-zur-Tür-Rückzug. | Es kann keine 3D-CAD-Modelle des Kunden öffnen oder selbstständig Fräsbahnen berechnen. |
| **[`cnc_video_generator_web.html`](file:///C:/Projekte/CNC/02_Software_und_Tools/web_tools/cnc_video_generator_web.html)** | Liest fertigen G-Code (`.nc`), visualisiert die Werkzeugbahnen im 3D-Raum, prüft Schraubstockkollisionen und filmt das Beweis-Video für den Kunden. | Es kann aus einer 3D-CAD-Datei (`.step` oder `.stl`) keinen Maschinencode erzeugen. |
| **`cnc_setup_sheet_extractor.py`** | Liest fertigen G-Code aus und erzeugt in 3 Sekunden das druckfertige Einrichteblatt mit Werkzeugliste, Drehzahlen und Z-MIN. | Es kann nur bereits fertig postprozessierte NC-Dateien analysieren. |

#### 2. Warum braucht man für neue Kundenbauteile trotzdem Autodesk Fusion 360?
Wenn ein Kunde Ihnen ein **neues, individuelles Bauteil** als 3D-CAD-Datei *(z. B. `gehaeuse.step` oder `flansch.stl`)* schickt, hat dieses Teil spezifische Konturen, Taschen, Radien und Gewindebohrungen:
* **Kein Skript der Welt** kann ein beliebiges 3D-Volumenmodell ohne CAM-Rechenkern *(Computer-Aided Manufacturing Kernel)* automatisch in Werkzeugbahnen zerlegen.
* Man muss festlegen: *Mit welchem Schaftfräser fährt man in die Tasche? Wo wird mit einer Helix-Spirale eingetaucht? Welche Kanten werden mit dem 45°-Fasenfräser entgratet?*
* Genau das erledigt **Autodesk Fusion 360**: Sie öffnen das 3D-Modell, klicken mit der Maus die Konturen und Taschen an – fertig! Das dauert bei einem normalen 3-Achs-Bauteil **nur 10 bis 15 Minuten**.
* Danach übernimmt unsere Pipeline wieder die 80 % Fleißarbeit: Unser Postprozessor erzeugt den G-Code, Agent 3 prüft die Crash-Sicherheit und unser Web-Studio filmt das Freigabevideo!

#### 3. Das perfekte Zusammenspiel der Werkzeuge in Weg A (Dein Hauptfokus: 0 % CAD-Klicks):
```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ WIE ALLE WERKZEUGE IN DEINEM HAUPTWEG (WEG A) ZUSAMMENARBEITEN                         │
└────────────────────────────────────────────────────────────────────────────────────────┘
  1. KUNDE / SYSTEMHAUS:   Schickt alten Postprozessor (.cps) + Referenz-NC-Programm
            │              (Der Kunde hat seine Werkzeuge & Fräsbahnen schon selbst!)
            ▼
  2. DEINE 20 % ARBEIT:    Du schaust kurz in den Code (Code-Review in VS Code).
     (Senior Engineer)     --> KEIN Fräsbahn-Mausklicken in Fusion 360! 0 % CAD-Klicks!
            │
            ▼
  3. UNSER CPS-GENERATOR:  Unser Web-Generator (kunden_cps_generator_web.html) & AGENT 2
     (Postprozessor-Bau)   bauen Tisch-Rückzug (G53 Y0), Z-MIN und M88 direkt in die .cps-Datei ein.
            │
            ▼
  4. AGENT 3 & SAFETY:     Prüft den generierten Code gegen die Sicherheitsprüfliste
     (NC-Safety-Check)     und verifiziert alle Modalen Befehle und Crash-Tiefen.
            │
            ▼
  5. AGENT 4 (BACKOFFICE): Erstellt Angebot, Begleitdokumentation und quittierte Schlussrechnung!
```

#### 4. Wann du Fusion 360 GAR NICHT brauchst (100 % reine Skript- und Code-Aufträge):
Es gibt zwei sehr häufige und hochbezahlte Auftragsarten, bei denen du **überhaupt kein Fusion 360 öffnen musst**:
1. **Reine Postprozessor-Entwicklung für Systemhäuser & Fräsereien:**  
   Ein Betrieb programmiert bereits selbst an der Maschine, aber ihr Postprozessor macht Fehler beim Werkzeugwechsel oder Tischrückzug. Du nutzt direkt unser Web-Tool [`kunden_cps_generator_web.html`](file:///C:/Projekte/CNC/02_Software_und_Tools/web_tools/kunden_cps_generator_web.html) und `Agent 2 (Postprocessor-Coder-Agent)`, passt den JavaScript-Code an und lieferst die fertige `.cps`-Datei aus. Honorar: **300 € bis 600 € ohne ein einziges 3D-Modell anzurühren!**
2. **Reiner Sicherheits-Prüfservice & Video-Erstellung (Second Opinion):**  
   Eine Werkstatt hat ein fertiges NC-Programm, ist sich aber unsicher wegen Werkzeugkollisionen. Du nimmst deren `.nc`-Datei, lässt `Agent 3` durchlaufen, erstellst das Simulations-Video mit [`cnc_video_generator_web.html`](file:///C:/Projekte/CNC/02_Software_und_Tools/web_tools/cnc_video_generator_web.html) und das Rüstblatt.

#### 5. Der rechtliche Hintergrund (§ 18 EStG – Freiberufler-Status):
Nach deutschem Steuerrecht muss ein freiberuflicher Ingenieur eine **„leitende und eigenverantwortliche Facharbeit“** leisten, um von der Gewerbesteuer und IHK-Zwangsmitgliedschaft befreit zu bleiben. Indem du die Frässtrategie und Werkzeuge im CAD/CAM festlegst und die Simulation freigibst, erfüllst du diese gesetzliche Voraussetzung zu 100 %!

---

### 📢 Phase 0: Neukunden finden, Anzeigen erstellen & veröffentlichen (Der Start)

Bevor ein Kunde Ihnen eine E-Mail schicken kann, muss er wissen, dass es Ihr Ingenieurbüro gibt!  
Hier sind die **4 stärksten Kanäle**, um als freiberuflicher CAM-Ingenieur Kundenaufträge zu gewinnen – inklusive fertiger Vorlagen zum direkten Kopieren:

#### 1. Kanal 1: Bundesweite Online-Anzeige auf Kleinanzeigen.de *(Extrem effektiv!)*
Viele Werkstatt-Chefs und Lohnfertiger (5 bis 20 Mitarbeiter) suchen bei Engpässen oder neuen Maschinen ganz pragmatisch auf **Kleinanzeigen.de *(Kategorie: Dienstleistungen $\rightarrow$ Gewerbe & Industrie)*** nach flexibler Unterstützung.

##### 📋 Fertige Vorlage für Ihre Kleinanzeigen-Anzeige:

> **Anzeigentitel:**  
> `100 % Remote: Dipl.-Ing. übernimmt CNC/CAM-Programmierung (3-5 Achsen) & Postprozessor-Anpassung (Heidenhain / Siemens / Haas)`
> 
> **Anzeigentext:**  
> Guten Tag,  
> haben Sie in Ihrer Fertigung Programmier-Engpässe, krankheitsbedingte Ausfälle oder benötigen Sie einen maßgeschneiderten Postprozessor für Ihre CNC-Fräsmaschine?  
> 
> Als **Diplom-Ingenieur & Senior Software Engineer** unterstütze ich Zerspanungsbetriebe, Lohnfertiger und Werkzeugbauer zuverlässig und zu **100 % digital (Remote)**:  
> 
> **Mein Leistungsspektrum:**  
> • **CAM-Programmierung (3-Achs bis 5-Achs simultan):** Erstellung fertiger NC-Programme für Aluminium, Stahl, Edelstahl und Kunststoffe.  
> • **Postprozessor-Entwicklung & Anpassung:** Maßgeschneiderte `.cps`-Postprozessoren für Autodesk Fusion 360 *(Heidenhain Klartext, Siemens Sinumerik 840D, Fanuc, Haas NGC)*.  
> • **100 % Kollisionsschutz vor dem ersten Span:** Jedes Programm wird durch eine digitale 3D-Simulation und automatische `Z-MIN`-Berechnung gegen Schraubstock-Crashs abgesichert.  
> • **Lieferumfang:** Fertige `.NC`-Maschinendatei, ausdruckbares Einrichteblatt (PDF) und ein **30-Sekunden-Simulationsvideo zur Vorab-Freigabe**.  
> 
> **Ablauf:**  
> 1. Sie senden mir Ihr 3D-CAD-Modell (`.step` oder `.stl`) und die Maschinenangabe per E-Mail.  
> 2. Sie erhalten vorab ein kurzes 3D-Simulationsvideo zur Freigabe.  
> 3. Schnelle und diskrete Umsetzung – ideal für Auftragsspitzen am Feierabend und Wochenende.  
> 
> Kontaktieren Sie mich gerne mit einer Zeichnung oder einem 3D-Modell für ein unverbindliches Festpreisangebot!  
> 
> **Ingenieurbüro für CAD/CAM-Technik**  
> Dipl.-Ing. Dipl.-Ing. Bujanovski  
> E-Mail: [Ihre geschäftliche E-Mail]  
> Sitz: 63526 Erlensee / 100 % Remote deutschlandweit
> 
> *(Rechnungsstellung erfolgt offiziell nach § 18 EStG als freiberuflicher Ingenieur).*

##### 📸 Welche Bilder laden Sie in der Anzeige hoch?
1. Ein Screenshot unseres 3D-Simulators: [`kundenauftrag_01_flanschplatte/3d_auftrag_simulator.html`](file:///c:/Projekte/CNC/01_Kundenauftraege/referenz_auftrag_flanschplatte/3d_auftrag_simulator.html).
2. Unser technisches CAD-Diagramm: [`docs/bilder/cnc_anfahrbewegung_lead_in_erklaerung.jpg`](file:///c:/Projekte/CNC/03_Fachdokumentation_und_Wissen/docs/bilder/cnc_anfahrbewegung_lead_in_erklaerung.jpg).
3. Das Schaubild der Spannsituation: [`docs/bilder/cnc_z_min_crash_prevention.jpg`](file:///c:/Projekte/CNC/03_Fachdokumentation_und_Wissen/docs/bilder/cnc_z_min_crash_prevention.jpg).

---

#### 2. Kanal 2: Fachforen – IndustryArena / CNC-Arena (`de.industryarena.com`)
Die **CNC-Arena** ist mit über 500.000 Mitgliedern die größte deutschsprachige Plattform für Zerspaner:
* Registrieren Sie sich mit Ihrem Ingenieurtitel *(z. B. `Dipl.-Ing. [Name] | CAM & Postprozessoren`)*.
* Schauen Sie in die Rubrik: **„Auftragsvergabe / Freie Kapazitäten“** – dort posten Firmen regelmäßig: *„Wer kann uns kurzfristig ein Teil programmieren?“*.
* Schreiben Sie kurze, fachlich fundierte Antworten in den Foren **„Heidenhain“**, **„Siemens Sinumerik“** und **„Postprozessoren“**.
* Fügen Sie in Ihre Foren-Signatur einen Link zu Ihrem Portfolio ein:  
  *„Freiberufliche CAM-Programmierung & Postprozessoren (100 % Remote) – Anfragen an: [E-Mail]“*.

---

#### 3. Kanal 3: Freelance-Projektportale *(Freelancermap.de, Malt.de, Gulp.de)*
Legen Sie ein kostenloses Profil auf **[Freelancermap.de](https://www.freelancermap.de)** und **[Malt.de](https://www.malt.de)** an:
* Setzen Sie den Filter zwingend auf: **`100 % Remote / Homeoffice`**.
* Wichtige Schlagworte *(Keywords)*: `CAM-Programmierer Remote`, `Postprozessor Entwicklung`, `Autodesk Fusion 360`, `Heidenhain TNC`, `Siemens Sinumerik 840D`, `Zerspanungstechnik`.
* Laden Sie unsere fertige Portfolio-Mappe hoch: [`Portfolio/Ingenieurbuero_CAD_CAM_Portfolio_Mappe.md`](file:///c:/Projekte/CNC/04_Recht_Steuern_und_Backoffice/Portfolio/Ingenieurbuero_CAD_CAM_Portfolio_Mappe.md).

---

#### 4. Kanal 4: Aktive Kunden-Recherche durch KI-Agent 1 (`Lead-Scout-Agent`)
Sie müssen nicht warten, bis jemand Ihre Anzeige liest! **`Agent 1 (Lead-Scout-Agent)`** durchsucht für Sie das Web nach metallverarbeitenden Betrieben im DACH-Raum *(Deutschland, Österreich, Schweiz)*:

Kopieren Sie diesen Prompt in den Chat, um Agent 1 zu starten:
```text
Starte AGENT 1 (Lead-Scout-Agent):
Recherchiere 5 reale CNC-Lohnfertiger oder Zerspanungsbetriebe (5 bis 30 Mitarbeiter) in Hessen / Bayern oder deutschlandweit, die 3- oder 5-Achs-Fräsmaschinen (Haas, DMG MORI, Hermle) im Maschinenpark haben.
Erstelle für jede Firma eine individuelle, professionelle Kooperations-E-Mail (ohne KI-Floskeln) mit dem Angebot unseres 100 % digitalen CAM-Dienstes bei Programmierengpässen.
```
Agent 1 listet Ihnen die Firmen mit Ansprechpartnern auf und schreibt für jede Firma die passende E-Mail vor – Sie müssen nur noch auf „Senden“ klicken!

---

#### 5. Kanal 5: CAM-Systemhäuser anschreiben *(Der Königsweg für Daueraufträge!)*
Das ist der lukrativste Kanal von allen:
* Schreiben Sie Software-Häuser an, die Autodesk Fusion, Siemens NX oder SolidCAM verkaufen *(z. B. Mensch und Maschine, JANUS Engineering, SolidCAM GmbH)*.
* Diese Firmen ertrinken oft in Postprozessor-Anfragen von Kunden und suchen händeringend nach fähigen externen Software-Entwicklern auf Honorarbasis.
* **Der unschlagbare Vorteil:** Wenn Sie ein einziges Systemhaus als freier Entwickler gelistet hat, bekommen Sie **Daueraufträge frei Haus**, ohne je wieder eine einzige Anzeige schalten zu müssen!  
*(Eine Liste von 10 konkreten Systemhäusern und ein fertiges Anschreiben finden Sie in [`CAM_Nebentaetigkeit_und_Gewerbe_Leitfaden.md#L830`](file:///c:/Projekte/CNC/04_Recht_Steuern_und_Backoffice/CAM_Nebentaetigkeit_und_Gewerbe_Leitfaden.md#L830)).*

---

### 📩 Phase 1: Die Kundenanfrage & das Angebot (10 Minuten)

* **🤖 Eingesetzter KI-Assistent:** **`Agent 4 (Backoffice-Ingenieur-Agent)`**
* **Was der Agent dir abnimmt:** Du musst kein Angebot von Hand tippen! Du sagst Agent 4 im Chat einfach deinen Befehl, und Agent 4 füllt in 5 Sekunden die Vorlage [`Vorlagen_Vertraege_Rechnungen/Vorlage_Angebot_und_Rechnung_Ingenieurbuero.md`](file:///c:/Projekte/CNC/04_Recht_Steuern_und_Backoffice/Vorlagen_Vertraege_Rechnungen/Vorlage_Angebot_und_Rechnung_Ingenieurbuero.md) inklusive **§ 18 EStG Ingenieurklausel** *(Steuerrechtliche Kennzeichnung als freiberuflicher Ingenieur ohne Gewerbesteuerpflicht)* und **Haftungsausschluss** aus!

#### 📋 Exakter Copy-Paste-Prompt zum Starten von Agent 4 (Angebot & 50 % Anzahlung):
Kopiere diesen Textblock einfach in das Chat-Eingabefeld:
```text
Starte AGENT 4 (Backoffice-Ingenieur-Agent):
Erstelle ein offizielles Angebot für folgenden Kunden:
- Kunde: [Firmenname, Ansprechpartner, Ort, z. B. Fa. Präzisionsbau Schmidt, Herr Müller, Kassel]
- Bauteil: [Name des 3D-Modells, Material, z. B. Flanschplatte Alu EN AW-6082, 80x50x12 mm]
- Maschinentyp: [z. B. Haas VF-2 oder Siemens Sinumerik 840D]
- Festpreis: [z. B. 240,00 €] netto (zzgl. MwSt.)
- Zahlungsbedingung: 50 % Anzahlung bei Auftragserteilung, restliche 50 % nach Vorlage des 3D-Simulations-Freigabevideos vor Code-Übergabe.
Fülle die Datei Vorlagen_Vertraege_Rechnungen/Vorlage_Angebot_und_Rechnung_Ingenieurbuero.md inklusive § 18 EStG Klausel und Haftungsausschluss vollständig aus!
```

1. **Die Kunden-E-Mail trifft ein:**  
   Der Kunde *(z. B. eine Fräserei)* schickt Ihnen:
   * Die 3D-CAD-Datei *(z. B. `bauteil.step` oder `flanschplatte.stl`)*.
   * Die Maschinenangabe *(z. B. „Haas VF-2“ oder „Hermle mit Heidenhain TNC 640“)*.
   * Die Stückzahl und das Material *(z. B. Aluminium EN AW-6082)*.
2. **Angebot schreiben:**  
   Sie öffnen unsere Vorlage [`Vorlagen_Vertraege_Rechnungen/Vorlage_Angebot_und_Rechnung_Ingenieurbuero.md`](file:///c:/Projekte/CNC/04_Recht_Steuern_und_Backoffice/Vorlagen_Vertraege_Rechnungen/Vorlage_Angebot_und_Rechnung_Ingenieurbuero.md) oder lassen sie von Agent 4 mit dem obigen Prompt ausfüllen.
   * Typischer Preis: **180 € bis 350 €** für ein 3-Achs-Bauteil.
   * **Die goldene Zahlungsbedingung im Angebot:**  
     *„50 % Anzahlung bei Auftragserteilung. Restliche 50 % nach Vorlage des 3D-Simulations-Freigabevideos vor Code-Übergabe.“*
3. **Anzahlung abwarten:**  
   Sobald die 50 % Anzahlung eingegangen sind, starten Sie mit der Bearbeitung!

---

### ⚙️ Phase 2: Postprozessor vorbereiten (1 Minute)

* **🤖 Eingesetzte Werkzeuge:** Web-Interface [`kunden_cps_generator_web.html`](file:///C:/Projekte/CNC/02_Software_und_Tools/web_tools/kunden_cps_generator_web.html) & **`Agent 2 (Postprocessor-Coder-Agent)`**
* **Was der Agent / das Tool dir abnimmt:**
  * Wenn es eine Standard-Maschine ist *(Haas, Siemens, Fanuc, Heidenhain)*: Nutzen Sie direkt das Web-Interface [`kunden_cps_generator_web.html`](file:///C:/Projekte/CNC/02_Software_und_Tools/web_tools/kunden_cps_generator_web.html).
  * Wenn der Kunde Sonderwünsche hat *(z. B. Laser-Werkzeugbruchkontrolle `TCH PROBE 586` oder Schwenkzyklen `CYCLE800`)*: Rufen Sie Agent 2 mit dem untenstehenden Befehl auf! Agent 2 schreibt den JavaScript-Code direkt in die `.cps`-Datei *(Custom Postprocessor Script - Steuerungsdatei)*!

#### 💻 Programm direkt im Browser oder Terminal aufrufen:
* **Option A (Browser per Doppelklick):** Öffnen Sie [`kunden_cps_generator_web.html`](file:///C:/Projekte/CNC/02_Software_und_Tools/web_tools/kunden_cps_generator_web.html) mit einem beliebigen Webbrowser *(Chrome, Edge, Firefox)*.
* **Option B (Per PowerShell-Befehl ausführen):**
  ```powershell
  Start-Process "C:\Projekte\CNC\kunden_cps_generator_web.html"
  ```
* **Option C (Per Node.js CLI-Skript automatisieren):**
  ```powershell
  node scripts/kunden_cps_generator.js --kunde "Schmidt Zerspanung" --maschine "haas" --zmin --tuer --output "schmidt_haas.cps"
  ```

#### 📋 Exakter Copy-Paste-Prompt zum Starten von Agent 2 (Sonderfunktionen & Postprozessor-Code):
Kopiere diesen Textblock in den Chat, wenn ein Kunde spezielle Zyklen oder Maschinenbefehle verlangt:
```text
Starte AGENT 2 (Postprocessor-Coder-Agent):
Ich habe einen Kundenauftrag für folgende Maschine und Steuerung:
- Maschinentyp / Steuerung: [z. B. Heidenhain TNC 640 oder Haas NGC / Siemens 840D]
- Kunde / Projekt: [z. B. Fa. Schmidt Zerspanungstechnik / Flanschplatte]
Folgende kundenspezifische Anpassungen in der .cps-Datei sind erforderlich:
- [z. B. Nach jedem Werkzeugwechsel M06 Laser-Bruchkontrolle TCH PROBE 586 ausgeben]
- [z. B. Tisch am Programmende mit M91 auf Y+0 fahren (Tisch zur Bedienertür)]
- [z. B. Z-MIN Tiefenprüfung im Kopfbereich des Programms als Kommentarzeile einfügen]
Passe die Datei an, speichere sie und dokumentiere alle geänderten Code-Zeilen mit präzisen Erläuterungen in Klammern (...).
```

1. Öffnen Sie per Doppelklick:  
   👉 [`kunden_cps_generator_web.html`](file:///C:/Projekte/CNC/02_Software_und_Tools/web_tools/kunden_cps_generator_web.html)
2. Tragen Sie den Kundennamen ein.
3. Klicken Sie auf die passende Maschinen-Kachel *(z. B. 🟡 Haas oder 🔵 Siemens)*.
4. Prüfen Sie, ob **`Z-MIN Tiefenprüfung`** und **`Tisch zur Tür fahren`** angehakt sind.
5. Klicken Sie auf **„📥 .cps-Datei herunterladen“**.
6. Sie haben nun Ihre maßgeschneiderte Postprozessor-Datei *(z. B. `schmidt_haas.cps`)* auf Ihrem Laptop!

---

### 💻 Phase 3: Postprozessor-Code anpassen & Funktionen einbinden (Weg A – Dein Hauptfokus!)

* **🤖 Eingesetzte Werkzeuge:** **`Agent 2 (Postprocessor-Coder-Agent)` & [`kunden_cps_generator_web.html`](file:///C:/Projekte/CNC/02_Software_und_Tools/web_tools/kunden_cps_generator_web.html)**
* **👤 Deine 20 % Kernaufgabe (Mensch / Senior Software Engineer):** Du musst **kein einziges 3D-Modell in Fusion 360 mit der Maus anklicken!** Deine Aufgabe ist reines, hochbezahltes Software-Engineering:
  1. Du schaust dir kurz die geänderten JavaScript-Zeilen in der `.cps`-Datei an *(Code-Review in VS Code)*.
  2. Du vergleichst die Syntax mit dem Referenz-NC-Programm des Kunden.
  3. Du gibst den Code frei.

#### 🛠️ Was hier technisch im Postprozessor angepasst wird:
1. **Programmkopf (`onOpen`):** Z-MIN Tiefenprüfung, Einheiten `G21 (mm)`, Sicherheitsabstand und Werkzeugtabelle einbinden.
2. **Werkzeugwechsel (`onSection`):** Innenkühlung `M88` *(Haas)* oder `M07` *(Siemens)* aktivieren, Spindeldrehzahl `S` und Rechtslauf `M03` absichern.
3. **Programmende (`onClose`):** Tisch am Ende automatisch ganz nach vorne an die Schiebetür fahren (`G53 G00 Y0.` bei Haas/Fanuc, `L Y+0 R0 FMAX M91` bei Heidenhain oder `SUPA G0 Y0` bei Siemens).

#### 📋 Exakter Copy-Paste-Prompt für Agent 2 in Phase 3:
```text
Starte AGENT 2 (Postprocessor-Coder-Agent):
Passe den Postprozessor [Pfad zur .cps-Datei] für folgenden Kunden an:
- Kunde: [Firmenname]
- Steuerung: [z. B. Haas NGC / Heidenhain TNC 640 / Siemens 840D]
- Sonderwünsche: [z. B. Tisch zur Tür G53 Y0, Z-MIN im Header, Innenkühlung M88]
Führe die Änderungen direkt im JavaScript-Code durch und dokumentiere jede geänderte Zeile mit Erläuterungen in Klammern (...).
```

---

#### 📦 *Optionaler Alternativweg (Nur für Weg B – Falls jemals ein Kunde explizit ein Einzelteil gefräst haben will):*
*(Wenn du dich auf reine Postprozessor- und Software-Aufträge konzentrierst, überspringst du diesen Kasten komplett!)*  
Falls du ausnahmsweise doch ein einfaches Bauteil programmieren möchtest, klickst du die 4 Standard-Operationen streng nach unserer Klick-Anleitung [`kundenauftrag_01_flanschplatte/KUNDEN_AUFTRAG_UND_KLICK_ANLEITUNG.md`](file:///C:/Projekte/CNC/01_Kundenauftraege/referenz_auftrag_flanschplatte/KUNDEN_AUFTRAG_UND_KLICK_ANLEITUNG.md) kurz ab *(Setup G54 vorne links oben, Planen, 2D-Kontur, Bohren G83)*.

---

### 📄 Phase 4: G-Code erzeugen & 5-Stufen-Sicherheitscheck (1 Minute)

* **🤖 Eingesetzte Werkzeuge:** **`Dein .cps-Postprozessor` & `Agent 3 (NC-Safety-Agent)`**
* **Was hier passiert:** Der Postprozessor übersetzt die 3D-Pfade in sauberen Maschinencode. Danach prüft Agent 3 den Maschinencode automatisch anhand der Checkliste aus [`SICHERHEITS_UND_QUALITAETS_PRUEFLISTE_GCODE.md`](file:///c:/Projekte/CNC/03_Fachdokumentation_und_Wissen/SICHERHEITS_UND_QUALITAETS_PRUEFLISTE_GCODE.md) *(Sicherheitszeile `G90 G17...`, Spindeldrehzahl vor Eintauchen, Z-MIN)*.

#### 📋 Exakter Copy-Paste-Prompt zum Starten von Agent 3 (NC-Safety-Check):
Kopiere diesen Textblock in den Chat, um den automatischen 5-Punkte-Crash-Check durchzuführen:
```text
Starte AGENT 3 (NC-Safety- & Setup-Agent):
Prüfe die fertige G-Code-Datei [z. B. kundenauftrag_01_flanschplatte/1001.nc] anhand unserer SICHERHEITS_UND_QUALITAETS_PRUEFLISTE_GCODE.md:
1. Sicherheitszeile prüfen: Sind Modale Befehle (G90 Absolutmaß, G17 XY-Ebene, G40 Radiuskorrektur aus, G80 Zyklen aus) in Satz N10 aktiv?
2. Spindelhochlauf: Startet M03 mit programmierter Drehzahl S vor dem ersten Z-Eintauchen ins Material?
3. Kühlmittelprüfung: Ist M08 (oder M88 Innenkühlung) vor dem Schnitt aktiv und M09 am Programmende gesetzt?
4. Z-MIN Tiefenkontrolle: Ermittle die absolut tiefste Z-Koordinate und gleiche sie mit der Schraubstock-Einspanntiefe (z. B. Z = -15.0 mm) ab. Besteht Kollisionsgefahr mit den Stahlbacken?
5. Gib das Prüfergebnis als übersichtliche Tabelle mit Ampelsymbolen (GRÜN / ROT) aus!
```

#### 💻 Durchführung in Fusion 360:
1. In Fusion 360 oben auf **`NC-Programm / Postprozess (Strg + P)`** klicken.
2. Bei **„Post-Konfiguration“** Ihre in Phase 2 erzeugte `.cps`-Datei auswählen.
3. Auf **`Postprozessieren (Post)`** klicken.
4. Fusion 360 schreibt die fertige **`.nc`-Datei** auf Ihre Festplatte!

---

### 🎥 Phase 5: Das 3D-Kunden-Freigabevideo aufnehmen (2 Minuten)

* **🤖 Eingesetzte Werkzeuge:** **`Agent 3` & [`cnc_video_generator_web.html`](file:///C:/Projekte/CNC/02_Software_und_Tools/web_tools/cnc_video_generator_web.html)**
* **Was hier passiert:** Das Web-Studio nimmt den echten Maschinencode (`.nc`), prüft live die Z-MIN-Höhe gegen die Spannbacken und rendert ein glasklares 30-Sekunden-Video mit Ihrem Ingenieurbüro-Wasserzeichen.

#### 💻 Programm / Web-Studio direkt aufrufen:
* **Option A (Web-Studio im Browser):** Öffnen Sie per Doppelklick die Datei [`cnc_video_generator_web.html`](file:///C:/Projekte/CNC/02_Software_und_Tools/web_tools/cnc_video_generator_web.html)
* **Option B (Per PowerShell-Befehl starten):**
  ```powershell
  Start-Process "C:\Projekte\CNC\cnc_video_generator_web.html"
  ```
* **Option C (Per Python & FFmpeg vollautomatisch als MP4 rendern):**
  ```powershell
  python scripts/render_simulation_video.py --gcode "kundenauftrag_01_flanschplatte/1001.nc" --output "docs/videos/kunden_freigabe.mp4"
  ```

#### 📋 Klick-Schritte im Web-Studio:
1. Ziehen Sie Ihre in Phase 4 erzeugte `.nc`-Datei per Drag & Drop in das Fenster *(oder wählen Sie das Preset aus)*.
2. Tragen Sie den Kundennamen ein.
3. Klicken Sie auf den roten Button **„🔴 Video-Aufnahme starten“**.
4. Das Tool spielt die Fräsbewegungen mit 30 FPS *(Bilder pro Sekunde)* im 3D-Raum ab, blendet Ihr Ingenieurbüro-Wasserzeichen ein und prüft live die Z-MIN Tiefe.
5. Nach Durchlauf öffnet sich das Vorschaufenster: Klicken Sie auf **„📥 Video herunterladen“** *(speichert z. B. `Freigabe_Simulation_Kunde.webm` oder `.mp4`)*.

---

### 💰 Phase 6: Vorab-Freigabe & 2. Teilzahlung anfordern (5 Minuten)

* **🤖 Eingesetzter KI-Assistent:** **`Agent 4 (Backoffice-Ingenieur-Agent)`**
* **Was der Agent dir abnimmt:** Schreibt die professionelle Freigabe-E-Mail und fügt die Teilrechnung bei.

#### 📋 Exakter Copy-Paste-Prompt zum Starten von Agent 4 (Freigabe-E-Mail & 2. Teilzahlung):
Kopiere diesen Textblock in den Chat:
```text
Starte AGENT 4 (Backoffice-Ingenieur-Agent):
Die CAM-Programmierung und das 3D-Simulationsvideo für folgenden Auftrag sind fertiggestellt:
- Kunde: [Firmenname, Ansprechpartner, E-Mail, z. B. Fa. Schmidt Zerspanung, Herr Müller]
- Bauteil: [Name des Bauteils, z. B. Flanschplatte Alu EN AW-6082]
- Z-MIN Tiefe: [z. B. -12.0 mm, kollisionsfrei geprüft gegen Schraubstock]
- Bearbeitungszeit: [z. B. 4 Minuten 30 Sekunden]
- Restbetrag (50 % Schlussrate): [z. B. 120,00 €] netto
Erstelle die professionelle Freigabe-E-Mail (lebendiger Ingenieur-Stil ohne KI-Floskeln) mit Verweis auf das beigefügte 30-Sekunden-Video und lege die Rechnung über den Restbetrag bei!
```

Sie versenden die von Agent 4 erstellte E-Mail an Ihren Kunden:

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
> Dipl.-Ing. Bujanovski – CAD/CAM Ingenieurbüro

👉 **Der psychologische Effekt:** Der Kunde sieht das Video, ist begeistert, weil er genau sieht, dass alles passt, gibt die Freigabe und überweist sofort das Geld!

---

### 📦 Phase 7: Finale Auslieferung & Projektabschluss

* **🤖 Eingesetzte KI-Assistenten:** **`Agent 3` (erzeugt Einrichteblatt) & `Agent 4` (verbucht Zahlung)**
* **Was vollautomatisch passiert:**
  * Agent 3 führt das Skript [`GitHub_Projekte/cnc_setup_sheet_extractor.py`](file:///c:/Projekte/CNC/02_Software_und_Tools/GitHub_Projekte/cnc_setup_sheet_extractor.py) aus und füllt in 3 Sekunden das fertige Einrichteblatt [`Portfolio/Vorlage_Einrichteblatt_und_Werkzeugliste.md`](file:///c:/Projekte/CNC/04_Recht_Steuern_und_Backoffice/Portfolio/Vorlage_Einrichteblatt_und_Werkzeugliste.md) mit allen Werkzeuglängen, Drehzahlen und Nullpunkten aus!
  * Agent 4 erstellt die Schlussrechnung mit bezahltem Stempel und das Begleitschreiben.

#### 💻 Einrichteblatt direkt per Terminal-Befehl erzeugen:
```powershell
python GitHub_Projekte/cnc_setup_sheet_extractor.py "kundenauftrag_01_flanschplatte/1001.nc" --output "docs/Einrichteblatt_Kunde.md"
```

#### 📋 Exakter Copy-Paste-Prompt zum Starten von Agent 3 & Agent 4 (Auslieferung & Quittung):
Kopiere diesen Textblock in den Chat:
```text
Starte AGENT 3 & AGENT 4 (Rüstplan & Projektabschluss):
Der Kunde [Firmenname] hat das 3D-Freigabevideo bestätigt und die restliche Zahlung überwiesen.
1. AGENT 3: Führe cnc_setup_sheet_extractor.py auf [Pfad zur .nc-Datei] aus und erstelle das fertige Einrichteblatt mit Werkzeugliste, T-Nummern, Drehzahlen F/S und Nullpunkten G54!
2. AGENT 4: Erstelle die finale Auslieferungs-E-Mail für die .NC-Datei sowie die offizielle Schlussrechnung mit Vermerk "VOLLSTÄNDIG BEZAHLT / QUITTUNG" für die Buchhaltung des Kunden!
```

Sobald das Geld auf Ihrem Konto gutgeschrieben ist:
1. **Liefer-E-Mail an den Kunden senden:**  
   Sie hängen die fertige **`.nc`-Datei** und das **Einrichteblatt (PDF)** an.
2. **Schlussrechnung beilegen:**  
   Die bezahlte Gesamtrechnung beilegen.
3. **Auftrag zu 100 % erfolgreich und rechtssicher abgeschlossen!**

---

## 📌 Schnell-Spickzettel: Die 3 Web-Tools auf einen Blick

* ⚙️ **Postprozessor bauen / anpassen:** [`kunden_cps_generator_web.html`](file:///C:/Projekte/CNC/02_Software_und_Tools/web_tools/kunden_cps_generator_web.html)
* 🎥 **Kunden-Freigabevideo aufnehmen:** [`cnc_video_generator_web.html`](file:///C:/Projekte/CNC/02_Software_und_Tools/web_tools/cnc_video_generator_web.html)
* 🔍 **G-Code Satz für Satz im 3D-Detail analysieren:** [`kundenauftrag_01_flanschplatte/3d_auftrag_simulator.html`](file:///c:/Projekte/CNC/01_Kundenauftraege/referenz_auftrag_flanschplatte/3d_auftrag_simulator.html)

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
> Dipl.-Ing. Bujanovski – Diplom-Ingenieur & Senior Software Engineer

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
> Dipl.-Ing. Bujanovski – CAD/CAM Ingenieurbüro

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
> Dipl.-Ing. Bujanovski – CAD/CAM Ingenieurbüro

---

## 🤖 10. Konkrete Befehle (Prompts), um deine 4 KI-Agenten im Chat zu starten

Damit du die Agenten nicht jedes Mal neu anweisen musst, sind hier die **fertigen Befehle *(Prompts)***, die du einfach kopieren und in den Chat eingeben kannst:

### 0. Neukunden & Systemhäuser finden: Agent 1 (Lead-Scout-Agent)
Kopiere diesen Text in den Chat:
```text
Starte AGENT 1 (Lead-Scout-Agent):
Recherchiere 5 reale CNC-Lohnfertiger oder Zerspanungsbetriebe (5 bis 30 Mitarbeiter) in Hessen / Bayern oder deutschlandweit, die 3- oder 5-Achs-Fräsmaschinen (Haas, DMG MORI, Hermle) im Maschinenpark haben.
Erstelle für jede Firma eine individuelle, professionelle Kooperations-E-Mail (ohne KI-Floskeln) mit dem Angebot unseres 100 % digitalen CAM-Dienstes bei Programmierengpässen.
```

---

### 1. Bei neuem Kundenkontakt: Angebot erstellen mit Agent 4
Kopiere diesen Text in den Chat:
```text
Starte AGENT 4 (Backoffice-Ingenieur-Agent):
Erstelle ein offizielles Angebot für folgenden Kunden:
- Kunde: [Firmenname, Ansprechpartner, Ort]
- Bauteil: [Name des 3D-Modells, Material, z. B. Alu 80x50x12 mm]
- Maschinentyp: [z. B. Haas VF-2 oder Siemens 840D]
- Festpreis: [z. B. 240,00 €] netto
- Zahlungsbedingung: 50 % Anzahlung, Rest nach Vorlage des 3D-Simulations-Freigabevideos.
Fülle die Datei Vorlagen_Vertraege_Rechnungen/Vorlage_Angebot_und_Rechnung_Ingenieurbuero.md aus!
```

---

### 2. Wenn der Postprozessor Sonderfunktionen braucht: Agent 2 rufen
Kopiere diesen Text in den Chat:
```text
Starte AGENT 2 (Postprocessor-Coder-Agent):
Ich habe einen Kundenauftrag für eine [Maschinentyp, z. B. Heidenhain TNC 640].
Der Kunde wünscht folgende Besonderheit:
- [z. B. Nach jedem Werkzeugwechsel Laser-Bruchkontrolle TCH PROBE 586 ausgeben]
- [z. B. Tisch am Programmende mit M91 auf Y+0 fahren]
Passe den Postprozessor an und dokumentiere die Änderungen in deutscher Sprache.
```

---

### 3. Vor dem Video und der Auslieferung: Crash-Check & Einrichteblatt mit Agent 3
Kopiere diesen Text in den Chat:
```text
Starte AGENT 3 (NC-Safety- & Setup-Agent):
Prüfe die fertige G-Code-Datei [tests/mein_generierter_gcode.nc] anhand unserer SICHERHEITS_UND_QUALITAETS_PRUEFLISTE_GCODE.md:
1. Prüfe Sicherheitszeile, Drehzahl M03 und Kühlmittel.
2. Ermittle Z-MIN und vergleiche es mit den Schraubstockbacken Z = -15.0 mm.
3. Führe cnc_setup_sheet_extractor.py aus und erstelle das fertige Einrichteblatt für den Kunden!
```

---

### 4. Nach der Freigabe: Schlussrechnung mit Agent 4
Kopiere diesen Text in den Chat:
```text
Starte AGENT 4 (Backoffice-Ingenieur-Agent):
Der Kunde [Firmenname] hat das 3D-Simulationsvideo freigegeben und die 2. Rate überwiesen.
Erstelle die finale Schlussrechnung (mit Status: VOLLSTÄNDIG BEZAHLT) und das Begleitschreiben zur Auslieferung der .NC-Datei!
```

---

### 💡 Fazit für deinen Arbeitsalltag:
* Du öffnest Autodesk Fusion 360 und klickst kurz die 3D-Kanten an.
* Alle lästigen Nebenarbeiten *(Angebot, Postprozessor-Syntax, 5-Punkte-Crash-Check, Rüstblatt und Rechnungen)* erledigen deine **4 KI-Agenten** in Sekundenschnelle auf Zuruf!



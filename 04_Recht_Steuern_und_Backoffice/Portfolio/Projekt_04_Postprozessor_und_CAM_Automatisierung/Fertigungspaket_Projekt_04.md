# Fertigungspaket Projekt 04: Postprozessor-Engineering & CAM-Automatisierung

**Projekt-ID:** `REF-2026-04`  
**Leistungsbereich:** Kundenspezifische Postprozessor-Entwicklung *(JavaScript / Python / Tcl)* & Automatisierte Shopfloor-Dokumentation  
**Zielgruppe:** Zerspanungsbetriebe, bei denen Maschinenbediener nach dem Postprozessor-Lauf noch manuell im NC-Code editieren müssen.

---

## 1. Das Praxisproblem in 80 % aller CNC-Fertigungsbetriebe

In vielen Betrieben liefert das CAM-System über einen ungepflegten Standard-Postprozessor fehlerhaften oder unpraktischen Code:
* Der Maschinenbediener muss nach jedem CAM-Lauf von Hand `M`-Befehle *(Zusatzfunktionen wie Innenkühlung `M7`, Späneförderer oder Absaugung)* nachtragen.
* Es fehlen die **Mindest-Auskraglängen** im Programmkopf – der Einrichter spannt den Fräser $5\,\text{mm}$ zu kurz ein, und der Werkzeughalter kollidiert in einer tiefen Tasche mit dem Bauteil.
* Bei einem Werkzeugbruch (z. B. Bohrer $\varnothing\,4{,}2\,\text{mm}$) merkt die Maschine nichts, und der nachfolgende Gewindebohrer reißt im Werkstück ab.

---

## 2. Vorher-/Nachher-Vergleich: Standard-CAM-Ausgabe vs. Angepasster Ingenieur-Postprozessor

### ❌ VORHER: Typische ungefilterte Standard-Postprozessor-Ausgabe
```text
0 BEGIN PGM TEIL1 MM
1 TOOL CALL 5 Z S4500
2 L Z+100 R0 FMAX
3 L X+20 Y+15 R0 FMAX M3
4 L Z+2 R0 FMAX M8
5 L Z-25 F600
6 L Z+100 R0 FMAX M30
7 END PGM TEIL1 MM
```
*(Kritik: Kein Rohteil definiert, keine Info welches Werkzeug T5 überhaupt ist, keine Mindest-Auskraglänge, kein Bezugspunkt-Aufruf, keine Innenkühlung, keine Werkzeugbruchkontrolle!)*

---

### ✅ NACHHER: Ausgabe meines maßgeschneiderten Postprozessors (100 % „Push-Button-Ready“)
```text
0  BEGIN PGM TEIL1_PRODUKTION MM
1  ; =====================================================================
2  ; AUTOMATISCH GENERIERTER HEADER (KEINE MANUELLE AENDERUNG NOETIG)
3  ; DATUM / ZEIT      : 17.10.2026 - 20:30 UHR
4  ; CAM-PROJEKT       : KUNDENAUFTRAG_4092_REV_B
5  ; NULLPUNKT (PRESET): Q339 = +1 (X0=MITTE / Y0=MITTE / Z0=OBERKANTE)
6  ; GESAMT-LAUFZEIT   : 08 MIN 14 SEK
7  ; ---------------------------------------------------------------------
8  ; VERWENDETE WERKZEUGE & MINDEST-AUSKRAGLAENGE (KOLLISIONSSCHUTZ!):
9  ; T5  | VHM-BOHRER D6.8 5xD IKZ | D=6.80 | R=0.00 | L_MIN = 42.0 MM !
10 ; =====================================================================
11 BLK FORM 0.1 Z X-50 Y-40 Z-35
12 BLK FORM 0.2 X+50 Y+40 Z+0
13 ;
14 ; --- SICHERHEITS-INITIALISIERUNG ---
15 L Z+250 R0 FMAX M91
16 PLANE RESET TURN FMAX
17 CYCL DEF 247 BEZUGSPUNKT SETZEN ~
    Q339=+1    ;BEZUGSPUNKT-NUMMER
18 ;
19 ; =====================================================================
20 ; OP 50: KERNLOCHBOHREN 6x M8 (TIEFE 25.0 MM)
21 ; WERKZEUG: T5 - VHM-BOHRER D6.8 (MINDEST-AUSKRAGLAENGE: 42.0 MM)
22 ; =====================================================================
23 TOOL CALL 5 Z S5150 F824
24 L Z+250 R0 FMAX M91
25 L X+20 Y+15 R0 FMAX M3 M7 ; AUTOMATISCH IKZ (M7) BEI INNENKUEHLUNGS-BOHRER!
26 CYCL DEF 200 BOHREN ~
    Q200=+2    ;SICHERHEITS-ABST. ~
    Q201=-25   ;TIEFE ~
    Q206=+824  ;VORSCHUB TIEFENZUST. ~
    Q202=+25   ;ZUSTELL-TIEFE ~
    Q210=+0    ;VERWEILZEIT OBEN ~
    Q203=+0    ;KOOR. OBERFLAECHE ~
    Q204=+50   ;2. SICHERHEITS-ABST. ~
    Q211=+0.1  ;VERWEILZEIT UNTEN ~
    Q395=+0    ;BEZUG TIEFE
27 CYCL CALL
28 L Z+250 R0 FMAX M91 M9 M5
29 ;
30 ; --- AUTOMATISCHE LASER-WERKZEUGBRUCHKONTROLLE NACH BOHRZYKLUS ---
31 TCH PROBE 586 WERKZEUGBRUCH ~
    Q356=+1    ;MESSRICHTUNG ~
    Q357=+2.0  ;SICHERHEITSABSTAND ~
    Q359=+0.5  ;BRUCHTOLERANZ LAENGE
32 ;
33 L Y+250 R0 FMAX M91 M30
34 END PGM TEIL1_PRODUKTION MM
```

---

## 3. Auszug aus der Postprozessor-Logik (Beispiel-Implementierung in JavaScript / CAM Post Engine)

Als **Software Engineer** implementiere ich direkt im Postprozessor intelligente Sicherheitsprüfungen, noch *bevor* die Datei auf die Maschine übertragen wird:

```javascript
/**
 * Automatische Prüfung im Postprozessor:
 * 1. Prüft, ob bei tiefen Bohrungen (> 3xD) automatisch Innenkühlung (IKZ / M7) aktiviert wird.
 * 2. Berechnet die erforderliche Mindest-Auskraglänge (L_min) inklusive 3 mm Sicherheitsabstand.
 * 3. Fügt bei kritischen Werkzeugen (D < 8 mm oder Gewindewerkzeugen) automatisch
 *    den Zyklus für die Werkzeugbruchkontrolle am Operationsende ein.
 */
function onSectionEnd() {
  var tool = getTool();
  var maxZDepth = Math.abs(getGlobalZRange().getMinimum());
  var safeFluteLength = Math.ceil(maxZDepth + 3.0);

  // Warnung im Header, falls Auskraglänge im CAM kürzer als die reale Frästiefe + 3mm ist
  if (tool.bodyLength < safeFluteLength) {
    writeComment(
      "WARNUNG: Werkzeug T" + tool.number +
      " benoetigt mindestens " + safeFluteLength + " mm Auskraglaenge!"
    );
  }

  // Automatische Werkzeugbruchkontrolle für Bohrer/Gewindewerkzeuge unter D = 8.0 mm
  if ((tool.type === TOOL_DRILL || tool.type === TOOL_TAP_RIGHT_HAND) && tool.diameter <= 8.0) {
    writeComment("--- AUTOMATISCHE WERKZEUGBRUCHKONTROLLE ---");
    writeBlock("TCH PROBE 586 WERKZEUGBRUCH ~");
    writeBlock("  Q356=+1    ;MESSRICHTUNG ~");
    writeBlock("  Q357=+2.0  ;SICHERHEITSABSTAND ~");
    writeBlock("  Q359=+0.5  ;BRUCHTOLERANZ LAENGE");
  }
}
```

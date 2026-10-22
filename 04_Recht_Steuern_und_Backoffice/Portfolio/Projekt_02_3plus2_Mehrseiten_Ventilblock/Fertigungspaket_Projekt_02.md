# Fertigungspaket Projekt 02: 3+2-Achsen-Mehrseitenbearbeitung (Hydraulik-Ventilblock)

**Projekt-ID:** `REF-2026-02`  
**Bauteil:** 5-Seiten-Hydraulikventilblock mit schrägen Tiefloch- und Anschlusskanälen  
**Werkstoff:** `EN AW-7075 T6 (3.4365)` – Hochfestes Flugzeug-Aluminium  
**Maschinenkinematik:** 5-Achs-Bearbeitungszentrum *(z. B. Hermle C 32 U oder DMG MORI DMU 50)* mit Dreh-Schwenktisch

---

## 1. Ingenieurtechnisches 5-Achsen-Spann- und Schwenkkonzept

* **Spannmittel:** 5-Achs-Zentrischspanner *(Lang Makro-Grip 125)* auf Pyramiden-Erhöhung, Formschluss-Prägung mit nur $3{,}0\,\text{mm}$ Spanntiefe.
* **Vorteil der 3+2-Komplettbearbeitung *(angestellte 5-Achs-Bearbeitung)***:
  * Alle 5 Raumseiten sowie die unter $\alpha = 35^\circ$ und $\beta = 60^\circ$ geneigten Hydraulik-Dichtflächen und Anschlussgewinde (`G 1/4"` und `M14x1,5`) werden in **einer einzigen Aufspannung** gefertigt.
  * **Null Umspannfehler:** Die schrägen Verbindungsbohrungen treffen im Inneren des Ventilblocks auf $\pm 0{,}02\,\text{mm}$ exakt aufeinander, was bei manuellem Umspannen in 3 Aufspannungen kaum prozesssicher erreichbar wäre.
* **Mathematische Ebenen-Transformation:**
  * Der Werkstücknullpunkt (`G54` / Bezugspunkt 1) liegt exakt im Schnittpunkt der Symmetrieachsen auf der Bauteiloberseite.
  * Die Steuerung verrechnet die Verschiebung des Nullpunkts beim Schwenken der Rundachsen automatisch über die hinterlegte **Kinematiktabelle *(Maschinen-Geometriemodell des Drehzentrums)*** mittels `PLANE SPATIAL` (Heidenhain) bzw. `CYCLE800` (Siemens).

---

## 2. Auszug aus dem erzeugten 3+2-Achsen-NC-Programm (Heidenhain Klartext `.H` – TNC 640)

```text
0  BEGIN PGM REF02_VENTILBLOCK_5ACHS MM
1  ; =====================================================================
2  ; PROJEKT    : REF-2026-02 HYDRAULIK-VENTILBLOCK EN AW-7075
3  ; KINEMATIK  : 5-ACHS (3+2 POSITIONIERBEARBEITUNG MIT PLANE SPATIAL)
4  ; AUFSPANNUNG: ZENTRISCHSPANNER MAKRO-GRIP (SPANNTIEFE 3.0 MM)
5  ; NULLPUNKT  : X0=MITTE / Y0=MITTE / Z0=OBERKANTE FERTIGTEIL
6  ; =====================================================================
7  BLK FORM 0.1 Z X-60 Y-60 Z-85
8  BLK FORM 0.2 X+60 Y+60 Z+0
9  ;
10 ; --- SICHERES ZURUECKSETZEN ALLER SCHWENKEBENEN VOR START ---
11 L Z+250 R0 FMAX M91 ; SICHERE MASCHINENPOSITION Z
12 PLANE RESET TURN FMAX
13 ;
14 ; --- BEARBEITUNG SCHRAEGFLAECHE SEITE 1 (RAUMWINKEL B+35 / C+90) ---
15 TOOL CALL 12 Z S10000 F2400 ; ALU-SCHLICHTFRAESER D16 Z3
16 L Z+250 R0 FMAX M91
17 CYCL DEF 247 BEZUGSPUNKT SETZEN ~
    Q339=+1    ;BEZUGSPUNKT-NUMMER
18 ; EBENEN-TRANSFORMATION MIT AUTOMATISCHEM EINSCHWENKEN (TURN MB MAX)
19 PLANE SPATIAL SPA+0 SPB+35 SPC+90 TURN MB MAX FMAX SEQ- TABLE ROT
20 ; NULLPUNKT LOKAL AUF SCHRAEGFLAECHE VERSCHIEBEN (CYCL DEF 7)
21 CYCL DEF 7.0 NULLPUNKT
22 CYCL DEF 7.1 X+25.000
23 CYCL DEF 7.2 Y+0.000
24 CYCL DEF 7.3 Z-18.500
25 L X+0 Y+0 R0 FMAX M3 M8
26 L Z+50 R0 FMAX
27 L Z+2 R0 FMAX
28 ; PLANFRAESEN DER DICHTFLAECHE UND ZIRKULARES SENKEN D28 H7
29 L Z+0 R0 F800
30 L X+8 Y+0 RL F1800
31 CC X+0 Y+0
32 C X+8 Y+0 DR+
33 L X+0 Y+0 R0 F2000
34 L Z+100 R0 FMAX M9
35 ;
36 ; --- SAUBERES RUECKSCHWENKEN IN DIE GRUNDEBENEN-STELLUNG ---
37 CYCL DEF 7.0 NULLPUNKT
38 CYCL DEF 7.1 X+0
39 CYCL DEF 7.2 Y+0
40 CYCL DEF 7.3 Z+0
41 L Z+250 R0 FMAX M91
42 PLANE RESET TURN MB MAX FMAX
43 L Y+250 R0 FMAX M91 M5 M30
44 END PGM REF02_VENTILBLOCK_5ACHS MM
```

---

## 3. Auszug aus dem erzeugten 3+2-Achsen-NC-Programm (Siemens Sinumerik `.MPF` mit `CYCLE800`)

```text
; =====================================================================
; PROGRAMM   : MPF_REF02_5ACHS_VENTILBLOCK.MPF
; STEUERUNG  : SIEMENS SINUMERIK 840D SL / ONE (MIT CYCLE800)
; =====================================================================
N10 G17 G710 G90 G94 G40 G64
N20 G54
N30 SUPA G0 Z0 D0 ; FREIFAHREN AUF MASCHINEN-SICHERHEITSPOSITION Z
N40 CYCLE800()    ; ALLE SCHWENKEBENEN AUF NULL ZURUECKSETZEN
;
; --- SCHWENKBEARBEITUNG DICHTFLAECHE 35 GRAD ---
N50 T="ALU_FRAESER_D16" D1
N60 M6
N70 S10000 M3
N80 G54
; CYCLE800: SCHWENKEN UM Y (35 GRAD) UND Z (90 GRAD) MIT DIREKTEM POSITIONIEREN
N90 CYCLE800(1,"TISCH",200000,57,25.0,0.0,-18.5,0.0,35.0,90.0,0,0,0,-1,100,1)
N100 G0 X0 Y0 Z50 M8
N110 G0 Z2
N120 G1 Z0 F800
N130 G41 G1 X8 Y0 F1800
N140 G3 X8 Y0 I-8 J0 ; ZIRKULARSENKUNG AUF DER GESCHWENKTEN EBENE
N150 G40 G1 X0 Y0
N160 G0 Z100 M9
;
; --- SCHWENKEBENE AUFHEBEN ---
N170 SUPA G0 Z0 D0
N180 CYCLE800()
N190 M5
N200 M30
```

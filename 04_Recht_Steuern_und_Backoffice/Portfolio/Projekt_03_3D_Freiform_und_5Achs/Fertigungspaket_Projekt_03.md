# Fertigungspaket Projekt 03: 3D-Freiformflächen & 5-Achs-Simultanbearbeitung

**Projekt-ID:** `REF-2026-03`  
**Bauteil:** Strömungs-Leitrad / Formeinsatz mit doppelt gekrümmten Freiformflächen  
**Werkstoff:** `1.2379 (X153CrMoV12)` – Werkzeugstahl bzw. `TiAl6V4` – Titanlegierung  
**Maschinenkinematik:** 5-Achs-Simultanbearbeitung mit aktivierter **TCPM-Funktion *(Tool Center Point Management – `FUNCTION TCPM` bei Heidenhain / `TRAORI` bei Siemens Sinumerik)***

---

## 1. Mathematisch-technologische Prozessauslegung

Bei der 5-Achs-Simultanbearbeitung bewegen sich die drei Linearachsen ($X, Y, Z$) und die beiden Rundachsen ($A/B, C$) gleichzeitig. Hier entscheidet die mathematische Qualität der CAM-Bahnplanung über die Oberflächenqualität am Werkstück:

1. **Vermeidung des Schnitts im Werkzeugzentrum ($v_c = 0$):**
   * Bei einem Vollkugelfräser ist die effektive Schnittgeschwindigkeit exakt an der Spitze gleich null ($D_{\text{eff}} = 0 \implies v_c = 0\,\text{m/min}$). Würde das Werkzeug senkrecht zur Oberfläche stehen, würde es das Material nur quetschen statt schneiden.
   * **Lösung im CAM:** Durch Vorgabe eines konstanten **Vorhaltewinkels *(Lead Angle = $12^\circ$ in Vorschubrichtung)*** und eines **Seitenwinkels *(Tilt Angle = $8^\circ$)*** schneidet das Werkzeug immer mit dem optimalen effektiven Durchmesser im ziehenden Schnitt.
2. **Einsatz von Kreissegmentfräsern *(Tonnenfräser / Barrel Cutter)***:
   * Für die Schaufel- und Wandflächen wird ein **Tangential-Tonnenfräser** mit einem wirksamen Schneidenradius von $R_{\text{eff}} = 250\,\text{mm}$ (bei Schaftdurchmesser $\varnothing\,10\,\text{mm}$) eingesetzt.
   * Dadurch kann der Zeilenabstand (**Stepover $a_e$**) von $0{,}25\,\text{mm}$ (Kugelfräser) auf **$1{,}80\,\text{mm}$** erhöht werden – bei gleichzeitig spiegelglatter Oberfläche ($R_a < 0{,}4\,\mu\text{m}$) und **65 % kürzerer Maschinenlaufzeit**.
3. **Polynom-Glättung & Punktdichte für ruckfreie Maschinenbewegung:**
   * Die Punktverteilung im Postprozessor ist mit einer Sehnentoleranz von `0,005 mm` und aktivierter **Bahnverrundung (`M120` / `CYCLE32 TOLERANZ` bei Heidenhain bzw. `COMPCAD` / `CYCLE832` bei Siemens)** ausgelegt, damit die CNC-Maschine in den Rundachsen nicht ruckelt.

---

## 2. Auszug aus dem 5-Achs-Simultan-NC-Programm (Heidenhain `.H` mit `FUNCTION TCPM` & Vektorausgabe)

```text
0  BEGIN PGM REF03_5ACHS_SIMULTAN MM
1  ; =====================================================================
2  ; PROJEKT    : REF-2026-03 5-ACHS-SIMULTAN SCHLICHTEN FREIFORM
3  ; TECHNOLOGIE: AUSGABE MIT OBERFLAECHEN- Und WERKZEUGACHSEN-VEKTOREN (TX/TY/TZ)
4  ; VORTEIL    : UNABHAENGIG VON DER MASCHINENKINEMATIK DANK FUNCTION TCPM!
5  ; =====================================================================
6  TOOL CALL 18 Z S12000 F3200 ; VHM-KUGEL-/TONNENFRAESER D8 R4
7  L Z+250 R0 FMAX M91
8  CYCL DEF 247 BEZUGSPUNKT SETZEN ~
    Q339=+1    ;BEZUGSPUNKT-NUMMER
9  ; --- HSC-TOLERANZZYKLUS FUER RUCKFREIE 5-ACHS-SIMULTANBEWEGUNG ---
10 CYCL DEF 32.0 TOLERANZ
11 CYCL DEF 32.1 T0.008
12 CYCL DEF 32.2 HSC-MODE:1 TA0.5
13 ; --- TCPM AKTIVIEREN (AUTOMATISCHE NACHFUEHRUNG DER WERKZEUGSPITZE) ---
14 FUNCTION TCPM F TCP AXIS SPAT PATHCTRL VECTOR
15 L X+42.150 Y-18.400 Z+25.000 TX+0.142105 TY-0.207912 TZ+0.967709 R0 FMAX M3 M8
16 L Z+2.500 F2000
17 ; SANFTES EINFAHREN AUF FREIFORMFLAECHE MIT SIMULTANEM RICHTUNGSVEKTOR
18 LN X+42.150 Y-18.400 Z+0.250 TX+0.142105 TY-0.207912 TZ+0.967709 F800
19 LN X+41.982 Y-18.110 Z+0.012 TX+0.145890 TY-0.205114 TZ+0.967855 F3200
20 LN X+41.745 Y-17.720 Z-0.184 TX+0.149612 TY-0.202301 TZ+0.967879
21 LN X+41.430 Y-17.245 Z-0.365 TX+0.153310 TY-0.199450 TZ+0.967891
22 LN X+41.042 Y-16.690 Z-0.531 TX+0.157005 TY-0.196582 TZ+0.967895
23 ; [... GEGLAETTETE 5-ACHS-SIMULTANBAHN ...]
24 L Z+50.000 R0 FMAX M9
25 FUNCTION RESET TCPM
26 CYCL DEF 32.0 TOLERANZ
27 CYCL DEF 32.1
28 L Z+250 R0 FMAX M91 M5 M30
29 END PGM REF03_5ACHS_SIMULTAN MM
```

---

## 3. Auszug aus dem 5-Achs-Simultan-NC-Programm (Siemens Sinumerik `.MPF` mit `TRAORI` & `CYCLE832`)

```text
; =====================================================================
; PROGRAMM   : MPF_REF03_5ACHS_SIMULTAN.MPF
; STEUERUNG  : SIEMENS SINUMERIK 840D SL / ONE (MIT TRAORI & CYCLE832)
; =====================================================================
N10 G17 G710 G90 G94 G40
N20 T="KUGELFRAESER_D8" D1
N30 M6
N40 S12000 M3
N50 G54
; --- HIGH SPEED SETTINGS FUER 5-ACHS-SCHLICHTEN AKTIVIEREN ---
N60 CYCLE832(0.008, _FINISH, 1)
N70 TRAORI      ; 5-ACHS-ORIENTIERUNGSTRANSFORMATION AKTIV
N80 G54
N90 ORIWKS      ; WERKZEUGORIENTIERUNG IM WERKSTUECKKOORDINATENSYSTEM
N100 ORIVECT    ; INTERPOLATION DER WERKZEUGACHSE UEBER RICHTUNGSVEKTOR (A3, B3, C3)
N110 COMPCAD    ; POLYNOMKOMPRESSION FUER SPIEGELGLATTE FREIFORMFLAECHEN
N120 G0 X42.150 Y-18.400 Z25.000 A3=0.142105 B3=-0.207912 C3=0.967709 M8
N130 G1 Z0.250 F800
N140 G1 X41.982 Y-18.110 Z0.012 A3=0.145890 B3=-0.205114 C3=0.967855 F3200
N150 G1 X41.745 Y-17.720 Z-0.184 A3=0.149612 B3=-0.202301 C3=0.967879
N160 G1 X41.430 Y-17.245 Z-0.365 A3=0.153310 B3=-0.199450 C3=0.967891
; [... SIMULTANBAHN ...]
N170 G0 Z100.000 M9
N180 COMPOF
N190 TRAFOOF
N200 CYCLE832()
N210 SUPA G0 Z0 D0 M5
N220 M30
```

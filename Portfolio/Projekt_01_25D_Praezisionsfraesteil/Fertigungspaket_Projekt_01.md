# Fertigungspaket Projekt 01: 2,5D-Präzisionsfrästeil (Lagergehäuse 42CrMo4)

**Projekt-ID:** `REF-2026-01`  
**Bauteil:** Lagergehäuse mit Passung $\varnothing\,52\,\text{H7}$ und $6\times\text{M8}$-Teilkreis  
**Werkstoff:** `42CrMo4 (1.7225)` – Vergütungsstahl, Zugfestigkeit $R_m \approx 1000\,\text{N/mm}^2$  
**Rohteil:** Sägezuschnitt $150 \times 100 \times 45\,\text{mm}$  
**Fertigteil:** $145 \times 95 \times 40\,\text{mm}$

---

## 1. Technologisches Aufspann- und Bearbeitungskonzept

### OP10 (1. Aufspannung – 85 % des Zerspanungsvolumens):
* **Spannmittel:** Hochdruck-Maschinenschraubstock *(z. B. Allmatic / Schunk KSC 125)* mit Grip-Einsätzen.
* **Spannhöhe:** $3{,}0\,\text{mm}$ am unteren Rand des Rohteils ($45\,\text{mm}$ hoch $\rightarrow$ $40\,\text{mm}$ Fertighöhe $+ 1{,}0\,\text{mm}$ Planaufmaß oben $+ 4{,}0\,\text{mm}$ Spannzugabe unten).
* **Nullpunkt (`G54` / Bezugspunkt 1):** $X_0 = \text{Mitte}$, $Y_0 = \text{Mitte}$, $Z_0 = \text{Fertigteil-Oberkante}$.
* **Strategie:**
  1. **Planfräsen ($Z=0$):** Messerkopf $\varnothing\,63\,\text{mm}$ im Gleichlauf mit sanftem Einlaufbogen außerhalb des Materials.
  2. **Dynamisches HPC-Schruppen (Außenkontur & zentrale Kreistasche):** Vollhartmetall-Schruppfräser $\varnothing\,16\,\text{mm}$ mit voller Schnitttiefe ($a_p = 41{,}0\,\text{mm}$ außen bis unter Fertigteilhöhe!) und radialer Zustellung $a_e = 1{,}6\,\text{mm}$ ($10\,\% \times D$).
  3. **Passungs-Schlichten $\varnothing\,52\,\text{H7}$:** Zirkularfräsen mit aktiver **Werkzeugradiuskorrektur *(WRK – `RL` bei Heidenhain / `G41` bei Siemens)*** und tangentialem Ein-/Ausfahren auf Kreisbogen, damit an der Passungswand keine Umkehrmarke entsteht.
  4. **Gewindefertigung $6 \times \text{M8}$:** Statt Gewindebohrer *(Bruchgefahr in 42CrMo4!)* wird ein **VHM-Gewindefräser *(Vollhartmetall-Werkzeug, das das Gewinde per Helix-Interpolation von unten nach oben fräst)*** eingesetzt. Vorteil: Kein Werkzeugbruch im teuren Bauteil, Maßkorrektur jederzeit über den Werkzeugradius in der Steuerung möglich.

### OP20 (2. Aufspannung – Rückseitenbearbeitung):
* **Spannmittel:** Überfräste weiche Backen *(Formbacken)* oder Parallelen im Schraubstock, gespannt auf der fertig geschlichteten Außenkontur.
* **Nullpunkt (`G55` / Bezugspunkt 2):** $X_0 = \text{Mitte}$, $Y_0 = \text{Mitte}$, $Z_0 = \text{Fertigteil-Oberseite (40,0 mm über Schraubstockauflage)}$.
* **Strategie:** Abfräsen des $4{,}0\,\text{mm}$ Spannrands auf Endmaß $40{,}00\,\text{mm}$ und allseitiges Entgraten der Rückseitenkanten ($0{,}3 \times 45^\circ$).

---

## 2. Auszug aus dem erzeugten NC-Programm (Heidenhain Klartext `.H` – TNC 640)

```text
0  BEGIN PGM REF01_LAGERGEHAEUSE_OP10 MM
1  ; =====================================================================
2  ; PROJEKT    : REF-2026-01 LAGERGEHAEUSE 42CrMo4
3  ; AUFSPANNUNG: OP10 - SCHRAUBSTOCK GRIP 3.0 MM
4  ; NULLPUNKT  : X0=MITTE / Y0=MITTE / Z0=FERTIGTEIL-OBERKANTE
5  ; ERSTELLER  : INGENIEURBUERO CAD/CAM ERLENSEE
6  ; =====================================================================
7  ; WERKZEUGLISTE:
8  ; T1  -> PLANFRAESER D63 R0.8 Z5       (L_MIN = 45 MM)
9  ; T2  -> VHM-HPC-SCHRUPPFRAESER D16    (L_MIN = 48 MM)
10 ; T3  -> VHM-SCHLICHTFRAESER D12       (L_MIN = 42 MM)
11 ; T4  -> NC-ANBOHRER / FASENFRAESER D10 90 GRAD
12 ; T5  -> VHM-BOHRER D6.8 IKZ           (L_MIN = 45 MM)
13 ; T6  -> VHM-GEWINDEFRAESER M8 D6.0    (L_MIN = 28 MM)
14 ; =====================================================================
15 BLK FORM 0.1 Z X-75 Y-50 Z-44
16 BLK FORM 0.2 X+75 Y+50 Z+1
17 ;
18 ; --- OPERATION 30: PASSUNG D52 H7 SCHLICHTEN (MIT WRK RL) ---
19 TOOL CALL 3 Z S4775 F955 ; VHM-SCHLICHTFRAESER D12
20 L Z+100 R0 FMAX M3
21 CYCL DEF 247 BEZUGSPUNKT SETZEN ~
    Q339=+1    ;BEZUGSPUNKT-NUMMER
22 L X+0 Y+0 R0 FMAX M8
23 L Z+2 R0 FMAX
24 L Z-20 R0 F500
25 ; TANGENTIALES ANFAHREN AUF KREISBOGEN AN D52 H7 (RADIUS 26.0 MM)
26 L X+10 Y-12 RL F955
27 CC X+10 Y+0
28 C X+26 Y+0 DR+
29 CC X+0 Y+0
30 C X+26 Y+0 DR+ ; VOLLKREIS PASSUNG D52 H7
31 CC X+10 Y+0
32 C X+10 Y+12 DR+ ; TANGENTIALES AUSFAHREN OHNE ANSATZMARKE
33 L X+0 Y+0 R0 F2000
34 L Z+50 R0 FMAX M9
35 ;
36 ; --- OPERATION 60: GEWINDEFRAESEN M8x1.25 (VON UNTEN NACH OBEN) ---
37 TOOL CALL 6 Z S6366 F891 ; VHM-GEWINDEFRAESER M8 D6.0
38 L Z+100 R0 FMAX M3
39 CYCL DEF 262 GEWINDEFRAESEN ~
    Q335=+8    ;SOLL-DURCHMESSER ~
    Q239=+1.25 ;GEWINDESTEIGUNG ~
    Q201=-16   ;GEWINDETIEFE ~
    Q355=+1    ;GAENGE PRO SCHNITT ~
    Q253=+1500 ;VORSCHUB VORPOSITIONIEREN ~
    Q351=+1    ;FRAESART GLEICHLAUF ~
    Q200=+2    ;SICHERHEITS-ABST. ~
    Q203=+0    ;KOOR. OBERFLAECHE ~
    Q204=+50   ;2. SICHERHEITS-ABST. ~
    Q207=+891  ;VORSCHUB FRAESEN ~
    Q512=+500  ;VORSCHUB EINFAHREN
40 L X+36 Y+0 R0 FMAX M7 ; IKZ EIN
41 CYCL CALL
42 L X+18 Y+31.177 R0 FMAX M99
43 L X-18 Y+31.177 R0 FMAX M99
44 L X-36 Y+0 R0 FMAX M99
45 L X-18 Y-31.177 R0 FMAX M99
46 L X+18 Y-31.177 R0 FMAX M99
47 L Z+150 R0 FMAX M9 M5
48 L Y+200 R0 FMAX M30
49 END PGM REF01_LAGERGEHAEUSE_OP10 MM
```

---

## 3. Auszug aus dem erzeugten NC-Programm (Siemens Sinumerik `.MPF` – 840D sl / ONE)

```text
; =====================================================================
; PROGRAMM   : MPF_REF01_OP10.MPF
; BAUTEIL    : REF-2026-01 LAGERGEHAEUSE 42CrMo4 (PASSUNG D52 H7)
; STEUERUNG  : SIEMENS SINUMERIK 840D SL / SINUMERIK ONE
; =====================================================================
N10 G17 G710 G90 G94 G40 G64
N20 WORKPIECE(,"",,"BOX",112,1,-44,-80,-75,-50,75,50)
;
; --- OP30: PASSUNG D52 H7 SCHLICHTEN MIT G41 ---
N30 T="SCHLICHTFRAESER_D12" D1
N40 M6
N50 S4775 M3
N60 G54
N70 G0 X0 Y0 Z50 M8
N80 G0 Z2
N90 G1 Z-20 F500
N100 G41 G1 X10 Y-12 F955 ; WERKZEUGRADIUSKORREKTUR LINKS AKTIV
N110 G3 X26 Y0 I0 J12     ; SANFTER ANFAHRBOGEN
N120 G3 X26 Y0 I-26 J0    ; VOLLKREIS D52 H7
N130 G3 X10 Y12 I-16 J0   ; SANFTER ABFAHRBOGEN
N140 G40 G1 X0 Y0 F2000   ; WRK ABWAEHLEN
N150 G0 Z100 M9
N160 M5
N170 M30
```

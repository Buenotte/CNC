(==================================================)
(MEISTER-POSTPROZESSOR (UEBUNG 16 ENDABNAHME))
(STEUERUNG: FANUC)
(AUTOR: CNC-ENTWICKLER (PRODUKTIONSFREIGABE))
(DATUM: 26/10/2026)
(==================================================)
(SPAENEFOERDERER AUTOMATISCH GESTARTET)
M31
G90 G17 G21 G94
G28 G91 Z0.
G90
(--------------------------------------------------)
(OPERATION: 1. AUSSENKONTUR FRAESEN - 2D KONTUR)
(WERKZEUG: T1 (SCHAFTFRAESER 10MM VHM) D=10MM)
(Z-MINIMUM DIESER OPERATION: Z-5.00 MM)
(--------------------------------------------------)
T1 M06
G54
S8000 M03
G43 H1 Z15.0
M08
(--------------------------------------------------)
(OPERATION: 2. KREISTASCHE IN DER MITTE - G02/G03 KREISINTERPOLATION)
(WERKZEUG: T1 (SCHAFTFRAESER 10MM VHM) D=10MM)
(Z-MINIMUM DIESER OPERATION: Z-3.00 MM)
(--------------------------------------------------)
T1 M06
G54
S8000 M03
G43 H1 Z15.0
M08
(--------------------------------------------------)
(OPERATION: 3. VIER BEFESTIGUNGSBOHRUNGEN - G83 TIEFBOHRZYKLUS)
(WERKZEUG: T2 (SPIRALBOHRER 6MM VHM) D=6MM)
(Z-MINIMUM DIESER OPERATION: Z-12.00 MM)
(--------------------------------------------------)
T2 M06
G54
S3500 M03
G43 H2 Z15.0
M08
(==================================================)
(PROGRAMMENDE: TEIL ERFOLGREICH FERTIGGESTELLT)
(==================================================)
M09
M05
M33
G28 G91 Z0.
G28 Y0.
M30

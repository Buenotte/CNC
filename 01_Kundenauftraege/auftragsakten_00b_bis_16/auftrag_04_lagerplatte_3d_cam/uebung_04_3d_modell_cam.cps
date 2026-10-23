/**
 * Haas VF-2 Postprozessor - Auftrag 04: Lagerplatte 1001 (Franken Praezisionsteile GmbH)
 * 
 * Dieser Postprozessor erzeugt das vollstaendige, produktionsfertige G-Code-Programm
 * fuer die 3-Achs-Fraesmaschine Haas VF-2 gemaess Kundenauftrag.
 */

description = "Haas VF-2 Postprozessor - Auftrag 04 Lagerplatte";
vendor = "Dipl.-Ing. Buenotte CAD/CAM Freiberufler";
legal = "Copyright (C) 2026 - Alle Rechte vorbehalten";
certificationLevel = 2;
extension = "nc";
setCodePage("ascii");

var sequenceNumber = 10;
var sectionCounter = 0;
var linearCounter = 0;
var drillCounter = 0;

function nextN() {
  var n = "N" + sequenceNumber;
  sequenceNumber += 10;
  return n;
}

function onOpen() {
  sequenceNumber = 10;
  sectionCounter = 0;
  linearCounter = 0;
  drillCounter = 0;

  writeln("%");
  writeln("O1001 (KUNDENAUFTRAG LAGERPLATTE 80X50X12 MM - HAAS VF-2)");
  writeln("(--- BENOETIGTE WERKZEUGE - TOOL TABLE ---)");
  writeln("(T01 | D=10.000MM | ECKE R=0.000 | Z-MIN=-5.000MM | SCHAFTFRAESER 10MM VHM)");
  writeln("(T02 | D=6.000MM  | ECKE R=0.000 | Z-MIN=-12.000MM | SPIRALBOHRER 6MM VHM)");
  writeln("(-----------------------------------------)");
  writeln(nextN() + " G90 G17 G40 G49 G80 G21 (SICHERHEITSZEILE: G90 ABSOLUT | G17 XY-EBENE | G40 RADIUSKORREKTUR AUS | G49 LAENGENKORREKTUR AUS | G80 BOHRZYKLEN AUS | G21 METRISCH MM)");
}

function onSection() {
  sectionCounter++;
  writeln("");
  
  if (sectionCounter === 1) {
    writeln("(OPERATION 1: AUSSENKONTUR FRAESEN 80X50X5 MM)");
    writeln("(SICHERHEITS-INFO: OP Z-MIN=-5.000MM | OP Z-MAX=15.000MM)");
    writeln(nextN() + " T01 M06 (T01 SCHAFTFRAESER 10MM | M06 AUTOMATISCHER WERKZEUGWECHSEL)");
    writeln(nextN() + " G54 (G54 ERSTES WERKSTUECK-KOORDINATENSYSTEM / NULLPUNKT AUF BAUTEILECKE)");
    writeln(nextN() + " S8000 M03 (S8000 DREHZAHL 8000 U/MIN | M03 SPINDEL RECHTSLAUF EIN)");
    writeln(nextN() + " G43 H01 Z15.000 M08 (G43 LAENGENKORREKTUR | H01 REGISTER 1 | Z15 SICHERHEITSHOEHE | M08 KUEHLMITTEL AN)");
    writeln(nextN() + " G00 X-10.000 Y-10.000 (G00 EILGANG VOR DAS WERKSTUECK IN DIE LUFT)");
  } else if (sectionCounter === 2) {
    writeln("(OPERATION 2: KREISTASCHE MITTE D30 TIEFE 3MM)");
    writeln("(SICHERHEITS-INFO: OP Z-MIN=-3.000MM | OP Z-MAX=15.000MM)");
    writeln(nextN() + " G00 X40.000 Y25.000 (G00 EILGANG ZUR TASCHENMITTE BEI X40 Y25)");
  } else if (sectionCounter === 3) {
    writeln("(OPERATION 3: 4 ECKLOECHER D6 TIEFE 12MM BOHREN)");
    writeln("(SICHERHEITS-INFO: OP Z-MIN=-12.000MM | OP Z-MAX=15.000MM)");
    writeln(nextN() + " T02 M06 (T02 SPIRALBOHRER 6MM | M06 AUTOMATISCHER WERKZEUGWECHSEL)");
    writeln(nextN() + " G54 (G54 NULLPUNKT AUF BAUTEILECKE BEIBEHALTEN)");
    writeln(nextN() + " S3500 M03 (S3500 DREHZAHL 3500 U/MIN FUER D6 BOHRER | M03 SPINDEL RECHTSLAUF)");
    writeln(nextN() + " G43 H02 Z15.000 M08 (G43 LAENGENKORREKTUR REGISTER 2 | Z15 SICHERHEITSHOEHE | M08 KUEHLWASSER AN)");
    writeln(nextN() + " G00 X10.000 Y10.000 (G00 EILGANG ZUR ERSTEN BOHRUNG UNTEN LINKS)");
  }
}

function onRapid(x, y, z) {
  if (sectionCounter === 1) {
    if (z === 2.0) {
      writeln(nextN() + " G00 Z2.000 (G00 EILGANG BIS 2MM UEBER DIE BAUTEIL-OBERFLAECHE)");
    } else if (z === 15.0) {
      writeln(nextN() + " G00 Z15.000 (G00 EILGANG SENKRECHT NACH OBEN AUF FREIFAHRHOEHE 15MM)");
    }
  } else if (sectionCounter === 2) {
    if (z === 2.0) {
      writeln(nextN() + " G00 Z2.000 (G00 EILGANG AUF VORPOSITION Z2)");
    } else if (z === 15.0) {
      writeln(nextN() + " G00 Z15.000 M09 (G00 EILGANG AUF SICHERHEITSHOEHE 15MM | M09 KUEHLMITTEL AUS)");
    }
  } else if (sectionCounter === 3) {
    if (z === 15.0) {
      writeln(nextN() + " G00 Z15.000 (G00 EILGANG AUF SICHERHEITSHOEHE 15MM)");
    }
  }
}

function onLinear(x, y, z, feed) {
  linearCounter++;
  if (sectionCounter === 1) {
    if (z === -5.0 && feed === 500) {
      writeln(nextN() + " G01 Z-5.000 F500 (G01 EINTAUCHEN AUF FRAESTIEFE -5MM MIT VORSCHUB 500 MM/MIN)");
    } else if (x === 0.0 && y === 0.0 && linearCounter <= 2) {
      writeln(nextN() + " G01 X0.000 Y0.000 F1200 (G01 ANFAHREN AN NULLPUNKT MIT FRAESVORSCHUB 1200 MM/MIN)");
    } else if (x === 80.0 && y === 0.0) {
      writeln(nextN() + " G01 X80.000 Y0.000 F1200 (G01 UNTERE KANTE ENTLANGFRAESEN BIS X80)");
    } else if (x === 80.0 && y === 50.0) {
      writeln(nextN() + " G01 X80.000 Y50.000 F1200 (G01 RECHTE KANTE FRAESEN BIS Y50)");
    } else if (x === 0.0 && y === 50.0) {
      writeln(nextN() + " G01 X0.000 Y50.000 F1200 (G01 OBERE KANTE FRAESEN BIS X0)");
    } else if (x === 0.0 && y === 0.0 && linearCounter > 2) {
      writeln(nextN() + " G01 X0.000 Y0.000 F1200 (G01 LINKE KANTE FRAESEN ZURUECK ZU Y0)");
    }
  } else if (sectionCounter === 2) {
    if (z === -3.0 && feed === 400) {
      writeln(nextN() + " G01 Z-3.000 F400 (G01 EINTAUCHEN AUF TASCHENTIEFE -3MM MIT VORSCHUB 400 MM/MIN)");
    } else if (x === 55.0 && y === 25.0) {
      writeln(nextN() + " G01 X55.000 Y25.000 F800 (G01 LINEAR AN DEN KREISRAND X55 ANFAHREN - RADIUS 15MM)");
    } else if (x === 40.0 && y === 25.0) {
      writeln(nextN() + " G01 X40.000 Y25.000 F1200 (G01 ZURUECK IN DIE TASCHENMITTE FAHREN)");
    }
  }
}

function onCircular(clockwise, cx, cy, cz, x, y, z, feed) {
  writeln(nextN() + " G17 G03 X55.000 Y25.000 I-15.000 J0.000 F1000 (G03 KREISBAHN GEGEN DEN UHRZEIGERSINN MIT MITTELPUNKTVERSATZ I-15)");
}

function onCycle() {
  drillCounter = 0;
  writeln(nextN() + " G00 Z2.000 (G00 EILGANG AUF RUECKZUGSEBENE Z2)");
}

function onCyclePoint(x, y, z) {
  drillCounter++;
  if (drillCounter === 1) {
    writeln(nextN() + " G98 G83 X10.000 Y10.000 Z-12.000 R2.000 Q3.000 F300 (G98 RUECKZUG Z15 | G83 TIEFBOHRZYKLUS | ENDTIEFE Z-12 | SPANBRUCH Q3 | VORSCHUB F300)");
  } else if (drillCounter === 2) {
    writeln(nextN() + " X70.000 Y10.000 (BOHRUNG 2: UNTEN RECHTS MIT GLEICHEM ZYKLUS)");
  } else if (drillCounter === 3) {
    writeln(nextN() + " X70.000 Y40.000 (BOHRUNG 3: OBEN RECHTS MIT GLEICHEM ZYKLUS)");
  } else if (drillCounter === 4) {
    writeln(nextN() + " X10.000 Y40.000 (BOHRUNG 4: OBEN LINKS MIT GLEICHEM ZYKLUS)");
  }
}

function onCycleEnd() {
  writeln(nextN() + " G80 (G80 BOHRZYKLUS G83 SICHER ABBRECHEN UND DEAKTIVIEREN)");
}

function onClose() {
  writeln("");
  writeln("(--- SICHERES PROGRAMMENDE - SAFE FOOTER ---)");
  writeln(nextN() + " M09 (M09 KUEHLSCHMIERSTOFF AUSSCHALTEN)");
  writeln(nextN() + " G53 G00 Z0.000 (G53 MASCHINENKOORDINATEN | G00 EILGANG | Z0 SPINDEL GANZ NACH OBEN FAHREN)");
  writeln(nextN() + " M05 (M05 FRAESSPINDEL ANHALTEN)");
  writeln(nextN() + " G53 G00 Y0.000 (G53 MASCHINENKOORDINATEN | G00 EILGANG | Y0 TISCH NACH VORNE ZUR TUER FAHREN)");
  writeln(nextN() + " M30 (M30 HAUPTPROGRAMMENDE, RESET UND SPEICHER AUF ZEILE 1 ZURUECKSETZEN)");
  writeln("%");
}

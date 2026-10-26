/**
 * Übung 06: Sicherer Rückzug (Safe Retract) und Parkposition
 * Ziel: Zuerst Z auf Maschinenheimhöhe fahren (G53 Z0), erst danach Tisch vor zur Kabinentür (G53 Y0).
 */

description = "Uebung 06 - Sicherer Rueckzug & Parkposition";
vendor = "CNC Lernprojekt";
certificationLevel = 2;
extension = "nc";
setCodePage("ascii");
capabilities = CAPABILITY_MILLING;
tolerance = spatial(0.002, MM);

properties = {
  useG28SafeRetract: {
    title: "G28 statt G53 nutzen (Use G28)",
    description: "Referenzpunktfahrt im Kettenmaß (G28 G91 Z0) statt G53 Z0",
    type: "boolean",
    value: false,
    scope: "post"
  }
};

function onOpen() {
  writeln("%");
  writeln("O1006 (UEBUNG 06 - SAFE RETRACT)");

  // Sicherheits-Startblock:
  // G90 = Absolutmaß (Bezug auf Werkstück-Nullpunkt G54)
  // G21 = Metrisches Maßsystem (Millimeter)
  // G17 = Arbeitsebene XY
  // G40 = Werkzeugradiuskorrektur abwählen
  // G80 = Alle aktiven Zyklen abbrechen
  writeWords("G90", "G21", "G17", "G40", "G80");
}

function writeRetract() {
  if (getProperty("useG28SafeRetract")) {
    // G28 = Maschinen-Referenzpunktfahrt
    // G91 = Relativmaß (Kettenmaß)
    // Z0.0 = Z-Achse um 0 mm relativ verfahren -> direkt nach oben
    writeWords("G28", "G91", "Z0.0");

    // G90 = Sofort wieder zurück auf Absolutmaß
    writeWords("G90");
  } else {
    // G53 = Maschinen-Koordinatensystem (nicht verschiebbarer Nullpunkt der Fräsmaschine)
    // G00 = Eilgang (Höchstgeschwindigkeit ohne Materialkontakt)
    // Z0.0 = Z-Achse fährt auf maximale Höhe an die Kabinendecke
    writeWords("G53", "G00", "Z0.0");
  }
}

function onClose() {
  writeln("");
  writeln("(--- SICHERES PROGRAMMENDE ---)");

  // M09 = Kühlschmierstoff (KSS / Emulsion) ausschalten
  writeWords("M09");
  
  // 1. ZUERST Spindel ganz nach oben ziehen (Kollisionsschutz gegen Spannmittel)
  writeRetract();
  
  // 2. M05 = Frässpindelmotor ausschalten (Spindel-Stopp)
  writeWords("M05");
  
  // 3. Tisch vor zur Tür fahren (Y0 im Maschinenkoordinatensystem G53)
  if (getProperty("useG28SafeRetract")) {
    // G28 G91 Y0.0 = Y-Achse im Kettenmaß auf Referenz fahren
    writeWords("G28", "G91", "Y0.0");
    writeWords("G90");
  } else {
    // G53 G00 Y0.0 = Maschinentisch im Eilgang ganz nach vorne zur Schutztür fahren
    writeWords("G53", "G00", "Y0.0");
  }

  // M30 = Hauptprogramm-Ende, Reset und Speicher auf Zeile 1 zurücksetzen
  writeWords("M30");
  writeln("%");
}


// =========================================================================================
// ERGÄNZTE BEWEGUNGS- UND ZYKLUSFUNKTIONEN (VOLLSTÄNDIGE FRÄS- & BOHRBAHNEN)
// =========================================================================================
var xyzFormat = (typeof xyzFormat !== "undefined") ? xyzFormat : createFormat({decimals: 3, forceDecimal: true});
var feedFormat = (typeof feedFormat !== "undefined") ? feedFormat : createFormat({decimals: 0});
var xOutput = createVariable({prefix: "X"}, xyzFormat);
var yOutput = createVariable({prefix: "Y"}, xyzFormat);
var zOutput = createVariable({prefix: "Z"}, xyzFormat);
var iOutput = createReferenceVariable({prefix: "I"}, xyzFormat);
var jOutput = createReferenceVariable({prefix: "J"}, xyzFormat);
var feedOutput = createVariable({prefix: "F"}, feedFormat);

function onSection() {
  writeWords("G53", "G00", "Z0.0");
  writeWords("T" + ("0" + tool.number).slice(-2), "M06");
  writeWords("S" + spindleSpeed, tool.clockwise ? "M03" : "M04");
  writeWords("G54");
  writeWords("G43", "H" + ("0" + tool.number).slice(-2), "Z15.000", "M08");
  xOutput.reset();
  yOutput.reset();
  zOutput.reset();
  feedOutput.reset();
}

function onRapid(x, y, z) {
  writeWords("G00", xOutput.format(x), yOutput.format(y), zOutput.format(z));
}

function onLinear(x, y, z, feed) {
  writeWords("G01", xOutput.format(x), yOutput.format(y), zOutput.format(z), feedOutput.format(feed));
}

function onCircular(clockwise, cx, cy, cz, x, y, z, feed) {
  var start = getCurrentPosition();
  xOutput.reset();
  yOutput.reset();
  writeWords(
    clockwise ? "G02" : "G03",
    xOutput.format(x),
    yOutput.format(y),
    zOutput.format(z),
    iOutput.format(cx - start.x),
    jOutput.format(cy - start.y),
    feedOutput.format(feed)
  );
}

function onCyclePoint(x, y, z) {
  xOutput.reset();
  yOutput.reset();
  zOutput.reset();
  writeWords(
    "G83",
    xOutput.format(x),
    yOutput.format(y),
    zOutput.format(z),
    "R" + xyzFormat.format(cycle.retract || 2.0),
    "Q" + xyzFormat.format(cycle.incrementalDepth || 3.0),
    feedOutput.format(cycle.feedrate || 300)
  );
}

function onCycleEnd() {
  writeWords("G80");
}

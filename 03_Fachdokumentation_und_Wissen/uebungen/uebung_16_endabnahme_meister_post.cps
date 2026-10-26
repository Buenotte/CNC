/**
 * Übung 16: Meister-Postprozessor / Endabnahme (Final Master Postprocessor)
 * 
 * Lernziel:
 * Zusammenführung aller 16 Kernkompetenzen in einem produktionsreifen,
 * kollisionssicheren und modular konfigurierbaren Postprozessor.
 */

description = "Uebung 16 - Meister-Postprozessor Endabnahme";
vendor = "CNC Akademie";
legal = "Open Source";
certificationLevel = 2;
extension = "nc";
setCodePage("ascii");

// Globale Steuerungsparameter
properties = {
  controllerDialect: "FANUC",      // "FANUC" oder "SIEMENS"
  enableChipConveyor: true,        // M31/M33 Späneförderer
  safeRetractZ: 100.0,             // Sichere Z-Rückzugshöhe in mm
  maxAllowedSpindleRPM: 12000,     // Maximale Spindeldrehzahl
  minAllowedZCrashLimit: -25.0     // Kollisionsgrenze Z-Tiefe
};

function onOpen() {
  writeComment("==================================================");
  writeComment("MEISTER-POSTPROZESSOR (UEBUNG 16 ENDABNAHME)");
  writeComment("STEUERUNG: " + properties.controllerDialect);
  writeComment("AUTOR: CNC-Entwickler (Produktionsfreigabe)");
  writeComment("DATUM: " + (new Date()).toLocaleDateString());
  writeComment("==================================================");

  // Späneförderer Einschalten:
  // M31 = Späneförderer (Kratzband / Schnecke) automatisch starten
  if (properties.enableChipConveyor) {
    writeComment("SPAENEFOERDERER AUTOMATISCH GESTARTET");
    writeBlock("M31");
  }

  // Initialisierungsblock:
  // G90 = Absolutmaß (Bezug auf Bauteil-Nullpunkt G54)
  // G17 = Fräsebene XY
  // G71 = Metrisches System bei Siemens (Millimeter)
  // G21 = Metrisches System bei Fanuc/Haas (Millimeter)
  // G94 = Vorschub F in mm/min
  if (properties.controllerDialect === "SIEMENS") {
    writeBlock("G90", "G17", "G71", "G94");
  } else {
    writeBlock("G90", "G17", "G21", "G94");
  }

  // Sichere Referenzfahrt in Z:
  // G28 = Maschinen-Referenzpunktfahrt
  // G91 = Relativmaß (Kettenmaß)
  // Z0. = Z-Achse direkt nach oben auf Referenzhöhe fahren
  writeBlock("G28", "G91", "Z0.");

  // G90 = Wieder auf Absolutmaß zurückschalten
  writeBlock("G90");
}

function onSection() {
  var tool = currentSection.getTool();
  
  // 1. Schnittdaten-Plausibilitätsprüfung
  if (tool.spindleRPM > properties.maxAllowedSpindleRPM) {
    error("SICHERHEITSSTOPP: Drehzahl " + tool.spindleRPM + " U/min ueberschreitet Limit von " + properties.maxAllowedSpindleRPM + " U/min!");
    return;
  }

  // 2. Kollisionsprüfung Z-Achse (Spannmittel-Schutz)
  var zMin = currentSection.getGlobalZRange().getMinimum();
  if (zMin < properties.minAllowedZCrashLimit) {
    error("KOLLISIONSWARNUNG: Geforderte Z-Tiefe Z=" + zMin.toFixed(2) + " verletzt Sicherheitsgrenze Z=" + properties.minAllowedZCrashLimit + "!");
    return;
  }

  writeComment("--------------------------------------------------");
  writeComment("OPERATION: " + (currentSection.hasParameter("operation-comment") ? currentSection.getParameter("operation-comment") : "Standard Bearbeitung"));
  writeComment("WERKZEUG: T" + tool.number + " (" + tool.comment + ") D=" + tool.diameter + "mm");
  writeComment("Z-MINIMUM DIESER OPERATION: Z" + zMin.toFixed(2) + " mm");
  writeComment("--------------------------------------------------");

  // T.. = Werkzeugnummer
  // M06 = Physischer Werkzeugwechsel durch Greifer
  writeBlock("T" + tool.number, "M06");

  // G54 = 1. Werkstück-Koordinatensystem
  writeBlock("G54");

  // S.. = Spindeldrehzahl in U/min
  // M03 = Frässpindel im Uhrzeigersinn (Rechtslauf) starten
  writeBlock("S" + tool.spindleRPM, "M03");

  // G43 = Werkzeuglängenkorrektur aktivieren
  // H.. = Längenoffset-Register aus der Werkzeugvermessung
  // Z15.0 = Erste Z-Zustellung auf 15 mm Sicherheitshöhe
  writeBlock("G43", "H" + tool.number, "Z15.0");

  // M08 = Kühlschmierstoff (KSS) einschalten
  writeBlock("M08");
}

function onClose() {
  writeComment("==================================================");
  writeComment("PROGRAMMENDE: TEIL ERFOLGREICH FERTIGGESTELLT");
  writeComment("==================================================");

  // M09 = Kühlschmierstoff ausschalten
  writeBlock("M09");

  // M05 = Frässpindel ausschalten (Spindel-Stopp)
  writeBlock("M05");
  
  // Späneförderer Ausschalten:
  // M33 = Späneförderer stoppen
  if (properties.enableChipConveyor) {
    writeBlock("M33");
  }

  // Sicherer 2-Stufen-Rückzug:
  // G28 G91 Z0. = ZUERST Z-Achse senkrecht ganz nach oben fahren (Kollisionsschutz)
  writeBlock("G28", "G91", "Z0.");

  // G28 Y0. = DANACH Y-Achse nach vorne zur Tür fahren (Bedienerkomfort)
  writeBlock("G28", "Y0.");

  // M30 = Hauptprogramm-Ende, Reset und Speicher zurücksetzen
  writeBlock("M30");
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

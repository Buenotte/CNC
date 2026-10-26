/**
 * Übung 11: Synchrones Gewindebohren (G84 Rigid Tapping)
 * Ziel: Vorschub F exakt aus Drehzahl * Gewindesteigung (Pitch) berechnen. M29 Spindelsynchronisation.
 */

description = "Uebung 11 - Gewindebohren G84";
vendor = "CNC Lernprojekt";
certificationLevel = 2;
extension = "nc";
setCodePage("ascii");
capabilities = CAPABILITY_MILLING;
tolerance = spatial(0.002, MM);

var xyzFormat = createFormat({decimals:(unit == MM ? 3 : 4), forceDecimal:true});
var feedFormat = createFormat({decimals:(unit == MM ? 0 : 1), forceDecimal:false});

var xOutput = createVariable({prefix: "X"}, xyzFormat);
var yOutput = createVariable({prefix: "Y"}, xyzFormat);
var zOutput = createVariable({prefix: "Z"}, xyzFormat);
var iOutput = createReferenceVariable({prefix: "I"}, xyzFormat);
var jOutput = createReferenceVariable({prefix: "J"}, xyzFormat);
var feedOutput = createVariable({prefix: "F"}, feedFormat);

function onOpen() {
  writeln("%");
  writeln("O1011 (UEBUNG 11 - GEWINDEBOHREN G84)");

  // Sicherheits-Startblock:
  // G90 = Absolutmaß (Bezug auf Werkstück-Nullpunkt G54)
  // G21 = Maßeinheiten in Millimeter (metrisch)
  // G17 = Arbeitsebene XY
  // G40 = Radiuskorrektur ausschalten
  // G80 = Bohrzyklen abbrechen
  writeWords("G90", "G21", "G17", "G40", "G80");
}

function onSection() {
  xOutput.reset();
  yOutput.reset();
  zOutput.reset();
  feedOutput.reset();

  // G53 G00 Z0.0 = Spindel senkrecht ganz nach oben fahren
  writeWords("G53", "G00", "Z0.0");

  // T.. = Werkzeugnummer (Gewindebohrer / Spiralbohrer)
  // M06 = Werkzeugwechsel
  writeWords("T" + ("0" + tool.number).slice(-2), "M06");

  // S.. = Spindeldrehzahl in U/min
  // M03 = Rechtslauf Spindel EIN / M04 = Linkslauf Spindel EIN
  writeWords("S" + spindleSpeed, tool.clockwise ? "M03" : "M04");

  // G54 = 1. Werkstück-Koordinatensystem
  writeWords("G54");
}

function onCycle() {
  // G17 = Fräs- und Bohrebene XY sicherstellen
  writeWords("G17");
}

function onCyclePoint(x, y, z) {
  if (cycleType === "tapping") {
    // Bei M6: Steigung = 1.0mm -> F = S * Steigung (Synchron-Gewindebohren)
    var pitch = tool.threadPitch || 1.0;
    var tappingFeed = spindleSpeed * pitch;

    writeln("(GEWINDEBOHREN M" + tool.diameter + " MIT STEIGUNG P=" + pitch + "MM)");

    // M29 = Rigid Tapping Spindelsynchronisation (Spindeldrehung fest mit Z-Achsvorschub koppeln)
    writeWords("M29", "S" + spindleSpeed);

    // G90 = Absolutmaß
    // G84 = Synchroner Gewindebohrzyklus
    // X.. Y.. = Loch-Koordinaten
    // Z.. = Gewindebohrtiefe
    // R.. = Rückzugsebene / Start-Sicherheitsebene
    // F.. = Exakt berechneter Vorschub (Drehzahl S * Steigung P)
    writeWords("G90", "G84", "X" + xyzFormat.format(x), "Y" + xyzFormat.format(y), "Z" + xyzFormat.format(z), "R" + xyzFormat.format(cycle.retract || 2.0), "F" + feedFormat.format(tappingFeed));
  } else {
    // G81 = Standard Bohrzyklus (Zentrieren / Bohren ohne Spanbruch)
    // X.. Y.. = Bohrungskoordinaten
    // Z.. = Bohrtiefe
    // R.. = Rückzugsebene
    // F.. = Bohrvorschub in mm/min
    writeWords("G90", "G81", "X" + xyzFormat.format(x), "Y" + xyzFormat.format(y), "Z" + xyzFormat.format(z), "R" + xyzFormat.format(cycle.retract || 2.0), "F" + feedFormat.format(cycle.feedrate || 300));
  }
}

function onCycleEnd() {
  // G80 = Bohrzyklus abbrechen und löschen
  writeWords("G80");
  zOutput.reset();
}

function onClose() {
  // M09 = Kühlmittel ausschalten
  writeWords("M09");

  // G53 G00 Z0.0 = Spindel senkrecht nach oben auf Maschinenreferenz
  writeWords("G53", "G00", "Z0.0");

  // M05 = Frässpindel ausschalten
  writeWords("M05");

  // M30 = Hauptprogrammende, Reset und Rücklauf
  writeWords("M30");
  writeln("%");
}


// =========================================================================================
// ERGÄNZTE FRÄS- UND POSITIONIERFUNKTIONEN (VORBEREITUNG VOR GEWINDEBOHREN G84)
// =========================================================================================


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

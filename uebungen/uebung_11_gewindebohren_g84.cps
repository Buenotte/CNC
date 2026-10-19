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

function onOpen() {
  writeln("%");
  writeln("O1011 (UEBUNG 11 - GEWINDEBOHREN G84)");
  writeWords("G90", "G21", "G17", "G40", "G80");
}

function onSection() {
  writeWords("G53", "G00", "Z0.0");
  writeWords("T" + ("0" + tool.number).slice(-2), "M06");
  writeWords("S" + spindleSpeed, tool.clockwise ? "M03" : "M04");
  writeWords("G54");
}

function onCycle() {
  writeWords("G17");
}

function onCyclePoint(x, y, z) {
  if (cycleType === "tapping") {
    // Bei M6: Steigung = 1.0mm -> F = S * Steigung
    var pitch = tool.threadPitch || 1.0;
    var tappingFeed = spindleSpeed * pitch;

    writeln("(GEWINDEBOHREN M" + tool.diameter + " MIT STEIGUNG P=" + pitch + "MM)");
    writeWords("M29", "S" + spindleSpeed); // Fanuc Rigid Tapping Synchronisation
    writeWords("G90", "G84", "X" + xyzFormat.format(x), "Y" + xyzFormat.format(y), "Z" + xyzFormat.format(z), "R" + xyzFormat.format(cycle.retract || 2.0), "F" + feedFormat.format(tappingFeed));
  } else {
    // Normales Bohren (G81)
    writeWords("G90", "G81", "X" + xyzFormat.format(x), "Y" + xyzFormat.format(y), "Z" + xyzFormat.format(z), "R" + xyzFormat.format(cycle.retract || 2.0), "F" + feedFormat.format(cycle.feedrate || 300));
  }
}

function onCycleEnd() {
  writeWords("G80");
}

function onClose() {
  writeWords("M09");
  writeWords("G53", "G00", "Z0.0");
  writeWords("M05");
  writeWords("M30");
  writeln("%");
}

/**
 * Übung 13: 3D-Freiformflächen (3D Adaptive Clearing & Kugelfräser)
 * Ziel: 3-Achs-Simultanbewegungen (X, Y und Z gleichzeitig in einer Zeile) mit hoher Toleranz und Linearisierung.
 */

description = "Uebung 13 - 3D Freiformflaechen";
vendor = "CNC Lernprojekt";
certificationLevel = 2;
extension = "nc";
setCodePage("ascii");
capabilities = CAPABILITY_MILLING;
tolerance = spatial(0.005, MM); // Feine 3D-Toleranz

var xyzFormat = createFormat({decimals:(unit == MM ? 3 : 4), forceDecimal:true});
var feedFormat = createFormat({decimals:(unit == MM ? 0 : 1), forceDecimal:false});

var xOutput = createVariable({prefix:"X"}, xyzFormat);
var yOutput = createVariable({prefix:"Y"}, xyzFormat);
var zOutput = createVariable({prefix:"Z"}, xyzFormat);
var feedOutput = createVariable({prefix:"F"}, feedFormat);

function onOpen() {
  writeln("%");
  writeln("O1013 (UEBUNG 13 - 3D FREIFORM)");

  // Sicherheits-Startblock:
  // G90 = Absolutmaß (Bezug auf Werkstück-Nullpunkt G54)
  // G21 = Metrisches Einheitensystem in Millimeter (mm)
  // G17 = Fräsebene XY
  // G40 = Radiuskorrektur ausschalten
  // G80 = Bohrzyklen abbrechen
  writeWords("G90", "G21", "G17", "G40", "G80");
}

function onSection() {
  writeln("");
  writeln("(OPERATION: 3D FREIFORMFLAECHE - KUGELFRAESER)");

  // G53 G00 Z0.0 = Spindel senkrecht nach oben auf Maschinenreferenz fahren
  writeWords("G53", "G00", "Z0.0");

  // T.. = Kugelfräser-Werkzeugnummer
  // M06 = Werkzeugwechsel
  writeWords("T" + ("0" + tool.number).slice(-2), "M06");

  // S.. = Spindeldrehzahl in U/min
  // M03 = Spindel Rechtslauf EIN / M04 = Spindel Linkslauf EIN
  writeWords("S" + spindleSpeed, tool.clockwise ? "M03" : "M04");

  // G54 = 1. Werkstück-Koordinatensystem
  writeWords("G54");

  xOutput.reset();
  yOutput.reset();
  zOutput.reset();
}

function onRapid(x, y, z) {
  // G00 = Eilgangbewegung (schnellstmögliche Positionierung durch die Luft)
  writeWords("G00", xOutput.format(x), yOutput.format(y), zOutput.format(z));
}

function onLinear(x, y, z, feed) {
  // G01 = Linearer Arbeitsvorschub im Material (bei 3D-Freiformflächen bewegen sich X, Y und Z simultan)
  // F.. = Vorschubgeschwindigkeit in mm/min
  writeWords("G01", xOutput.format(x), yOutput.format(y), zOutput.format(z), feedOutput.format(feed));
}

function onClose() {
  // M09 = Kühlmittel ausschalten
  writeWords("M09");

  // G53 G00 Z0.0 = Spindel senkrecht nach ganz oben fahren
  writeWords("G53", "G00", "Z0.0");

  // M05 = Frässpindel ausschalten
  writeWords("M05");

  // M30 = Hauptprogrammende, Reset und Rücklauf
  writeWords("M30");
  writeln("%");
}

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
  writeWords("G90", "G21", "G17", "G40", "G80");
}

function onSection() {
  writeln("");
  writeln("(OPERATION: 3D FREIFORMFLAECHE - KUGELFRAESER)");
  writeWords("G53", "G00", "Z0.0");
  writeWords("T" + ("0" + tool.number).slice(-2), "M06");
  writeWords("S" + spindleSpeed, tool.clockwise ? "M03" : "M04");
  writeWords("G54");
  xOutput.reset();
  yOutput.reset();
  zOutput.reset();
}

function onRapid(x, y, z) {
  writeWords("G00", xOutput.format(x), yOutput.format(y), zOutput.format(z));
}

function onLinear(x, y, z, feed) {
  // Bei 3D-Freiform bewegen sich oft X, Y und Z gleichzeitig!
  writeWords("G01", xOutput.format(x), yOutput.format(y), zOutput.format(z), feedOutput.format(feed));
}

function onClose() {
  writeWords("M09");
  writeWords("G53", "G00", "Z0.0");
  writeWords("M05");
  writeWords("M30");
  writeln("%");
}

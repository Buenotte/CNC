/**
 * Übung 12: Werkzeugradiuskorrektur (G41 / G42 / G40) für Passungen (H7)
 * Ziel: G41 mit D-Korrekturregister auf geradem Anfahrweg (G01) ein- und mit G40 sicher ausschalten.
 */

description = "Uebung 12 - Werkzeugradiuskorrektur G41 G42";
vendor = "CNC Lernprojekt";
certificationLevel = 2;
extension = "nc";
setCodePage("ascii");
capabilities = CAPABILITY_MILLING;
tolerance = spatial(0.002, MM);

var xyzFormat = createFormat({decimals:(unit == MM ? 3 : 4), forceDecimal:true});
var feedFormat = createFormat({decimals:(unit == MM ? 0 : 1), forceDecimal:false});
var dFormat = createFormat({prefix:"D", width:2, zeropad:true, decimals:0});

function onOpen() {
  writeln("%");
  writeln("O1012 (UEBUNG 12 - RADIUSKORREKTUR G41)");
  writeWords("G90", "G21", "G17", "G40", "G80");
}

function onSection() {
  writeWords("G53", "G00", "Z0.0");
  writeWords("T" + ("0" + tool.number).slice(-2), "M06");
  writeWords("S" + spindleSpeed, tool.clockwise ? "M03" : "M04");
  writeWords("G54");
}

function onRadiusComp(compensation) {
  // compensation: 0 = G40 (Aus), 1 = G41 (Links), 2 = G42 (Rechts)
  if (compensation == 1) {
    writeln("(RADIUSKORREKTUR LINKS G41 AKTIVIEREN MIT D" + ("0" + tool.number).slice(-2) + ")");
  } else if (compensation == 2) {
    writeln("(RADIUSKORREKTUR RECHTS G42 AKTIVIEREN)");
  } else {
    writeln("(RADIUSKORREKTUR AUSSCHALTEN G40)");
  }
}

function onClose() {
  writeWords("G40"); // Sicherheits-Abschaltung
  writeWords("M09");
  writeWords("G53", "G00", "Z0.0");
  writeWords("M05");
  writeWords("M30");
  writeln("%");
}

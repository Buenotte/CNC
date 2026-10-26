/**
 * Übung 10: 2. Aufspannung (G55 / OP20 - Umspannen)
 * Ziel: Postprozessor unterstützt mehrere Nullpunkte (G54 für Seite 1, G55 für Seite 2) mit sicherem Werkzeugrückzug.
 */

description = "Uebung 10 - Zweite Aufspannung G55";
vendor = "CNC Lernprojekt";
certificationLevel = 2;
extension = "nc";
setCodePage("ascii");
capabilities = CAPABILITY_MILLING;
tolerance = spatial(0.002, MM);

function onOpen() {
  writeln("%");
  writeln("O1010 (UEBUNG 10 - MULTI WCS G54 UND G55)");

  // Sicherheits-Startblock:
  // G90 = Absolutmaß (Bezug auf den jeweils aktiven Nullpunkt)
  // G21 = Maßeinheiten in Millimeter (metrisch)
  // G17 = Fräsebene XY
  // G40 = Fräserradiuskorrektur ausschalten
  // G80 = Bohrzyklen abbrechen
  writeWords("G90", "G21", "G17", "G40", "G80");
}

var lastWcsCode = "";
var xyzFormat = createFormat({decimals: 3, forceDecimal: true});
var feedFormat = createFormat({decimals: 0});
var xOutput = createVariable({prefix: "X"}, xyzFormat);
var yOutput = createVariable({prefix: "Y"}, xyzFormat);
var zOutput = createVariable({prefix: "Z"}, xyzFormat);
var iOutput = createReferenceVariable({prefix: "I"}, xyzFormat);
var jOutput = createReferenceVariable({prefix: "J"}, xyzFormat);
var feedOutput = createVariable({prefix: "F"}, feedFormat);

function onSection() {
  // Wenn Nullpunkt gewechselt wird, ZUERST Z senkrecht hochfahren (Kollisionsschutz beim Umspannen):
  // G53 = Maschinen-Koordinatensystem
  // G00 = Eilgang
  // Z0.0 = Maximale Spindel-Rückzugshöhe
  writeWords("G53", "G00", "Z0.0");

  var wcs = currentSection.workOffset || 1;
  var wcsCode = "G" + (53 + wcs); // 1 -> G54 (1. Aufspannung), 2 -> G55 (2. Aufspannung umgedreht)

  // Wenn von G54 (OP10) auf G55 (OP20 - 2. Aufspannung) gewechselt wird:
  // Maschine stoppen (M00), Tisch nach vorne fahren (G53 G00 Y0.0) und Bediener zum Bauteil-Umdrehen auffordern!
  if (lastWcsCode !== "" && lastWcsCode !== wcsCode) {
    writeWords("M09");
    writeWords("M05");
    writeWords("G53", "G00", "Y0.0");
    writeln("(==========================================================)");
    writeln("(UMSPANN-STOPP OP10 -> OP20: BAUTEIL UM 180 GRAD UMDREHEN!)");
    writeln("(TEIL UMDREHEN UND AUF PARALLELUNTERLAGEN IN G55 SPANNEN)");
    writeln("(==========================================================)");
    writeWords("M00");
  }
  lastWcsCode = wcsCode;

  writeln("(=== NEUE AUFSPANNUNG: NULLPUNKT " + wcsCode + " ===)");
  if (hasParameter("operation-comment")) {
    writeln("(OPERATION: " + getParameter("operation-comment") + ")");
  }

  // T.. = Werkzeugplatz im Magazin
  // M06 = Werkzeugwechsel
  writeWords("T" + ("0" + tool.number).slice(-2), "M06");

  // S.. = Spindeldrehzahl in U/min
  // M03 = Rechtslauf Spindel EIN / M04 = Linkslauf Spindel EIN
  writeWords("S" + spindleSpeed, tool.clockwise ? "M03" : "M04");

  // G54 / G55 = Aktiviert den Nullpunkt der jeweiligen Aufspannung
  writeWords(wcsCode);
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
    "R" + xyzFormat.format(cycle.retract),
    "Q" + xyzFormat.format(cycle.incrementalDepth || 3.0),
    feedOutput.format(cycle.feedrate)
  );
}

function onCycleEnd() {
  writeWords("G80");
}

function onClose() {
  // M09 = Kühlmittel ausschalten
  writeWords("M09");

  // G53 G00 Z0.0 = Spindel senkrecht nach ganz oben fahren
  writeWords("G53", "G00", "Z0.0");

  // M05 = Frässpindel ausschalten (Spindel-Stopp)
  writeWords("M05");

  // G53 G00 Y0.0 = Maschinentisch nach vorne zum Bediener fahren
  writeWords("G53", "G00", "Y0.0");

  // M30 = Hauptprogrammende, Reset und Rücklauf zum Programmanfang
  writeWords("M30");
  writeln("%");
}

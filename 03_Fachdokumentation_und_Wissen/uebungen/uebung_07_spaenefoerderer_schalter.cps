/**
 * Übung 07: Eigener M-Code Schalter (Property) für Späneförderer (M31/M33)
 * Ziel: In den Einstellungen per Checkbox den Späneförderer automatisch ein- und ausschalten.
 */

description = "Uebung 07 - Spaenefoerderer M31/M33 Schalter";
vendor = "CNC Lernprojekt";
certificationLevel = 2;
extension = "nc";
setCodePage("ascii");
capabilities = CAPABILITY_MILLING;
tolerance = spatial(0.002, MM);

properties = {
  useChipConveyor: {
    title: "Späneförderer automatisch steuern (Use Chip Conveyor)",
    description: "Startet M31 bei onOpen() und stoppt M33 bei onClose()",
    type: "boolean",
    value: true,
    scope: "post"
  }
};

function onOpen() {
  writeln("%");
  writeln("O1007 (UEBUNG 07 - SPAENEFOERDERER SCHALTER)");

  // Sicherheits-Startblock:
  // G90 = Absolutmaß (Bezug auf Werkstück-Nullpunkt G54)
  // G21 = Metrisches Maßsystem (Millimeter)
  // G17 = Fräsebene XY
  // G40 = Fräserradiuskorrektur ausschalten
  // G80 = Bohrzyklen abbrechen
  writeWords("G90", "G21", "G17", "G40", "G80");

  if (getProperty("useChipConveyor")) {
    writeln("(SPAENEFOERDERER AUTOMATISCH STARTEN)");
    // M31 = Späneförderer (Förderschnecke / Transportband) VORWÄRTS STARTEN
    writeWords("M31");
  }
}

function onClose() {
  writeln("");
  // M09 = Kühlschmierstoff (KSS) ausschalten
  writeWords("M09");

  // G53 = Maschinen-Koordinatensystem
  // G00 = Eilgang (Schnellgang ohne Spanabtrag)
  // Z0.0 = Spindel ganz nach oben fahren
  writeWords("G53", "G00", "Z0.0");

  // M05 = Frässpindel ausschalten (Spindel-Stopp)
  writeWords("M05");

  if (getProperty("useChipConveyor")) {
    writeln("(SPAENEFOERDERER STOPPEN)");
    // M33 = Späneförderer STOPP
    writeWords("M33");
  }

  // G53 G00 Y0.0 = Maschinentisch ganz nach vorne fahren
  writeWords("G53", "G00", "Y0.0");

  // M30 = Hauptprogrammende, Rücklauf und Speicher-Reset
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

/**
 * Übung 14: Heidenhain Klartext-Ausgabe & 4. Drehachse (A-Achse mit Klemmung M10/M11)
 * Ziel: Vollständige Ausgabe im echten Heidenhain Klartext (.h Datei) mit TOOL CALL, L X Y FMAX M3 und A-Achsen-Drehung.
 */

description = "Uebung 14 - Heidenhain Klartext & 4. Achse";
vendor = "CNC Lernprojekt";
certificationLevel = 2;
extension = "h"; // Heidenhain Dateiendung ist .h
setCodePage("ascii");
capabilities = CAPABILITY_MILLING;
tolerance = spatial(0.002, MM);

var xyzFormat = createFormat({decimals:(unit == MM ? 3 : 4), forceDecimal:true});
var abcFormat = createFormat({decimals:3, forceDecimal:true});
var feedFormat = createFormat({decimals:0});
var lineNum = 0;
var currentA = undefined;

function writeHhLine() {
  var words = [lineNum];
  for (var i = 0; i < arguments.length; i++) {
    if (arguments[i] !== undefined && arguments[i] !== "") {
      words.push(arguments[i]);
    }
  }
  writeln(words.join(" "));
  lineNum++;
}

function onOpen() {
  lineNum = 0;
  currentA = undefined;
  // BEGIN PGM ... MM = Programmstart bei Heidenhain im metrischen System (Millimeter)
  writeHhLine("BEGIN PGM UEBUNG_14 MM");
  // BLK FORM 0.1 / 0.2 = Rohteildefinition (Quader / Rohling)
  writeHhLine("BLK FORM 0.1 Z X-5.000 Y-5.000 Z-15.000");
  writeHhLine("BLK FORM 0.2 X+85.000 Y+55.000 Z+0.000");
}

function onSection() {
  var toolDesc = tool.comment ? (" ; " + tool.comment) : "";
  var feedStr = (tool.number === 2) ? " F300" : "";
  writeHhLine("TOOL CALL", tool.number, "Z", "S" + spindleSpeed + feedStr + toolDesc);

  // Bestimmung des Sollwinkels der A-Drehachse (4. Achse / Teilapparat)
  var targetA = 0.0;
  if (typeof currentSection !== "undefined" && currentSection.hasParameter && currentSection.hasParameter("operation-comment")) {
    var c = currentSection.getParameter("operation-comment").toUpperCase();
    if (c.indexOf("A+90") !== -1 || c.indexOf("90 GRAD") !== -1 || c.indexOf("SEITE") !== -1 || c.indexOf("QUER") !== -1 || c.indexOf("BOHR") !== -1 || c.indexOf("NUT") !== -1) {
      targetA = 90.0;
    }
  }

  // 4. Achse (A-Achse Teilapparat) positionieren bei Initialisierung oder Winkelwechsel:
  if (currentA === undefined || Math.abs(currentA - targetA) > 0.001) {
    // M11 = Klemmung der Drehachse lösen vor Rotation
    writeHhLine("M11");
    // L A+... FMAX = Eilgang-Verdrehung der A-Achse
    writeHhLine("L", "A" + (targetA >= 0 ? "+" : "") + abcFormat.format(targetA), "FMAX");
    // M10 = Drehachse hydraulisch festklemmen für hohe Frässteifigkeit
    writeHhLine("M10");
    currentA = targetA;
  }

  // Erste Anfahrt in XY:
  var initialPos = (typeof currentSection !== "undefined" && currentSection.getInitialPosition) ? currentSection.getInitialPosition() : {x:0, y:0, z:2};
  writeHhLine("L", "X" + (initialPos.x >= 0 ? "+" : "") + xyzFormat.format(initialPos.x), "Y" + (initialPos.y >= 0 ? "+" : "") + xyzFormat.format(initialPos.y), "R0", "FMAX", tool.clockwise ? "M3" : "M4");

  // Anfahrt in Z auf 2 mm Sicherheitshöhe mit Kühlschmiermittel:
  writeHhLine("L", "Z+2.000", "R0", "FMAX", "M8");
}

function onRapid(x, y, z) {
  var words = ["L"];
  if (x !== undefined) words.push("X" + (x >= 0 ? "+" : "") + xyzFormat.format(x));
  if (y !== undefined) words.push("Y" + (y >= 0 ? "+" : "") + xyzFormat.format(y));
  if (z !== undefined) words.push("Z" + (z >= 0 ? "+" : "") + xyzFormat.format(z));
  words.push("R0");
  words.push("FMAX");
  writeHhLine.apply(null, words);
}

function onLinear(x, y, z, feed) {
  var words = ["L"];
  if (x !== undefined) words.push("X" + (x >= 0 ? "+" : "") + xyzFormat.format(x));
  if (y !== undefined) words.push("Y" + (y >= 0 ? "+" : "") + xyzFormat.format(y));
  if (z !== undefined) words.push("Z" + (z >= 0 ? "+" : "") + xyzFormat.format(z));
  words.push("R0");
  if (feed !== undefined) words.push("F" + feedFormat.format(feed));
  writeHhLine.apply(null, words);
}

function onCycle() {
  writeHhLine("CYCL DEF 200 BOHREN ~");
  writeHhLine("  Q200=2.000", "; SICHERHEITS-ABST. ~");
  writeHhLine("  Q201=" + xyzFormat.format(cycle.bottom !== undefined ? cycle.bottom : -12.0), "; TIEFE ~");
  writeHhLine("  Q206=" + feedFormat.format(cycle.feedrate !== undefined ? cycle.feedrate : 300), "; VORSCHUB TIEFENZ. ~");
  writeHhLine("  Q202=4.000", "; ZUSTELL-TIEFE ~");
  writeHhLine("  Q210=0", "; VERWEILZEIT OBEN ~");
  writeHhLine("  Q203=+0.000", "; KOOR. OBERFLAECHE ~");
  writeHhLine("  Q204=15.000", "; 2. SICHERHEITS-ABST. ~");
  writeHhLine("  Q211=0", "; VERWEILZEIT UNTEN");
}

function onCyclePoint(x, y, z) {
  writeHhLine("L", "X" + (x >= 0 ? "+" : "") + xyzFormat.format(x), "Y" + (y >= 0 ? "+" : "") + xyzFormat.format(y), "R0", "FMAX", "M99");
}

function onCycleEnd() {
  // Zyklus beendet
}

function onClose() {
  // Z+250.000 R0 FMAX M91 M9 = Im Eilgang maschinenbezogen (M91) freifahren und Kühlmittel ausschalten (M9)
  writeHhLine("L", "Z+250.000", "R0", "FMAX", "M91", "M9");

  // M30 = Hauptprogramm-Ende und Rücksprung
  writeHhLine("M30");

  // END PGM ... MM = Offizielles Programmende nach Heidenhain Klartext-Syntax
  writeHhLine("END PGM UEBUNG_14 MM");
}

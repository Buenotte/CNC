/**
 * ==============================================================================
 * MAßGESCHNEIDERTER KUNDEN-POSTPROZESSOR (.CPS)
 * ==============================================================================
 * KUNDE       : Mueller Praezisionsteile GmbH
 * ENTWICKLER  : Dipl.-Ing. CNC-Büro
 * STEUERUNG   : SIEMENS
 * GENERIERT AM: 2026-10-21 16:43
 * BESCHREIBUNG: VENTILBLOCK OP10
 * ==============================================================================
 */

description = "Mueller Praezisionsteile GmbH - SIEMENS Postprozessor";
vendor = "Mueller Praezisionsteile GmbH";
vendorUrl = "https://github.com/Buenotte/CNC";
legal = "Erstellt durch CAD/CAM Ingenieurbuero. Alle Rechte vorbehalten.";
certificationLevel = 2;
minimumRevision = 45700;

extension = "mpf";
programNameIsInteger = true;
setCodePage("ascii");

capabilities = CAPABILITY_MILLING;
tolerance = spatial(0.002, MM);

minimumChordLength = spatial(0.25, MM);
minimumCircularRadius = spatial(0.01, MM);
maximumCircularRadius = spatial(1000, MM);
minimumCircularAngle = toRad(0.01);
maximumCircularAngle = toRad(180);
underscaledArcGoal = false;

// Formatierer für Koordinaten und Vorschübe
var xyzFormat = createFormat({decimals: 3, forceDecimal: true});
var feedFormat = createFormat({decimals: 0});
var toolFormat = createFormat({decimals: 0});

var xOutput = createVariable({prefix: "X"}, xyzFormat);
var yOutput = createVariable({prefix: "Y"}, xyzFormat);
var zOutput = createVariable({prefix: "Z"}, xyzFormat);
var feedOutput = createVariable({prefix: "F"}, feedFormat);

// Benutzer-Optionen (Properties in Autodesk Fusion)
properties = {
  showZMinInfo: {
    title: "Z-Min Sicherheitsprüfung anzeigen",
    description: "Berechnet automatisch die tiefste Frästiefe Z-MIN für jedes Werkzeug",
    type: "boolean",
    value: true
  },
  showToolTable: {
    title: "Werkzeugtabelle im Header ausgeben",
    description: "Gibt alle benötigten Werkzeuge im Programmkopf aus",
    type: "boolean",
    value: true
  },
  retractTableToDoor: {
    title: "Tisch am Ende zur Tür fahren",
    description: "Fährt Maschinentisch zum bequemen Entladen zur Tür (G53 Y0)",
    type: "boolean",
    value: true
  }
};

/**
 * 🛡️ SICHERHEITSFUNKTION: Berechnet die tiefste Z-Koordinate (Z-MIN)
 */
function getToolMinimumZ(tool) {
  var zMin = undefined;
  var numberOfSections = getNumberOfSections();
  for (var i = 0; i < numberOfSections; ++i) {
    var section = getSection(i);
    if (section.getTool().number == tool.number) {
      var currentMin = section.getGlobalZRange().getMinimum();
      if (zMin === undefined || currentMin < zMin) {
        zMin = currentMin;
      }
    }
  }
  return zMin;
}


/**
 * 1. onOpen() - PROGRAMMSTART & HEADER
 */
function onOpen() {
  writeln("%");
  writeComment("==================================================");
  writeComment("KUNDE      : " + "Mueller Praezisionsteile GmbH");
  writeComment("PROGRAMM   : O" + 2002 + " (" + "VENTILBLOCK OP10" + ")");
  writeComment("STEUERUNG  : " + "SIEMENS");
  writeComment("ENTWICKLER : " + "Dipl.-Ing. CNC-Büro");
  writeComment("DATUM/ZEIT : " + "2026-10-21 16:43");
  writeComment("EINHEITEN  : " + "METRISCH (MM)");
  writeComment("==================================================");

  if (getProperty("showToolTable")) {
    writeComment("--- BENOETIGTE WERKZEUGE - TOOL TABLE ---");
    var tools = getToolTable();
    for (var i = 0; i < tools.getNumberOfTools(); ++i) {
      var t = tools.getTool(i);
      var zMinVal = getToolMinimumZ(t);
      var zMinStr = (zMinVal !== undefined) ? (" | Z-MIN=" + xyzFormat.format(zMinVal) + "MM") : "";
      writeComment("T" + toolFormat.format(t.number) + " | D=" + xyzFormat.format(t.diameter) + "MM" + zMinStr + " | " + t.comment);
    }
    writeComment("-----------------------------------------");
  }

  // Sicherheits-Startblock (Maschinen-Reset)
  writeWords("G90", "G71", "G17", "G40", "G64");
}

/**
 * 2. onSection() - WERKZEUGWECHSEL & OPERATIONS-START
 */
function onSection() {
  var tool = currentSection.getTool();
  writeComment("--------------------------------------------------");
  var opComment = currentSection.hasParameter("operation-comment") ? currentSection.getParameter("operation-comment") : "OPERATION";
  writeComment("OPERATION: " + opComment);
  
  if (getProperty("showZMinInfo")) {
    var zRange = currentSection.getGlobalZRange();
    writeComment("SICHERHEITS-INFO: OP Z-MIN=" + xyzFormat.format(zRange.getMinimum()) + "MM | OP Z-MAX=" + xyzFormat.format(zRange.getMaximum()) + "MM");
    if (zRange.getMinimum() < -18) {
      writeComment("ACHTUNG KOLLISIONSGEFAHR: DIESE OPERATION GEHT TIEFER ALS " + -18 + "MM!");
    }
  }

  writeComment("--------------------------------------------------");

  // Werkzeugwechsel
  writeWords("T=" + tool.number, "M06");

  // Nullpunkt G54 aufrufen
  writeWords("G54");

  // Spindeldrehzahl & Drehrichtung im Uhrzeigersinn
  writeWords("S" + tool.spindleRPM, "M03");

  // Längenkorrektur & Kühlmittel einschalten (M88)
  writeWords("D1", "Z15.0", "M88");
}

/**
 * 3. FAHRBEWEGUNGEN
 */
function onRapid(x, y, z) {
  var xStr = xOutput.format(x);
  var yStr = yOutput.format(y);
  var zStr = zOutput.format(z);
  if (xStr || yStr || zStr) {
    writeWords("G00", xStr, yStr, zStr);
  }
}

function onLinear(x, y, z, feed) {
  var xStr = xOutput.format(x);
  var yStr = yOutput.format(y);
  var zStr = zOutput.format(z);
  var fStr = feedOutput.format(feed);
  writeWords("G01", xStr, yStr, zStr, fStr);
}

function onCircular(clockwise, cx, cy, cz, x, y, z, feed) {
  var xStr = xOutput.format(x);
  var yStr = yOutput.format(y);
  var zStr = zOutput.format(z);
  var fStr = feedOutput.format(feed);
  var cmd = clockwise ? "G02" : "G03";
  writeWords(cmd, xStr, yStr, zStr, fStr);
}

function onCyclePoint(x, y, z) {
  var xStr = xOutput.format(x);
  var yStr = yOutput.format(y);
  var zStr = zOutput.format(z);
  writeWords("G83", xStr, yStr, zStr, "R2.000", "Q3.000", "F300");
}

/**
 * 4. onClose() - PROGRAMMENDE
 */
function onClose() {
  // Kühlmittel ausschalten
  writeWords("M09");
  
  // Spindel anhalten
  writeWords("M05");

  // Werkzeug auf Maschinen-Z-Home freifahren
  writeWords("SUPA", "G00", "Z0.0", "D0");

  if (getProperty("retractTableToDoor")) {
    writeComment("TISCH ZUR TUER FAHREN ZUM BEQUEMEN ENTLADEN");
    writeWords("SUPA", "G00", "Y0.0", "D0");
  }

  // Programmende & Rücksprung
  writeWords("M30");
  writeln("%");
}

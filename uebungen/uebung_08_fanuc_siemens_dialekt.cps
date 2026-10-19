/**
 * Übung 08: Steuerungs-Dialekt Umschalter (Haas / Fanuc ISO vs. Siemens Sinumerik)
 * Ziel: Derselbe Postprozessor erzeugt per Dropdown-Schalter entweder ISO-Format (...) oder Siemens-Format ;
 */

description = "Uebung 08 - Fanuc vs Siemens Umschalter";
vendor = "CNC Lernprojekt";
certificationLevel = 2;
extension = "nc";
setCodePage("ascii");
capabilities = CAPABILITY_MILLING;
tolerance = spatial(0.002, MM);

properties = {
  controllerDialect: {
    title: "Steuerungs-Dialekt (Controller Dialect)",
    description: "Wähle zwischen Haas/Fanuc ISO oder Siemens Sinumerik",
    type: "enum",
    values: [
      {id: "fanuc", title: "Haas / Fanuc ISO Standard"},
      {id: "siemens", title: "Siemens Sinumerik (840D/ONE)"}
    ],
    value: "fanuc",
    scope: "post"
  }
};

function writeCustomComment(text) {
  if (getProperty("controllerDialect") === "siemens") {
    writeln("; " + String(text).toUpperCase());
  } else {
    writeln("(" + String(text).toUpperCase() + ")");
  }
}

function onOpen() {
  var isSiemens = (getProperty("controllerDialect") === "siemens");

  if (!isSiemens) {
    writeln("%");
    writeln("O1008 (UEBUNG 08 - FANUC)");
  } else {
    writeln("; PROGRAMM: UEBUNG_08_SIEMENS");
  }

  writeCustomComment("STEUERUNG GEWAEHLT: " + (isSiemens ? "SIEMENS SINUMERIK" : "HAAS/FANUC ISO"));

  if (isSiemens) {
    writeWords("G90", "G71", "G17"); // G71 = metrisch bei Siemens
  } else {
    writeWords("G90", "G21", "G17", "G40", "G80");
  }
}

function onSection() {
  var isSiemens = (getProperty("controllerDialect") === "siemens");
  writeCustomComment("OPERATION: " + (currentSection.getTool().description || "BEARBEITUNG"));

  if (isSiemens) {
    writeWords("T=\"" + (tool.description || "TOOL_" + tool.number) + "\"", "D1");
    writeWords("M06");
  } else {
    writeWords("T" + ("0" + tool.number).slice(-2), "M06");
  }

  writeWords("S" + spindleSpeed, tool.clockwise ? "M03" : "M04");
  writeWords(isSiemens ? "G54" : "G54");
}

function onClose() {
  var isSiemens = (getProperty("controllerDialect") === "siemens");
  writeWords("M09");
  writeWords(isSiemens ? "SUPA G00 Z0.0" : "G53 G00 Z0.0"); // SUPA = Siemens Maschinenkoordinaten
  writeWords("M05");
  writeWords("M30");

  if (!isSiemens) {
    writeln("%");
  }
}

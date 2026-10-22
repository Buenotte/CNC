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
    // Siemens Sinumerik Initialisierung:
    // G90 = Absolutmaß (Bezug auf Werkstück-Nullpunkt)
    // G71 = Maßeinheit Millimeter (metrisch nach DIN/ISO bei Siemens)
    // G17 = Arbeitsebene XY
    writeWords("G90", "G71", "G17");
  } else {
    // Fanuc / Haas ISO-Standard Initialisierung:
    // G90 = Absolutmaß
    // G21 = Maßeinheit Millimeter (metrisch bei Fanuc/Haas)
    // G17 = Arbeitsebene XY
    // G40 = Radiuskorrektur ausschalten
    // G80 = Bohrzyklen abbrechen
    writeWords("G90", "G21", "G17", "G40", "G80");
  }
}

function onSection() {
  var isSiemens = (getProperty("controllerDialect") === "siemens");
  writeCustomComment("OPERATION: " + (currentSection.getTool().description || "BEARBEITUNG"));

  if (isSiemens) {
    // Siemens: Werkzeugaufruf im Klartext-Namen mit Schneidennummer D1
    // T="NAME" = Werkzeugname in Anführungszeichen
    // D1 = Schneide 1 (Schneiden-Korrekturregister)
    // M06 = Werkzeugwechsel durchführen
    writeWords("T=\"" + (tool.description || "TOOL_" + tool.number) + "\"", "D1");
    writeWords("M06");
  } else {
    // Fanuc/Haas: Werkzeugnummer 2-stellig mit M06
    // T01, T02... = Werkzeugnummer
    // M06 = Werkzeugwechsel
    writeWords("T" + ("0" + tool.number).slice(-2), "M06");
  }

  // S.. = Spindeldrehzahl in U/min
  // M03 = Spindeldrehung im Uhrzeigersinn (Rechtslauf)
  // M04 = Spindeldrehung gegen den Uhrzeigersinn (Linkslauf)
  writeWords("S" + spindleSpeed, tool.clockwise ? "M03" : "M04");

  // G54 = Erstes einstellbares Werkstück-Koordinatensystem
  writeWords(isSiemens ? "G54" : "G54");
}

function onClose() {
  var isSiemens = (getProperty("controllerDialect") === "siemens");

  // M09 = Kühlschmierstoff ausschalten
  writeWords("M09");

  // Sicherer Z-Rückzug:
  // Siemens: SUPA G00 Z0.0 = Satzweise Unterdrückung aller programmierbaren Nullpunktverschiebungen (Maschinen-Z0)
  // Fanuc: G53 G00 Z0.0 = Fahrt im Maschinenkoordinatensystem G53 im Eilgang G00 auf Z0.0
  writeWords(isSiemens ? "SUPA G00 Z0.0" : "G53 G00 Z0.0");

  // M05 = Frässpindel ausschalten
  writeWords("M05");

  // M30 = Hauptprogrammende, Reset und Rücksprung
  writeWords("M30");

  if (!isSiemens) {
    writeln("%");
  }
}

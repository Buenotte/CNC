/**
 * Übung 09: Schnittdaten-Prüfung und Drehzahlschutz (Schnittgeschwindigkeit Vc)
 * Ziel: Postprozessor warnt automatisch, wenn Spindeldrehzahl oder Vorschub für das Material unpassend sind.
 */

description = "Uebung 09 - Schnittdaten Pruefung";
vendor = "CNC Lernprojekt";
certificationLevel = 2;
extension = "nc";
setCodePage("ascii");
capabilities = CAPABILITY_MILLING;
tolerance = spatial(0.002, MM);

properties = {
  maxSpindleSpeedWarning: {
    title: "Max. Drehzahl Warnschwelle (RPM)",
    description: "Gibt im G-Code eine Warnung aus, wenn Drehzahl höher ist",
    type: "integer",
    value: 10000,
    scope: "post"
  }
};

function onOpen() {
  writeln("%");
  writeln("O1009 (UEBUNG 09 - SCHNITTDATEN-CHECK)");

  // Sicherheits-Startblock:
  // G90 = Absolutmaß (Bezug auf Werkstück-Nullpunkt G54)
  // G21 = Metrisches Maßsystem (Millimeter mm)
  // G17 = Fräsebene XY (Werkzeugachse ist Z)
  // G40 = Werkzeugradiuskorrektur ausschalten
  // G80 = Bohrzyklen abbrechen
  writeWords("G90", "G21", "G17", "G40", "G80");
}

function onSection() {
  var maxRpm = getProperty("maxSpindleSpeedWarning");
  if (spindleSpeed > maxRpm) {
    writeln("(ACHTUNG SICHERHEIT: DREHZAHL S=" + spindleSpeed + " UEBERSCHREITET SCHWELLE " + maxRpm + " RPM!)");
  } else {
    writeln("(SCHNITTDATEN OK: S=" + spindleSpeed + " RPM)");
  }

  // T.. = Werkzeugnummer (Tool)
  // M06 = Automatischer Werkzeugwechsel durch Greifer
  writeWords("T" + ("0" + tool.number).slice(-2), "M06");

  // S.. = Spindeldrehzahl in U/min
  // M03 = Spindel Rechtslauf EIN (im Uhrzeigersinn)
  // M04 = Spindel Linkslauf EIN (gegen den Uhrzeigersinn)
  writeWords("S" + spindleSpeed, tool.clockwise ? "M03" : "M04");

  // G54 = 1. Werkstück-Koordinatensystem
  writeWords("G54");
}

function onClose() {
  // M09 = Kühlschmierstoff ausschalten
  writeWords("M09");

  // G53 = Maschinen-Koordinatensystem
  // G00 = Eilgang (Schnellgang ohne Spanabtrag)
  // Z0.0 = Spindel senkrecht nach oben auf Maschinen-Referenzhöhe fahren
  writeWords("G53", "G00", "Z0.0");

  // M05 = Frässpindel ausschalten (Spindel-Stopp)
  writeWords("M05");

  // M30 = Hauptprogrammende, Rücklauf und Speicher-Reset
  writeWords("M30");
  writeln("%");
}

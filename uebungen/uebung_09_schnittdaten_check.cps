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
  writeWords("G90", "G21", "G17", "G40", "G80");
}

function onSection() {
  var maxRpm = getProperty("maxSpindleSpeedWarning");
  if (spindleSpeed > maxRpm) {
    writeln("(ACHTUNG SICHERHEIT: DREHZAHL S=" + spindleSpeed + " UEBERSCHREITET SCHWELLE " + maxRpm + " RPM!)");
  } else {
    writeln("(SCHNITTDATEN OK: S=" + spindleSpeed + " RPM)");
  }

  writeWords("T" + ("0" + tool.number).slice(-2), "M06");
  writeWords("S" + spindleSpeed, tool.clockwise ? "M03" : "M04");
  writeWords("G54");
}

function onClose() {
  writeWords("M09");
  writeWords("G53", "G00", "Z0.0");
  writeWords("M05");
  writeWords("M30");
  writeln("%");
}

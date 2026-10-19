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
  writeWords("G90", "G21", "G17", "G40", "G80");
}

function onSection() {
  // Wenn Nullpunkt gewechselt wird, zuerst Z hochfahren!
  writeWords("G53", "G00", "Z0.0");

  var wcs = currentSection.workOffset || 1;
  var wcsCode = "G" + (53 + wcs); // 1 -> G54, 2 -> G55

  writeln("(=== NEUE AUFSPANNUNG: NULLPUNKT " + wcsCode + " ===)");
  writeWords("T" + ("0" + tool.number).slice(-2), "M06");
  writeWords("S" + spindleSpeed, tool.clockwise ? "M03" : "M04");
  writeWords(wcsCode);
}

function onClose() {
  writeWords("M09");
  writeWords("G53", "G00", "Z0.0");
  writeWords("M05");
  writeWords("G53", "G00", "Y0.0");
  writeWords("M30");
  writeln("%");
}

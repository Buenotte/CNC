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

function onSection() {
  // Wenn Nullpunkt gewechselt wird, ZUERST Z senkrecht hochfahren (Kollisionsschutz beim Umspannen):
  // G53 = Maschinen-Koordinatensystem
  // G00 = Eilgang
  // Z0.0 = Maximale Spindel-Rückzugshöhe
  writeWords("G53", "G00", "Z0.0");

  var wcs = currentSection.workOffset || 1;
  var wcsCode = "G" + (53 + wcs); // 1 -> G54 (1. Aufspannung), 2 -> G55 (2. Aufspannung umgedreht)

  writeln("(=== NEUE AUFSPANNUNG: NULLPUNKT " + wcsCode + " ===)");

  // T.. = Werkzeugplatz im Magazin
  // M06 = Werkzeugwechsel
  writeWords("T" + ("0" + tool.number).slice(-2), "M06");

  // S.. = Spindeldrehzahl in U/min
  // M03 = Rechtslauf Spindel EIN / M04 = Linkslauf Spindel EIN
  writeWords("S" + spindleSpeed, tool.clockwise ? "M03" : "M04");

  // G54 / G55 = Aktiviert den Nullpunkt der jeweiligen Aufspannung
  writeWords(wcsCode);
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

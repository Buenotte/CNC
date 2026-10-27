/**
 * Übung 13: 3D-Freiformflächen (3D Adaptive Clearing & Kugelfräser)
 * Ziel: 3-Achs-Simultanbewegungen (X, Y und Z gleichzeitig in einer Zeile) mit hoher Toleranz und Linearisierung.
 */

description = "Uebung 13 - 3D Freiformflaechen";
vendor = "CNC Lernprojekt";
certificationLevel = 2;
extension = "nc";
setCodePage("ascii");
capabilities = CAPABILITY_MILLING;
tolerance = spatial(0.005, MM); // Feine 3D-Toleranz

var xyzFormat = createFormat({decimals:(unit == MM ? 3 : 4), forceDecimal:true});
var feedFormat = createFormat({decimals:(unit == MM ? 0 : 1), forceDecimal:false});

var xOutput = createVariable({prefix:"X"}, xyzFormat);
var yOutput = createVariable({prefix:"Y"}, xyzFormat);
var zOutput = createVariable({prefix:"Z"}, xyzFormat);
var feedOutput = createVariable({prefix:"F"}, feedFormat);
var coolantOn = false; // merkt sich, ob der Kühlschmierstoff (M08) schon läuft
var smoothingActive = false; // merkt sich, ob G187 (HSM-Bahnverschleifung) aktiv ist

function onOpen() {
  writeln("%");
  writeln("O1013 (UEBUNG 13 - 3D FREIFORM)");

  // Sicherheits-Startblock:
  // G90 = Absolutmaß (Bezug auf Werkstück-Nullpunkt G54)
  // G21 = Metrisches Einheitensystem in Millimeter (mm)
  // G17 = Fräsebene XY
  // G40 = Radiuskorrektur ausschalten
  // G49 = Werkzeuglängenkorrektur ausschalten (löscht eine alte G43 vom Vorprogramm)
  // G80 = Bohrzyklen abbrechen
  writeWords("G90", "G21", "G17", "G40", "G49", "G80");
}

function onSection() {
  writeln("");
  var isBall = (typeof tool.type !== "undefined" && tool.type === TOOL_MILLING_END_BALL) ||
               (tool.cornerRadius > 0 && Math.abs(tool.cornerRadius - tool.diameter / 2) < 0.01) ||
               (tool.comment && /KUGEL|BALL/i.test(tool.comment));

  if (hasParameter("operation-comment")) {
    writeln("(OPERATION: " + getParameter("operation-comment") + ")");
  } else if (isBall) {
    writeln("(OPERATION: 3D FREIFORMFLAECHEN SCHLICHTEN - KUGELFRAESER)");
  } else {
    writeln("(OPERATION: 3D ADAPTIVE CLEARING - VORRAEUMUNG MIT SCHAFTFRAESER)");
  }

  if (isBall) {
    writeln("(WERKZEUG-INFO: KUGELFRAESER VOLLRADIUS R=" + (tool.diameter / 2).toFixed(3) + "MM | D=" + tool.diameter.toFixed(3) + "MM)");
    writeln("(HSM-INFO: 3-ACHS-SIMULTANBEWEGUNGEN MIT SEHNEN-TOLERANZ 0.005MM)");
  }

  // G53 G00 Z0.0 = Spindel senkrecht nach oben auf Maschinenreferenz fahren
  writeWords("G53", "G00", "Z0.0");

  // T.. = Kugelfräser-Werkzeugnummer
  // M06 = Werkzeugwechsel
  writeWords("T" + ("0" + tool.number).slice(-2), "M06");

  // S.. = Spindeldrehzahl in U/min
  // M03 = Spindel Rechtslauf EIN / M04 = Spindel Linkslauf EIN
  writeWords("S" + spindleSpeed, tool.clockwise ? "M03" : "M04");

  // G54 = 1. Werkstück-Koordinatensystem
  writeWords("G54");

  // G00 G43 H.. Z15.000 = Werkzeuglängenkorrektur EIN (G43 = Längenkorrektur positiv, H.. = Korrekturregister
  // passend zur Werkzeugnummer: T01 -> H01) und gleichzeitig auf sichere Höhe Z+15 mm fahren.
  // Erst ab hier rechnet die Steuerung mit der gemessenen Werkzeuglänge - vor jeder Bewegung ins Material!
  writeWords("G00", "G43", "H" + ("0" + tool.lengthOffset).slice(-2), "Z" + xyzFormat.format(15));

  // M08 = Kühlschmierstoff EIN (einmal pro Programm, ausgeschaltet wird mit M09 am Ende)
  if (tool.coolant != COOLANT_OFF && !coolantOn) {
    writeWords("M08");
    coolantOn = true;
  }

  // G187 P3 E0.005 = Haas-Bahnverschleifung (Look-Ahead / HSM-Glättung) nur für das 3D-Schlichten mit Kugelfräser:
  //   P3 = Genauigkeitsstufe "Finish" (höchste Konturtreue, Steuerung bremst vor Ecken nur minimal)
  //   E0.005 = maximal zulässige Eckenverrundung 0,005 mm (passt zur CAM-Sehnentoleranz 0.005 mm)
  if (isBall) {
    writeWords("G187", "P3", "E0.005");
    smoothingActive = true;
  }

  xOutput.reset();
  yOutput.reset();
  zOutput.reset();
  feedOutput.reset();
}

function onRapid(x, y, z) {
  // G00 = Eilgangbewegung (schnellstmögliche Positionierung durch die Luft)
  writeWords("G00", xOutput.format(x), yOutput.format(y), zOutput.format(z));
}

function onLinear(x, y, z, feed) {
  // G01 = Linearer Arbeitsvorschub im Material (bei 3D-Freiformflächen bewegen sich X, Y und Z simultan)
  // F.. = Vorschubgeschwindigkeit in mm/min
  writeWords("G01", xOutput.format(x), yOutput.format(y), zOutput.format(z), feedOutput.format(feed));
}

function onClose() {
  // G187 (ohne Parameter) = Bahnverschleifung zurück auf Maschinen-Standard setzen
  if (smoothingActive) {
    writeWords("G187");
    smoothingActive = false;
  }

  // M09 = Kühlmittel ausschalten
  writeWords("M09");
  coolantOn = false;

  // G53 G00 Z0.0 = Spindel senkrecht nach ganz oben fahren
  writeWords("G53", "G00", "Z0.0");

  // M05 = Frässpindel ausschalten
  writeWords("M05");

  // M30 = Hauptprogrammende, Reset und Rücklauf
  writeWords("M30");
  writeln("%");
}

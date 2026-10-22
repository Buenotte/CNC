/**
 * Übung 12: Werkzeugradiuskorrektur (G41 / G42 / G40) für Passungen (H7)
 * Ziel: G41 mit D-Korrekturregister auf geradem Anfahrweg (G01) ein- und mit G40 sicher ausschalten.
 */

description = "Uebung 12 - Werkzeugradiuskorrektur G41 G42";
vendor = "CNC Lernprojekt";
certificationLevel = 2;
extension = "nc";
setCodePage("ascii");
capabilities = CAPABILITY_MILLING;
tolerance = spatial(0.002, MM);

var xyzFormat = createFormat({decimals:(unit == MM ? 3 : 4), forceDecimal:true});
var feedFormat = createFormat({decimals:(unit == MM ? 0 : 1), forceDecimal:false});
var dFormat = createFormat({prefix:"D", width:2, zeropad:true, decimals:0});

function onOpen() {
  writeln("%");
  writeln("O1012 (UEBUNG 12 - RADIUSKORREKTUR G41)");

  // Sicherheits-Startblock:
  // G90 = Absolutmaß (Bezug auf Werkstück-Nullpunkt G54)
  // G21 = Maßeinheiten in Millimeter (metrisch)
  // G17 = Fräsebene XY
  // G40 = Werkzeugradiuskorrektur ausschalten (Grundstellung)
  // G80 = Bohrzyklen abbrechen
  writeWords("G90", "G21", "G17", "G40", "G80");
}

function onSection() {
  // G53 G00 Z0.0 = Spindel vor Werkzeugwechsel ganz nach oben fahren
  writeWords("G53", "G00", "Z0.0");

  // T.. = Fräswerkzeugnummer
  // M06 = Werkzeugwechsel
  writeWords("T" + ("0" + tool.number).slice(-2), "M06");

  // S.. = Spindeldrehzahl in U/min
  // M03 = Spindel Rechtslauf EIN / M04 = Spindel Linkslauf EIN
  writeWords("S" + spindleSpeed, tool.clockwise ? "M03" : "M04");

  // G54 = 1. Werkstück-Koordinatensystem
  writeWords("G54");
}

function onRadiusComp(compensation) {
  // compensation: 0 = G40 (Aus), 1 = G41 (Links), 2 = G42 (Rechts)
  if (compensation == 1) {
    // G41 = Fräserradiuskorrektur LINKS in Vorschubrichtung (Gleichlauffräsen)
    // D.. = Korrekturregister für Werkzeugdurchmesser/Radius an der Steuerung
    writeln("(RADIUSKORREKTUR LINKS G41 AKTIVIEREN MIT D" + ("0" + tool.number).slice(-2) + ")");
  } else if (compensation == 2) {
    // G42 = Fräserradiuskorrektur RECHTS in Vorschubrichtung (Gegenlauffräsen)
    writeln("(RADIUSKORREKTUR RECHTS G42 AKTIVIEREN)");
  } else {
    // G40 = Fräserradiuskorrektur ABWÄHLEN (Fräsermitte fährt wieder direkt auf Kontur)
    writeln("(RADIUSKORREKTUR AUSSCHALTEN G40)");
  }
}

function onClose() {
  // G40 = Sicherheits-Abschaltung der Radiuskorrektur am Programmende
  writeWords("G40");

  // M09 = Kühlschmierstoff ausschalten
  writeWords("M09");

  // G53 G00 Z0.0 = Spindel senkrecht nach oben auf Maschinenreferenz
  writeWords("G53", "G00", "Z0.0");

  // M05 = Frässpindel ausschalten
  writeWords("M05");

  // M30 = Hauptprogrammende, Reset und Rücklauf
  writeWords("M30");
  writeln("%");
}

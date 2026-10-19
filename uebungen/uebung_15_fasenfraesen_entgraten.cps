/**
 * Übung 15: Fasenfräsen und Entgraten (45-Grad-Fasenfräser)
 * 
 * Lernziel:
 * Sichere Führung von Entgratfräsern (Fasenfräsern) zur Entfernung scharfer Kanten
 * mit Radiuskorrektur (G41/G42) und präziser Z-Zustellung unter Berücksichtigung
 * der Werkzeugspitze (Tip Offset / Spitzenversatz).
 */

description = "Uebung 15 - Fasenfraesen und Entgraten 45 Grad";
vendor = "CNC Akademie";
legal = "Open Source";
certificationLevel = 2;
extension = "nc";
setCodePage("ascii");

// Eigenschaft: Fasenbreite in Millimeter
properties = {
  chamferWidth: 0.5, // 0.5 mm Fase
  tipOffset: 1.0     // 1.0 mm Werkzeugspitze unter die Fase eintauchen (verhindert Schnitt an empfindlicher Nullspitze)
};

function onOpen() {
  writeComment("========================================");
  writeComment("UEBUNG 15: ENTGRATEN UND FASENFRAESEN (45 GRAD)");
  writeComment("FASENBREITE: " + properties.chamferWidth + " mm");
  writeComment("SPITZENVERSATZ (TIP OFFSET): " + properties.tipOffset + " mm");
  writeComment("========================================");
  
  // Grundinitialisierung der Fräsmaschine:
  // G90 = Absolutmaß (Bezug auf Werkstück-Nullpunkt G54)
  // G17 = Fräsebene XY
  // G21 = Maßeinheiten in Millimeter (metrisch)
  // G94 = Vorschub F in mm/min
  writeBlock("G90", "G17", "G21", "G94");

  // Sicherheitsfahrt der Z-Achse auf den Referenzpunkt:
  // G28 = Maschinen-Referenzpunktfahrt
  // G91 = Relativmaß (Kettenmaß)
  // Z0. = Direkt senkrecht nach oben fahren
  writeBlock("G28", "G91", "Z0.");

  // G90 = Sofort wieder zurückschalten in den Absolutmaß-Modus
  writeBlock("G90");
}

function onSection() {
  var tool = currentSection.getTool();
  writeComment("--- FASENFRAESER T" + tool.number + " EINWECHSELN ---");

  // T.. = Werkzeugplatz im Magazin (45-Grad-Fasenfräser)
  // M06 = Werkzeugwechsel durchführen
  writeBlock("T" + tool.number, "M06");

  // G54 = 1. Werkstück-Koordinatensystem
  writeBlock("G54");

  // S.. = Spindeldrehzahl in U/min
  // M03 = Spindel Rechtslauf EIN
  writeBlock("S" + tool.spindleRPM, "M03");

  // G43 = Werkzeuglängenkorrektur EIN
  // H.. = Längen-Korrekturregister
  // Z5.0 = Erste Z-Zustellung auf 5 mm Sicherheitshöhe
  writeBlock("G43", "H" + tool.number, "Z5.0");

  // M08 = Kühlschmierstoff EIN
  writeBlock("M08");

  // Effektive Frästiefe = Fasenbreite + Spitzenversatz
  var zDepth = -(properties.chamferWidth + properties.tipOffset);
  writeComment("EFFEKTIVE FASENTIEFE: Z" + zDepth.toFixed(3));

  // G00 = Eilgang-Vorpositionierung neben dem Werkstück
  writeBlock("G00", "X0.", "Y-5.0");

  // G01 = Linearer Vorschub auf die programmierte Fasentiefe
  writeBlock("G01", "Z" + zDepth.toFixed(3), "F1000");

  // G41 = Fräserradiuskorrektur LINKS aktivieren (Werkzeug fährt links an der Kontur entlang)
  // D.. = Schneiden-Durchmesserregister an der Steuerung
  writeBlock("G41", "X0.", "Y0.", "D" + tool.number, "F1500");

  writeComment("--- KONTUR UMLAUFEN (FASENFRAESEN) ---");
  // G01 = Geradliniges Konturfräsen der 4 Außenkanten
  writeBlock("G01", "X100.0");
  writeBlock("G01", "Y100.0");
  writeBlock("G01", "X0.");
  writeBlock("G01", "Y0.");

  // G40 = Radiuskorrektur sauber abwählen auf der Freifahrbewegung
  writeBlock("G40", "X0.", "Y-5.0");

  // G00 Z10.0 = Eilgang-Rückzug auf sichere Höhe
  writeBlock("G00", "Z10.0");
}

function onClose() {
  writeComment("--- FASENFRAESEN ERFOLGREICH BEENDET ---");

  // M09 = Kühlschmierstoff ausschalten
  writeBlock("M09");

  // M05 = Frässpindel ausschalten
  writeBlock("M05");

  // G28 G91 Z0. = Z-Achse ganz nach oben auf Maschinenreferenz fahren
  writeBlock("G28", "G91", "Z0.");

  // G28 Y0. = Maschinentisch nach vorne zum Bediener fahren
  writeBlock("G28", "Y0.");

  // M30 = Hauptprogramm-Ende und Rücklauf
  writeBlock("M30");
}

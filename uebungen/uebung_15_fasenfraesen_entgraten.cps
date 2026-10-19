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
  
  writeBlock("G90", "G17", "G21", "G94");
  writeBlock("G28", "G91", "Z0.");
  writeBlock("G90");
}

function onSection() {
  var tool = currentSection.getTool();
  writeComment("--- FASENFRAESER T" + tool.number + " EINWECHSELN ---");
  writeBlock("T" + tool.number, "M06");
  writeBlock("G54");
  writeBlock("S" + tool.spindleRPM, "M03");
  writeBlock("G43", "H" + tool.number, "Z5.0");
  writeBlock("M08");

  // Effektive Frästiefe = Fasenbreite + Spitzenversatz
  var zDepth = -(properties.chamferWidth + properties.tipOffset);
  writeComment("EFFEKTIVE FASENTIEFE: Z" + zDepth.toFixed(3));
  writeBlock("G00", "X0.", "Y-5.0");
  writeBlock("G01", "Z" + zDepth.toFixed(3), "F1000");
  writeBlock("G41", "X0.", "Y0.", "D" + tool.number, "F1500"); // Radiuskorrektur links mit Anfahrbewegung
  writeComment("--- KONTUR UMLAUFEN (FASENFRAESEN) ---");
  writeBlock("G01", "X100.0");
  writeBlock("G01", "Y100.0");
  writeBlock("G01", "X0.");
  writeBlock("G01", "Y0.");
  writeBlock("G40", "X0.", "Y-5.0"); // Radiuskorrektur sauber abwählen
  writeBlock("G00", "Z10.0");        // Sicher abheben
}

function onClose() {
  writeComment("--- FASENFRAESEN ERFOLGREICH BEENDET ---");
  writeBlock("M09");
  writeBlock("M05");
  writeBlock("G28", "G91", "Z0.");
  writeBlock("G28", "Y0.");
  writeBlock("M30");
}

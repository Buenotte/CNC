/**
 * Übung 06: Sicherer Rückzug (Safe Retract) und Parkposition
 * Ziel: Zuerst Z auf Maschinenheimhöhe fahren (G53 Z0), erst danach Tisch vor zur Kabinentür (G53 Y0).
 */

description = "Uebung 06 - Sicherer Rueckzug & Parkposition";
vendor = "CNC Lernprojekt";
certificationLevel = 2;
extension = "nc";
setCodePage("ascii");
capabilities = CAPABILITY_MILLING;
tolerance = spatial(0.002, MM);

properties = {
  useG28SafeRetract: {
    title: "G28 statt G53 nutzen (Use G28)",
    description: "Referenzpunktfahrt im Kettenmaß (G28 G91 Z0) statt G53 Z0",
    type: "boolean",
    value: false,
    scope: "post"
  }
};

function onOpen() {
  writeln("%");
  writeln("O1006 (UEBUNG 06 - SAFE RETRACT)");
  writeWords("G90", "G21", "G17", "G40", "G80");
}

function writeRetract() {
  if (getProperty("useG28SafeRetract")) {
    writeWords("G28", "G91", "Z0.0");
    writeWords("G90");
  } else {
    writeWords("G53", "G00", "Z0.0");
  }
}

function onClose() {
  writeln("");
  writeln("(--- SICHERES PROGRAMMENDE ---)");
  writeWords("M09"); // Kühlmittel aus
  
  // 1. ZUERST Spindel ganz nach oben ziehen
  writeRetract();
  
  // 2. Spindelmotor ausschalten
  writeWords("M05");
  
  // 3. Tisch vor zur Tür fahren (Y0 im Maschinenkoordinatensystem G53)
  if (getProperty("useG28SafeRetract")) {
    writeWords("G28", "G91", "Y0.0");
    writeWords("G90");
  } else {
    writeWords("G53", "G00", "Y0.0");
  }

  writeWords("M30"); // Programmende
  writeln("%");
}

/**
 * Übung 16: Meister-Postprozessor / Endabnahme (Final Master Postprocessor)
 * 
 * Lernziel:
 * Zusammenführung aller 16 Kernkompetenzen in einem produktionsreifen,
 * kollisionssicheren und modular konfigurierbaren Postprozessor.
 */

description = "Uebung 16 - Meister-Postprozessor Endabnahme";
vendor = "CNC Akademie";
legal = "Open Source";
certificationLevel = 2;
extension = "nc";
setCodePage("ascii");

// Globale Steuerungsparameter
properties = {
  controllerDialect: "FANUC",      // "FANUC" oder "SIEMENS"
  enableChipConveyor: true,        // M31/M33 Späneförderer
  safeRetractZ: 100.0,             // Sichere Z-Rückzugshöhe in mm
  maxAllowedSpindleRPM: 12000,     // Maximale Spindeldrehzahl
  minAllowedZCrashLimit: -25.0     // Kollisionsgrenze Z-Tiefe
};

function onOpen() {
  writeComment("==================================================");
  writeComment("MEISTER-POSTPROZESSOR (UEBUNG 16 ENDABNAHME)");
  writeComment("STEUERUNG: " + properties.controllerDialect);
  writeComment("AUTOR: CNC-Entwickler (Produktionsfreigabe)");
  writeComment("DATUM: " + (new Date()).toLocaleDateString());
  writeComment("==================================================");

  // Späneförderer Einschalten
  if (properties.enableChipConveyor) {
    writeComment("SPAENEFOERDERER AUTOMATISCH GESTARTET");
    writeBlock("M31");
  }

  // Initialisierungsblock
  if (properties.controllerDialect === "SIEMENS") {
    writeBlock("G90", "G17", "G71", "G94"); // G71 = metrisch bei Siemens
  } else {
    writeBlock("G90", "G17", "G21", "G94"); // G21 = metrisch bei Fanuc/Haas
  }

  // Sichere Referenzfahrt in Z
  writeBlock("G28", "G91", "Z0.");
  writeBlock("G90");
}

function onSection() {
  var tool = currentSection.getTool();
  
  // 1. Schnittdaten-Plausibilitätsprüfung
  if (tool.spindleRPM > properties.maxAllowedSpindleRPM) {
    error("SICHERHEITSSTOPP: Drehzahl " + tool.spindleRPM + " U/min ueberschreitet Limit von " + properties.maxAllowedSpindleRPM + " U/min!");
    return;
  }

  // 2. Kollisionsprüfung Z-Achse (Spannmittel-Schutz)
  var zMin = currentSection.getGlobalZRange().getMinimum();
  if (zMin < properties.minAllowedZCrashLimit) {
    error("KOLLISIONSWARNUNG: Geforderte Z-Tiefe Z=" + zMin.toFixed(2) + " verletzt Sicherheitsgrenze Z=" + properties.minAllowedZCrashLimit + "!");
    return;
  }

  writeComment("--------------------------------------------------");
  writeComment("OPERATION: " + (currentSection.hasParameter("operation-comment") ? currentSection.getParameter("operation-comment") : "Standard Bearbeitung"));
  writeComment("WERKZEUG: T" + tool.number + " (" + tool.comment + ") D=" + tool.diameter + "mm");
  writeComment("Z-MINIMUM DIESER OPERATION: Z" + zMin.toFixed(2) + " mm");
  writeComment("--------------------------------------------------");

  writeBlock("T" + tool.number, "M06");
  writeBlock("G54");
  writeBlock("S" + tool.spindleRPM, "M03");
  writeBlock("G43", "H" + tool.number, "Z15.0");
  writeBlock("M08");
}

function onClose() {
  writeComment("==================================================");
  writeComment("PROGRAMMENDE: TEIL ERFOLGREICH FERTIGGESTELLT");
  writeComment("==================================================");
  writeBlock("M09"); // Kühlmittel AUS
  writeBlock("M05"); // Spindel AUS
  
  // Späneförderer Ausschalten
  if (properties.enableChipConveyor) {
    writeBlock("M33");
  }

  // Sicherer 2-Stufen-Rückzug
  writeBlock("G28", "G91", "Z0."); // Erst Z ganz nach oben
  writeBlock("G28", "Y0.");        // Dann Y nach vorne zum Bediener
  writeBlock("M30");               // Programmende
}

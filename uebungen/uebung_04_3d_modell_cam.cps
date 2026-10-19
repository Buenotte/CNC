/**
 * Übung 04 & 05: 3D-Modell & CAM-Operationen (Planfräsen, Konturfräsen, Bohren)
 * 
 * Lernziel:
 * Verknüpfung der CAM-Operationen (Computer-Aided Manufacturing / rechnerunterstützte Fertigung)
 * mit den passenden NC-Zyklen und Z-Tiefen für die Flanschplatte (Bauteil 1001).
 */

description = "Uebung 04 und 05 - 3D Modell CAM Operationen";
vendor = "CNC Akademie";
legal = "Open Source";
certificationLevel = 2;
extension = "nc";
setCodePage("ascii");

function onOpen() {
  writeComment("========================================");
  writeComment("UEBUNG 04 & 05: FERTIGUNG FLANSCHPLATTE 1001");
  writeComment("BAUTEIL: bauteil_1001.stl");
  writeComment("ROHMATERIAL: 105 x 105 x 25 mm (ALUMINIUM)");
  writeComment("========================================");
  
  writeBlock("G90", "G17", "G21", "G94");
  writeBlock("G28", "G91", "Z0.");
  writeBlock("G90");
}

function onSection() {
  var tool = currentSection.getTool();
  writeComment("----------------------------------------");
  writeComment("OPERATION: " + (currentSection.hasParameter("operation-comment") ? currentSection.getParameter("operation-comment") : "Standard Bearbeitung"));
  writeComment("WERKZEUG: T" + tool.number + " (" + tool.comment + ") D=" + tool.diameter + "mm");
  writeComment("----------------------------------------");

  writeBlock("T" + tool.number, "M06");
  writeBlock("G54"); // WCS 1 (Werkstück-Nullpunkt oben links)
  writeBlock("S" + tool.spindleRPM, "M03");
  writeBlock("G43", "H" + tool.number, "Z15.0"); // Werkzeuglängenkorrektur auf Sicherheitsebene 15mm
  writeBlock("M08"); // Kühlmittel AN
}

function onClose() {
  writeComment("========================================");
  writeComment("FLANSCHPLATTE KOMPLETT FERTIG BEARBEITET");
  writeComment("========================================");
  writeBlock("M09");
  writeBlock("M05");
  writeBlock("G28", "G91", "Z0.");
  writeBlock("G28", "Y0.");
  writeBlock("M30");
}

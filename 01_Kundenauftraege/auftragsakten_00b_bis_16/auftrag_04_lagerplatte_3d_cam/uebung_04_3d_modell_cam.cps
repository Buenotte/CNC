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
  writeComment("UEBUNG 04 & 05: FERTIGUNG LAGERPLATTE 1001 (HAAS VF-2)");
  writeComment("BAUTEIL: bauteil_1001.stl");
  writeComment("ROHMATERIAL: 85 x 55 x 15 mm (ALUMINIUM EN AW-6082)");
  writeComment("========================================");
  
  // Grundinitialisierung der Fräsmaschine:
  // G90 = Absolutmaß (alle Verfahrwege beziehen sich auf den Nullpunkt G54)
  // G17 = Fräsbearbeitung in der XY-Hauptebene (Z ist die Werkzeugachse)
  // G21 = Maßeinheiten in Millimeter (metrisch)
  // G94 = Vorschubgeschwindigkeit F in mm/min (Millimeter pro Minute)
  writeBlock("G90", "G17", "G21", "G94");

  // Sicherheitsfahrt der Z-Achse auf den Referenzpunkt:
  // G28 = Fahre auf Maschinen-Referenzpunkt (feste Endschalter der Fräsmaschine)
  // G91 = Relativmaß / Kettenmaß (inkrementelle Bewegung)
  // Z0. = Um 0 mm relativ verfahren, also direkt senkrecht nach ganz oben auf Z-Heimathöhe
  writeBlock("G28", "G91", "Z0.");

  // G90 = Sofort wieder auf Absolutmaß zurückschalten
  writeBlock("G90");
}

function onSection() {
  var tool = currentSection.getTool();
  writeComment("----------------------------------------");
  writeComment("OPERATION: " + (currentSection.hasParameter("operation-comment") ? currentSection.getParameter("operation-comment") : "Standard Bearbeitung"));
  writeComment("WERKZEUG: T" + tool.number + " (" + tool.comment + ") D=" + tool.diameter + "mm");
  writeComment("----------------------------------------");

  // T.. = Werkzeugplatz im Magazin (Tool Number)
  // M06 = Automatischer Werkzeugwechsel durch mechanischen Greifer
  writeBlock("T" + tool.number, "M06");

  // G54 = 1. Werkstück-Koordinatensystem (Nullpunkt oben links an der festen Anschlagbacke)
  writeBlock("G54");

  // S.. = Spindeldrehzahl in U/min (Spindle Speed)
  // M03 = Frässpindel im Uhrzeigersinn (Rechtslauf) einschalten
  writeBlock("S" + tool.spindleRPM, "M03");

  // G43 = Werkzeuglängenkorrektur EIN (liest die vermessene Werkzeuglänge aus dem H-Register)
  // H.. = Register-Nummer der Werkzeuglänge (muss zur Werkzeugnummer T.. passen)
  // Z15.0 = Erste Positionierung auf 15 mm Sicherheitshöhe über Werkstück
  writeBlock("G43", "H" + tool.number, "Z15.0");

  // M08 = Kühlschmierstoff (KSS / Kühlwasser) einschalten
  writeBlock("M08");
}

function onClose() {
  writeComment("========================================");
  writeComment("FLANSCHPLATTE KOMPLETT FERTIG BEARBEITET");
  writeComment("========================================");

  // M09 = Kühlschmierstoff (KSS) ausschalten
  writeBlock("M09");

  // M05 = Frässpindel ausschalten (Spindel-Stopp)
  writeBlock("M05");

  // G28 G91 Z0. = Z-Achse im Kettenmaß senkrecht nach ganz oben fahren (Kollisionsschutz)
  writeBlock("G28", "G91", "Z0.");

  // G28 Y0. = Maschinentisch nach vorne zur Kabinentür fahren (bequemes Entnehmen des Bauteils)
  writeBlock("G28", "Y0.");

  // M30 = Hauptprogramm-Ende, Reset und Rücklauf zum Programmanfang
  writeBlock("M30");
}

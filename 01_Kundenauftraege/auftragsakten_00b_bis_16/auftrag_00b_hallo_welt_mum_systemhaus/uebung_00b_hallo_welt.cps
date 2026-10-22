/**
 * =========================================================================================
 * ÜBUNG 00b: HALLO WELT (ERSTE EIGENE ZEILE IM POSTPROZESSOR)
 * =========================================================================================
 * 
 * LERNZIEL DIESER ÜBUNG:
 * Verstehen, wie ein Kommentar mit writeComment(...) und ein G-Code-Befehl mit writeBlock(...)
 * in die Ausgabedatei geschrieben werden.
 */

// 1. KOPFDATEN DES POSTPROZESSORS
description = "Uebung 00b - Hallo Welt Postprozessor"; // Name des Postprozessors im CAM-System
vendor = "CNC Akademie";                              // Entwickler- bzw. Firmenbezeichnung
legal = "Open Source";                                // Lizenzstatus
certificationLevel = 2;                               // Zertifizierungsstufe
extension = "nc";                                     // Dateiendung der fertigen CNC-Datei (.nc)
setCodePage("ascii");                                 // Zeichenkodierung ohne Umlaute für Maschinen-Kompatibilität

// 1b. HILFSFUNKTIONEN FÜR DIE TEXT- UND BLOCKAUSGABE (HELPER FUNCTIONS)
function writeComment(text) {
  // Schreibt einen Kommentar in runden Klammern (...) in die CNC-Datei
  writeln("(" + String(text).toUpperCase() + ")");
}

function writeBlock() {
  // Schreibt einen G-Code-Befehlsblock mit Leerzeichen getrennt
  writeWords.apply(null, arguments);
}

// 2. onOpen() - WIRD EINMALIG AM PROGRAMMANFANG AUSGEFÜHRT
function onOpen() {
  // Hier steht Ihre allererste eigene Zeile im CNC-Code:
  writeComment("========================================"); // Schreibt eine optische Trennlinie als Kommentar
  writeComment("HALLO WELT - MEIN ERSTER CNC POSTPROZESSOR"); // Schreibt den Begrüßungstext in runden Klammern (...)
  writeComment("ERFOLGREICH ERSTE ZEILE EINGEFUEGT");        // Bestätigungskommentar
  writeComment("========================================"); // Trennlinie

  // Grundinitialisierung der Fräsmaschine:
  // G90 = Absolute Maßangaben in Bezug auf das Werkstück
  // G17 = Fräsbearbeitung in der XY-Hauptebene
  // G21 = Alle Maßeinheiten sind in Millimeter (metrisch)
  // G94 = Vorschubgeschwindigkeit F wird in mm/min (Millimeter pro Minute) interpretiert
  writeBlock("G90", "G17", "G21", "G94");

  // Sicherheitsfahrt der Z-Achse auf den Referenzpunkt:
  // G28 = Fahre auf Maschinen-Referenzpunkt
  // G91 = Relativmaß (Inkrementell)
  // Z0. = Relativ um 0 mm verfahren, also direkt nach oben auf Z-Referenz
  writeBlock("G28", "G91", "Z0.");

  // G90 = Sofort wieder zurückschalten in den Absolutmaß-Modus für sichere weitere Befehle
  writeBlock("G90");
}

// 3. onSection() - WIRD VOR JEDEM BEARBEITUNGSSCHRITT (OPERATION) AUSGEFÜHRT
function onSection() {
  var tool = currentSection.getTool(); // Holt die Daten des aktuell verwendeten Werkzeugs (Fräser oder Bohrer)
  
  writeComment("--- WERKZEUGWECHSEL ---"); // Kommentar zur Orientierung im G-Code
  writeBlock("T" + tool.number, "M06");   // T = Werkzeugnummer (Tool), M06 = Physischer Werkzeugwechsel durch Greifer
  writeBlock("S" + tool.spindleRPM, "M03"); // S = Drehzahl in U/min, M03 = Spindel im Uhrzeigersinn (Rechtslauf) EIN
  writeBlock("G54");                      // G54 = Erstes Werkstück-Koordinatensystem (Nullpunkt auf Bauteilecke)
}

// 4. onClose() - WIRD GANZ AM ENDE DES PROGRAMMS AUSGEFÜHRT
function onClose() {
  writeComment("--- PROGRAMMENDE ---"); // Kommentar am Ende der Datei
  writeBlock("M05");                   // M05 = Spindelmotor ausschalten (Spindel-Stopp)
  writeBlock("M09");                   // M09 = Kühlmittelpumpe ausschalten (Wasser AUS)
  writeBlock("G28", "G91", "Z0.");     // Z-Achse ganz nach oben auf sichere Referenzhöhe fahren
  writeBlock("G28", "Y0.");            // Y-Achse nach vorne fahren (Maschinentisch fährt zur Schutztür)
  writeBlock("M30");                   // M30 = Hauptprogrammende, Rücklauf zum Anfang und Speicher zurücksetzen
}

/**
 * =========================================================================================
 * ÜBUNG 03: SICHERHEITS-SCHUTZ GEGEN CRASHS - TIEFSTE FRÄSTIEFE (Z-MIN) BERECHNEN
 * =========================================================================================
 * 
 * LERNZIEL DIESER ÜBUNG:
 * Verstehen, wie ein Postprozessor über alle Bearbeitungsschritte (Sections) iteriert,
 * für jedes Werkzeug die absolut tiefste Frästiefe (Z-MIN) berechnet und im Header ausgibt,
 * damit der Maschinenbediener weiß, wie weit das Bauteil aus dem Schraubstock ragen muss.
 */

// 1. KOPFDATEN DES POSTPROZESSORS
description = "Uebung 03 - Z-MIN Crashschutz Berechnung"; // Name im CAM-Dialog
vendor = "CNC Lernprojekt";                              // Entwickler
certificationLevel = 2;                                  // Zertifizierungsstufe
extension = "nc";                                        // Endung .nc
setCodePage("ascii");                                    // ASCII-Kodierung
capabilities = CAPABILITY_MILLING;                       // Maschinentyp Fräsen
tolerance = spatial(0.002, MM);                          // Toleranz 0,002 mm

// 2. KONFIGURATIONSPARAMETER FÜR DEN BEDIENER
properties = {
  showZMinInfo: {
    title: "Z-MIN Crash-Info ausgeben (Show Z-Min Info)", // Menütitel
    description: "Berechnet die tiefste Frästiefe zur Vermeidung von Schraubstock-Kollisionen", // Hilfetext
    type: "boolean",                                     // Checkbox
    value: true,                                         // Aktiviert
    scope: "post"                                        // Gilt für Postprozesslauf
  }
};

// 3. FORMATIERER
var xyzFormat = createFormat({decimals:3, forceDecimal:true}); // 3 Dezimalstellen (z. B. -12.000)
var permittedCommentChars = " ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,=_-/:+*%@";

function formatComment(text) {
  return "(" + filterText(String(text).toUpperCase(), permittedCommentChars) + ")";
}

function writeComment(text) {
  writeln(formatComment(text));
}

// 4. KERNFUNKTION DIESER ÜBUNG: BERECHNUNG DES KLEINSTEN Z-WERTES FÜR EIN WERKZEUG
function getToolMinimumZ(tool) {
  var zMin = undefined; // Startwert ist undefiniert (noch kein Z-Wert gefunden)
  var numberOfSections = getNumberOfSections(); // Gesamtzahl aller Fräs- und Bohroperationen im CAM-Projekt

  // Durchlaufe alle Operationen (von Schritt 0 bis zum letzten Schritt):
  for (var i = 0; i < numberOfSections; ++i) {
    var section = getSection(i); // Nimm den i-ten Bearbeitungsschritt

    // Prüfe: Wird in diesem Schritt genau unser gesuchtes Werkzeug verwendet?
    if (section.getTool().number == tool.number) {
      var zRange = section.getGlobalZRange(); // Ermittle den Z-Bereich (von Z-Höchstwert bis Z-Tiefstwert)
      var currentMin = zRange.getMinimum();   // Lies die tiefste erreichte Z-Koordinate dieser Operation aus

      // Wenn wir noch kein zMin gespeichert haben oder der aktuelle Wert noch tiefer (kleiner) ist:
      if (zMin === undefined || currentMin < zMin) {
        zMin = currentMin; // Speichere den neuen absoluten Tiefstwert!
      }
    }
  }
  return zMin; // Gib die tiefste gefundene Z-Koordinate an den Aufrufer zurück
}

// 5. onOpen() - WIRD GANZ ZU ANFANG AUSGEFÜHRT
function onOpen() {
  writeln("%"); // Übertragungsstart
  writeln("O1001 " + formatComment("CRASHSCHUTZ Z-MIN PRUEFUNG")); // Programmnummer

  // Wenn der Crashschutz-Schalter aktiv ist:
  if (getProperty("showZMinInfo")) {
    writeComment("==================================================");
    writeComment("SICHERHEITS-ANALYSE: TIEFSTE WERKZEUGTIEFEN (Z-MIN)");
    writeComment("HINWEIS: BAUTEIL MUSS MINDESTENS SO WEIT AUS DEM");
    writeComment("SCHRAUBSTOCK RAGEN, UM KOLLISIONEN ZU VERMEIDEN!");
    writeComment("==================================================");

    var tools = getToolTable(); // Hole alle benutzten Werkzeuge
    for (var i = 0; i < tools.getNumberOfTools(); ++i) {
      var tool = tools.getTool(i);           // Aktuelles Werkzeug
      var minZ = getToolMinimumZ(tool);      // Rufe unsere Z-MIN-Berechnungsfunktion auf

      var toolStr = "T" + ("0" + tool.number).slice(-2); // Z. B. "T01"
      var descStr = tool.comment ? tool.comment : "WERKZEUG"; // Werkzeugbezeichnung
      var zMinStr = (minZ !== undefined) ? ("Z-MIN = " + xyzFormat.format(minZ) + "MM") : "KEINE Z-BEWEGUNG";

      // Schreibe die berechnete Sicherheitstiefe in den Header:
      writeComment(toolStr + " (" + descStr + ") -> " + zMinStr);
    }
    writeComment("==================================================");
  }

  // Sicherheitsstartzeile
  writeWords("G90", "G21", "G17", "G40", "G80");
}

// 6. onSection() - WIRD VOR JEDER EINZELNEN OPERATION AUSGEFÜHRT
function onSection() {
  var tool = currentSection.getTool(); // Werkzeug dieser Operation
  var sectionZ = currentSection.getGlobalZRange(); // Z-Bereich NUR für diesen speziellen Schritt

  writeComment("--------------------------------------------------");
  writeComment("START OPERATION: " + (currentSection.hasParameter("operation-comment") ? currentSection.getParameter("operation-comment") : "FRAESUNG"));
  writeComment("WERKZEUG T" + tool.number + " | DIESE OP Z-MIN: " + xyzFormat.format(sectionZ.getMinimum()) + "MM");
  writeComment("--------------------------------------------------");

  writeWords("T" + tool.number, "M06"); // Werkzeug einwechseln
  writeWords("G54");                    // Nullpunkt G54
  writeWords("S" + tool.spindleRPM, "M03"); // Drehzahl & Spindelstart
}

// 7. onClose() - PROGRAMMENDE
function onClose() {
  writeWords("M09");                 // Kühlwasser AUS
  writeWords("M05");                 // Spindel AUS
  writeWords("G53", "G00", "Z0.0"); // Spindel hoch
  writeWords("M30");                 // Programmende
  writeln("%");                      // Übertragungsende
}

/**
 * =========================================================================================
 * ÜBUNG 02: AUTOMATISCHE WERKZEUGLISTE (TOOL TABLE)
 * =========================================================================================
 * 
 * LERNZIEL DIESER ÜBUNG:
 * Verstehen, wie mit der CAM-Funktion getToolTable() alle im 3D-Projekt benutzten Fräser
 * und Bohrer ausgelesen und mit einer for-Schleife in eine übersichtliche Werkzeugliste
 * ganz oben im Maschinencode (G-Code) geschrieben werden.
 */

// 1. KOPFDATEN DES POSTPROZESSORS
description = "Uebung 02 - Werkzeugliste Tool Table"; // Bezeichnung im CAM-Menü
vendor = "CNC Lernprojekt";                           // Herstellerangabe
certificationLevel = 2;                               // Zertifizierungsstufe
extension = "nc";                                     // Dateiendung der NC-Datei
setCodePage("ascii");                                 // Zeichensatz ohne Sonderzeichen
capabilities = CAPABILITY_MILLING;                    // Maschinentyp: Fräsen
tolerance = spatial(0.002, MM);                       // Berechnungsgenauigkeit: 0,002 mm

// 2. EINSTELLUNGEN FÜR DEN ANWENDER (PROPERTIES)
properties = {
  writeToolList: {
    title: "Werkzeugliste ausgeben (Write Tool List)", // Beschriftung des Schalters im Menü
    description: "Gibt alle benötigten Werkzeuge am Programmanfang aus", // Erklärungstext
    type: "boolean",                                  // Datentyp: Ja/Nein-Schalter (Checkbox)
    value: true,                                      // Standardwert: Eingeschaltet (true)
    scope: "post"                                     // Gilt für den Postprozessor
  }
};

// 3. FORMATIERUNGS-REGELN FÜR ZAHLEN
// xyzFormat sorgt dafür, dass Maße immer 3 Nachkommastellen haben (z. B. 10.000 für 10 mm)
var xyzFormat = createFormat({decimals:3, forceDecimal:true});
var permittedCommentChars = " ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,=_-/:+*%@";

// 4. HILFSFUNKTIONEN ZUM SCHREIBEN VON MASCHINEN-KOMMENTAREN
function formatComment(text) {
  // Wandelt Kleinbuchstaben in Großbuchstaben um und setzt runde Klammern (...)
  return "(" + filterText(String(text).toUpperCase(), permittedCommentChars) + ")";
}

function writeComment(text) {
  // Schreibt die Zeile in die Ausgabedatei
  writeln(formatComment(text));
}

// 5. onOpen() - WIRD BEIM EXPORT GANZ ZU ANFANG AUSGEFÜHRT
function onOpen() {
  writeln("%"); // Startzeichen der NC-Datei
  writeln("O1001 " + formatComment("PROGRAMM MIT WERKZEUGLISTE")); // Programmnummer mit Kommentar

  // Prüfen, ob der Anwender die Werkzeugliste eingeschaltet hat:
  if (getProperty("writeToolList")) {
    writeComment("==================================================");
    writeComment("BENOETIGTE WERKZEUGE FUER DIESEN AUFTRAG (TOOL TABLE)");
    writeComment("==================================================");

    // getToolTable() ist der fertige API-Befehl von Autodesk, der alle Werkzeuge sammelt:
    var tools = getToolTable();
    var numberOfTools = tools.getNumberOfTools(); // Zählt, wie viele verschiedene Werkzeuge benutzt werden

    // for-Schleife: Durchläuft jedes einzelne Werkzeug der Reihe nach von 0 bis zum letzten Werkzeug:
    for (var i = 0; i < numberOfTools; ++i) {
      var tool = tools.getTool(i); // Holt das i-te Werkzeug aus der Liste

      // Werkzeugnummer 2-stellig formatieren (z. B. aus 1 wird "T01"):
      var toolNumStr = "T" + ("0" + tool.number).slice(-2);

      // Durchmesser mit 3 Nachkommastellen und Einheit MM versehen (z. B. D=10.000MM):
      var diaStr = "D=" + xyzFormat.format(tool.diameter) + "MM";

      // Schneidenecken-Radius ausgeben (0.000 = scharfe Ecke, 3.000 = Radiusfräser):
      var cornerStr = "ECKE R=" + xyzFormat.format(tool.cornerRadius);

      // Typ bzw. Beschreibung des Werkzeugs (z. B. Schaftfräser oder Spiralbohrer):
      var descStr = tool.description ? tool.description : (tool.comment ? tool.comment : "FRAESWERKZEUG");

      // Zusammensetzen der Zeile mit Trennstrichen "|" für perfekte Lesbarkeit an der Maschine:
      var line = toolNumStr + " | " + diaStr + " | " + cornerStr + " | " + descStr;

      // Fertige Zeile als Kommentar in den G-Code schreiben:
      writeComment(line);
    }
    writeComment("==================================================");
  }

  // Sicherheits-Startblock: Absolutmaß G90, Metrisch G21, Ebene G17
  writeWords("G90", "G21", "G17", "G40", "G80");
}

// 6. onClose() - PROGRAMMENDE
function onClose() {
  writeWords("G53", "G00", "Z0.0"); // Spindel hoch
  writeWords("M30");                 // Programmende
  writeln("%");                      // Endezeichen
}

/**
 * =========================================================================================
 * ÜBUNG 01: ENTWICKLER-INFOBLOCK & SICHERHEITS-STARTBLOCK IN onOpen()
 * =========================================================================================
 * 
 * LERNZIEL DIESER ÜBUNG:
 * Verstehen, wie beim Start der Übersetzung (Funktion onOpen) automatisch ein
 * Informationsblock mit Name, Firma, Datum und der wichtige Sicherheits-Startblock
 * (Safe Start Block) in den CNC-Maschinencode (G-Code) geschrieben wird.
 */

// 1. ALLGEMEINE POSTPROZESSOR-EINSTELLUNGEN
description = "Uebung 01 - Entwickler Infoblock"; // Name des Postprozessors, wie er im CAM-Menü angezeigt wird
vendor = "CNC Lernprojekt";                     // Hersteller- oder Projektbezeichnung
certificationLevel = 2;                         // Zertifizierungsstufe (2 = Standard für Fräsen)
extension = "nc";                               // Dateiendung der erzeugten Maschinendatei (.nc = Numerical Control)
setCodePage("ascii");                           // Zeichensatzkodierung (ASCII = Standard ohne deutsche Umlaute für Maschinen)
capabilities = CAPABILITY_MILLING;              // Maschinentyp: Fräsmaschine (Milling)
tolerance = spatial(0.002, MM);                 // Lineare Rechengenauigkeit: 0,002 Millimeter

// 2. KONFIGURATIONSPARAMETER (PROPERTIES - EINSTELLUNGEN FÜR DEN ANWENDER)
properties = {
  developerName: {
    title: "Entwickler-Name (Developer Name)",   // Beschriftung im Einstellungsdialog
    description: "Name des Postprozessor-Entwicklers", // Hilfetext für den Bediener
    type: "string",                             // Datentyp: Textzeichenkette (String)
    value: "Mein Name",                         // Standardwert: Ihr Name als Entwickler
    scope: "post"                               // Gültigkeit: Gilt für den gesamten Postprozesslauf
  },
  companyName: {
    title: "Firmenname (Company Name)",         // Beschriftung für den Kundenbetrieb
    description: "Name der Zerspanungsfirma",   // Hilfetext
    type: "string",                             // Datentyp: Textzeichenkette
    value: "Zerspanungstechnik GmbH",           // Standardwert des Betriebs
    scope: "post"                               // Gilt für den Postprozessor
  }
};

// 3. FORMATIERER FÜR G-CODE ZAHLEN UND WÖRTER
// createFormat definiert, wie Zahlen ausgegeben werden: "G" als Buchstabe, 2-stellig mit führender Null (z. B. G01, G90)
var gFormat = createFormat({prefix:"G", width:2, zeropad:true, decimals:0});

// Erlaubte Zeichen für Kommentare (Maschinensteuerungen stürzen bei Sonderzeichen wie ä, ö, ü oder Sonderklammern ab)
var permittedCommentChars = " ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,=_-/:+*%@";

// 4. HILFSFUNKTIONEN ZUM SCHREIBEN VON MASCHINEN-KOMMENTAREN
function formatComment(text) {
  // Wandelt Text in Großbuchstaben um, filtert unzulässige Zeichen heraus und setzt runde Klammern (...) herum
  return "(" + filterText(String(text).toUpperCase(), permittedCommentChars) + ")";
}

function writeComment(text) {
  // Schreibt die fertig formatierte Kommentarzeile mit Zeilenumbruch in die Ausgabedatei
  writeln(formatComment(text));
}

// 5. onOpen() - DIE ERSTE FUNKTION, DIE BEIM EXPORTIEREN AUTOMATISCH GESTARTET WIRD
function onOpen() {
  writeln("%"); // ISO-Standard: Prozentzeichen leitet auf vielen Steuerungen (Fanuc/Haas) die Übertragung ein
  
  // Zeile 1: Programmnummer O1001 (O-Nummer = Hauptprogramm-Adresse) mit Kommentar
  writeln("O1001 " + formatComment("UEBUNG 01 PROGRAMM"));

  // Datum vom Computer holen und ins Format JAHR-MONAT-TAG formatieren
  var now = new Date(); // Erzeugt ein Datumsobjekt mit der aktuellen Systemzeit
  var dateStr = now.getFullYear() + "-" + 
                ("0" + (now.getMonth() + 1)).slice(-2) + "-" + 
                ("0" + now.getDate()).slice(-2); // 2-stelliger Tag

  // Entwickler-Infoblock (Visitenkarte) in runden Klammern in den G-Code schreiben
  writeComment("==================================================");
  writeComment("AUTOMATISCH GENERIERTER CNC G-CODE");
  writeComment("ENTWICKLER : " + getProperty("developerName")); // Liest die Eigenschaft developerName aus
  writeComment("BETRIEB    : " + getProperty("companyName"));   // Liest die Eigenschaft companyName aus
  writeComment("DATUM      : " + dateStr);                      // Gibt das Tagesdatum aus
  writeComment("==================================================");

  // Sicherheits-Startblock (Safe Start Block - stellt sicher, dass die Maschine in einem definierten Zustand startet):
  // G90 = Absolute Programmierung (Maße beziehen sich auf den Werkstück-Nullpunkt)
  // G21 = Maßeinheit Millimeter (metrisches System)
  // G17 = Arbeitsebene XY (Standard für vertikale Fräsmaschinen)
  // G40 = Werkzeugradiuskorrektur ausschalten (keine alten Korrekturwerte aktiv)
  // G80 = Alle aktiven Bohrzyklen abbrechen und löschen
  writeWords(
    gFormat.format(90), // Gibt "G90" aus
    gFormat.format(21), // Gibt "G21" aus
    gFormat.format(17), // Gibt "G17" aus
    gFormat.format(40), // Gibt "G40" aus
    gFormat.format(80)  // Gibt "G80" aus
  );
}

// 6. onClose() - DIE LETZTE FUNKTION BEIM ABSCHLUSS DES PROGRAMMS
function onClose() {
  // G53 = Maschinen-Koordinatensystem (feste Nullage der Maschine an der oberen Decke)
  // G00 = Eilgang (schnellstmögliche Bewegung)
  // Z0.0 = Spindel senkrecht nach ganz oben fahren, weg vom Werkstück
  writeWords(gFormat.format(53), gFormat.format(0), "Z0.0");
  
  // M30 = Programm-Ende und Rücksprung zum Programmanfang
  writeWords("M30");
  
  // Abschluss-Prozentzeichen für Dateiübertragung
  writeln("%");
}

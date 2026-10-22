/**
  Mein erster CNC-Postprozessor (Übersetzungsprogramm von CAM-Daten in G-Code)
  Basierend auf dem Fanuc / Haas NGC (Next Generation Control) ISO-Standard.

  Dateityp: .cps (CAM Post Script - JavaScript-Datei für Autodesk Fusion)
  Sprache:  JavaScript (ECMAScript-kompatible Skriptsprache der Autodesk Post-Engine)
*/

// ============================================================================
// 1. METADATEN DES POSTPROZESSORS (Grundinformationen für Autodesk Fusion)
// ============================================================================
description = "Mein Erster Custom Postprozessor (Haas NGC / Fanuc Basis)";
vendor = "Custom CNC Solutions";
vendorUrl = "https://cam.autodesk.com";
legal = "Copyright (C) 2026 - Custom CNC Postprocessor Development";
certificationLevel = 2;
minimumRevision = 45702;

longDescription = "Lern- und Referenz-Postprozessor (Übersetzungsprogramm) in JavaScript mit personalisiertem Entwickler-Header (Kopfzeilen-Infoblock), automatischer Werkzeugliste (Tool Table) und Sicherheits-Startblock (Safe Start Block).";

extension = "nc"; // Dateiendung der erzeugten G-Code-Datei (Numerical Control Datei)
setCodePage("ascii"); // Zeichensatz (ASCII - American Standard Code for Information Interchange)

capabilities = CAPABILITY_MILLING; // Fähigkeit: Fräsbearbeitung (Milling)
tolerance = spatial(0.002, MM); // Geometrische Toleranz (Abweichungstoleranz in Millimetern)

minimumChordLength = spatial(0.25, MM); // Minimale Sehnenlänge bei Kreisbögen
minimumCircularRadius = spatial(0.01, MM); // Minimaler Kreisradius für G02/G03 (Kreisinterpolation)
maximumCircularRadius = spatial(1000, MM); // Maximaler Kreisradius für G02/G03
minimumCircularSweep = toRad(0.01); // Minimaler Öffnungswinkel im Bogenmaß (Radiant)
maximumCircularSweep = toRad(180); // Maximaler Öffnungswinkel (180 Grad Halbkreis)
allowHelicalMoves = true; // Erlaubt Helix-Bewegungen (schraubenförmiges Eintauchen beim Fräsen)
allowedCircularPlanes = undefined; // Erlaubt Kreisbögen in allen Ebenen (G17 XY, G18 XZ, G19 YZ)

// ============================================================================
// 2. BENUTZEREIGENSCHAFTEN (Properties - Einstellbare Optionen im CAM-Dialog)
// ============================================================================
properties = {
  developerName: {
    title      : "Entwickler-Name (Developer Name)",
    description: "Name des Postprozessor-Entwicklers, der im G-Code-Header (Kopfbereich) ausgegeben wird.",
    group      : "customHeader",
    type       : "string",
    value      : "JavaScript CNC-Entwickler",
    scope      : "post"
  },
  companyName: {
    title      : "Firmenname / Auftraggeber (Company Name)",
    description: "Name des Kundenbetriebs oder Projekts für den G-Code-Kopfbereich.",
    group      : "customHeader",
    type       : "string",
    value      : "Präzisions-Zerspanung GmbH",
    scope      : "post"
  },
  writeToolList: {
    title      : "Werkzeugliste ausgeben (Write Tool List)",
    description: "Schreibt eine komplette Übersicht aller benötigten Fräswerkzeuge an den Anfang des G-Codes.",
    group      : "customHeader",
    type       : "boolean",
    value      : true,
    scope      : "post"
  },
  showSequenceNumbers: {
    title      : "Zeilennummern N ausgeben (Show Sequence Numbers)",
    description: "Schreibt N-Satznummern (z. B. N10, N20, N30) vor jede G-Code-Zeile.",
    group      : "formats",
    type       : "boolean",
    value      : true,
    scope      : "post"
  },
  sequenceNumberStart: {
    title      : "Start-Zeilennummer (First Sequence Number)",
    description: "Erste N-Zeilennummer im Programm.",
    group      : "formats",
    type       : "integer",
    value      : 10,
    scope      : "post"
  },
  sequenceNumberIncrement: {
    title      : "Schrittweite der Zeilennummern (Sequence Number Increment)",
    description: "Abstand zwischen zwei aufeinanderfolgenden N-Zeilennummern.",
    group      : "formats",
    type       : "integer",
    value      : 10,
    scope      : "post"
  },
  useG28SafeRetract: {
    title      : "G28 statt G53 für sicheren Rückzug (Use G28 Safe Retract)",
    description: "Verwendet G28 G91 Z0 (Referenzpunktfahrt im Kettenmaß) statt G53 G00 Z0 (Maschinenkoordinatensystem).",
    group      : "safety",
    type       : "boolean",
    value      : false,
    scope      : "post"
  },
  showZMinInfo: {
    title      : "Maximale Frästiefe Z-Min ausgeben (Show Z-Min Safety Info)",
    description: "Berechnet automatisch den tiefsten Z-Punkt (Z-Min) für jedes Werkzeug im Header und vor jeder Operation als Sicherheits-Kommentar gegen Schraubstock-Kollisionen.",
    group      : "safety",
    type       : "boolean",
    value      : true,
    scope      : "post"
  }
};

// ============================================================================
// 3. FORMATIERUNGS-REGELN (Wie Zahlen und Koordinaten im G-Code aussehen)
// ============================================================================
var gFormat = createFormat({prefix:"G", width:2, zeropad:true, decimals:1}); // G-Befehle (Wegbedingungen, z. B. G00, G01)
var mFormat = createFormat({prefix:"M", width:2, zeropad:true, decimals:0}); // M-Befehle (Zusatzfunktionen, z. B. M03, M06, M08)
var hFormat = createFormat({prefix:"H", width:2, zeropad:true, decimals:0}); // H-Nummer (Werkzeuglängenkorrektur-Speicherplatz)
var dFormat = createFormat({prefix:"D", width:2, zeropad:true, decimals:0}); // D-Nummer (Werkzeugradiuskorrektur-Speicherplatz)
var toolFormat = createFormat({prefix:"T", width:2, zeropad:true, decimals:0}); // T-Nummer (Werkzeugnummer im Magazin, z. B. T01)

// Koordinaten-Format: 3 Nachkommastellen bei Millimetern (0.001 mm = 1 Mikrometer), 4 bei Zoll (Inch)
var xyzFormat = createFormat({decimals:(unit == MM ? 3 : 4), forceDecimal:true});
var feedFormat = createFormat({decimals:(unit == MM ? 0 : 1), forceDecimal:false}); // Vorschub F (mm/min)
var rpmFormat = createFormat({decimals:0}); // Spindeldrehzahl S (Umdrehungen pro Minute / RPM)
var secFormat = createFormat({decimals:3, forceDecimal:true}); // Verweilzeit P/X in Sekunden

// Ausgangsvariablen (Modal-Variablen: Werden nur ausgegeben, wenn sich ihr Wert ändert!)
var xOutput = createVariable({prefix:"X"}, xyzFormat);
var yOutput = createVariable({prefix:"Y"}, xyzFormat);
var zOutput = createVariable({onchange:function() {retracted = false;}, prefix:"Z"}, xyzFormat);
var feedOutput = createVariable({prefix:"F"}, feedFormat);
var sOutput = createVariable({prefix:"S", force:true}, rpmFormat);

// Kreisbogen-Offsets (Abstand vom Startpunkt zum Kreismittelpunkt in X, Y, Z)
var iOutput = createReferenceVariable({prefix:"I", force:true}, xyzFormat);
var jOutput = createReferenceVariable({prefix:"J", force:true}, xyzFormat);
var kOutput = createReferenceVariable({prefix:"K", force:true}, xyzFormat);

// Modale Gruppen für G-Codes (verhindert unnötige Wiederholung desselben Befehls in Folgezeilen)
var gMotionModal = createModal({}, gFormat); // G00, G01, G02, G03, G80...
var gPlaneModal = createModal({onchange:function () {gMotionModal.reset();}}, gFormat); // G17, G18, G19
var gAbsIncModal = createModal({}, gFormat); // G90 (Absolut), G91 (Inkremental/Kettenmaß)
var gUnitModal = createModal({}, gFormat); // G20 (Inch/Zoll), G21 (Millimeter)
var gCycleModal = createModal({}, gFormat); // Bohrzyklen G81, G83, G84...

// Globale Statusvariablen (Zustandsspeicher während des Programmablaufs)
var sequenceNumber;
var retracted = false; // Speichert, ob die Z-Achse (Höhenachse) bereits auf sicherer Rückzugshöhe steht

// ============================================================================
// 4. HILFSFUNKTIONEN FÜR DIE TEXTAUSGABE (Helper Functions)
// ============================================================================

/**
  Gibt eine G-Code-Zeile (Block) inklusive optionaler Zeilennummer (N-Nummer) aus.
*/
function writeBlock() {
  if (getProperty("showSequenceNumbers")) {
    writeWords2("N" + sequenceNumber, arguments);
    sequenceNumber += getProperty("sequenceNumberIncrement");
  } else {
    writeWords(arguments);
  }
}

/**
  Formatiert einen Kommentar sicher für die CNC-Steuerung (entfernt unerlaubte Klammern im Text
  und umschließt den Kommentar mit runden Klammern, wie bei Fanuc und Haas vorgeschrieben).
*/
function formatComment(text) {
  return "(" + filterText(String(text).toUpperCase(), permittedCommentChars) + ")";
}

var permittedCommentChars = " ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,=_-/:+*%@";

/**
  Schreibt eine reine Kommentarzeile in den G-Code (ohne N-Zeilennummer).
*/
function writeComment(text) {
  writeln(formatComment(text));
}

/**
  PRAXIS-FUNKTION (Kunden-Anforderung): Berechnet die tiefste Z-Koordinate (Z-Min / maximale Eintauchtiefe)
  für ein bestimmtes Werkzeug über alle Bearbeitungsoperationen (Sections) hinweg.
  Damit sieht der Maschinenbediener sofort, wie weit das Werkzeug aus der Spannzange (Werkzeughalter)
  herausragen muss und ob Gefahr einer Kollision mit dem Schraubstock besteht!
*/
function getToolMinimumZ(tool) {
  var zMin = undefined;
  var numberOfSections = getNumberOfSections(); // Gesamtzahl aller Bearbeitungsschritte im CAM-Programm
  for (var i = 0; i < numberOfSections; ++i) {
    var section = getSection(i); // Einzelnen Bearbeitungsschritt (Section) abrufen
    if (section.getTool().number == tool.number) {
      var zRange = section.getGlobalZRange(); // Holt den minimalen und maximalen Z-Bereich dieser Operation
      var currentMin = zRange.getMinimum(); // Tiefster Z-Wert dieser Operation
      if (zMin === undefined || currentMin < zMin) {
        zMin = currentMin;
      }
    }
  }
  return zMin;
}

// ============================================================================
// 5. HAUPTFUNKTION: onOpen() - WIRD GANZ AM ANFANG DES EXPORTS AUFGERUFEN
//    (Hier setzen wir die Aufgabe aus Schritt 4 Ihrer doc.txt exakt um!)
// ============================================================================
function onOpen() {
  // Startwert für die Zeilennummerierung (z. B. N10) aus den Properties (Eigenschaften) laden
  sequenceNumber = getProperty("sequenceNumberStart");

  // 1. Startzeichen der CNC-Datei (Prozentzeichen % signalisiert der Steuerung den Dateianfang)
  writeln("%");

  // 2. Programmnummer ausgeben (Bei Fanuc/Haas: Buchstabe "O" gefolgt von 4 bis 5 Ziffern, z. B. O1001)
  var progId = programName ? (parseInt(programName, 10) || 1001) : 1001;
  writeln("O" + ("0000" + progId).slice(-4) + " " + formatComment(programComment ? programComment : "CNC FERTIGUNGSPROGRAMM"));

  // 3. PERSONALISIERTER ENTWICKLER-INFOBLOCK (Ihre erste eigene Erweiterung!)
  var now = new Date();
  var dateString = now.getFullYear() + "-" +
                   ("0" + (now.getMonth() + 1)).slice(-2) + "-" +
                   ("0" + now.getDate()).slice(-2) + " " +
                   ("0" + now.getHours()).slice(-2) + ":" +
                   ("0" + now.getMinutes()).slice(-2);

  writeComment("==================================================");
  writeComment("AUTOMATISCH GENERIERTER CNC G-CODE (MASCHINENCODE)");
  writeComment("ENTWICKLER : " + getProperty("developerName"));
  writeComment("BETRIEB    : " + getProperty("companyName"));
  writeComment("DATUM/ZEIT : " + dateString);
  writeComment("EINHEITEN  : " + (unit == MM ? "MILLIMETER (METRISCH G21)" : "INCH / ZOLL (G20)"));
  writeComment("==================================================");

  // 4. AUTOMATISCHE WERKZEUGLISTE (Tool Table) im Header ausgeben (INKLUSIVE Z-MIN BERECHNUNG!)
  if (getProperty("writeToolList")) {
    writeComment("--- BENOETIGTE WERKZEUGE (TOOL TABLE) ---");
    var tools = getToolTable(); // Liest alle verwendeten Werkzeuge aus der CAM-Datei aus
    if (tools.getNumberOfTools() > 0) {
      for (var i = 0; i < tools.getNumberOfTools(); ++i) {
        var tool = tools.getTool(i);
        var toolInfo = "T" + ("0" + tool.number).slice(-2) +
                       " | D=" + xyzFormat.format(tool.diameter) + (unit == MM ? "MM" : "IN") +
                       " | ECKE R=" + xyzFormat.format(tool.cornerRadius);
        // Kunden-Feature: Tiefsten Z-Punkt (Z-Min) dieses Werkzeugs berechnen und anhängen
        if (getProperty("showZMinInfo")) {
          var toolZMin = getToolMinimumZ(tool);
          if (toolZMin !== undefined) {
            toolInfo += " | Z-MIN=" + xyzFormat.format(toolZMin) + (unit == MM ? "MM" : "IN");
          }
        }
        if (tool.description) {
          toolInfo += " | " + tool.description;
        }
        writeComment(toolInfo);
      }
    } else {
      writeComment("KEINE WERKZEUGDATEN IN DER CAM-DATEI GEFUNDEN");
    }
    writeComment("-----------------------------------------");
  }

  // 5. SICHERHEITS-STARTZEILE (Safe Start Block)
  // G90 = Absolutbemaßung (alle Koordinaten vom Werkstück-Nullpunkt aus gemessen)
  // G17 = Auswahl der XY-Hauptebene für Kreisbögen
  // G40 = Werkzeugradiuskorrektur ausschalten (Sicherheit!)
  // G49 = Werkzeuglängenkorrektur aufheben (Sicherheit!)
  // G80 = Alle aktiven Bohrzyklen abbrechen
  // G21 = Metrische Maßeinheit in Millimetern (oder G20 bei Zoll)
  writeBlock(
    gAbsIncModal.format(90),
    gPlaneModal.format(17),
    gFormat.format(40),
    gFormat.format(49),
    gMotionModal.format(80),
    gUnitModal.format(unit == MM ? 21 : 20)
  );
}

// ============================================================================
// 6. onSection() - WIRD FÜR JEDEN BEARBEITUNGSSCHRITT (Operation) AUFGERUFEN
// ============================================================================
function onSection() {
  var insertToolCall = isFirstSection() ||
    currentSection.getForceToolChange && currentSection.getForceToolChange() ||
    (tool.number != getPreviousSection().getTool().number);

  writeln(""); // Leerzeile zur besseren Lesbarkeit im G-Code

  // Name der aktuellen CAM-Operation als Kommentar ausgeben (z. B. "2D-TASCHE" oder "PLANFRAESEN")
  if (hasParameter("operation-comment")) {
    var comment = getParameter("operation-comment");
    if (comment) {
      writeComment("OPERATION: " + comment);
    }
  }

  // Kunden-Feature: Maximale Frästiefe (Z-Min) und maximale Rückzugshöhe (Z-Max) der aktuellen Operation ausgeben
  if (getProperty("showZMinInfo")) {
    var sectionZRange = currentSection.getGlobalZRange();
    writeComment(
      "SICHERHEITS-INFO: OP Z-MIN=" + xyzFormat.format(sectionZRange.getMinimum()) + (unit == MM ? "MM" : "IN") +
      " | OP Z-MAX=" + xyzFormat.format(sectionZRange.getMaximum()) + (unit == MM ? "MM" : "IN")
    );
  }

  // Werkzeugwechsel durchführen, wenn ein neues Werkzeug benötigt wird
  if (insertToolCall) {
    // Zuerst sicher auf Z-Heimposition zurückziehen (Kollisionsschutz!)
    writeRetract(Z);

    // Werkzeug Txx aufrufen und mit M06 (Werkzeugwechsel-Befehl) in die Spindel einwechseln
    writeBlock(toolFormat.format(tool.number), mFormat.format(6));
    if (tool.comment) {
      writeComment("WERKZEUG: " + tool.comment);
    }
  }

  // Spindeldrehzahl S und Drehrichtung (M03 = Rechtslauf im Uhrzeigersinn, M04 = Linkslauf) starten
  writeBlock(
    sOutput.format(spindleSpeed),
    mFormat.format(tool.clockwise ? 3 : 4)
  );

  // Werkstück-Nullpunkt (Work Coordinate System, z. B. G54) aktivieren
  var wcsCode = currentSection.workOffset;
  if (wcsCode == 0) {
    wcsCode = 1; // Standardmäßig G54 verwenden, falls im CAM "0" eingetragen wurde
  }
  if (wcsCode <= 6) {
    writeBlock(gFormat.format(53 + wcsCode)); // 1 -> G54, 2 -> G55, ..., 6 -> G59
  }

  // Koordinaten-Ausgabe zurücksetzen, damit nach einem Werkzeugwechsel garantiert X, Y und Z ausgegeben werden
  xOutput.reset();
  yOutput.reset();
  zOutput.reset();

  // Startposition der Operation in X und Y im Eilgang (G00) über dem Bauteil anfahren
  var initialPosition = getFramePosition(currentSection.getInitialPosition());
  writeBlock(
    gAbsIncModal.format(90),
    gMotionModal.format(0),
    xOutput.format(initialPosition.x),
    yOutput.format(initialPosition.y)
  );

  // Werkzeuglängenkorrektur (G43 mit H-Nummer = Werkzeugnummer) aktivieren und auf Start-Z-Höhe fahren
  writeBlock(
    gMotionModal.format(0),
    gFormat.format(43),
    zOutput.format(initialPosition.z),
    hFormat.format(tool.lengthOffset)
  );

  // Kühlmittel einschalten (M08 = Überflutungskühlung / Emulsion ein)
  if (tool.coolant != COOLANT_OFF) {
    writeBlock(mFormat.format(8));
  }
}

// ============================================================================
// 7. BEWEGUNGSFUNKTIONEN: Eilgang (G00), Geradenfräsen (G01) & Kreise (G02/G03)
// ============================================================================

/**
  Eilgang-Bewegung (G00 - Schnelle Positionierung in der Luft ohne Materialkontakt).
*/
function onRapid(_x, _y, _z) {
  var x = xOutput.format(_x);
  var y = yOutput.format(_y);
  var z = zOutput.format(_z);
  if (x || y || z) {
    writeBlock(gMotionModal.format(0), x, y, z);
    feedOutput.reset();
  }
}

/**
  Lineare Fräsbewegung (G01 - Bewegung im Material mit definierter Vorschubgeschwindigkeit F).
*/
function onLinear(_x, _y, _z, feed) {
  var x = xOutput.format(_x);
  var y = yOutput.format(_y);
  var z = zOutput.format(_z);
  var f = feedOutput.format(feed);
  if (x || y || z) {
    writeBlock(gMotionModal.format(1), x, y, z, f);
  } else if (f) {
    writeBlock(gMotionModal.format(1), f);
  }
}

/**
  Kreisbogen-Fräsbewegung (G02 = im Uhrzeigersinn / CW, G03 = gegen den Uhrzeigersinn / CCW).
*/
function onCircular(clockwise, cx, cy, cz, x, y, z, feed) {
  var start = getCurrentPosition();

  switch (getCircularPlane()) {
  case PLANE_XY: // Standard-Ebene G17 (Draufsicht X/Y)
    writeBlock(
      gPlaneModal.format(17),
      gMotionModal.format(clockwise ? 2 : 3),
      xOutput.format(x),
      yOutput.format(y),
      zOutput.format(z),
      iOutput.format(cx - start.x, 0),
      jOutput.format(cy - start.y, 0),
      feedOutput.format(feed)
    );
    break;
  default:
    // Falls der Kreis schräg im Raum liegt, zerlegt linearize() ihn automatisch in feine G01-Geraden
    linearize(tolerance);
  }
}

// ============================================================================
// 8. BOHRZYKLEN (Canned Cycles - z. B. G81 Standardbohren, G83 Tiefbohren)
// ============================================================================
function onCycle() {
  writeBlock(gPlaneModal.format(17));
}

function onCyclePoint(x, y, z) {
  if (isFirstCyclePoint()) {
    repositionToCycleClearance(cycle, x, y, z);
    var F = cycle.feedrate;
    switch (cycleType) {
    case "drilling": // Einfaches Zentrieren / Bohren (G81)
      writeBlock(
        gAbsIncModal.format(90),
        gCycleModal.format(81),
        xOutput.format(x),
        yOutput.format(y),
        "Z" + xyzFormat.format(z),
        "R" + xyzFormat.format(cycle.retract),
        feedOutput.format(F)
      );
      break;
    case "deep-drilling": // Tiefbohren mit Spanbruch / Entspanen (G83 mit Zustelltiefe Q)
      writeBlock(
        gAbsIncModal.format(90),
        gCycleModal.format(83),
        xOutput.format(x),
        yOutput.format(y),
        "Z" + xyzFormat.format(z),
        "R" + xyzFormat.format(cycle.retract),
        "Q" + xyzFormat.format(cycle.incrementalDepth),
        feedOutput.format(F)
      );
      break;
    default:
      expandCyclePoint(x, y, z); // Löst unbekannte Zyklen automatisch in sichere G00/G01-Einzelbewegungen auf
    }
  } else {
    if (!cycleExpanded) {
      writeBlock(xOutput.format(x), yOutput.format(y));
    } else {
      expandCyclePoint(x, y, z);
    }
  }
}

function onCycleEnd() {
  if (!cycleExpanded) {
    writeBlock(gCycleModal.format(80)); // G80 hebt den aktiven Bohrzyklus sicher wieder auf
    zOutput.reset();
  }
}

// ============================================================================
// 9. SICHERER RÜCKZUG (writeRetract) & PROGRAMMENDE (onClose)
// ============================================================================

/**
  Fährt das Werkzeug auf die maximale Sicherheitshöhe der Maschine zurück (Kollisionsschutz).
*/
function writeRetract() {
  if (!retracted) {
    if (getProperty("useG28SafeRetract")) {
      // Variante A: G28 G91 Z0 (Referenzpunktfahrt im Kettenmaß, danach sofort wieder G90 Absolutmaß!)
      writeBlock(gFormat.format(28), gAbsIncModal.format(91), "Z" + xyzFormat.format(0));
      writeBlock(gAbsIncModal.format(90));
    } else {
      // Variante B (Modern & Sicherer bei Haas/Siemens/Fanuc): G53 G00 Z0 (Maschinenkoordinatensystem)
      writeBlock(gFormat.format(53), gMotionModal.format(0), "Z" + xyzFormat.format(0));
    }
    retracted = true;
    zOutput.reset();
  }
}

/**
  onSectionEnd() wird am Ende jedes einzelnen Bearbeitungsschritts aufgerufen.
*/
function onSectionEnd() {
  writeBlock(gPlaneModal.format(17));
  invalidate();
}

/**
  onClose() wird ganz am Schluss des gesamten CNC-Programms aufgerufen.
*/
function onClose() {
  writeln("");
  writeComment("--- SICHERES PROGRAMMENDE (SAFE FOOTER) ---");

  // 1. Kühlmittel ausschalten (M09)
  writeBlock(mFormat.format(9));

  // 2. Z-Achse (Spindel) ganz nach oben in Sicherheit bringen
  writeRetract(Z);

  // 3. Spindel anhalten (M05)
  writeBlock(mFormat.format(5));

  // 4. Tisch in Richtung Kabinentür fahren (Y0 im Maschinenkoordinatensystem G53), damit der Bediener das Bauteil entnehmen kann
  if (getProperty("useG28SafeRetract")) {
    writeBlock(gFormat.format(28), gAbsIncModal.format(91), "Y" + xyzFormat.format(0));
    writeBlock(gAbsIncModal.format(90));
  } else {
    writeBlock(gFormat.format(53), gMotionModal.format(0), "Y" + xyzFormat.format(0));
  }

  // 5. Programmende mit Rücksprung zum Programmanfang (M30)
  writeBlock(mFormat.format(30));

  // 6. Abschlusszeichen der Datei (%)
  writeln("%");
}

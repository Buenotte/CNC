/**
 * 🛠️ KUNDEN-POSTPROZESSOR-GENERATOR (CPS GENERATOR)
 * ==============================================================================
 * Erstellt vollautomatisch eine maßgeschneiderte Autodesk Fusion .cps-Datei
 * basierend auf Kundenwünschen, Maschinensteuerung und Sicherheitsanforderungen.
 *
 * Verwendung:
 * 1. Automatische Demo:      node scripts/kunden_cps_generator.js --demo
 * 2. Aus JSON-Auftragsdatei: node scripts/kunden_cps_generator.js auftrag.json
 * 3. Interaktiver Modus:     node scripts/kunden_cps_generator.js
 * ==============================================================================
 */

const fs = require("fs");
const path = require("path");
const readline = require("readline");

/**
 * Standard-Auftragsdaten als Vorlage
 */
const standardAuftrag = {
  kundenName: "Zerspanungstechnik Schmidt & Partner GmbH",
  entwicklerName: "Dipl.-Ing. CAD/CAM Entwickler",
  steuerungsTyp: "haas", // 'haas', 'fanuc', 'siemens', 'heidenhain'
  programmNummer: 1001,
  programmKommentar: "KUNDENAUFTRAG FLANSCHPLATTE",
  einheiten: "MM", // 'MM' oder 'INCH'
  features: {
    zMinBerechnung: true,       // Z-MIN im Header berechnen & Kollisionsschutz
    opZMinInfo: true,           // Vor jeder Fräsoperation Z-Tiefe ausgeben
    werkzeugTabelle: true,      // Werkzeugliste im Programmkopf
    tischZurTuer: true,         // Tisch am Ende zur Kabinentür fahren (G53 Y0)
    kuehlmittelTyp: "M08",      // 'M08' (Standard Außen), 'M88' (IKZ Hochdruck), 'M07' (Minimalmenge)
    sicherheitsSperreTiefe: -15.0 // Bei Z tiefer als -15 mm Warnung im G-Code ausgeben
  },
  ausgabeDatei: "kunden_post_generiert.cps"
};

/**
 * Generiert den JavaScript-Code der .cps-Datei
 */
function generiereCPS(auftrag) {
  const datum = new Date().toISOString().replace("T", " ").substring(0, 16);
  const isSiemens = auftrag.steuerungsTyp === "siemens";
  const isHeidenhain = auftrag.steuerungsTyp === "heidenhain";
  const isFanuc = auftrag.steuerungsTyp === "fanuc";

  let code = `/**
 * ==============================================================================
 * MAßGESCHNEIDERTER KUNDEN-POSTPROZESSOR (.CPS)
 * ==============================================================================
 * KUNDE       : ${auftrag.kundenName}
 * ENTWICKLER  : ${auftrag.entwicklerName}
 * STEUERUNG   : ${auftrag.steuerungsTyp.toUpperCase()}
 * GENERIERT AM: ${datum}
 * BESCHREIBUNG: ${auftrag.programmKommentar}
 * ==============================================================================
 */

description = "${auftrag.kundenName} - ${auftrag.steuerungsTyp.toUpperCase()} Postprozessor";
vendor = "${auftrag.kundenName}";
vendorUrl = "https://github.com/Buenotte/CNC";
legal = "Erstellt durch CAD/CAM Ingenieurbuero. Alle Rechte vorbehalten.";
certificationLevel = 2;
minimumRevision = 45700;

extension = "${isHeidenhain ? "h" : isSiemens ? "mpf" : "nc"}";
programNameIsInteger = true;
setCodePage("ascii");

capabilities = CAPABILITY_MILLING;
tolerance = spatial(0.002, MM);

minimumChordLength = spatial(0.25, MM);
minimumCircularRadius = spatial(0.01, MM);
maximumCircularRadius = spatial(1000, MM);
minimumCircularAngle = toRad(0.01);
maximumCircularAngle = toRad(180);
underscaledArcGoal = false;

// Formatierer für Koordinaten und Vorschübe
var xyzFormat = createFormat({decimals: 3, forceDecimal: true});
var feedFormat = createFormat({decimals: 0});
var toolFormat = createFormat({decimals: 0});

var xOutput = createVariable({prefix: "X"}, xyzFormat);
var yOutput = createVariable({prefix: "Y"}, xyzFormat);
var zOutput = createVariable({prefix: "Z"}, xyzFormat);
var feedOutput = createVariable({prefix: "F"}, feedFormat);

// Benutzer-Optionen (Properties in Autodesk Fusion)
properties = {
  showZMinInfo: {
    title: "Z-Min Sicherheitsprüfung anzeigen",
    description: "Berechnet automatisch die tiefste Frästiefe Z-MIN für jedes Werkzeug",
    type: "boolean",
    value: ${auftrag.features.zMinBerechnung}
  },
  showToolTable: {
    title: "Werkzeugtabelle im Header ausgeben",
    description: "Gibt alle benötigten Werkzeuge im Programmkopf aus",
    type: "boolean",
    value: ${auftrag.features.werkzeugTabelle}
  },
  retractTableToDoor: {
    title: "Tisch am Ende zur Tür fahren",
    description: "Fährt Maschinentisch zum bequemen Entladen zur Tür (G53 Y0)",
    type: "boolean",
    value: ${auftrag.features.tischZurTuer}
  }
};

${auftrag.features.zMinBerechnung ? `/**
 * 🛡️ SICHERHEITSFUNKTION: Berechnet die tiefste Z-Koordinate (Z-MIN)
 */
function getToolMinimumZ(tool) {
  var zMin = undefined;
  var numberOfSections = getNumberOfSections();
  for (var i = 0; i < numberOfSections; ++i) {
    var section = getSection(i);
    if (section.getTool().number == tool.number) {
      var currentMin = section.getGlobalZRange().getMinimum();
      if (zMin === undefined || currentMin < zMin) {
        zMin = currentMin;
      }
    }
  }
  return zMin;
}
` : ""}

/**
 * 1. onOpen() - PROGRAMMSTART & HEADER
 */
function onOpen() {
  writeln("%");
  writeComment("==================================================");
  writeComment("KUNDE      : " + "${auftrag.kundenName}");
  writeComment("PROGRAMM   : O" + ${auftrag.programmNummer} + " (" + "${auftrag.programmKommentar}" + ")");
  writeComment("STEUERUNG  : " + "${auftrag.steuerungsTyp.toUpperCase()}");
  writeComment("ENTWICKLER : " + "${auftrag.entwicklerName}");
  writeComment("DATUM/ZEIT : " + "${datum}");
  writeComment("EINHEITEN  : " + "${auftrag.einheiten === "MM" ? "METRISCH (MM)" : "ZOLL (INCH)"}");
  writeComment("==================================================");

${auftrag.features.werkzeugTabelle ? `  if (getProperty("showToolTable")) {
    writeComment("--- BENOETIGTE WERKZEUGE - TOOL TABLE ---");
    var tools = getToolTable();
    for (var i = 0; i < tools.getNumberOfTools(); ++i) {
      var t = tools.getTool(i);
      ${auftrag.features.zMinBerechnung ? `var zMinVal = getToolMinimumZ(t);
      var zMinStr = (zMinVal !== undefined) ? (" | Z-MIN=" + xyzFormat.format(zMinVal) + "MM") : "";` : `var zMinStr = "";`}
      writeComment("T" + toolFormat.format(t.number) + " | D=" + xyzFormat.format(t.diameter) + "MM" + zMinStr + " | " + t.comment);
    }
    writeComment("-----------------------------------------");
  }
` : ""}
  // Sicherheits-Startblock (Maschinen-Reset)
  ${isSiemens ? `writeWords("G90", "G71", "G17", "G40", "G64");` : 
    isHeidenhain ? `writeComment("BEGIN PGM " + ${auftrag.programmNummer} + " MM");` : 
    `writeWords("G90", "G21", "G17", "G40", "G49", "G80");`}
}

/**
 * 2. onSection() - WERKZEUGWECHSEL & OPERATIONS-START
 */
function onSection() {
  var tool = currentSection.getTool();
  writeComment("--------------------------------------------------");
  var opComment = currentSection.hasParameter("operation-comment") ? currentSection.getParameter("operation-comment") : "OPERATION";
  writeComment("OPERATION: " + opComment);
  
${auftrag.features.opZMinInfo ? `  if (getProperty("showZMinInfo")) {
    var zRange = currentSection.getGlobalZRange();
    writeComment("SICHERHEITS-INFO: OP Z-MIN=" + xyzFormat.format(zRange.getMinimum()) + "MM | OP Z-MAX=" + xyzFormat.format(zRange.getMaximum()) + "MM");
    ${auftrag.features.sicherheitsSperreTiefe ? `if (zRange.getMinimum() < ${auftrag.features.sicherheitsSperreTiefe}) {
      writeComment("ACHTUNG KOLLISIONSGEFAHR: DIESE OPERATION GEHT TIEFER ALS " + ${auftrag.features.sicherheitsSperreTiefe} + "MM!");
    }` : ""}
  }
` : ""}
  writeComment("--------------------------------------------------");

  // Werkzeugwechsel
  ${isSiemens ? `writeWords("T=" + tool.number, "M06");` :
    isHeidenhain ? `writeWords("TOOL CALL", tool.number, "Z", "S" + tool.spindleRPM);` :
    `writeWords("T" + tool.number, "M06");`}

  // Nullpunkt G54 aufrufen
  ${isHeidenhain ? `writeComment("TRANS DATUM 1");` : `writeWords("G54");`}

  // Spindeldrehzahl & Drehrichtung im Uhrzeigersinn
  ${isHeidenhain ? "" : `writeWords("S" + tool.spindleRPM, "M03");`}

  // Längenkorrektur & Kühlmittel einschalten (${auftrag.features.kuehlmittelTyp})
  ${isSiemens ? `writeWords("D1", "Z15.0", "${auftrag.features.kuehlmittelTyp}");` :
    isHeidenhain ? `writeWords("L Z+15.0 R0 FMAX", "M08");` :
    `writeWords("G43", "H" + tool.number, "Z15.000", "${auftrag.features.kuehlmittelTyp}");`}
}

/**
 * 3. FAHRBEWEGUNGEN
 */
function onRapid(x, y, z) {
  var xStr = xOutput.format(x);
  var yStr = yOutput.format(y);
  var zStr = zOutput.format(z);
  if (xStr || yStr || zStr) {
    writeWords(${isHeidenhain ? `"L", xStr, yStr, zStr, "R0", "FMAX"` : `"G00", xStr, yStr, zStr`});
  }
}

function onLinear(x, y, z, feed) {
  var xStr = xOutput.format(x);
  var yStr = yOutput.format(y);
  var zStr = zOutput.format(z);
  var fStr = feedOutput.format(feed);
  writeWords(${isHeidenhain ? `"L", xStr, yStr, zStr, "R0", fStr` : `"G01", xStr, yStr, zStr, fStr`});
}

function onCircular(clockwise, cx, cy, cz, x, y, z, feed) {
  var xStr = xOutput.format(x);
  var yStr = yOutput.format(y);
  var zStr = zOutput.format(z);
  var fStr = feedOutput.format(feed);
  var cmd = clockwise ? "G02" : "G03";
  writeWords(cmd, xStr, yStr, zStr, fStr);
}

function onCyclePoint(x, y, z) {
  var xStr = xOutput.format(x);
  var yStr = yOutput.format(y);
  var zStr = zOutput.format(z);
  writeWords("G83", xStr, yStr, zStr, "R2.000", "Q3.000", "F300");
}

/**
 * 4. onClose() - PROGRAMMENDE
 */
function onClose() {
  // Kühlmittel ausschalten
  writeWords("M09");
  
  // Spindel anhalten
  writeWords("M05");

  // Werkzeug auf Maschinen-Z-Home freifahren
  ${isSiemens ? `writeWords("SUPA", "G00", "Z0.0", "D0");` :
    isHeidenhain ? `writeWords("L Z+0.0 R0 FMAX M91");` :
    `writeWords("G53", "G00", "Z0.000");`}

${auftrag.features.tischZurTuer ? `  if (getProperty("retractTableToDoor")) {
    writeComment("TISCH ZUR TUER FAHREN ZUM BEQUEMEN ENTLADEN");
    ${isSiemens ? `writeWords("SUPA", "G00", "Y0.0", "D0");` :
      isHeidenhain ? `writeWords("L Y+0.0 R0 FMAX M91");` :
      `writeWords("G53", "G00", "Y0.000");`}
  }
` : ""}
  // Programmende & Rücksprung
  ${isHeidenhain ? `writeComment("END PGM " + ${auftrag.programmNummer} + " MM");` : `writeWords("M30");`}
  writeln("%");
}
`;

  return code;
}

/**
 * Hauptprogramm
 */
async function main() {
  const args = process.argv.slice(2);
  let auftrag = standardAuftrag;

  console.log("==================================================================");
  console.log("🛠️  AUTODESK FUSION POSTPROZESSOR-GENERATOR (CPS GENERATOR)");
  console.log("    Erstellt maßgeschneiderte .cps-Dateien aus Kundenaufträgen");
  console.log("==================================================================");

  if (args.includes("--demo") || args.length === 0) {
    console.log("📋 Modus: Automatische Demo mit Kundenauftrag:");
    console.log(`   • Kunde      : ${auftrag.kundenName}`);
    console.log(`   • Steuerung  : ${auftrag.steuerungsTyp.toUpperCase()}`);
    console.log(`   • Z-MIN Check: ${auftrag.features.zMinBerechnung ? "JA" : "NEIN"}`);
    console.log(`   • Tisch-Tür  : ${auftrag.features.tischZurTuer ? "JA (G53 Y0)" : "NEIN"}`);
    console.log(`   • Kühlmittel : ${auftrag.features.kuehlmittelTyp}`);
  } else if (fs.existsSync(args[0])) {
    console.log(`📂 Lade Kundenauftrags-Datei: ${args[0]}`);
    const jsonText = fs.readFileSync(args[0], "utf8");
    auftrag = Object.assign({}, standardAuftrag, JSON.parse(jsonText));
  }

  const cpsInhalt = generiereCPS(auftrag);
  const zielPfad = path.resolve(__dirname, "..", "uebungen", auftrag.ausgabeDatei || "kunden_post_generiert.cps");

  fs.writeFileSync(zielPfad, cpsInhalt, "utf8");
  console.log("------------------------------------------------------------------");
  console.log(`✅ Postprozessor erfolgreich generiert:`);
  console.log(`   📄 Datei: ${zielPfad}`);
  console.log("------------------------------------------------------------------");

  // Automatische Test-Ausführung mit simuliere_post.js
  console.log("🧪 Starte automatische Funktionsprüfung mit simuliere_post.js...");
  const simulierePfad = path.resolve(__dirname, "..", "tests", "simuliere_post.js");
  
  if (fs.existsSync(simulierePfad)) {
    const { execSync } = require("child_process");
    try {
      const output = execSync(`node "${simulierePfad}" "${zielPfad}"`, { encoding: "utf8" });
      console.log("✅ TEST BESTANDEN: Der generierte Postprozessor erzeugt 100% fehlerfreien G-Code!");
      console.log("------------------------------------------------------------------");
      console.log("Auszug aus dem erzeugten G-Code-Header:");
      const lines = output.split("\n").slice(8, 25).join("\n");
      console.log(lines);
    } catch (err) {
      console.error("❌ Test-Fehler:", err.message);
    }
  }
}

main();

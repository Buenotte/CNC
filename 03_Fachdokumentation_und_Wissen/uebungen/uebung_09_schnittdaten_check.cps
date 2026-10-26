/**
 * Übung 09: Schnittdaten-Prüfung und Drehzahlschutz (Schnittgeschwindigkeit Vc)
 * Entwickler: Dipl.-Ing. Bujanovski (Ingenieurbüro für CAD/CAM-Fertigungstechnik)
 * Ziel: Postprozessor berechnet Vc und warnt werkstoffspezifisch vor Werkzeugbruch und Überhitzung.
 */

description = "Uebung 09 - Schnittdaten & Werkstoff Vc Pruefung (Dipl.-Ing. Bujanovski)";
vendor = "Ingenieurbuero Dipl.-Ing. Bujanovski";
certificationLevel = 2;
extension = "nc";
setCodePage("ascii");
capabilities = CAPABILITY_MILLING;
tolerance = spatial(0.002, MM);

properties = {
  materialType: {
    title      : "Werkstueck-Werkstoff (Material Selection)",
    description: "Waehlen Sie den Werkstoff fuer die automatische Vc-Grenzpruefung",
    group      : "technologie",
    type       : "enum",
    values     : [
      {id: "alu",       title: "1. Aluminium (EN AW-6082) - Vc max 350 m/min"},
      {id: "steel",     title: "2. Baustahl / 42CrMo4 - Vc max 180 m/min"},
      {id: "stainless", title: "3. Edelstahl (1.4301 / V2A) - Vc max 90 m/min"},
      {id: "plastic",   title: "4. Kunststoff (POM / PEEK) - Vc max 500 m/min"}
    ],
    value      : "alu",
    scope      : "post"
  },
  autoSpeedClamp: {
    title      : "Drehzahl bei zu hohem Vc automatisch drosseln (Auto-Speed-Clamp)",
    description: "Begrenzt die Spindeldrehzahl S im NC-Code bei Werkstoff-Ueberhitzungsgefahr automatisch auf das zulaessige Maximum",
    group      : "technologie",
    type       : "boolean",
    value      : true,
    scope      : "post"
  },
  maxSpindleSpeedWarning: {
    title      : "Max. Spindeldrehzahl Grenze (RPM)",
    description: "Maximale zulaessige Maschinendrehzahl der Spindel",
    group      : "safety",
    type       : "integer",
    value      : 12000,
    scope      : "post"
  }
};

function onOpen() {
  writeln("%");
  writeln("O1009 (UEBUNG 09 - SCHNITTDATEN- & WERKSTOFF-PRUEFUNG)");
  writeln("(==================================================)");
  writeln("(ENTWICKLER : DIPL.-ING. BUJANOVSKI)");
  writeln("(BETRIEB    : INGENIEURBUERO DIPL.-ING. BUJANOVSKI)");
  writeln("(GEWAEHLTER WERKSTOFF : " + getProperty("materialType").toUpperCase() + ")");
  writeln("(==================================================)");

  // Sicherheits-Startblock:
  // G90 = Absolutmaß (Bezug auf Werkstück-Nullpunkt G54)
  // G21 = Metrisches Maßsystem (Millimeter mm)
  // G17 = Fräsebene XY (Werkzeugachse ist Z)
  // G40 = Werkzeugradiuskorrektur ausschalten
  // G80 = Bohrzyklen abbrechen
  writeWords("G90", "G21", "G17", "G40", "G80");
}

function onSection() {
  var selectedMaterial = getProperty("materialType");
  var maxRpm = getProperty("maxSpindleSpeedWarning");

  // 1. Maximale erlaubte Schnittgeschwindigkeit nach Werkstoff bestimmen:
  var maxVcAllowed = 350; // Standard: Aluminium
  if (selectedMaterial === "stainless") {
    maxVcAllowed = 90;    // Edelstahl: Extreme Hitzeentwicklung bei zu hoher Vc!
  } else if (selectedMaterial === "steel") {
    maxVcAllowed = 180;   // Baustahl / Verguetungsstahl
  } else if (selectedMaterial === "plastic") {
    maxVcAllowed = 500;   // Kunststoff (POM/PEEK)
  }

  // 2. Tatsaechliche Schnittgeschwindigkeit berechnen: Vc = (pi * D * n) / 1000 in m/min
  var currentTool = (typeof currentSection !== "undefined" && currentSection.getTool) ? currentSection.getTool() : tool;
  var toolDia = currentTool.diameter || 10.0;
  var rpm = spindleSpeed || 8000;
  var vc = (Math.PI * toolDia * rpm) / 1000.0;
  var vcRounded = Math.round(vc);

  writeln("(--------------------------------------------------)");
  writeln("(OPERATION : " + (currentSection.getId ? currentSection.getId() : "FRAESOPERATION") + ")");
  writeln("(TECHNOLOGIE-CHECK : MATERIAL=" + selectedMaterial.toUpperCase() + " | D=" + toolDia.toFixed(1) + "MM | S=" + rpm + " U/MIN)");
  writeln("(SCHNITTGESCHWINDIGKEIT : VC = " + vcRounded + " M/MIN | ZULAESSIG MAX: " + maxVcAllowed + " M/MIN)");

  // 3. Sicherheits-Warnung und aktive automatische Drehzahl-Drosselung (Auto-Speed-Clamp):
  var originalRpm = rpm;
  if (vc > maxVcAllowed) {
    writeln("(!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!)");
    writeln("(ACHTUNG ALARM: VC = " + vcRounded + " M/MIN IST FUER " + selectedMaterial.toUpperCase() + " ZU HOCH!)");
    writeln("(MAXIMAL ERLAUBT FUER DIESEN WERKSTOFF: " + maxVcAllowed + " M/MIN!)");
    writeln("(GEFAHR: SCHNEIDEN-UEBERHITZUNG, BRAND UND WERKZEUGBRUCH!)");

    var clampActive = (typeof getProperty === "function" && getProperty("autoSpeedClamp") !== undefined) ? getProperty("autoSpeedClamp") : true;
    if (clampActive) {
      // Physikalische Umkehrformel fuer sichere Drehzahl: n_safe = (Vc_max * 1000) / (pi * D)
      var safeRpm = Math.round((maxVcAllowed * 1000.0) / (Math.PI * toolDia));
      var safeVc = Math.round((Math.PI * toolDia * safeRpm) / 1000.0);
      writeln("(--------------------------------------------------)");
      writeln("(AKTIVER WERKZEUGSCHUTZ: AUTO-SPEED-CLAMP AKTIVIERT!)");
      writeln("(SPINDELDREHZAHL WURDE VOM POSTPROZESSOR AUTOMATISCH GEDROSSELT:)");
      writeln("(URSPRUENGLICH PROGRAMMIERT     : S = " + originalRpm + " U/MIN)");
      writeln("(KORRIGIERT AUF SICHERE DREHZAHL: S = " + safeRpm + " U/MIN)");
      writeln("(NEUE SCHNITTGESCHWINDIGKEIT    : VC = " + safeVc + " M/MIN <= MAX " + maxVcAllowed + " M/MIN)");
      writeln("(--------------------------------------------------)");
      rpm = safeRpm;
    }
    writeln("(!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!)");
  }

  // 4. Maschinendrehzahl-Limit pruefen:
  if (rpm > maxRpm) {
    writeln("(ACHTUNG MASCHINENSCHUTZ: DREHZAHL S=" + rpm + " UEBERSCHREITET MASCHINENGRENZE " + maxRpm + " U/MIN!)");
    rpm = maxRpm;
  }

  // T.. = Werkzeugnummer (Tool)
  // M06 = Automatischer Werkzeugwechsel durch Greifer
  writeWords("T" + ("0" + currentTool.number).slice(-2), "M06");

  // S.. = Spindeldrehzahl in U/min
  // M03 = Spindel Rechtslauf EIN (im Uhrzeigersinn)
  writeWords("S" + rpm, currentTool.clockwise ? "M03" : "M04");

  // G54 = 1. Werkstück-Koordinatensystem
  writeWords("G54");

  // G43 H.. Z.. M08 = Werkzeuglaengenkorrektur und Kuehlmittel EIN
  writeWords("G43", "H" + ("0" + currentTool.number).slice(-2), "Z15.000", "M08");
  xOutput.reset();
  yOutput.reset();
  zOutput.reset();
  feedOutput.reset();
}

var xyzFormat = createFormat({decimals: 3, forceDecimal: true});
var feedFormat = createFormat({decimals: 0});
var xOutput = createVariable({prefix: "X"}, xyzFormat);
var yOutput = createVariable({prefix: "Y"}, xyzFormat);
var zOutput = createVariable({prefix: "Z"}, xyzFormat);
var iOutput = createReferenceVariable({prefix: "I"}, xyzFormat);
var jOutput = createReferenceVariable({prefix: "J"}, xyzFormat);
var feedOutput = createVariable({prefix: "F"}, feedFormat);

function onRapid(x, y, z) {
  writeWords("G00", xOutput.format(x), yOutput.format(y), zOutput.format(z));
}

function onLinear(x, y, z, feed) {
  writeWords("G01", xOutput.format(x), yOutput.format(y), zOutput.format(z), feedOutput.format(feed));
}

function onCircular(clockwise, cx, cy, cz, x, y, z, feed) {
  var start = getCurrentPosition();
  xOutput.reset();
  yOutput.reset();
  writeWords(
    clockwise ? "G02" : "G03",
    xOutput.format(x),
    yOutput.format(y),
    zOutput.format(z),
    iOutput.format(cx - start.x),
    jOutput.format(cy - start.y),
    feedOutput.format(feed)
  );
}

function onCyclePoint(x, y, z) {
  xOutput.reset();
  yOutput.reset();
  zOutput.reset();
  writeWords(
    "G83",
    xOutput.format(x),
    yOutput.format(y),
    zOutput.format(z),
    "R" + xyzFormat.format(cycle.retract),
    "Q" + xyzFormat.format(cycle.incrementalDepth || 3.0),
    feedOutput.format(cycle.feedrate)
  );
}

function onCycleEnd() {
  writeWords("G80");
}

function onClose() {
  // M09 = Kuehlschmierstoff ausschalten
  writeWords("M09");

  // G53 G00 Z0.0 = Spindel senkrecht nach oben auf Maschinen-Referenzhoehe fahren
  writeWords("G53", "G00", "Z0.0");

  // M05 = Fraesspindel ausschalten (Spindel-Stopp)
  writeWords("M05");

  // G53 G00 Y0.0 = Tisch nach vorne zur Schiebetuer fahren
  writeWords("G53", "G00", "Y0.0");

  // M30 = Hauptprogrammende, Ruecklauf und Speicher-Reset
  writeWords("M30");
  writeln("%");
}

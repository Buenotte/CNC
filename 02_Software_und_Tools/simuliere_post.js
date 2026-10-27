/**
 * Lokaler CNC-Postprozessor-Simulator & Test-Runner (Ausführungsprogramm für .cps-Dateien)
 * 
 * Dieses Skript simuliert die Autodesk Fusion CAM-Engine (Fertigungs-Software-Kern) lokal mit Node.js!
 * Wenn Sie "node tests/simuliere_post.js" ausführen, passiert Folgendes:
 * 1. Ihre Datei "src/mein_erster_post.cps" wird eingelesen und ausgeführt.
 * 2. Das 3D-Bauteil "Bauteil_1001" (80x50x12mm Platte mit Kreistasche Ø30 und 4 Bohrungen Ø6)
 *    wird durch Ihren Postprozessor geschickt (onOpen -> onSection -> onRapid/onLinear/onCircular/onCycle -> onClose).
 * 3. Der erzeugte G-Code (Maschinencode) wird in "tests/mein_generierter_gcode.nc" gespeichert
 *    und direkt im Terminal (Befehlsfenster) angezeigt!
 */

const fs = require("fs");
const path = require("path");
const vm = require("vm");

// Wenn ein Pfad als Befehlszeilen-Argument übergeben wurde (z.B. node tests/simuliere_post.js uebungen/uebung_01_entwickler_header.cps),
// wird dieser geladen. Andernfalls wird standardmäßig "src/mein_erster_post.cps" ausgeführt.
const targetArg = process.argv[2];
let cpsPath;
if (targetArg) {
  const directPath = path.resolve(process.cwd(), targetArg);
  if (fs.existsSync(directPath)) {
    cpsPath = directPath;
  } else {
    // Intelligente Pfadauflösung für verschobene Ordnerstrukturen (03_Fachdokumentation_und_Wissen etc.)
    const candidates = [
      path.resolve(process.cwd(), "03_Fachdokumentation_und_Wissen", targetArg),
      path.resolve(process.cwd(), "02_Software_und_Tools", targetArg),
      path.resolve(process.cwd(), "01_Kundenauftraege", targetArg),
      path.resolve(__dirname, "..", targetArg),
      path.resolve(__dirname, "..", "..", targetArg),
      path.resolve(__dirname, "..", "..", "03_Fachdokumentation_und_Wissen", targetArg)
    ];
    const found = candidates.find(c => fs.existsSync(c));
    cpsPath = found || directPath;
  }
} else {
  const defaultLocal = path.join(__dirname, "src", "mein_erster_post.cps");
  cpsPath = fs.existsSync(defaultLocal) ? defaultLocal : path.join(__dirname, "..", "src", "mein_erster_post.cps");
}
const exerciseName = path.basename(cpsPath, path.extname(cpsPath));
const directNcPath = path.join(path.dirname(cpsPath), exerciseName + ".nc");
const exerciseNcPath = path.join(__dirname, exerciseName + ".nc");
const outNcPath = path.join(__dirname, "mein_generierter_gcode.nc");

const outputLines = [];

// Hilfsfunktion zur Zahlenformatierung wie in der echten Autodesk Post-API (Programmierschnittstelle)
function makeFormatter(spec) {
  spec = spec || {};
  const prefix = spec.prefix || "";
  const decimals = spec.decimals !== undefined ? spec.decimals : 3;
  const width = spec.width || 0;
  const zeropad = !!spec.zeropad;
  const forceDecimal = !!spec.forceDecimal;

  return {
    format: function (val) {
      if (val === undefined || val === null || isNaN(val)) return "";
      let numStr;
      if (decimals === 0 && !forceDecimal) {
        numStr = String(Math.round(val));
      } else {
        numStr = Number(val).toFixed(decimals);
        if (!forceDecimal && decimals > 0) {
          numStr = numStr.replace(/\.?0+$/, "");
        }
      }
      if (zeropad && width > 0) {
        const isNeg = numStr.startsWith("-");
        const clean = isNeg ? numStr.slice(1) : numStr;
        numStr = (isNeg ? "-" : "") + clean.padStart(width, "0");
      }
      return prefix + numStr;
    }
  };
}

// Simulierte 3D-CAM-Daten (Werkzeuge & Bearbeitungs-Operationen von Bauteil_1001)
const mockTools = [
  {
    number: 1,
    diameter: 10.0,
    cornerRadius: 0.0,
    lengthOffset: 1,
    diameterOffset: 1,
    description: "SCHAFTFRAESER 10MM VHM",
    comment: "SCHAFTFRAESER 10MM VHM",
    spindleRPM: 8000,
    clockwise: true,
    coolant: 1
  },
  {
    number: 2,
    diameter: 6.0,
    cornerRadius: 0.0,
    lengthOffset: 2,
    diameterOffset: 2,
    description: "SPIRALBOHRER 6MM VHM",
    comment: "SPIRALBOHRER 6MM VHM",
    spindleRPM: 3500,
    clockwise: true,
    coolant: 1
  }
];

if (exerciseName.indexOf("uebung_10") !== -1) {
  mockTools.push({
    number: 3,
    diameter: 50.0,
    cornerRadius: 0.0,
    lengthOffset: 3,
    diameterOffset: 3,
    description: "PLANMESSERKOPF 50MM (OP20 RUECKSEITE)",
    comment: "PLANMESSERKOPF 50MM (OP20 RUECKSEITE)",
    spindleRPM: 4000,
    clockwise: true,
    coolant: 1
  });
}

if (exerciseName.indexOf("uebung_11") !== -1) {
  mockTools.push({
    number: 3,
    diameter: 8.0,
    cornerRadius: 0.0,
    lengthOffset: 3,
    diameterOffset: 3,
    threadPitch: 1.25,
    description: "GEWINDEBOHRER M8 (P=1.25MM)",
    comment: "GEWINDEBOHRER M8 (P=1.25MM)",
    spindleRPM: 600,
    clockwise: true,
    coolant: 1
  });
}

const mockSections = [
  {
    comment: "1. AUSSENKONTUR FRAESEN - 2D KONTUR",
    tool: mockTools[0],
    spindleSpeed: 8000,
    workOffset: 1,
    initialPos: { x: -10.0, y: -10.0, z: 15.0 },
    zMin: -5.0,
    zMax: 15.0,
    runMoves: function (sandbox) {
      if (typeof sandbox.onRapid === "function") sandbox.onRapid(-10.0, -10.0, 2.0);
      if (typeof sandbox.onLinear === "function") {
        sandbox.onLinear(-10.0, -10.0, -5.0, 500);
        sandbox.onLinear(0.0, 0.0, -5.0, 1200);
        sandbox.onLinear(80.0, 0.0, -5.0, 1200);
        sandbox.onLinear(80.0, 50.0, -5.0, 1200);
        sandbox.onLinear(0.0, 50.0, -5.0, 1200);
        sandbox.onLinear(0.0, 0.0, -5.0, 1200);
      }
      if (typeof sandbox.onRapid === "function") sandbox.onRapid(0.0, 0.0, 15.0);
    }
  },
  {
    comment: "2. KREISTASCHE IN DER MITTE - G02/G03 KREISINTERPOLATION",
    tool: mockTools[0],
    spindleSpeed: 8000,
    workOffset: 1,
    initialPos: { x: 40.0, y: 25.0, z: 15.0 },
    zMin: -3.0,
    zMax: 15.0,
    runMoves: function (sandbox) {
      if (typeof sandbox.onRapid === "function") sandbox.onRapid(40.0, 25.0, 2.0);
      if (typeof sandbox.onLinear === "function") {
        sandbox.onLinear(40.0, 25.0, -3.0, 400);
        sandbox.onLinear(55.0, 25.0, -3.0, 1000);
      }
      sandbox._currentPos = { x: 55.0, y: 25.0, z: -3.0 };
      if (typeof sandbox.onCircular === "function") sandbox.onCircular(false, 40.0, 25.0, -3.0, 55.0, 25.0, -3.0, 1000);
      if (typeof sandbox.onLinear === "function") sandbox.onLinear(40.0, 25.0, -3.0, 1000);
      if (typeof sandbox.onRapid === "function") sandbox.onRapid(40.0, 25.0, 15.0);
    }
  },
  {
    comment: "3. VIER BEFESTIGUNGSBOHRUNGEN - G83 TIEFBOHRZYKLUS",
    tool: mockTools[1],
    spindleSpeed: 3500,
    workOffset: 1,
    initialPos: { x: 10.0, y: 10.0, z: 15.0 },
    zMin: -12.0,
    zMax: 15.0,
    runMoves: function (sandbox) {
      sandbox.cycleType = "deep-drilling";
      sandbox.cycle = { feedrate: 300, retract: 2.0, clearance: 15.0, incrementalDepth: 3.0 };
      sandbox.cycleExpanded = false;
      sandbox._firstCycle = true;
      if (typeof sandbox.onCycle === "function") sandbox.onCycle();
      if (typeof sandbox.onCyclePoint === "function") {
        sandbox.onCyclePoint(10.0, 10.0, -12.0);
        sandbox._firstCycle = false;
        sandbox.onCyclePoint(70.0, 10.0, -12.0);
        sandbox.onCyclePoint(70.0, 40.0, -12.0);
        sandbox.onCyclePoint(10.0, 40.0, -12.0);
      }
      if (typeof sandbox.onCycleEnd === "function") sandbox.onCycleEnd();
      if (typeof sandbox.onRapid === "function") sandbox.onRapid(10.0, 40.0, 15.0);
    }
  }
];

// Für Übung 10 (2. Aufspannung G55 / OP20 - Bauteil umdrehen) fügen wir die 2. Aufspannung mit workOffset = 2 (G55) hinzu:
if (exerciseName.indexOf("uebung_10") !== -1) {
  mockSections.push(
    {
      comment: "4. OP20 (2. AUFSPANNUNG G55): BAUTEIL 180 GRAD UMGEDREHT - 3MM RESTBODEN PLANFRAESEN AUF 12MM",
      tool: mockTools[2],
      spindleSpeed: 4000,
      workOffset: 2, // 2 -> G55 (2. Aufspannung nach Bauteil-Umdrehen)
      initialPos: { x: -20.0, y: 12.0, z: 15.0 },
      zMin: 0.0,
      zMax: 15.0,
      runMoves: function (sandbox) {
        if (typeof sandbox.onRapid === "function") sandbox.onRapid(-20.0, 12.0, 5.0);
        if (typeof sandbox.onLinear === "function") {
          // 1. Zustellung Z+1.5 mm (erste 1.5 mm vom 3mm Spannrand abtragen)
          sandbox.onLinear(-20.0, 12.0, 1.5, 600);
          sandbox.onLinear(100.0, 12.0, 1.5, 1500);
          sandbox.onLinear(100.0, 38.0, 1.5, 1500);
          sandbox.onLinear(-20.0, 38.0, 1.5, 1500);
          // 2. Schlicht-Zustellung Z0.0 mm (Fertigmaß 12.0 mm Dicke herstellen)
          sandbox.onLinear(-20.0, 12.0, 0.0, 600);
          sandbox.onLinear(100.0, 12.0, 0.0, 1200);
          sandbox.onLinear(100.0, 38.0, 0.0, 1200);
          sandbox.onLinear(-20.0, 38.0, 0.0, 1200);
        }
        if (typeof sandbox.onRapid === "function") sandbox.onRapid(-20.0, 38.0, 15.0);
      }
    },
    {
      comment: "5. OP20 (2. AUFSPANNUNG G55): RUECKSEITEN-AUSSENKONTUR ENTGRATEN",
      tool: mockTools[0],
      spindleSpeed: 8000,
      workOffset: 2, // 2 -> G55
      initialPos: { x: 0.0, y: 0.0, z: 15.0 },
      zMin: -1.0,
      zMax: 15.0,
      runMoves: function (sandbox) {
        if (typeof sandbox.onRapid === "function") sandbox.onRapid(0.0, 0.0, 2.0);
        if (typeof sandbox.onLinear === "function") {
          sandbox.onLinear(0.0, 0.0, -1.0, 500);
          sandbox.onLinear(80.0, 0.0, -1.0, 1200);
          sandbox.onLinear(80.0, 50.0, -1.0, 1200);
          sandbox.onLinear(0.0, 50.0, -1.0, 1200);
          sandbox.onLinear(0.0, 0.0, -1.0, 1200);
        }
        if (typeof sandbox.onRapid === "function") sandbox.onRapid(0.0, 0.0, 15.0);
      }
    }
  );
}

// Für Übung 11 (Gewindebohren G84 / Rigid Tapping M8x1.25) fügen wir die Gewindebohr-Operation mit T03 hinzu:
if (exerciseName.indexOf("uebung_11") !== -1) {
  var tapTool = mockTools.find(function (t) { return t.number === 3; }) || {
    number: 3,
    diameter: 8.0,
    cornerRadius: 0.0,
    lengthOffset: 3,
    diameterOffset: 3,
    threadPitch: 1.25,
    description: "GEWINDEBOHRER M8 (P=1.25MM)",
    comment: "GEWINDEBOHRER M8 (P=1.25MM)",
    spindleRPM: 600,
    clockwise: true,
    coolant: 1
  };

  mockSections.push({
    comment: "4. GEWINDEBOHREN 4X M8 - G84 SYNCHRONES GEWINDEBOHREN (RIGID TAPPING)",
    tool: tapTool,
    spindleSpeed: 600,
    workOffset: 1,
    initialPos: { x: 10.0, y: 10.0, z: 15.0 },
    zMin: -10.0,
    zMax: 15.0,
    runMoves: function (sandbox) {
      sandbox.cycleType = "tapping";
      sandbox.cycle = { feedrate: 750, retract: 2.0, clearance: 15.0 };
      sandbox.cycleExpanded = false;
      sandbox._firstCycle = true;
      if (typeof sandbox.onCycle === "function") sandbox.onCycle();
      if (typeof sandbox.onCyclePoint === "function") {
        sandbox.onCyclePoint(10.0, 10.0, -10.0);
        sandbox._firstCycle = false;
        sandbox.onCyclePoint(70.0, 10.0, -10.0);
        sandbox.onCyclePoint(70.0, 40.0, -10.0);
        sandbox.onCyclePoint(10.0, 40.0, -10.0);
      }
      if (typeof sandbox.onCycleEnd === "function") sandbox.onCycleEnd();
      if (typeof sandbox.onRapid === "function") sandbox.onRapid(10.0, 40.0, 15.0);
    }
  });
}

// Für Übung 13 (3D-Freiformflächen & Kugelfräser-Schlichten) konfigurieren wir T02 als echten Kugelfräser und erzeugen simultane 3D-Zeilenschlichtbahnen:
if (exerciseName.indexOf("uebung_13") !== -1) {
  mockTools[1] = {
    number: 2,
    diameter: 6.0,
    cornerRadius: 3.0, // R = D/2 = 3.0 mm (Vollradius / Kugelfräser)
    type: 3, // TOOL_MILLING_END_BALL
    lengthOffset: 2,
    diameterOffset: 2,
    description: "KUGELFRAESER 6MM VHM (3D FREIFORM)",
    comment: "KUGELFRAESER 6MM VHM (3D FREIFORM)",
    spindleRPM: 10000,
    clockwise: true,
    coolant: 1
  };

  mockSections.length = 0; // Standard-Abschnitte leeren

  // Op 1: Schruppen / Adaptive Vorräumung der Außenkontur mit T01 Schaftfräser
  mockSections.push({
    comment: "1. 3D ADAPTIVE CLEARING - VORRAEUMUNG DER KONTUR (SCHAFTFRAESER D=10MM)",
    tool: mockTools[0],
    spindleSpeed: 8000,
    workOffset: 1,
    initialPos: { x: -10.0, y: -10.0, z: 15.0 },
    zMin: -5.0,
    zMax: 15.0,
    runMoves: function (sandbox) {
      if (typeof sandbox.onRapid === "function") sandbox.onRapid(-10.0, -10.0, 2.0);
      if (typeof sandbox.onLinear === "function") {
        sandbox.onLinear(-10.0, -10.0, -5.0, 500);
        sandbox.onLinear(-5.0, -5.0, -5.0, 1200);
        sandbox.onLinear(85.0, -5.0, -5.0, 1200);
        sandbox.onLinear(85.0, 55.0, -5.0, 1200);
        sandbox.onLinear(-5.0, 55.0, -5.0, 1200);
        sandbox.onLinear(-5.0, -5.0, -5.0, 1200);
      }
      if (typeof sandbox.onRapid === "function") sandbox.onRapid(-5.0, -5.0, 15.0);
    }
  });

  // Op 2: 3D-Freiformflächen-Schlichten mit T02 Kugelfräser D=6mm (Simultane 3D-Zeilen X/Y/Z)
  mockSections.push({
    comment: "2. 3D FREIFORMFLAECHEN SCHLICHTEN - KUGELFRAESER D=6MM (SIMULTANE 3D-BAHNEN)",
    tool: mockTools[1],
    spindleSpeed: 10000,
    workOffset: 1,
    initialPos: { x: 20.0, y: 15.0, z: 15.0 },
    zMin: -4.8,
    zMax: 15.0,
    runMoves: function (sandbox) {
      if (typeof sandbox.onRapid === "function") sandbox.onRapid(20.0, 15.0, 2.0);
      if (typeof sandbox.onLinear === "function") {
        // Eintauchen auf Start-Freiformhöhe
        sandbox.onLinear(20.0, 15.0, -2.0, 600);

        // Zeile 1: Y = 15.0 (3D-Welle simultan X/Y/Z)
        sandbox.onLinear(28.0, 15.0, -3.2, 1500);
        sandbox.onLinear(36.0, 15.0, -4.2, 1500);
        sandbox.onLinear(44.0, 15.0, -4.2, 1500);
        sandbox.onLinear(52.0, 15.0, -3.2, 1500);
        sandbox.onLinear(60.0, 15.0, -2.0, 1500);

        // Quer-Zustellung zu Zeile 2
        sandbox.onLinear(60.0, 20.0, -2.0, 1500);

        // Zeile 2: Y = 20.0 (Rückweg 3D-Welle simultan X/Y/Z)
        sandbox.onLinear(52.0, 20.0, -3.5, 1500);
        sandbox.onLinear(44.0, 20.0, -4.6, 1500);
        sandbox.onLinear(36.0, 20.0, -4.6, 1500);
        sandbox.onLinear(28.0, 20.0, -3.5, 1500);
        sandbox.onLinear(20.0, 20.0, -2.0, 1500);

        // Quer-Zustellung zu Zeile 3
        sandbox.onLinear(20.0, 25.0, -2.0, 1500);

        // Zeile 3: Y = 25.0 (Tiefster Scheitelpunkt Z-4.8mm)
        sandbox.onLinear(28.0, 25.0, -3.8, 1500);
        sandbox.onLinear(36.0, 25.0, -4.8, 1500);
        sandbox.onLinear(44.0, 25.0, -4.8, 1500);
        sandbox.onLinear(52.0, 25.0, -3.8, 1500);
        sandbox.onLinear(60.0, 25.0, -2.0, 1500);

        // Quer-Zustellung zu Zeile 4
        sandbox.onLinear(60.0, 30.0, -2.0, 1500);

        // Zeile 4: Y = 30.0 (Rückweg)
        sandbox.onLinear(52.0, 30.0, -3.5, 1500);
        sandbox.onLinear(44.0, 30.0, -4.6, 1500);
        sandbox.onLinear(36.0, 30.0, -4.6, 1500);
        sandbox.onLinear(28.0, 30.0, -3.5, 1500);
        sandbox.onLinear(20.0, 30.0, -2.0, 1500);

        // Quer-Zustellung zu Zeile 5
        sandbox.onLinear(20.0, 35.0, -2.0, 1500);

        // Zeile 5: Y = 35.0 (Auslauf-Zeile)
        sandbox.onLinear(28.0, 35.0, -3.2, 1500);
        sandbox.onLinear(36.0, 35.0, -4.2, 1500);
        sandbox.onLinear(44.0, 35.0, -4.2, 1500);
        sandbox.onLinear(52.0, 35.0, -3.2, 1500);
        sandbox.onLinear(60.0, 35.0, -2.0, 1500);
      }
      if (typeof sandbox.onRapid === "function") sandbox.onRapid(60.0, 35.0, 15.0);
    }
  });
}

// Für Übung 14 (Heidenhain Klartext & 4. Drehachse A-Achse / Teilapparat):
if (exerciseName.indexOf("uebung_14") !== -1) {
  mockTools[0] = {
    number: 1,
    diameter: 10.0,
    cornerRadius: 0.0,
    lengthOffset: 1,
    diameterOffset: 1,
    description: "VHM-SCHAFTFRAESER D=10MM (SCHLUESSELFLAECHEN A+0 / A+90)",
    comment: "VHM-SCHAFTFRAESER D=10MM",
    spindleRPM: 8000,
    clockwise: true,
    coolant: 1
  };
  mockTools[1] = {
    number: 2,
    diameter: 6.0,
    cornerRadius: 0.0,
    lengthOffset: 2,
    diameterOffset: 2,
    description: "VHM-SPIRALBOHRER D=6MM (QUERBOHRUNGEN BIS Z-12MM)",
    comment: "VHM-SPIRALBOHRER D=6MM",
    spindleRPM: 3500,
    clockwise: true,
    coolant: 1
  };

  mockSections.length = 0; // Standard-Abschnitte leeren

  // Op 1: 2D-Außenkontur / Schlüsselfläche 1 bei A = 0°
  mockSections.push({
    comment: "1. KONTURFRAESEN / SCHLUESSELFLAECHE 1 (A+0 GRAD)",
    tool: mockTools[0],
    spindleSpeed: 8000,
    workOffset: 1,
    initialPos: { x: -10.0, y: -10.0, z: 15.0 },
    zMin: -5.0,
    zMax: 15.0,
    runMoves: function (sandbox) {
      if (typeof sandbox.onRapid === "function") sandbox.onRapid(-10.0, -10.0, 2.0);
      if (typeof sandbox.onLinear === "function") {
        sandbox.onLinear(-10.0, -10.0, -5.0, 500);
        sandbox.onLinear(0.0, 0.0, -5.0, 1200);
        sandbox.onLinear(80.0, 0.0, -5.0, 1200);
        sandbox.onLinear(80.0, 50.0, -5.0, 1200);
        sandbox.onLinear(0.0, 50.0, -5.0, 1200);
        sandbox.onLinear(0.0, 0.0, -5.0, 1200);
      }
      if (typeof sandbox.onRapid === "function") sandbox.onRapid(0.0, 0.0, 15.0);
    }
  });

  // Op 2: Schlüsselfläche 2 / Längsnut bei A = 90° (Teilapparat geschwenkt)
  mockSections.push({
    comment: "2. SCHLUESSELFLAECHE 2 / LAENGSEINSCHNITT (A+90 GRAD)",
    tool: mockTools[0],
    spindleSpeed: 8000,
    workOffset: 1,
    initialPos: { x: 40.0, y: 25.0, z: 15.0 },
    zMin: -3.0,
    zMax: 15.0,
    runMoves: function (sandbox) {
      if (typeof sandbox.onRapid === "function") sandbox.onRapid(40.0, 25.0, 2.0);
      if (typeof sandbox.onLinear === "function") {
        sandbox.onLinear(40.0, 25.0, -3.0, 400);
        sandbox.onLinear(55.0, 25.0, -3.0, 1000);
        sandbox.onLinear(40.0, 25.0, -3.0, 1000);
      }
      if (typeof sandbox.onRapid === "function") sandbox.onRapid(40.0, 25.0, 15.0);
    }
  });

  // Op 3: 4x Querbohrungen D=6mm bei A = 90° mit Bohrzyklus CYCL DEF 200 bis Z-12.0mm
  mockSections.push({
    comment: "3. VIER QUERBOHRUNGEN D=6MM (A+90 GRAD) - CYCL DEF 200 BOHREN BIS Z-12MM",
    tool: mockTools[1],
    spindleSpeed: 3500,
    workOffset: 1,
    initialPos: { x: 10.0, y: 10.0, z: 15.0 },
    zMin: -12.0,
    zMax: 15.0,
    runMoves: function (sandbox) {
      sandbox.cycleType = "drilling";
      sandbox.cycle = { feedrate: 300, retract: 2.0, clearance: 15.0, bottom: -12.0 };
      sandbox.cycleExpanded = false;
      sandbox._firstCycle = true;
      if (typeof sandbox.onCycle === "function") sandbox.onCycle();
      if (typeof sandbox.onCyclePoint === "function") {
        sandbox.onCyclePoint(10.0, 10.0, -12.0);
        sandbox._firstCycle = false;
        sandbox.onCyclePoint(70.0, 10.0, -12.0);
        sandbox.onCyclePoint(70.0, 40.0, -12.0);
        sandbox.onCyclePoint(10.0, 40.0, -12.0);
      }
      if (typeof sandbox.onCycleEnd === "function") sandbox.onCycleEnd();
      if (typeof sandbox.onRapid === "function") sandbox.onRapid(10.0, 40.0, 15.0);
    }
  });
}

function wrapSection(sec) {
  return {
    workOffset: sec.workOffset,
    getTool: () => sec.tool,
    getInitialPosition: () => sec.initialPos,
    getForceToolChange: () => false,
    hasParameter: (paramName) => paramName === "operation-comment" && !!sec.comment,
    getParameter: (paramName) => (paramName === "operation-comment" ? sec.comment : ""),
    getGlobalZRange: () => ({
      getMinimum: () => sec.zMin,
      getMaximum: () => sec.zMax
    })
  };
}

// Autodesk Post-API Sandbox-Umgebung (Simulierte Laufzeitumgebung) aufbauen
let currentSecIndex = 0;

const sandbox = {
  MM: 1,
  IN: 0,
  unit: 1, // 1 = MM (Millimeter)
  CAPABILITY_MILLING: 1,
  TOOL_MILLING_END_FLAT: 1,
  TOOL_MILLING_END_BALL: 3,
  COOLANT_OFF: 0,
  PLANE_XY: 0,
  X: 0,
  Y: 1,
  Z: 2,
  programName: "1001",
  programComment: "CNC FERTIGUNGSPROGRAMM - MUSTERBAUTEIL",
  properties: {},
  tool: mockTools[0],
  spindleSpeed: 8000,
  currentSection: wrapSection(mockSections[0]),
  cycle: {},
  cycleType: "",
  cycleExpanded: false,
  _currentPos: { x: 0, y: 0, z: 15 },
  _firstCycle: true,

  setCodePage: function () {},
  spatial: function (val) { return val; },
  toRad: function (deg) { return (deg * Math.PI) / 180; },

  createFormat: function (spec) {
    return makeFormatter(spec);
  },

  createVariable: function (spec, formatter) {
    spec = spec || {};
    const prefix = spec.prefix || "";
    const force = !!spec.force;
    const onchange = spec.onchange;
    let lastVal = undefined;
    return {
      format: function (val) {
        if (val === undefined || val === null) return "";
        const formatted = formatter ? formatter.format(val) : String(val);
        if (!force && formatted === lastVal) {
          return "";
        }
        if (formatted !== lastVal && typeof onchange === "function") {
          onchange();
        }
        lastVal = formatted;
        return prefix + formatted;
      },
      reset: function () {
        lastVal = undefined;
      }
    };
  },

  createReferenceVariable: function (spec, formatter) {
    spec = spec || {};
    const prefix = spec.prefix || "";
    return {
      format: function (val) {
        if (val === undefined || val === null) return "";
        return prefix + (formatter ? formatter.format(val) : String(val));
      },
      reset: function () {}
    };
  },

  createModal: function (spec, formatter) {
    spec = spec || {};
    const onchange = spec.onchange;
    let lastVal = undefined;
    return {
      format: function (val) {
        const formatted = formatter ? formatter.format(val) : String(val);
        if (formatted === lastVal) return "";
        if (typeof onchange === "function") onchange();
        lastVal = formatted;
        return formatted;
      },
      reset: function () {
        lastVal = undefined;
      }
    };
  },

  getProperty: function (name) {
    if (sandbox.properties && sandbox.properties[name] !== undefined) {
      const prop = sandbox.properties[name];
      return prop && typeof prop === "object" && "value" in prop ? prop.value : prop;
    }
    return undefined;
  },

  filterText: function (text, allowed) {
    let res = "";
    for (let i = 0; i < text.length; i++) {
      if (allowed.indexOf(text[i]) !== -1) res += text[i];
    }
    return res;
  },

  writeln: function (str) {
    outputLines.push(String(str !== undefined ? str : ""));
  },

  writeComment: function (text) {
    outputLines.push("(" + String(text !== undefined ? text : "").toUpperCase() + ")");
  },

  writeBlock: function () {
    const words = [];
    for (let i = 0; i < arguments.length; i++) {
      const arg = arguments[i];
      if (Array.isArray(arg)) {
        arg.forEach(a => { if (a !== undefined && a !== "") words.push(a); });
      } else if (arg !== undefined && arg !== "") {
        words.push(arg);
      }
    }
    if (words.length > 0) outputLines.push(words.join(" "));
  },

  writeWords: function () {
    const words = [];
    for (let i = 0; i < arguments.length; i++) {
      const arg = arguments[i];
      if (Array.isArray(arg)) {
        arg.forEach(a => { if (a !== undefined && a !== "") words.push(a); });
      } else if (arg !== undefined && arg !== "") {
        words.push(arg);
      }
    }
    if (words.length > 0) outputLines.push(words.join(" "));
  },

  writeWords2: function (prefixWord, args) {
    const words = [prefixWord];
    for (let i = 0; i < args.length; i++) {
      const a = args[i];
      if (a !== undefined && a !== "") words.push(a);
    }
    if (words.length > 1) outputLines.push(words.join(" "));
  },

  getToolTable: function () {
    return {
      getNumberOfTools: () => mockTools.length,
      getTool: (idx) => mockTools[idx]
    };
  },

  getNumberOfSections: function () {
    return mockSections.length;
  },

  getSection: function (idx) {
    return wrapSection(mockSections[idx]);
  },

  isFirstSection: function () {
    return currentSecIndex === 0;
  },

  getPreviousSection: function () {
    return wrapSection(mockSections[Math.max(0, currentSecIndex - 1)]);
  },

  hasParameter: function (paramName) {
    return paramName === "operation-comment";
  },

  getParameter: function (paramName) {
    if (paramName === "operation-comment") {
      return mockSections[currentSecIndex].comment;
    }
    return "";
  },

  getFramePosition: function (pos) {
    return pos;
  },

  getCurrentPosition: function () {
    return sandbox._currentPos;
  },

  getCircularPlane: function () {
    return sandbox.PLANE_XY;
  },

  linearize: function () {},

  isFirstCyclePoint: function () {
    return sandbox._firstCycle;
  },

  repositionToCycleClearance: function () {},
  expandCyclePoint: function () {},
  invalidate: function () {},
  onRapid: function () {},
  onLinear: function () {},
  onCircular: function () {},
  onCycle: function () {},
  onCyclePoint: function () {},
  onCycleEnd: function () {},
  Date: Date,
  Math: Math,
  String: String,
  Number: Number,
  parseInt: parseInt
};

// 1. Lade src/mein_erster_post.cps und führe ihn in der Sandbox aus
const cpsCode = fs.readFileSync(cpsPath, "utf8");
vm.createContext(sandbox);
vm.runInContext(cpsCode, sandbox, { filename: "mein_erster_post.cps" });

// 2. Starte den Lebenszyklus des Postprozessors (onOpen -> alle Sections -> onClose)
if (typeof sandbox.onOpen === "function") {
  sandbox.onOpen();
}

for (let i = 0; i < mockSections.length; i++) {
  currentSecIndex = i;
  const sec = mockSections[i];
  sandbox.currentSection = wrapSection(sec);
  sandbox.tool = sec.tool;
  sandbox.spindleSpeed = sec.spindleSpeed;
  if (typeof sandbox.onSection === "function") {
    sandbox.onSection();
  }
  sec.runMoves(sandbox);
  if (typeof sandbox.onSectionEnd === "function") {
    sandbox.onSectionEnd();
  }
}

if (typeof sandbox.onClose === "function") {
  sandbox.onClose();
}

// 3. Speichere den frisch generierten G-Code sowohl direkt bei der Übung als auch im tests-Ordner
const finalGCode = outputLines.join("\n") + "\n";
fs.writeFileSync(directNcPath, finalGCode, "utf8");



console.log("==================================================================");
console.log("✅ POSTPROZESSOR ERFOLGREICH AUSGEFÜHRT (" + path.basename(cpsPath) + ")");
console.log("📄 Direkt bei Ihrer Übung       : " + path.relative(process.cwd(), directNcPath));


console.log("==================================================================\n");
console.log(finalGCode);

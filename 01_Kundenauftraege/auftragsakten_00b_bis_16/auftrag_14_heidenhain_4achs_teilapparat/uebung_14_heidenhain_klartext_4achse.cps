/**
 * Übung 14: Heidenhain Klartext-Ausgabe & 4. Drehachse (A-Achse mit Klemmung M10/M11)
 * Ziel: Vollständige Ausgabe im echten Heidenhain Klartext (.h Datei) mit TOOL CALL, L X Y FMAX M3 und A-Achsen-Drehung.
 */

description = "Uebung 14 - Heidenhain Klartext & 4. Achse";
vendor = "CNC Lernprojekt";
certificationLevel = 2;
extension = "h"; // Heidenhain Dateiendung ist .h
setCodePage("ascii");
capabilities = CAPABILITY_MILLING;
tolerance = spatial(0.002, MM);

var xyzFormat = createFormat({decimals:(unit == MM ? 3 : 4), forceDecimal:true});
var lineNum = 0;

function writeHhLine() {
  var words = [lineNum];
  for (var i = 0; i < arguments.length; i++) {
    if (arguments[i] !== undefined && arguments[i] !== "") {
      words.push(arguments[i]);
    }
  }
  writeln(words.join(" "));
  lineNum++;
}

function onOpen() {
  lineNum = 0;
  // BEGIN PGM ... MM = Programmstart bei Heidenhain im metrischen System (Millimeter)
  writeHhLine("BEGIN PGM UEBUNG_14 MM");
}

function onSection() {
  // TOOL CALL <Nr> Z S<Drehzahl> = Werkzeugaufruf im Heidenhain-Klartext
  // tool.number = Werkzeugplatz
  // Z = Werkzeugachse (Spindelachse)
  // S = Spindeldrehzahl in U/min
  writeHhLine("TOOL CALL", tool.number, "Z", "S" + spindleSpeed);

  // 4. Achse (A-Achse Teilapparat) ansteuern falls vorhanden:
  // M11 = A-Achsen-Klemmung/Bremse LÖSEN (Entklemmen vor Rotation)
  writeHhLine("M11");

  // L = Linear-Satz (Lineare Verfahrbewegung)
  // A+90.000 = Drehachse um 90 Grad drehen
  // FMAX = Eilgang / Maximaler Maschinenvorschub bei Heidenhain
  writeHhLine("L", "A+90.000", "FMAX");

  // M10 = A-Achsen-Klemmung FESTKLEMMEN (hydraulische/pneumatische Bremse aktiv gegen Schnittkräfte)
  writeHhLine("M10");

  // Erste Anfahrt in XY:
  // R0 = Fräserradiuskorrektur AUS (Werkzeug fährt mit Fräsermitte)
  // M3 = Spindel im Uhrzeigersinn (Rechtslauf) / M4 = Spindel gegen Uhrzeigersinn (Linkslauf)
  writeHhLine("L", "X+0.000", "Y+0.000", "R0", "FMAX", tool.clockwise ? "M3" : "M4");

  // Anfahrt in Z auf 2 mm Sicherheitshöhe mit Kühlschmiermittel:
  // M8 = Kühlmittelpumpe EIN (KSS an)
  writeHhLine("L", "Z+2.000", "R0", "FMAX", "M8");
}

function onLinear(x, y, z, feed) {
  // L = Linearer Vorschubsatz im Material
  // R0 = Radiuskorrektur aus
  // F = Arbeitsvorschub in mm/min
  writeHhLine("L", "X" + (x >= 0 ? "+" : "") + xyzFormat.format(x), "Y" + (y >= 0 ? "+" : "") + xyzFormat.format(y), "Z" + (z >= 0 ? "+" : "") + xyzFormat.format(z), "R0", "F" + feed);
}

function onClose() {
  // Z+100.000 R0 FMAX M9 = Im Eilgang FMAX senkrecht auf Z+100 mm hochfahren und Kühlmittel ausschalten (M9)
  writeHhLine("L", "Z+100.000", "R0", "FMAX", "M9");

  // M30 = Hauptprogramm-Ende und Rücksprung
  writeHhLine("M30");

  // END PGM ... MM = Offizielles Programmende nach Heidenhain Klartext-Syntax
  writeHhLine("END PGM UEBUNG_14 MM");
}

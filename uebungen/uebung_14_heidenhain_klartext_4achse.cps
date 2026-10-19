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
  writeHhLine("BEGIN PGM UEBUNG_14 MM");
}

function onSection() {
  // Werkzeugaufruf im Heidenhain-Format
  writeHhLine("TOOL CALL", tool.number, "Z", "S" + spindleSpeed);

  // 4. Achse (A-Achse) ansteuern falls vorhanden:
  writeHhLine("M11"); // A-Achse Bremse lösen (Entklemmen)
  writeHhLine("L", "A+90.000", "FMAX"); // Drehung auf 90 Grad
  writeHhLine("M10"); // A-Achse Bremse festklemmen

  // Erste Anfahrt
  writeHhLine("L", "X+0.000", "Y+0.000", "R0", "FMAX", tool.clockwise ? "M3" : "M4");
  writeHhLine("L", "Z+2.000", "R0", "FMAX", "M8");
}

function onLinear(x, y, z, feed) {
  writeHhLine("L", "X" + (x >= 0 ? "+" : "") + xyzFormat.format(x), "Y" + (y >= 0 ? "+" : "") + xyzFormat.format(y), "Z" + (z >= 0 ? "+" : "") + xyzFormat.format(z), "R0", "F" + feed);
}

function onClose() {
  writeHhLine("L", "Z+100.000", "R0", "FMAX", "M9");
  writeHhLine("M30");
  writeHhLine("END PGM UEBUNG_14 MM");
}

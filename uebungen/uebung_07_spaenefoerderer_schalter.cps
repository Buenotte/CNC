/**
 * Übung 07: Eigener M-Code Schalter (Property) für Späneförderer (M31/M33)
 * Ziel: In den Einstellungen per Checkbox den Späneförderer automatisch ein- und ausschalten.
 */

description = "Uebung 07 - Spaenefoerderer M31/M33 Schalter";
vendor = "CNC Lernprojekt";
certificationLevel = 2;
extension = "nc";
setCodePage("ascii");
capabilities = CAPABILITY_MILLING;
tolerance = spatial(0.002, MM);

properties = {
  useChipConveyor: {
    title: "Späneförderer automatisch steuern (Use Chip Conveyor)",
    description: "Startet M31 bei onOpen() und stoppt M33 bei onClose()",
    type: "boolean",
    value: true,
    scope: "post"
  }
};

function onOpen() {
  writeln("%");
  writeln("O1007 (UEBUNG 07 - SPAENEFOERDERER SCHALTER)");
  writeWords("G90", "G21", "G17", "G40", "G80");

  if (getProperty("useChipConveyor")) {
    writeln("(SPAENEFOERDERER AUTOMATISCH STARTEN)");
    writeWords("M31");
  }
}

function onClose() {
  writeln("");
  writeWords("M09");
  writeWords("G53", "G00", "Z0.0");
  writeWords("M05");

  if (getProperty("useChipConveyor")) {
    writeln("(SPAENEFOERDERER STOPPEN)");
    writeWords("M33");
  }

  writeWords("G53", "G00", "Y0.0");
  writeWords("M30");
  writeln("%");
}

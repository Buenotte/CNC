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

  // Sicherheits-Startblock:
  // G90 = Absolutmaß (Bezug auf Werkstück-Nullpunkt G54)
  // G21 = Metrisches Maßsystem (Millimeter)
  // G17 = Fräsebene XY
  // G40 = Fräserradiuskorrektur ausschalten
  // G80 = Bohrzyklen abbrechen
  writeWords("G90", "G21", "G17", "G40", "G80");

  if (getProperty("useChipConveyor")) {
    writeln("(SPAENEFOERDERER AUTOMATISCH STARTEN)");
    // M31 = Späneförderer (Förderschnecke / Transportband) VORWÄRTS STARTEN
    writeWords("M31");
  }
}

function onClose() {
  writeln("");
  // M09 = Kühlschmierstoff (KSS) ausschalten
  writeWords("M09");

  // G53 = Maschinen-Koordinatensystem
  // G00 = Eilgang (Schnellgang ohne Spanabtrag)
  // Z0.0 = Spindel ganz nach oben fahren
  writeWords("G53", "G00", "Z0.0");

  // M05 = Frässpindel ausschalten (Spindel-Stopp)
  writeWords("M05");

  if (getProperty("useChipConveyor")) {
    writeln("(SPAENEFOERDERER STOPPEN)");
    // M33 = Späneförderer STOPP
    writeWords("M33");
  }

  // G53 G00 Y0.0 = Maschinentisch ganz nach vorne fahren
  writeWords("G53", "G00", "Y0.0");

  // M30 = Hauptprogrammende, Rücklauf und Speicher-Reset
  writeWords("M30");
  writeln("%");
}

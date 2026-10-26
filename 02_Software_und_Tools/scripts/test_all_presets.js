const fs = require('fs');
const content = fs.readFileSync('02_Software_und_Tools/web_tools/3d_auftrag_simulator.html', 'utf8');

// Teste alle Presets durch
const gcodeLinesKundenauftrag = [];
const gcodeLinesUebung00b = [];
let PRESET_GCODES;
eval(content.match(/PRESET_GCODES = \{[\s\S]*?\n    \};/)[0]);
let centerOffset = { x: 40, y: 25, z: -4 };
eval(content.match(/function parseGCodeToSimulation[\s\S]*?\n    \}/)[0]);

for (const [key, code] of Object.entries(PRESET_GCODES)) {
  try {
    const res = parseGCodeToSimulation(code, key);
    console.log(`Preset [${key}]: lines=${res.lines.length}, waypoints=${res.waypoints.length}`);
    for (let w = 0; w < res.waypoints.length; w++) {
      const wp = res.waypoints[w];
      if (!wp) console.error(`  wp[${w}] is null/undefined!`);
      else if (!wp.tool) console.error(`  wp[${w}] has NO TOOL property!`, wp);
    }
  } catch (err) {
    console.error(`Error parsing preset [${key}]:`, err);
  }
}

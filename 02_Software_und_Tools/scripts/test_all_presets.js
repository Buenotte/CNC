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


// Vollstaendiger Laufzeit-Test (Full Script Runtime & Render Check) inkl. .nc Datei-Upload
const fullScript = content.match(/<script>([\s\S]*?)<\/script>/)[1];
const mockCtx = {
  clearRect(){}, beginPath(){}, setLineDash(){}, moveTo(){}, lineTo(){}, stroke(){},
  save(){}, restore(){}, measureText(){ return { width: 50 }; }, roundRect(){}, fill(){}, fillRect(){}, fillText(){}
};
const els = {};
function getEl(id) {
  if (!els[id]) {
    els[id] = {
      id, style: {}, classList: { add(){}, remove(){} },
      addEventListener(){}, appendChild(){}, scrollIntoView(){},
      getContext(){ return mockCtx; }, getBoundingClientRect(){ return { left:0, top:0 }; },
      clientWidth: 800, clientHeight: 600, width: 800, height: 600, options: [{text:'Test'}], selectedIndex: 0
    };
  }
  return els[id];
}
global.window = { devicePixelRatio: 1, innerWidth: 1200, addEventListener(){} };
global.document = {
  getElementById: getEl,
  createElement: (tag) => getEl('dyn_' + Math.random()),
  body: { style: {} }
};
let frameCount = 0;
global.requestAnimationFrame = () => {};

const ncSample = fs.readFileSync('03_Fachdokumentation_und_Wissen/uebungen/uebung_10_zweite_aufspannung_g55.nc', 'utf8');
eval(
  fullScript +
  '\nloadGCodeText(ncSample, "uebung_10_zweite_aufspannung_g55.nc", true);' +
  '\nfor (let i = 0; i < 1200; i++) { frameCount = 0; render(); }' +
  '\nconsole.log("FULL RENDER TEST OK! Waypoints:", waypoints.length, "Progress:", progress.toFixed(1), "PartFlipDeg:", Math.round(partFlipAngle * 180 / Math.PI));'
);

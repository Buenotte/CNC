const fs = require('fs');
const content = fs.readFileSync('kundenauftrag_01_flanschplatte/3d_auftrag_simulator.html', 'utf8');

const scriptMatch = content.match(/<script>([\s\S]*?)<\/script>/)[1];

// Simuliere Browser-Umgebung
const dom = {
  createElement: () => ({
    style: {},
    classList: { add: () => {}, remove: () => {} },
    title: '',
    onclick: null,
    textContent: '',
    appendChild: () => {}
  }),
  getElementById: (id) => ({
    textContent: '',
    style: {},
    classList: { add: () => {}, remove: () => {} },
    innerHTML: '',
    appendChild: () => {},
    scrollIntoView: () => {},
    clientWidth: 1200,
    clientHeight: 800,
    addEventListener: () => {},
    getContext: () => ({
      clearRect: () => {},
      beginPath: () => {},
      setLineDash: () => {},
      moveTo: () => {},
      lineTo: () => {},
      stroke: () => {},
      measureText: () => ({ width: 50 }),
      fillText: () => {},
      fillRect: () => {},
      save: () => {},
      restore: () => {}
    })
  }),
  addEventListener: () => {},
  clientWidth: 1200,
  clientHeight: 800,
  getContext: () => ({
    clearRect: () => {},
    beginPath: () => {},
    setLineDash: () => {},
    moveTo: () => {},
    lineTo: () => {},
    stroke: () => {},
    measureText: () => ({ width: 50 }),
    fillText: () => {},
    fillRect: () => {},
    save: () => {},
    restore: () => {}
  })
};

const window = {
  devicePixelRatio: 1,
  addEventListener: () => {},
  innerWidth: 1200,
  innerHeight: 800
};
const document = dom;

let requestAnimationFrameCount = 0;
function requestAnimationFrame(cb) {
  if (requestAnimationFrameCount++ < 5) cb();
}

try {
  eval(scriptMatch);
  console.log('Simulator script executed without error!');
  console.log('Default waypoints length:', waypoints.length);
  
  // Jetzt parse uebungen/uebung_03_z_min_berechnung.nc
  const nc = fs.readFileSync('uebungen/uebung_03_z_min_berechnung.nc', 'utf8');
  const res = parseGCodeToSimulation(nc, 'Uebung 03');
  console.log('Parsed uebung 03 lines:', res.lines.length);
  console.log('Parsed uebung 03 waypoints:', res.waypoints.length);
  console.log('Waypoints summary:', res.waypoints);
} catch (e) {
  console.error('Error running simulator script:', e);
}

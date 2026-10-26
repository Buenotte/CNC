const fs = require('fs');
const content = fs.readFileSync('02_Software_und_Tools/web_tools/3d_auftrag_simulator.html', 'utf8');

const idsInHtml = new Set();
const idRegex = /id="([^"]+)"/g;
let m;
while ((m = idRegex.exec(content)) !== null) {
  idsInHtml.add(m[1]);
}

const getElemRegex = /document\.getElementById\("([^"]+)"\)/g;
const missingIds = [];
while ((m = getElemRegex.exec(content)) !== null) {
  if (!idsInHtml.has(m[1])) {
    missingIds.push(m[1]);
  }
}

console.log('Total IDs found in HTML:', idsInHtml.size);
console.log('Missing IDs called in JS:', missingIds);

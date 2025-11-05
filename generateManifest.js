// generateManifest.js

const fs = require('fs');
const path = require('path');

// Base directory for all webcomics
const BASE_DIR = path.join(__dirname, 'webcomics');
const manifestPath = path.join(BASE_DIR, 'manifest.json');

const manifest = {};

// Scan each series folder
fs.readdirSync(BASE_DIR).forEach(series => {
  const seriesPath = path.join(BASE_DIR, series);
  if (!fs.statSync(seriesPath).isDirectory()) return;

  // Find chapter folders inside the series
  const chapters = fs.readdirSync(seriesPath)
    .filter(f => fs.statSync(path.join(seriesPath, f)).isDirectory())
    .sort();

  if (chapters.length === 0) return;

  manifest[series] = {
    title: series,
    chapters
  };
});

// Write manifest.json
fs.writeFileSync(manifestPath, JSON.stringify(manifest, null, 2));

console.log(`Manifest generated at: ${manifestPath}`);
console.log(JSON.stringify(manifest, null, 2));
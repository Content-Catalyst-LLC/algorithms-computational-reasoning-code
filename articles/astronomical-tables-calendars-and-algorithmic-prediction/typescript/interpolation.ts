const x0 = 10.0, y0 = 1.2;
const x1 = 20.0, y1 = 2.8;
const x = 15.0;
const y = y0 + ((x - x0) / (x1 - x0)) * (y1 - y0);
console.log(`interpolated_y=${y.toFixed(6)}`);

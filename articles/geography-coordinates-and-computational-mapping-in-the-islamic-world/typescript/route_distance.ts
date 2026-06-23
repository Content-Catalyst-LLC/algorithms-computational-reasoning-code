const segments = [12.0, 20.0, 7.5];
const total = segments.reduce((a, b) => a + b, 0);
console.log(`segments=${segments.length}`);
console.log(`total_distance=${total.toFixed(6)}`);

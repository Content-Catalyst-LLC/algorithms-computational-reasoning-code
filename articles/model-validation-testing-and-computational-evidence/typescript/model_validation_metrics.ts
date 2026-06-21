const observed = [33.1, 39.7, 38.8, 39.3, 8.4];
const predicted = [31.92, 31.58, 36.48, 25.30, 11.30];
const errors = observed.map((value, idx) => value - predicted[idx]);
const rmse = Math.sqrt(errors.reduce((acc, err) => acc + err * err, 0) / errors.length);
const mae = errors.reduce((acc, err) => acc + Math.abs(err), 0) / errors.length;
console.log(`rmse=${rmse.toFixed(4)}`);
console.log(`mae=${mae.toFixed(4)}`);

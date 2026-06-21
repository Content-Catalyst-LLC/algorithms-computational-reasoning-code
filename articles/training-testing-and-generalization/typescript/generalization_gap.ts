const trainAccuracy = 0.88;
const testAccuracy = 0.81;
console.log(`generalization_gap=${(trainAccuracy - testAccuracy).toFixed(4)}`);

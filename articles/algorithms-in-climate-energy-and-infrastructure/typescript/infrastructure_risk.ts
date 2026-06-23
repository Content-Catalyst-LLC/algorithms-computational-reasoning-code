const hazard = 0.80;
const exposure = 0.75;
const vulnerability = 0.60;
const risk = hazard * exposure * vulnerability;
console.log(`infrastructure_risk=${risk.toFixed(4)}`);

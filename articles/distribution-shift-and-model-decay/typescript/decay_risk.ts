const inputDrift = 0.31;
const labelDrift = 0.16;
const performanceDecay = 0.10;
const calibrationGap = 0.14;
const subgroupGap = 0.15;
const overrideRate = 0.11;
const score = (inputDrift + labelDrift + performanceDecay + calibrationGap + subgroupGap + overrideRate) / 6.0;
console.log(`decay_risk_score=${score.toFixed(4)}`);

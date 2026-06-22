const validityGap = 0.42;
const missingness = 0.12;
const differentialError = 0.24;
const labelError = 0.08;
const score = (validityGap + missingness + differentialError + labelError) / 4.0;
console.log(`measurement_risk_score=${score.toFixed(4)}`);

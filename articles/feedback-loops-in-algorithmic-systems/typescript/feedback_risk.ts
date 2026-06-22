const amplification = 0.82;
const concentration = 0.76;
const intervention = 0.44;
const drift = 0.28;
const recursiveData = 0.31;
const score = (amplification + concentration + intervention + drift + recursiveData) / 5.0;
console.log(`feedback_risk_score=${score.toFixed(4)}`);

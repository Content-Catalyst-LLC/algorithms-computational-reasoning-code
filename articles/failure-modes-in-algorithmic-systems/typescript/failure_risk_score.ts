const likelihood = 0.42;
const severity = 0.86;
const detectability = 0.38;
const controllability = 0.44;
const failureRisk = likelihood * severity * (1.0 - detectability) * (1.0 - controllability);
console.log(`failure_risk_score=${failureRisk.toFixed(4)}`);

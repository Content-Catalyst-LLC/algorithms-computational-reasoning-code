const errorLikelihood = 0.34;
const severity = 0.92;
const exposure = 0.78;
const contestability = 0.42;
const harmRisk = errorLikelihood * severity * exposure * (1.0 - contestability);
console.log(`harm_risk_score=${harmRisk.toFixed(4)}`);

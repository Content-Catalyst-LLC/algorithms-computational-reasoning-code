const provenanceRisk = 0.66;
const measurementWeakness = 0.58;
const proxyRisk = 0.62;
const remediation = 0.42;
const score = (provenanceRisk + measurementWeakness + proxyRisk + (1.0 - remediation)) / 4.0;
console.log(`historical_risk_score=${score.toFixed(4)}`);

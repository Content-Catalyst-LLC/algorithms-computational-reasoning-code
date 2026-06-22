const proxyGap = 0.38;
const pressure = 0.88;
const gaming = 0.72;
const guardrailPenalty = 1.0;
const score = (proxyGap + pressure + gaming + guardrailPenalty) / 4.0;
console.log(`goodhart_risk_score=${score.toFixed(4)}`);

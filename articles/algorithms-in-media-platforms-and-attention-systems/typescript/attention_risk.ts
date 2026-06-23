const engagementPressure = 0.92;
const creatorImpact = 0.88;
const publicKnowledgeImpact = 0.78;
const userControl = 0.44;
const contestability = 0.42;
const score = (engagementPressure + creatorImpact + publicKnowledgeImpact + (1.0 - userControl) + (1.0 - contestability)) / 5.0;
console.log(`attention_risk_score=${score.toFixed(4)}`);

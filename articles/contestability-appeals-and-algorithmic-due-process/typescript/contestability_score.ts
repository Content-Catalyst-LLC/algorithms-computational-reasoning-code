const notice = 0.70;
const reasons = 0.62;
const evidenceAccess = 0.48;
const humanReview = 0.55;
const correction = 0.52;
const remedy = 0.44;
const score = (notice + reasons + evidenceAccess + humanReview + correction + remedy) / 6.0;
console.log(`contestability_score=${score.toFixed(4)}`);

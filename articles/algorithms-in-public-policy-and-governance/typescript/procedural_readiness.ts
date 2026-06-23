const dueProcess = 0.58;
const transparency = 0.52;
const humanReview = 0.60;
const appealReadiness = 0.54;
const score = (dueProcess + transparency + humanReview + appealReadiness) / 4.0;
console.log(`procedural_readiness_score=${score.toFixed(4)}`);

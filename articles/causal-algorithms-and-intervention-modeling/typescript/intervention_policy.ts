function decision(score: number, threshold: number): string {
  return score >= threshold ? "act" : "monitor";
}

const baseline = 0.42;
const intervention = 0.57;
console.log(`estimated_effect=${(intervention - baseline).toFixed(6)}`);
console.log(`baseline_decision=${decision(0.53, 0.55)}`);
console.log(`new_threshold_decision=${decision(0.53, 0.50)}`);

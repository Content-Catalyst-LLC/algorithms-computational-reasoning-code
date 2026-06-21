function classify(score: number, stakes: string): string {
  if (stakes === "high" && score < 1.0) return "escalate";
  if (score >= 0.8) return "pass";
  return "review";
}
console.log(classify(0.67, "medium"));

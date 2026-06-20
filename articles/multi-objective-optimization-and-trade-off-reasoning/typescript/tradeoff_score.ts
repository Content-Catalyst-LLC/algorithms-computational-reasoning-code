type AlternativeScore = { alternative: string; score: number };
const scores: AlternativeScore[] = [
  { alternative: "A", score: 0.52 },
  { alternative: "B", score: 0.49 },
  { alternative: "C", score: 0.82 },
  { alternative: "D", score: 0.35 }
];
console.log(scores.sort((a, b) => b.score - a.score));

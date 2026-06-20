export function rankingScore(textMatch: number, quality: number, freshness: number, diversityBonus: number, riskPenalty: number): number {
  return 0.36 * textMatch + 0.30 * quality + 0.16 * freshness + 0.14 * diversityBonus - 0.20 * riskPenalty;
}
console.log(rankingScore(0.92, 0.88, 0.60, 0.35, 0.04).toFixed(6));

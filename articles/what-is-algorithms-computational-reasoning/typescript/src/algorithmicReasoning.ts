export type Scenario = {
  name: string;
  representation: number;
  correctness: number;
  governance: number;
  bruteForce: number;
};

export function reasoningScore(scenario: Scenario): number {
  const score =
    0.30 * scenario.representation +
    0.30 * scenario.correctness +
    0.30 * scenario.governance -
    0.10 * scenario.bruteForce;
  return Math.max(0, Math.min(100, score));
}

export const scenarios: Scenario[] = [
  { name: "Brute-force procedure", representation: 40, correctness: 28, governance: 20, bruteForce: 92 },
  { name: "Indexed search design", representation: 62, correctness: 52, governance: 38, bruteForce: 42 },
  { name: "Graph-aware reasoning", representation: 76, correctness: 68, governance: 54, bruteForce: 30 },
  { name: "Governed computational reasoning", representation: 86, correctness: 82, governance: 86, bruteForce: 18 }
];

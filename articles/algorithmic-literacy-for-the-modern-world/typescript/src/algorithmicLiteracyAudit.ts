export type LiteracyCase = {
  name: string;
  transparency: number;
  interpretability: number;
  contestability: number;
  governance: number;
  judgment: number;
};

export function literacySupportScore(item: LiteracyCase): number {
  return 0.22 * item.transparency + 0.22 * item.interpretability + 0.18 * item.contestability + 0.18 * item.governance + 0.20 * item.judgment;
}

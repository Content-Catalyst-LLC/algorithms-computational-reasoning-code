export type AbstractionCase = {
  name: string;
  clarity: number;
  scope: number;
  detail: number;
  interpretation: number;
  governance: number;
};

export function abstractionScore(item: AbstractionCase): number {
  return 0.22 * item.clarity + 0.20 * item.scope + 0.20 * item.detail + 0.23 * item.interpretation + 0.15 * item.governance;
}

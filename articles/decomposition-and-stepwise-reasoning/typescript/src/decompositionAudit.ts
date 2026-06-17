export type DecompositionCase = {
  name: string;
  subproblem: number;
  boundary: number;
  sequencing: number;
  dependencies: number;
  recomposition: number;
};

export function decompositionScore(item: DecompositionCase): number {
  return 0.22 * item.subproblem + 0.20 * item.boundary + 0.18 * item.sequencing + 0.20 * item.dependencies + 0.20 * item.recomposition;
}

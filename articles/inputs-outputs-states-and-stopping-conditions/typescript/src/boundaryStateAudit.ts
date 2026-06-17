export type BoundaryCase = {
  name: string;
  input: number;
  output: number;
  state: number;
  stopping: number;
  failure: number;
};

export function boundaryScore(item: BoundaryCase): number {
  return 0.22 * item.input + 0.22 * item.output + 0.22 * item.state + 0.20 * item.stopping + 0.14 * item.failure;
}

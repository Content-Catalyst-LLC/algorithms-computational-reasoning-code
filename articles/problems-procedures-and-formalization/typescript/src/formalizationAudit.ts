export type FormalizationCase = {
  name: string;
  input: number;
  output: number;
  objective: number;
  assumptions: number;
  governance: number;
};

export function formalizationScore(item: FormalizationCase): number {
  return 0.20 * item.input + 0.20 * item.output + 0.25 * item.objective + 0.20 * item.assumptions + 0.15 * item.governance;
}

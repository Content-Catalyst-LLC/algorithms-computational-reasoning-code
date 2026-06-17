export type LogicCase = {
  name: string;
  rule: number;
  predicate: number;
  trace: number;
  test: number;
  governance: number;
};

export function logicQuality(item: LogicCase): number {
  return 0.24 * item.rule + 0.24 * item.predicate + 0.20 * item.trace + 0.18 * item.test + 0.14 * item.governance;
}

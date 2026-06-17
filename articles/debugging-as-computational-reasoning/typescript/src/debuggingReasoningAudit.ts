export type DebugCase = {
  name: string;
  reproduce: number;
  trace: number;
  isolate: number;
  verify: number;
  regression: number;
};

export function debuggingQuality(item: DebugCase): number {
  return 0.22 * item.reproduce + 0.20 * item.trace + 0.18 * item.isolate + 0.22 * item.verify + 0.18 * item.regression;
}

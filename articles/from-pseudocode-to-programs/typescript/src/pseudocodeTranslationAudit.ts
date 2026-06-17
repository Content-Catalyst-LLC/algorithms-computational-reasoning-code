export type TranslationCase = {
  name: string;
  intent: number;
  control: number;
  edge: number;
  tests: number;
  maintain: number;
};

export function translationQuality(item: TranslationCase): number {
  return 0.22 * item.intent + 0.22 * item.control + 0.18 * item.edge + 0.18 * item.tests + 0.20 * item.maintain;
}

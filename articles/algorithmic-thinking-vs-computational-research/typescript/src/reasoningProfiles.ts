export type ReasoningProfile = {
  name: string;
  step: number;
  decomposition: number;
  control: number;
  testability: number;
  representation: number;
  governance: number;
};

export function algorithmicScore(profile: ReasoningProfile): number {
  return 0.28 * profile.step + 0.24 * profile.decomposition + 0.24 * profile.control + 0.24 * profile.testability;
}

export function computationalScore(profile: ReasoningProfile): number {
  return 0.16 * profile.step + 0.14 * profile.decomposition + 0.14 * profile.control + 0.14 * profile.testability + 0.22 * profile.representation + 0.20 * profile.governance;
}

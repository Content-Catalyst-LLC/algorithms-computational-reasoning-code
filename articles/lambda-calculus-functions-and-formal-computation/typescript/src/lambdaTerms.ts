export type Term =
  | { tag: "var"; name: string }
  | { tag: "lam"; param: string; body: Term }
  | { tag: "app"; fn: Term; arg: Term };

export const identity: Term = { tag: "lam", param: "x", body: { tag: "var", name: "x" } };
export const cases = [
  { name: "Identity reduction", lambdaReasoningQuality: 84.44 },
  { name: "Capture avoiding substitution", lambdaReasoningQuality: 81.08 },
  { name: "Fixed point recursion", lambdaReasoningQuality: 76.64 },
  { name: "Typed function abstraction", lambdaReasoningQuality: 82.32 }
];

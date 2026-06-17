export type VerificationStatus = "proved" | "checked" | "counterexample" | "unknown";
export type FormalMethodsCase = { name: string; formalMethodsQuality: number; status: VerificationStatus };
export const cases: FormalMethodsCase[] = [
  { name: "Verified sorting function", formalMethodsQuality: 81.32, status: "checked" },
  { name: "Protocol model checking", formalMethodsQuality: 80.24, status: "checked" },
  { name: "SMT backed contract check", formalMethodsQuality: 80.04, status: "checked" },
  { name: "Institutional rule verification", formalMethodsQuality: 76.00, status: "unknown" }
];

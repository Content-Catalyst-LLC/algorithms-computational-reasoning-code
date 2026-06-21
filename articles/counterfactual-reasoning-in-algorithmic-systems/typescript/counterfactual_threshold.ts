type Label = "favorable" | "not_favorable";

function label(score: number, threshold: number): Label {
  return score >= threshold ? "favorable" : "not_favorable";
}

const original = label(0.57, 0.62);
const counterfactual = label(0.65, 0.62);
console.log({ original, counterfactual, decisionFlipped: original !== counterfactual });

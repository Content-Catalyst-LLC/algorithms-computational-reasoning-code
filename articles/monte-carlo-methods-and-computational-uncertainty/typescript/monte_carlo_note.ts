type MonteCarloSummary = {
  experiment: string;
  samples: number;
  estimate: number;
  standardError: number;
  interpretation: string;
};

const summary: MonteCarloSummary = {
  experiment: "threshold_risk",
  samples: 10000,
  estimate: 0.18,
  standardError: 0.004,
  interpretation: "Estimated probability under documented assumptions."
};

console.log(summary);

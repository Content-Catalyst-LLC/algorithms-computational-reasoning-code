type RunRecord = {
  dataVersion: string;
  codeVersion: string;
  parameters: Record<string, number | string>;
  environment: string;
  outputs: string[];
};

const run: RunRecord = {
  dataVersion: "synthetic-v1",
  codeVersion: "main",
  parameters: { seed: 101, sampleSize: 1000 },
  environment: "documented-runtime",
  outputs: ["scenario_experiment_summaries.csv"]
};

console.log(JSON.stringify(run, null, 2));

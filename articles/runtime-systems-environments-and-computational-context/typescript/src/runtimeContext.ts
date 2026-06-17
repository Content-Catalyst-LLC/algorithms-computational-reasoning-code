export type RuntimeContext = {
  runtime: string;
  platform: string;
  dependenciesPinned: boolean;
  configurationValidated: boolean;
  observabilityEnabled: boolean;
};
export const context: RuntimeContext = {
  runtime: "TypeScript",
  platform: "browser-or-node",
  dependenciesPinned: true,
  configurationValidated: true,
  observabilityEnabled: true
};

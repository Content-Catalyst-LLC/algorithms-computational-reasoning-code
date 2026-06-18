export type FailureModel="crash"|"omission"|"timing"|"partition"|"restart"|"byzantine"|"operator"|"dependency";
export const majorityQuorum=(n:number)=>Math.floor(n/2)+1;
export const crashFaultTolerance=(n:number)=>Math.floor((n-1)/2);
export const byzantineReplicaRequirement=(f:number)=>3*f+1;

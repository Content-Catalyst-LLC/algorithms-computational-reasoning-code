export type ArrivalModel = "adversarial" | "stochastic" | "random-order" | "prediction-augmented";
export function acceptThreshold(value: number, threshold: number): boolean { return value >= threshold; }
export function queueUtilization(arrivalRate: number, serviceRate: number): number { return arrivalRate / serviceRate; }

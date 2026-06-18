export type StreamingState = "counter" | "sketch" | "sample" | "window";
export function queueUtilization(arrivalRate: number, processingRate: number): number { return arrivalRate / processingRate; }
export function stableQueue(arrivalRate: number, processingRate: number): boolean { return arrivalRate < processingRate; }
export function slidingWindow<T>(items: T[], windowSize: number): T[] { return items.slice(Math.max(0, items.length - windowSize)); }

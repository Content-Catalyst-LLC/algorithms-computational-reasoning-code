export type RetrievalModel = "boolean" | "vector_space" | "bm25" | "hybrid";
export function precision(tp: number, retrieved: number): number { return retrieved === 0 ? 0 : tp / retrieved; }
export function recall(tp: number, relevant: number): number { return relevant === 0 ? 0 : tp / relevant; }

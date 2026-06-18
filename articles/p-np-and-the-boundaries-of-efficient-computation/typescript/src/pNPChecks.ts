export type ComplexityClass = "P" | "NP" | "NP-hard" | "NP-complete" | "unknown";
export function verifyColoring(edges: Array<[number, number]>, colors: Record<number, number>): boolean {
  return edges.every(([u, v]) => colors[u] !== colors[v]);
}

export type GraphKind = "directed" | "undirected" | "weighted" | "labeled";
export type Traversal = "breadth_first" | "depth_first" | "dijkstra" | "heuristic_pathfinding";
export function graphDensity(nodeCount: number, edgeCount: number): number {
  return nodeCount <= 1 ? 0 : edgeCount / (nodeCount * (nodeCount - 1));
}
export function pathCost(edgeWeights: number[]): number {
  return edgeWeights.reduce((total, weight) => total + weight, 0);
}

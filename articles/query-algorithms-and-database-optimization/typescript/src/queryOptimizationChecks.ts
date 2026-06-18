export type JoinAlgorithm = "nested_loop" | "index_nested_loop" | "hash_join" | "merge_join" | "broadcast_join" | "shuffle_join";
export function selectionRows(rows: number, selectivity: number): number { return rows * selectivity; }
export function joinRows(leftRows: number, rightRows: number, leftDistinct: number, rightDistinct: number): number { return (leftRows * rightRows) / Math.max(leftDistinct, rightDistinct); }

export type TreeKind = "document_tree" | "syntax_tree" | "decision_tree" | "btree" | "taxonomy";
export type TreeStructureCase = { name: string; kind: TreeKind; treeStructureQuality: number };
export const cases: TreeStructureCase[] = [
  { name: "Document outline tree", kind: "document_tree", treeStructureQuality: 81.40 },
  { name: "Syntax tree", kind: "syntax_tree", treeStructureQuality: 85.56 },
  { name: "Decision classification tree", kind: "decision_tree", treeStructureQuality: 82.00 },
  { name: "Database B-tree index", kind: "btree", treeStructureQuality: 84.32 }
];

export type Paradigm = "imperative" | "procedural" | "functional" | "object_oriented" | "logic" | "declarative" | "event_driven" | "concurrent";
export type StyleCase = { name: string; primaryParadigm: Paradigm; styleQuality: number };
export const cases: StyleCase[] = [
  { name: "Functional data transformation", primaryParadigm: "functional", styleQuality: 88.82 },
  { name: "Object-oriented domain model", primaryParadigm: "object_oriented", styleQuality: 85.78 },
  { name: "Declarative query layer", primaryParadigm: "declarative", styleQuality: 85.68 },
  { name: "Event-driven platform workflow", primaryParadigm: "event_driven", styleQuality: 82.08 }
];

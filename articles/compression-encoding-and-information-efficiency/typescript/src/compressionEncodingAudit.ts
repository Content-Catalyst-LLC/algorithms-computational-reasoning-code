export type CompressionMode = "lossless" | "lossy" | "hybrid" | "encoded_only";
export type CompressionEncodingCase = { name: string; mode: CompressionMode; representationQuality: number };
export const cases: CompressionEncodingCase[] = [
  { name: "Institutional archive records", mode: "lossless", representationQuality: 88.92 },
  { name: "Web media delivery", mode: "hybrid", representationQuality: 84.32 },
  { name: "Scientific simulation outputs", mode: "lossless", representationQuality: 87.08 },
  { name: "AI context packing", mode: "hybrid", representationQuality: 81.22 }
];

function trustQuality(verification: number, validation: number, security: number, provenance: number, monitoring: number, governance: number): number {
  return 100 * (0.18 * verification + 0.18 * validation + 0.18 * security + 0.16 * provenance + 0.15 * monitoring + 0.15 * governance);
}

console.log(`trust quality=${trustQuality(0.88, 0.82, 0.88, 0.90, 0.84, 0.82).toFixed(3)}`);

function standardError(pHat: number, n: number): number {
  return Math.sqrt((pHat * (1 - pHat)) / n);
}

const pHat = 0.57;
const n = 1000;
console.log(JSON.stringify({ pHat, n, standardError: standardError(pHat, n) }, null, 2));

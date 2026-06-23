function gcdAlgorithm(a: number, b: number): number {
  while (b !== 0) {
    const r = a % b;
    a = b;
    b = r;
  }
  return Math.abs(a);
}

console.log(`gcd=${gcdAlgorithm(252, 105)}`);

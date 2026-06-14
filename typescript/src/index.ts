function factorial(n: number): number {
  return n === 0 ? 1 : n * factorial(n - 1);
}

console.log(Array.from({ length: 7 }, (_, i) => [i, factorial(i)]));

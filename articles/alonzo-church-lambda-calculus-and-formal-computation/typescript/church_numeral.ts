function churchApply<T>(n: number, f: (x: T) => T, x: T): T {
  for (let i = 0; i < n; i += 1) {
    x = f(x);
  }
  return x;
}

console.log(`church_3_successor_0=${churchApply(3, (x: number) => x + 1, 0)}`);

function sumTo(n: number): number {
  let acc = 0;
  for (let i = 0; i <= n; i += 1) {
    acc += i;
  }
  return acc;
}

console.log(`sum_to_5=${sumTo(5)}`);

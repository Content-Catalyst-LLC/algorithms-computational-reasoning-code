for (const n of [10, 100, 1000, 10000]) {
  const log2 = Math.log2(n);
  console.log(`n=${n}, log2=${log2.toFixed(6)}, nlogn=${(n * log2).toFixed(6)}, n2=${n * n}`);
}

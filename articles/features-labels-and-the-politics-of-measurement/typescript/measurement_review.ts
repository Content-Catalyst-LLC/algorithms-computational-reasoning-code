function rate(num: number, den: number): number { return den === 0 ? 0 : num / den; }
console.log(`proxy_missingness_rate=${rate(171, 900).toFixed(4)}`);

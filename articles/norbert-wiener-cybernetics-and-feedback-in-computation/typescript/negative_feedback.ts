let x = 10.0;
const target = 0.0;
const gain = 0.2;
for (let i = 0; i < 5; i += 1) {
  x = x - gain * (x - target);
}
console.log(`final_state=${x.toFixed(6)}`);

const b = 10.0;
const c = 39.0;
const completion = Math.pow(b / 2.0, 2);
console.log(`completion_term=${completion.toFixed(6)}`);
console.log(`completed_rhs=${(c + completion).toFixed(6)}`);

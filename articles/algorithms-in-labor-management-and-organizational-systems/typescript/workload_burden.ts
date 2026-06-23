const pace = 0.84;
const hours = 0.72;
const fatigue = 0.70;
const scheduleVolatility = 0.78;
const burden = (pace + hours + fatigue + scheduleVolatility) / 4.0;
console.log(`workload_burden_score=${burden.toFixed(4)}`);

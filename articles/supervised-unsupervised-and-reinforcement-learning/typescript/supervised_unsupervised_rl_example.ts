const expectedReward = (p: number, value: number, cost: number): number => p * value - cost;
console.log(`expected_reward=${expectedReward(0.54, 1.0, 0.08).toFixed(6)}`);

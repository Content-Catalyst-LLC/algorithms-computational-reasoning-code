type ClientUpdate = { examples: number; weight: number };

const updates: ClientUpdate[] = [
  { examples: 100, weight: 0.42 },
  { examples: 240, weight: 0.55 },
  { examples: 160, weight: 0.49 },
];

const total = updates.reduce((acc, item) => acc + item.examples, 0);
const weighted = updates.reduce((acc, item) => acc + item.examples * item.weight, 0);
console.log(`federated average weight=${(weighted / total).toFixed(6)}`);

type Case = { name: string; threatModel: number; keys: number; validation: number; integrity: number; authentication: number };

function score(c: Case): number {
  return 100 * (0.22 * c.threatModel + 0.24 * c.keys + 0.18 * c.validation + 0.18 * c.integrity + 0.18 * c.authentication);
}

const cases: Case[] = [
  { name: "standard secure channel", threatModel: 0.86, keys: 0.82, validation: 0.90, integrity: 0.86, authentication: 0.84 },
  { name: "legacy manual transfer", threatModel: 0.36, keys: 0.24, validation: 0.18, integrity: 0.34, authentication: 0.28 }
];

for (const c of cases) {
  console.log(`${c.name} score=${score(c).toFixed(2)}`);
}

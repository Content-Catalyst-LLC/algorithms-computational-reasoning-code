const facts = new Set<string>(["has_documentation", "logs_decisions"]);
const premises = ["has_documentation", "logs_decisions"];
const fires = premises.every((premise) => facts.has(premise));
console.log(`rule_fires=${fires}`);

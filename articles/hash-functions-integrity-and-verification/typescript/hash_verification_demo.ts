// TypeScript hash verification teaching demo using Node's crypto module.
import { createHash } from "crypto";

function sha256Prefix(input: string): string {
  return createHash("sha256").update(input, "utf8").digest("hex").slice(0, 16);
}

const original = "verified artifact manifest";
const altered = "verified artifact manifest!";
console.log(`original sha256=${sha256Prefix(original)}`);
console.log(`altered sha256=${sha256Prefix(altered)}`);
console.log(`match=${sha256Prefix(original) === sha256Prefix(altered)}`);

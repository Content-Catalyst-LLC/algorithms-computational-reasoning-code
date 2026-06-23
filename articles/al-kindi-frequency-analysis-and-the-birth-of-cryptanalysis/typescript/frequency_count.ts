const text = "THIS IS A TOY CLASSICAL CIPHER EXAMPLE";
const counts: Record<string, number> = {};
for (const ch of text.toLowerCase()) {
  if (/[a-z]/.test(ch)) counts[ch] = (counts[ch] ?? 0) + 1;
}
console.log(counts);

# Substitution Cipher Notes

A monoalphabetic substitution cipher replaces each plaintext symbol with a corresponding cipher symbol.

Why frequency analysis can work:

- one-to-one replacement preserves relative frequencies;
- repeated plaintext letters become repeated cipher symbols;
- word lengths and repeated clusters may remain visible;
- longer ciphertext gives more stable estimates.

Why it can fail:

- too little data;
- no spaces;
- homophonic substitution;
- spelling variation;
- deliberate nulls;
- polyalphabetic substitution;
- codebooks or phrase-level replacements.

The lesson is not that all ciphers are weak. The lesson is that transformations can leak structure.

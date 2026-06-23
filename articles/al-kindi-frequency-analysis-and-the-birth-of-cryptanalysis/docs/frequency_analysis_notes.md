# Frequency Analysis Notes

Frequency analysis is a classical cryptanalytic method based on linguistic regularity.

Core steps:

- collect ciphertext;
- count symbols;
- normalize counts into relative frequencies;
- rank observed symbols;
- compare with expected language frequencies;
- propose substitutions;
- test partial plaintext;
- revise contradictions.

Important limits:

- short samples distort frequencies;
- spelling and genre matter;
- homophones and nulls can reduce frequency signals;
- polyalphabetic methods can defeat simple one-table analysis;
- modern encryption is not vulnerable to this toy method when properly designed.

This folder uses only synthetic toy examples for historical education.

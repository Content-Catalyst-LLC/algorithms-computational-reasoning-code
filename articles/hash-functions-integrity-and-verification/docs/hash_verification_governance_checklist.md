# Hash Verification Governance Checklist

- Define the artifact precisely before hashing.
- Record the hash algorithm and digest length.
- Store reference digests in a trusted location.
- Prefer signed manifests for release artifacts.
- Automate verification checks where possible.
- Record verification events and mismatch responses.
- Migrate weak or obsolete hash algorithms.
- Distinguish checksums, non-cryptographic hashes, cryptographic hashes, HMACs, and signatures.
- Communicate that a matching hash proves sameness relative to a trusted reference, not truth or safety.

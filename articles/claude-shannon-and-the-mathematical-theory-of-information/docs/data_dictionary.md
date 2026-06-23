# Data Dictionary

## shannon_themes.csv

- `theme_id`: interpretive theme in the Shannon information map.
- `entropy_centrality`: importance of entropy, uncertainty, and probability.
- `coding_relevance`: relevance to source coding, channel coding, compression, and error correction.
- `channel_capacity`: relevance to capacity, bandwidth, and transmission limits.
- `noise_awareness`: degree to which noise, corruption, and uncertainty are visible.
- `redundancy_design`: degree to which redundancy is used or removed deliberately.
- `computation_relevance`: relevance to algorithms, data systems, and digital computation.
- `cryptography_relevance`: relevance to secrecy, keys, leakage, and adversarial inference.
- `ai_relevance`: relevance to machine learning, AI systems, tokens, representations, and uncertainty.
- `semantic_boundary`: degree to which meaning/truth boundaries are explicit.
- `governance_caution`: relevance to responsible information systems and institutional use.

## shannon_information_map.csv

- `information_score`: average of the theme dimensions.
- `interpretive_status`: core, major, or supporting Shannon information thread.

## entropy_examples.csv

- `source`: teaching source name.
- `probabilities`: distribution used.
- `entropy_bits`: entropy in bits.

## interpretation_cautions.csv

- `caution`: interpretive risk to avoid.
- `meaning`: explanation of the caution.

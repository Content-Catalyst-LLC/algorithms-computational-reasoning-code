from __future__ import annotations

import argparse

parser = argparse.ArgumentParser(description="Return safer phrasing for common risky algorithm origin claims.")
parser.add_argument("--claim-type", choices=["khwarizmi_invented_algorithms", "algorithms_began_with_computers", "islamic_scholars_preserved_only", "ai_endpoint"], required=True)
args = parser.parse_args()

rewrites = {
    "khwarizmi_invented_algorithms": "Al-Khwārizmī's name is central to the word history of algorithm through Latin algorism, and his works helped transmit powerful arithmetic and algebraic procedures.",
    "algorithms_began_with_computers": "Modern computer-science algorithms formalized and mechanized much older traditions of rule-governed procedure.",
    "islamic_scholars_preserved_only": "Islamic-world scholars translated, corrected, synthesized, criticized, extended, and created mathematical and scientific traditions.",
    "ai_endpoint": "AI is one modern branch of a longer history of calculation, reasoning, automation, statistics, data, institutions, and governance.",
}
print(rewrites[args.claim_type])

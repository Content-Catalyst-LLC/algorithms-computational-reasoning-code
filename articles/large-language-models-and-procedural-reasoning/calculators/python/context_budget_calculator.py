from __future__ import annotations
import argparse
import math


def main() -> None:
    parser = argparse.ArgumentParser(description="Estimate context-window token budget from rough word counts.")
    parser.add_argument("--context-window", type=int, required=True)
    parser.add_argument("--system-words", type=int, default=0)
    parser.add_argument("--prompt-words", type=int, default=0)
    parser.add_argument("--retrieved-words", type=int, default=0)
    parser.add_argument("--reserved-output-tokens", type=int, default=1000)
    args = parser.parse_args()
    estimated_input_tokens = math.ceil((args.system_words + args.prompt_words + args.retrieved_words) * 1.33)
    remaining = args.context_window - estimated_input_tokens - args.reserved_output_tokens
    print(f"estimated_input_tokens={estimated_input_tokens}")
    print(f"reserved_output_tokens={args.reserved_output_tokens}")
    print(f"remaining_context_tokens={remaining}")
    print(f"fits={remaining >= 0}")


if __name__ == "__main__":
    main()

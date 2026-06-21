from __future__ import annotations

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Recommend agent autonomy level from audit counts.")
    parser.add_argument("--blocked", type=int, required=True)
    parser.add_argument("--escalated", type=int, required=True)
    parser.add_argument("--actions", type=int, required=True)
    args = parser.parse_args()

    if args.blocked > 0:
        level = "supervised_action_only"
    elif args.escalated > 0:
        level = "bounded_automation_with_escalation"
    elif args.actions <= 3:
        level = "bounded_automation"
    else:
        level = "supervised_periodic_review"

    print(f"actions={args.actions}")
    print(f"blocked={args.blocked}")
    print(f"escalated={args.escalated}")
    print(f"recommended_autonomy_level={level}")


if __name__ == "__main__":
    main()

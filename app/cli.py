"""
Oklix CLI.
"""

from app.agent import OklixAgent
import sys


def main():

    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    print()
    print("=" * 50)
    print("Oklix AI")
    print("Type 'exit' to quit.")
    print("=" * 50)
    print()

    agent = OklixAgent()

    while True:

        prompt = input("> ").strip()

        if not prompt:
            continue

        if prompt.lower() in {"exit", "quit"}:
            break

        try:

            print()
            print("Thinking...")
            print()

            response = agent.chat(prompt)

            print(response)
            print()

        except Exception as exc:

            print()
            print(f"Error: {exc}")
            print()


if __name__ == "__main__":
    main()

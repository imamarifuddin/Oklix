from app.agent import OklixAgent
import sys


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    print("=" * 50)
    print("OKLIX DEMO")
    print("=" * 50)

    agent = OklixAgent()

    prompt = "Apa itu Decision Intelligence?"

    print(f"\nPrompt:\n{prompt}\n")

    response = agent.chat(prompt)

    print("Response:\n")
    print(response)


if __name__ == "__main__":
    main()

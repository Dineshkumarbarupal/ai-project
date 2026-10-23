"""A small, dependency-free starter program for ai-project."""

def get_response(message: str) -> str:
    """Return a simple rule-based response to the user's message."""
    text = message.strip().lower()

    if not text:
        return "Please type a message."
    if any(word in text for word in ("hello", "hi", "hey")):
        return "Hello! Welcome to ai-project."
    if "your name" in text:
        return "I'm AI Project Assistant, a simple rule-based demo."
    if "help" in text:
        return "Try saying hello, asking my name, or type exit to quit."
    return "I am a starter demo, so I don't know that yet."


def main() -> None:
    print("AI Project Assistant")
    print("Type 'help' for options, or 'exit' to quit.")

    while True:
        try:
            message = input("\nYou: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        if message.lower() in {"exit", "quit"}:
            print("Assistant: Goodbye!")
            break

        print(f"Assistant: {get_response(message)}")


if __name__ == "__main__":
    main()

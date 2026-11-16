"""
Rule-Based Interactive Terminal Assistant / Chatbot
Author: Muhammad Usama Shokat

Run:
    python chatbot.py
"""

import json
import re
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
FAQ_FILE = BASE_DIR / "sample_faq.json"


def load_faq_data():
    """Load greetings and FAQ entries from the provided JSON dataset."""
    try:
        with FAQ_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, dict):
            raise ValueError("The FAQ file must contain a JSON object.")

        data.setdefault("greetings", [])
        data.setdefault("faqs", [])

        if not isinstance(data["greetings"], list) or not isinstance(data["faqs"], list):
            raise ValueError("The greetings and faqs values must be lists.")

        return data
    except FileNotFoundError:
        print(f"Warning: {FAQ_FILE.name} was not found. Using built-in FAQs.")
    except (json.JSONDecodeError, ValueError) as error:
        print(f"Warning: Could not read FAQ data ({error}). Using built-in FAQs.")

    return {
        "greetings": ["hello", "hi", "hey", "good morning", "good afternoon"],
        "faqs": [
            {
                "question": "What are your hours of operation?",
                "answer": "We operate Monday through Friday from 9:00 AM to 6:00 PM IST."
            },
            {
                "question": "How do I submit my internship project?",
                "answer": "You can submit your public GitHub repository link through your Student Workspace."
            },
            {
                "question": "When will I receive my certificate?",
                "answer": "Certificates are reviewed and issued within 3-5 business days after your code review."
            }
        ]
    }


def normalize_text(text):
    """Lowercase input and remove punctuation while preserving useful words."""
    text = text.lower().strip()
    text = re.sub(r"[^\w\s]", " ", text)
    return re.sub(r"\s+", " ", text)


def find_faq_matches(message, faqs):
    """Return FAQ answers whose keywords or question words match the message."""
    normalized_message = normalize_text(message)
    words = set(normalized_message.split())
    matches = []

    stop_words = {
        "what", "when", "where", "how", "do", "does", "is", "are", "the",
        "a", "an", "i", "my", "your", "you", "me", "to", "of", "for",
        "and", "can", "will", "please", "tell", "about"
    }

    for faq in faqs:
        question = faq.get("question", "")
        answer = faq.get("answer", "")
        normalized_question = normalize_text(question)
        question_words = {
            word for word in normalized_question.split()
            if word not in stop_words and len(word) > 2
        }

        # Match a phrase or meaningful question words.
        phrase_match = normalized_question in normalized_message
        matched_words = words.intersection(question_words)

        if phrase_match or len(matched_words) >= 2:
            matches.append((len(matched_words), answer))

    matches.sort(key=lambda item: item[0], reverse=True)
    return [answer for _, answer in matches]


def get_response(user_input, data):
    """Recognize greetings, multiple FAQ intents, and unknown questions."""
    message = normalize_text(user_input)

    if not message:
        return "Please type a question so I can help."

    exit_commands = {"bye", "exit", "quit"}
    if message in exit_commands:
        return None

    greetings = [normalize_text(item) for item in data.get("greetings", [])]
    if message in greetings:
        return "Hello! Welcome to the support assistant. You can ask me about working hours, project submission, or certificates."

    answers = find_faq_matches(user_input, data.get("faqs", []))
    if answers:
        # Avoid repeating an identical answer if multiple FAQ entries match.
        unique_answers = list(dict.fromkeys(answers))
        return "\n".join(unique_answers)

    # Helpful fallback for common wording not covered by exact question matching.
    if re.search(r"\b(hour|hours|timing|open|closing)\b", message):
        return "Our working hours are Monday through Friday, 9:00 AM to 6:00 PM IST."
    if re.search(r"\b(submit|submission|upload|github|repository|repo)\b", message):
        return "You can submit your public GitHub repository link through your Student Workspace."
    if re.search(r"\b(certificate|certification)\b", message):
        return "Certificates are reviewed and issued within 3-5 business days after your code review."

    return (
        "Sorry, I could not understand that question. Please ask about working "
        "hours, internship project submission, or certificate delivery."
    )


def main():
    data = load_faq_data()

    print("=" * 58)
    print("        DATH EON INTERACTIVE SUPPORT CHATBOT")
    print("        Type 'bye', 'exit', or 'quit' to close.")
    print("=" * 58)

    while True:
        try:
            user_input = input("\nYou: ")
        except (EOFError, KeyboardInterrupt):
            print("\nBot: Goodbye! Have a great day.")
            break

        response = get_response(user_input, data)

        if response is None:
            print("Bot: Goodbye! Thank you for chatting.")
            break

        print(f"Bot: {response}")


if __name__ == "__main__":
    main()

# Task 4: Rule-Based Interactive Terminal Assistant / Chatbot

**Author:** Muhammad Usama Shokat

## Description
A beginner-friendly Python terminal chatbot that recognizes greetings, answers questions from a JSON FAQ dataset, supports common alternate keywords, handles unknown questions, and exits with `bye`, `exit`, or `quit`.

## Files
- `chatbot.py` — chatbot logic, input normalization, intent matching, fallback handling, and conversation loop.
- `sample_faq.json` — the sample FAQ dataset provided with the task.

## Requirements
- Python 3
- No external packages are required.

## Run
Open a terminal in this folder and execute:

```bash
python chatbot.py
```

## Example questions
- `hello`
- `What are your hours of operation?`
- `How do I submit my internship project?`
- `When will I receive my certificate?`
- `quit`

## Features
1. Loads greeting phrases and FAQ answers from JSON.
2. Normalizes user input using lowercase conversion and regular expressions.
3. Matches multiple meaningful keywords and can return more than one matching FAQ answer.
4. Provides helpful fallback responses for common related terms.
5. Handles blank input and unrecognized questions.
6. Supports clean exit commands: `bye`, `exit`, and `quit`.

---
Created by **Muhammad Usama Shokat**.

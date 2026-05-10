"""
Replay previously-failing questions against a running server to see
what the model actually responds. Helps diagnose whether correctness
failures are real model errors or check_answer false negatives.

Usage:
    python scripts/debug_correctness.py <results.json> [--api-base URL]
"""
from __future__ import annotations

import argparse
import json
import random
import re
import sys

import openai


def check_answer(response: str, expected: int) -> bool:
    return bool(re.search(r'\b' + re.escape(str(expected)) + r'\b', response))


def _generate_questions(n: int, seed: int = 42) -> list[tuple[str, int]]:
    rng = random.Random(seed)
    questions = []
    for _ in range(n):
        op = rng.choice(["+", "-", "*", "/"])
        if op == "/":
            b = rng.randint(2, 50)
            a = b * rng.randint(2, 50)
            answer = a // b
        elif op == "*":
            a = rng.randint(2, 99)
            b = rng.randint(2, 99)
            answer = a * b
        elif op == "-":
            a = rng.randint(50, 2000)
            b = rng.randint(1, a)
            answer = a - b
        else:
            a = rng.randint(1, 2000)
            b = rng.randint(1, 2000)
            answer = a + b
        questions.append((f"{a} {op} {b} =", answer))
    return questions


FEW_SHOT_EXAMPLES = [
    {"question": "15 + 27 =", "answer": 42},
    {"question": "198 - 53 =", "answer": 145},
    {"question": "12 * 14 =", "answer": 168},
    {"question": "225 / 9 =", "answer": 25},
    {"question": "347 + 258 =", "answer": 605},
]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("results_json", help="Path to results.json from a previous run")
    parser.add_argument("--api-base", default="http://localhost:8001/v1")
    parser.add_argument("--provider", default="vllm")
    parser.add_argument("--benchmark", default="few_shot")
    parser.add_argument("--max-requests", type=int, default=50)
    args = parser.parse_args()

    with open(args.results_json) as f:
        data = json.load(f)

    raw = data["providers"][args.provider]["benchmarks"][args.benchmark]["raw_requests"]
    incorrect_indices = [r["request_idx"] for r in raw if r.get("correct") is False]
    print(f"Found {len(incorrect_indices)} incorrect responses for {args.provider}/{args.benchmark}")

    questions = _generate_questions(10000)

    example_text = "\n\n".join(
        f"Q: {ex['question']}\nA: {ex['answer']}" for ex in FEW_SHOT_EXAMPLES
    )
    system_prompt = (
        "You are a calculator. Compute the answer to each math equation. "
        "Respond with only the numerical answer, nothing else.\n\n"
        "Examples:\n\n" + example_text
    )

    client = openai.OpenAI(base_url=args.api_base, api_key="not-needed", timeout=60.0)

    model = data["model"]
    test_indices = incorrect_indices[:args.max_requests]
    still_wrong = 0
    checker_bug = 0

    for i, qidx in enumerate(test_indices):
        question, expected = questions[qidx]
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Q: {question}\nA:"},
        ]
        resp = client.chat.completions.create(
            model=model, messages=messages, temperature=0.0, max_tokens=256
        )
        text = resp.choices[0].message.content or ""
        correct = check_answer(text, expected)

        if not correct:
            still_wrong += 1
            print(f"  WRONG  q={qidx}: {question:25s} expected={expected:6d}  got={text!r}")
        else:
            checker_bug += 1
            print(f"  NOW OK q={qidx}: {question:25s} expected={expected:6d}  got={text!r}")

    print(f"\nResults: {still_wrong} still wrong, {checker_bug} now correct out of {len(test_indices)} replayed")
    if checker_bug > 0:
        print("^ 'now correct' means the original failure was likely a transient issue under load")


if __name__ == "__main__":
    main()

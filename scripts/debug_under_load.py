"""
Send few_shot questions at full concurrency (64 workers) and capture
the actual response text for incorrect answers. This reproduces the
benchmark conditions to see what the server returns under load.
"""
from __future__ import annotations

import concurrent.futures
import random
import re

import openai

NUM_REQUESTS = 10000
MAX_WORKERS = 64

FEW_SHOT_EXAMPLES = [
    {"question": "15 + 27 =", "answer": 42},
    {"question": "198 - 53 =", "answer": 145},
    {"question": "12 * 14 =", "answer": 168},
    {"question": "225 / 9 =", "answer": 25},
    {"question": "347 + 258 =", "answer": 605},
]


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


def main():
    client = openai.OpenAI(
        base_url="http://localhost:8001/v1",
        api_key="not-needed",
        timeout=300.0,
    )
    model = "meta-llama/Meta-Llama-3.1-70B-Instruct"

    questions = _generate_questions(NUM_REQUESTS)

    example_text = "\n\n".join(
        f"Q: {ex['question']}\nA: {ex['answer']}" for ex in FEW_SHOT_EXAMPLES
    )
    system_prompt = (
        "You are a calculator. Compute the answer to each math equation. "
        "Respond with only the numerical answer, nothing else.\n\n"
        "Examples:\n\n" + example_text
    )

    incorrect = []
    completed = [0]

    def _do_request(idx: int):
        question, expected = questions[idx]
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Q: {question}\nA:"},
        ]
        chunks = []
        stream = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=0.0,
            max_tokens=256,
            stream=True,
        )
        for chunk in stream:
            delta = chunk.choices[0].delta if chunk.choices else None
            if delta and delta.content:
                chunks.append(delta.content)

        text = "".join(chunks)
        correct = check_answer(text, expected)
        completed[0] += 1
        if completed[0] % 2000 == 0:
            print(f"  Progress: {completed[0]}/{NUM_REQUESTS}")
        return idx, question, expected, text, correct, len(chunks)

    print(f"Sending {NUM_REQUESTS} requests with {MAX_WORKERS} workers...")
    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as pool:
        futures = [pool.submit(_do_request, i) for i in range(NUM_REQUESTS)]
        for f in concurrent.futures.as_completed(futures):
            results.append(f.result())

    wrong = [(idx, q, exp, text, n_chunks) for idx, q, exp, text, correct, n_chunks in results if not correct]
    wrong.sort(key=lambda x: x[0])

    print(f"\n{len(wrong)} incorrect out of {NUM_REQUESTS}")
    print(f"\nAll incorrect responses:")
    print(f"{'idx':>6} {'question':>25} {'expected':>8} {'chunks':>6}  response")
    print("-" * 100)
    for idx, q, exp, text, n_chunks in wrong:
        print(f"{idx:>6} {q:>25} {exp:>8} {n_chunks:>6}  {text!r}")


if __name__ == "__main__":
    main()

"""
generate.py

Author: Maddy Guthridge
"""
from typing import Callable
import pyhtml as p
import random

terms = [
    *(["AI"] * 10),
    *(["ai"] * 4),
    *(["artificial intelligence"] * 5),
    *(["Artificial Intelligence"] * 3),
    *(["machine learning"] * 7),
    *(["ML"] * 4),
    *(["large language models"] * 6),
    *(["LLMs"] * 4),
    *(["neural networks"] * 3),
    "ADMS",
    *(["automated decision-making systems"] * 3),
]

elements: list[Callable[[str], p.Tag]] = [
    *([p.span] * 20),
    *([p.i] * 10),
    *([p.b] * 5),
    *([p.u] * 3),
    p.em,
    p.small,
    lambda s: p.b(p.i(s)),
    lambda s: p.b(p.i(s)),
    lambda s: p.b(p.u(s)),
    lambda s: p.u(p.i(s)),
    lambda s: p.u(p.i(p.b(s))),
]

paragraphs = []

for _ in range(500):
    if random.random() > 0.7:
        paragraphs.append(random.choice([p.ol, p.ul])([
            p.li(random.choice(elements)(random.choice(terms)))
            for _ in range(random.randint(5, 50))
        ]))
    else:
        paragraphs.append(p.p([
            random.choice(elements)(f"{random.choice(terms)},")
            for _ in range(random.randint(10, 100))
        ]))


print(p.html(
    p.head(p.title("COMP4920 Summary")),
    p.body(
        p.h1("COMP4920 Summary"),
        p.p("""
            This page contains a summary of the course content, including
            lecture, tutorial and assignment content for UNSW's COMP4920
            "Professional Issues and Ethics in Information Technology" course.
        """),
        p.p("I hope you find it helpful!"),
        paragraphs,
        p.p("Thank you for reading. I hope your experience was enjoyable!"),
        p.p(
            "If this website helped you revise the primary content of",
            "COMP4920, please",
            p.a(href="https://github.com/MaddyGuthridge/comp4920-summary")(
                "star the project on GitHub"
            ),
        ),
    ),
))

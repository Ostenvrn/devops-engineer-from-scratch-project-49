"""Игра «Арифметическая прогрессия»."""

import random

DESCRIPTION = "What number is missing in the progression?"

START_MIN = 1
START_MAX = 20
STEP_MIN = 1
STEP_MAX = 10
LENGTH_MIN = 5
LENGTH_MAX = 10


def generate_progression(start, step, length):
    """Генерирует арифметическую прогрессию."""
    return [start + index * step for index in range(length)]


def generate_round():
    """Возвращает вопрос и правильный ответ для одного раунда."""
    start = random.randint(START_MIN, START_MAX)
    step = random.randint(STEP_MIN, STEP_MAX)
    length = random.randint(LENGTH_MIN, LENGTH_MAX)

    progression = generate_progression(start, step, length)

    hidden_index = random.randint(0, length - 1)
    correct_answer = progression[hidden_index]
    progression[hidden_index] = ".."

    question = " ".join(str(num) for num in progression)
    return question, correct_answer

"""Игра «Проверка на чётность»."""

import random

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'

RANDOM_MIN = 1
RANDOM_MAX = 100


def is_even(number):
    """Предикат: True, если число чётное."""
    return number % 2 == 0


def generate_round():
    """Возвращает вопрос и правильный ответ для одного раунда."""
    number = random.randint(RANDOM_MIN, RANDOM_MAX)
    correct_answer = "yes" if is_even(number) else "no"
    return number, correct_answer

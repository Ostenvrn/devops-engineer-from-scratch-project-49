"""Игра «Проверка на чётность»."""

import random

DESCRIPTION = 'Ответь "да", если число чётное, иначе "нет".'

RANDOM_MIN = 1
RANDOM_MAX = 100


def is_even(number):
    """Предикат: True, если число чётное."""
    return number % 2 == 0


def generate_round():
    """Возвращает вопрос и правильный ответ для одного раунда."""
    number = random.randint(RANDOM_MIN, RANDOM_MAX)
    correct_answer = "да" if is_even(number) else "нет"
    return number, correct_answer

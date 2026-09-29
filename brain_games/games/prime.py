"""Игра «Простое ли число?»."""

import random

DESCRIPTION = 'Ответь "да", если число простое, иначе "нет.'

RANDOM_MIN = 1
RANDOM_MAX = 100


def is_prime(number):
    """Предикат: True, если число простое."""
    if number < 2:
        return False

    divisor = 2
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 1

    return True


def generate_round():
    """Возвращает вопрос и правильный ответ для одного раунда."""
    number = random.randint(RANDOM_MIN, RANDOM_MAX)
    correct_answer = "да" if is_prime(number) else "нет"
    return number, correct_answer

"""Игра «Наибольший общий делитель»."""

import random

DESCRIPTION = "Find the greatest common divisor of given numbers."

RANDOM_MIN = 1
RANDOM_MAX = 100


def gcd(num1, num2):
    """Находит НОД двух чисел алгоритмом Евклида."""
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    return num1


def generate_round():
    """Возвращает вопрос и правильный ответ для одного раунда."""
    num1 = random.randint(RANDOM_MIN, RANDOM_MAX)
    num2 = random.randint(RANDOM_MIN, RANDOM_MAX)
    question = f"{num1} {num2}"
    correct_answer = gcd(num1, num2)
    return question, correct_answer

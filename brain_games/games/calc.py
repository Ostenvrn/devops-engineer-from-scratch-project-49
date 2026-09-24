"""Игра «Калькулятор»."""

import random

DESCRIPTION = "What is the result of the expression?"

OPERATORS = ["+", "-", "*"]
RANDOM_MIN = 1
RANDOM_MAX = 25


def calculate(num1, num2, operator):
    """Вычисляет результат арифметической операции."""
    if operator == "+":
        return num1 + num2
    if operator == "-":
        return num1 - num2
    return num1 * num2


def generate_round():
    """Возвращает вопрос и правильный ответ для одного раунда."""
    num1 = random.randint(RANDOM_MIN, RANDOM_MAX)
    num2 = random.randint(RANDOM_MIN, RANDOM_MAX)
    operator = random.choice(OPERATORS)
    question = f"{num1} {operator} {num2}"
    correct_answer = calculate(num1, num2, operator)
    return question, correct_answer

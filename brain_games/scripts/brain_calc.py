"""Игра «Калькулятор»."""

import random

import prompt


def calculate(num1, num2, operator):
    """Вычисляет результат арифметической операции."""
    if operator == "+":
        return num1 + num2
    if operator == "-":
        return num1 - num2
    return num1 * num2


def main():
    """Запускает игру «Калькулятор»."""
    # Приветствие и знакомство
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")

    # Правило игры
    print("What is the result of the expression?")

    # Доступные операции
    operators = ["+", "-", "*"]

    # Победа — три правильных ответа подряд
    rounds_to_win = 3

    for _ in range(rounds_to_win):
        # Генерируем два числа и случайную операцию
        num1 = random.randint(1, 25)
        num2 = random.randint(1, 25)
        operator = random.choice(operators)

        # Вычисляем правильный ответ
        correct_answer = calculate(num1, num2, operator)

        # Задаём вопрос и получаем ответ
        print(f"Question: {num1} {operator} {num2}")
        user_answer = prompt.string("Your answer: ")

        # Ответ сравниваем как строку, prompt.string возвращает строку
        if user_answer != str(correct_answer):
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return

        print("Correct!")

    # Все раунды пройдены
    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()

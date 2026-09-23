"""Игра «Наибольший общий делитель»."""

import random

import prompt


def gcd(num1, num2):
    """Находит наибольший общий делитель двух чисел.

    Использует алгоритм Евклида: пока второе число не станет нулём,
    заменяем пару (num1, num2) на (num2, num1 % num2).
    Когда num2 == 0, num1 — это и есть НОД.
    """
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    return num1


def main():
    """Запускает игру «НОД»."""
    # Приветствие и знакомство с игроком
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")

    # Правило игры, которое видит игрок
    print("Find the greatest common divisor of given numbers.")

    # Победа — три правильных ответа подряд
    rounds_to_win = 3

    for _ in range(rounds_to_win):
        # Генерируем два случайных числа
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)

        # Вычисляем правильный ответ через алгоритм Евклида
        correct_answer = gcd(num1, num2)

        # Задаём вопрос и получаем ответ игрока
        print(f"Question: {num1} {num2}")
        user_answer = prompt.string("Your answer: ")

        # Сравниваем как строку: prompt.string возвращает str,
        # а gcd возвращает int
        if user_answer != str(correct_answer):
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return

        print("Correct!")

    # Если все раунды пройдены — поздравляем
    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()

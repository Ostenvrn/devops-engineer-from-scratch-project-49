"""Игра «Проверка на чётность»."""

import random

import prompt


def is_even(number):
    """Предикат: возвращает True, если число чётное."""
    return number % 2 == 0


def main():
    """Запускает игру «Проверка на чётность»."""
    # Приветствие и знакомство с игроком
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")

    # Правило игры, которое видит игрок
    print('Answer "yes" if the number is even, otherwise answer "no".')

    # Победа — три правильных ответа подряд
    rounds_to_win = 3

    for _ in range(rounds_to_win):
        # Генерируем случайное число от 1 до 100
        number = random.randint(1, 100)

        # Определяем правильный ответ на основе чётности
        correct_answer = "yes" if is_even(number) else "no"

        # Задаём вопрос и получаем ответ игрока
        print(f"Question: {number}")
        user_answer = prompt.string("Your answer: ")

        # Проверяем ответ: если неверный — завершаем игру
        if user_answer != correct_answer:
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

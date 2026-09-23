"""Игра «Арифметическая прогрессия»."""

import random

import prompt


def generate_progression(start, step, length):
    """Генерирует арифметическую прогрессию.

    Формула: current_element = start + index * step.
    Возвращает список чисел прогрессии.
    """
    return [start + index * step for index in range(length)]


def main():
    """Запускает игру «Арифметическая прогрессия»."""
    # Приветствие и знакомство с игроком
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")

    # Правило игры, которое видит игрок
    print("What number is missing in the progression?")

    # Победа — три правильных ответа подряд
    rounds_to_win = 3

    for _ in range(rounds_to_win):
        # Случайные параметры прогрессии
        start = random.randint(1, 20)
        step = random.randint(1, 10)
        length = random.randint(5, 10)

        # Генерируем прогрессию
        progression = generate_progression(start, step, length)

        # Прячем случайный элемент
        hidden_index = random.randint(0, length - 1)
        correct_answer = progression[hidden_index]
        progression[hidden_index] = ".."

        # Формируем вопрос из чисел через пробел
        question = " ".join(str(num) for num in progression)

        # Задаём вопрос и получаем ответ игрока
        print(f"Question: {question}")
        user_answer = prompt.string("Your answer: ")

        # Сравниваем как строку: prompt.string возвращает str,
        # а correct_answer — int
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

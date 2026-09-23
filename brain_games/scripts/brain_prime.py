"""Игра «Простое ли число?»."""

import random

import prompt


def is_prime(number):
    """Предикат: возвращает True, если число простое."""
    # Числа меньше 2 не являются простыми
    if number < 2:
        return False

    # Проверяем делители от 2 до квадратного корня числа
    # Если делитель больше корня, то второй множитель будет меньше корня
    divisor = 2
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 1

    return True


def main():
    """Запускает игру «Простое ли число?»."""
    # Приветствие и знакомство с игроком
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")

    # Правило игры, которое видит игрок
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    # Победа — три правильных ответа подряд
    rounds_to_win = 3

    for _ in range(rounds_to_win):
        # Генерируем случайное число
        number = random.randint(1, 100)

        # Определяем правильный ответ через предикат
        correct_answer = "yes" if is_prime(number) else "no"

        # Задаём вопрос и получаем ответ игрока
        print(f"Question: {number}")
        user_answer = prompt.string("Your answer: ")

        # Если ответ неверный — завершаем игру
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

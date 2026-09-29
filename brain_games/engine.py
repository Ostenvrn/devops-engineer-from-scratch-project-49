"""Игровой движок — общая логика для всех игр."""

import prompt

from brain_games.cli import welcome_user

ROUNDS_TO_WIN = 3


def run_game(game_module):
    """Запускает игру с переданным модулем.

    game_module должен содержать:
    - DESCRIPTION: str — описание игры
    - generate_round(): tuple — (вопрос, правильный ответ)
    """
    name = welcome_user()
    print(game_module.DESCRIPTION)

    for _ in range(ROUNDS_TO_WIN):
        question, correct_answer = game_module.generate_round()
        print(f"Вопрос: {question}")
        user_answer = prompt.string("Твой ответ: ")

        if user_answer != str(correct_answer):
            print(
                f"'{user_answer}' — неправильный ответ ;(. "
                f"Правильный ответ: '{correct_answer}'."
            )
            print(f"Попробуй ещё раз, {name}!")
            return

        print("Верно!")

    print(f"Поздравляю, {name}!")

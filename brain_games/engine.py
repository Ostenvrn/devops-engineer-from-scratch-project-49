"""Игровой движок — общая логика для всех игр."""

import prompt
from colorama import Fore, Style, init

from brain_games.cli import welcome_user

init(autoreset=True)

ROUNDS_TO_WIN = 3


def run_game(game_module):
    """Запускает игру с переданным модулем.

    game_module должен содержать:
    - DESCRIPTION: str — описание игры
    - generate_round(): tuple — (вопрос, правильный ответ)
    """
    name = welcome_user()
    print(f"{Fore.MAGENTA}{game_module.DESCRIPTION}{Style.RESET_ALL}")

    for _ in range(ROUNDS_TO_WIN):
        question, correct_answer = game_module.generate_round()
        print(f"{Fore.CYAN}Вопрос: {question}{Style.RESET_ALL}")
        prompt_text = f"{Fore.YELLOW}Твой ответ: {Style.RESET_ALL}"
        user_answer = prompt.string(prompt_text)
        if user_answer != str(correct_answer):
            print(
                f"{Fore.RED}'{user_answer}' — неправильный ответ ;(. "
                f"Правильный ответ: '{correct_answer}'.{Style.RESET_ALL}"
            )
            print(f"{Fore.RED}Попробуй ещё раз, {name}!{Style.RESET_ALL}")
            return

        print(f"{Fore.GREEN}Верно!{Style.RESET_ALL}")

    print(f"{Fore.GREEN}Поздравляю, {name}!{Style.RESET_ALL}")

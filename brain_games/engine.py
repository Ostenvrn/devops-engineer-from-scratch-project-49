"""Игровой движок — общая логика для всех игр."""

import prompt
from colorama import Fore, Style, init

from brain_games.banner import BANNERS, LOSE_BANNER, WIN_BANNER
from brain_games.cli import welcome_user

init(autoreset=True)

ROUNDS_TO_WIN = 3


def run_game(game_name, game_module):
    """Запускает игру с переданным модулем.

    game_name: str — ключ для баннера (even, calc, gcd, progression, prime)
    game_module: модуль с DESCRIPTION и generate_round()
    """
    # Баннер игры
    banner = BANNERS.get(game_name, "")
    if banner:
        print(banner)

    name = welcome_user()
    print(f"{Fore.MAGENTA}{game_module.DESCRIPTION}{Style.RESET_ALL}\n")

    for round_num in range(1, ROUNDS_TO_WIN + 1):
        question, correct_answer = game_module.generate_round()
        round_info = f"{round_num}/{ROUNDS_TO_WIN}"
        print(f"{Fore.YELLOW}Раунд {round_info}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}Вопрос: {question}{Style.RESET_ALL}")

        prompt_text = f"{Fore.YELLOW}Твой ответ: {Style.RESET_ALL}"
        user_answer = prompt.string(prompt_text)

        if user_answer != str(correct_answer):
            print(LOSE_BANNER)
            print(
                f"{Fore.RED}'{user_answer}' — неправильный ответ ;(. "
                f"Правильный ответ: '{correct_answer}'.{Style.RESET_ALL}"
            )
            print(f"{Fore.RED}Попробуй ещё раз, {name}!{Style.RESET_ALL}")
            return

        print(f"{Fore.GREEN}Верно!{Style.RESET_ALL}\n")

    print(WIN_BANNER)
    print(f"{Fore.GREEN}Поздравляю, {name}!{Style.RESET_ALL}")

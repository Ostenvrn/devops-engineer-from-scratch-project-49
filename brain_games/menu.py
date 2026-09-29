"""Меню выбора игры."""

import prompt
from colorama import Fore, Style, init

from brain_games.engine import run_game
from brain_games.games import calc, even, gcd, prime, progression

init(autoreset=True)

# Словарь игр: номер → (название, модуль)
GAMES = {
    "1": ("Чётность", even),
    "2": ("Калькулятор", calc),
    "3": ("НОД", gcd),
    "4": ("Прогрессия", progression),
    "5": ("Простое число", prime),
}

MENU_HEADER = f"""
{Fore.CYAN}╔══════════════════════════════════════╗
║      🧠 ДОБРО ПОЖАЛОВАТЬ В           ║
║         ИГРЫ РАЗУМА!                 ║
╚══════════════════════════════════════╝{Style.RESET_ALL}
"""


def show_menu():
    """Показывает меню и возвращает выбор пользователя."""
    print(MENU_HEADER)
    print(f"{Fore.YELLOW}Выбери игру:{Style.RESET_ALL}")
    print(f"  {Fore.GREEN}1.{Style.RESET_ALL} Чётность")
    print(f"  {Fore.GREEN}2.{Style.RESET_ALL} Калькулятор")
    print(f"  {Fore.GREEN}3.{Style.RESET_ALL} НОД")
    print(f"  {Fore.GREEN}4.{Style.RESET_ALL} Прогрессия")
    print(f"  {Fore.GREEN}5.{Style.RESET_ALL} Простое число")
    print(f"  {Fore.RED}0.{Style.RESET_ALL} Выход")
    print(f"{Fore.CYAN}{'─' * 40}{Style.RESET_ALL}")
    return prompt.string(f"{Fore.YELLOW}Твой выбор: {Style.RESET_ALL}")


def main():
    """Запускает меню выбора игры."""
    while True:
        choice = show_menu()

        if choice == "0":
            print(f"\n{Fore.CYAN}До встречи! 👋{Style.RESET_ALL}")
            return

        if choice in GAMES:
            name, game = GAMES[choice]
            print(f"\n{Fore.MAGENTA}▶ Запускаю: {name}{Style.RESET_ALL}\n")
            run_game(game)
            print(f"\n{Fore.CYAN}{'─' * 40}{Style.RESET_ALL}\n")
        else:
            error_msg = f"\n{Fore.RED}❌ Неверный выбор. "
            print(f"{error_msg}Попробуй снова.{Style.RESET_ALL}\n")


if __name__ == "__main__":
    main()

"""Меню выбора игры."""

import prompt
from colorama import Fore, Style, init

from brain_games.engine import run_game
from brain_games.games import calc, even, gcd, prime, progression

init(autoreset=True)

# Словарь игр: номер → (название, модуль, иконка)
GAMES = {
    "1": ("Чётность", even, "🔢"),
    "2": ("Калькулятор", calc, "🧮"),
    "3": ("НОД", gcd, "🔗"),
    "4": ("Прогрессия", progression, "📈"),
    "5": ("Простое число", prime, "🔍"),
}

MENU_HEADER = f"""
{Fore.CYAN}╔══════════════════════════════════════════╗
║                                          ║
║       🧠  И Г Р Ы   Р А З У М А  🧠      ║
║                                          ║
║          Тренировка для мозга            ║
║                                          ║
╚══════════════════════════════════════════╝{Style.RESET_ALL}
"""


def show_menu():
    """Показывает меню и возвращает выбор пользователя."""
    print(MENU_HEADER)
    print(f"{Fore.YELLOW}Выбери игру:{Style.RESET_ALL}\n")

    for num, (name, _, icon) in GAMES.items():
        print(f"  {Fore.GREEN}{num}.{Style.RESET_ALL} {icon}  {name}")

    print(f"\n  {Fore.RED}0.{Style.RESET_ALL} 🚪  Выход")
    print(f"\n{Fore.CYAN}{'─' * 44}{Style.RESET_ALL}")
    return prompt.string(f"{Fore.YELLOW}Твой выбор: {Style.RESET_ALL}")


def main():
    """Запускает меню выбора игры."""
    while True:
        choice = show_menu()

        if choice == "0":
            print(f"\n{Fore.CYAN}До встречи! 👋{Style.RESET_ALL}\n")
            return

        if choice in GAMES:
            name, game, icon = GAMES[choice]
            print(f"\n{Fore.MAGENTA}{'═' * 44}")
            print(f"  {icon}  Запускаю: {name}")
            print(f"{'═' * 44}{Style.RESET_ALL}\n")
            run_game(game)
            print(f"\n{Fore.CYAN}{'─' * 44}{Style.RESET_ALL}\n")
        else:
            error_msg = f"\n{Fore.RED}❌ Неверный выбор. "
            print(f"{error_msg}Попробуй снова.{Style.RESET_ALL}\n")


if __name__ == "__main__":
    main()

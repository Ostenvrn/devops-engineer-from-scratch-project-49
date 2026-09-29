"""Меню выбора игры."""

import prompt

from brain_games.engine import run_game
from brain_games.games import calc, even, gcd, prime, progression

# Словарь игр: номер → (название, модуль)
GAMES = {
    "1": ("Чётность", even),
    "2": ("Калькулятор", calc),
    "3": ("НОД", gcd),
    "4": ("Прогрессия", progression),
    "5": ("Простое число", prime),
}

MENU_HEADER = """
╔══════════════════════════════════════╗
║      🧠 ДОБРО ПОЖАЛОВАТЬ В           ║
║         ИГРЫ РАЗУМА!                 ║
╚══════════════════════════════════════╝
"""


def show_menu():
    """Показывает меню и возвращает выбор пользователя."""
    print(MENU_HEADER)
    print("Выбери игру:")
    print("  1. Чётность")
    print("  2. Калькулятор")
    print("  3. НОД")
    print("  4. Прогрессия")
    print("  5. Простое число")
    print("  0. Выход")
    print("─" * 40)
    return prompt.string("Твой выбор: ")


def main():
    """Запускает меню выбора игры."""
    while True:
        choice = show_menu()

        if choice == "0":
            print("\nДо встречи! 👋")
            return

        if choice in GAMES:
            name, game = GAMES[choice]
            print(f"\n▶ Запускаю: {name}\n")
            run_game(game)
            print("\n" + "─" * 40 + "\n")
        else:
            print("\n❌ Неверный выбор. Попробуй снова.\n")


if __name__ == "__main__":
    main()

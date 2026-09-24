"""Точка входа для игры «Калькулятор»."""

from brain_games.engine import run_game
from brain_games.games import calc


def main():
    """Запускает игру «Калькулятор»."""
    run_game(calc)


if __name__ == "__main__":
    main()

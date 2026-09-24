"""Точка входа для игры «НОД»."""

from brain_games.engine import run_game
from brain_games.games import gcd


def main():
    """Запускает игру «НОД»."""
    run_game(gcd)


if __name__ == "__main__":
    main()

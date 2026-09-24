"""Точка входа для игры «Простое число»."""

from brain_games.engine import run_game
from brain_games.games import prime


def main():
    """Запускает игру «Простое число»."""
    run_game(prime)


if __name__ == "__main__":
    main()

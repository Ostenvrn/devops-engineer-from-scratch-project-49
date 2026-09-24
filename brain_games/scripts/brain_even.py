"""Точка входа для игры «Проверка на чётность»."""

from brain_games.engine import run_game
from brain_games.games import even


def main():
    """Запускает игру «Проверка на чётность»."""
    run_game(even)


if __name__ == "__main__":
    main()

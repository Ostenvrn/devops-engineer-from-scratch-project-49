"""Точка входа для игры «Прогрессия»."""

from brain_games.engine import run_game
from brain_games.games import progression


def main():
    """Запускает игру «Прогрессия»."""
    run_game(progression)


if __name__ == "__main__":
    main()

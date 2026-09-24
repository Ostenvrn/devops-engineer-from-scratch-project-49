"""Модуль для взаимодействия с пользователем."""

import prompt


def welcome_user():
    """Спрашивает имя пользователя, приветствует и возвращает имя."""
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    return name

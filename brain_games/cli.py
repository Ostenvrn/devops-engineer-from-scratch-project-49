"""Модуль для взаимодействия с пользователем."""

import prompt
from colorama import Fore, Style, init

init(autoreset=True)


def welcome_user():
    """Спрашивает имя пользователя, приветствует и возвращает имя."""
    print(f"{Fore.CYAN}Добро пожаловать в Игры разума!{Style.RESET_ALL}")
    name = prompt.string(f"{Fore.YELLOW}Как тебя зовут? {Style.RESET_ALL}")
    print(f"{Fore.GREEN}Привет, {name}!{Style.RESET_ALL}")
    return name

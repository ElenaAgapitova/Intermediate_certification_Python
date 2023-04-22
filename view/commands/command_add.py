"""Модуль реализующий класс CommandAdd (добавление заметки)"""
from .command_abstract import Command


class CommandAdd(Command):
    """Класс реализует команду добавления заметки"""

    def description(self):
        """Возвращает описание команды"""
        return "Добавить заметку"

    def execute(self):
        """Запускает метод добавления заметки"""
        self.console.add_note()

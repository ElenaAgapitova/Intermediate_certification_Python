"""Модуль, реализующий класс CommandChange"""
from .command_abstract import Command


class CommandChange(Command):
    """Данный класс реализует команду изменение заметки"""

    def description(self):
        """Возвращает описание команды"""
        return "Изменить заметку"

    def execute(self):
        """Запускает метод изменения заметки"""
        self.console.change_note()

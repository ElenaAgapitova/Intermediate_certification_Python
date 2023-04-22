"""Модуль, реализующий класс CommandOpen"""
from .command_abstract import Command


class CommandOpen(Command):
    """Данный класс реализует команду заполнение записной книжки из файла"""

    def description(self):
        """Возвращает описание команды"""
        return "Открыть записную книжку"

    def execute(self):
        """Запускает метод заполнения записной книжки из файла"""
        self.console.open_notebook()

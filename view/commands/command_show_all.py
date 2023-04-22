"""Модуль, реализующий класс CommandShowAll"""
from .command_abstract import Command


class CommandShowAll(Command):
    """Данный класс реализует команду вывода всех заметок в консоль"""

    def description(self):
        """Возвращает описание команды"""
        return "Показать все заметки"

    def execute(self):
        """Запускает метод вывода заметок в консоль"""
        self.console.show_all()

"""Модуль реализующий класс CommandFilter (фильтрация заметок по дате)"""
from .command_abstract import Command


class CommandFilter(Command):
    """Класс реализует команду фильтрации заметок по дате добавления или изменения"""

    def description(self):
        """Возвращает описание команды"""
        return "Сделать выборку заметок по дате"

    def execute(self):
        """Запускает метод фильтрации заметок по дате и вывода результата"""
        self.console.show_filtered_notebook()

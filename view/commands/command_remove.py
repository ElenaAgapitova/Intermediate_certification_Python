"""Модуль реализующий класс CommandRemove (удаление заметки)"""
from .command_abstract import Command


class CommandRemove(Command):
    """Класс реализует удаление заметки"""

    def description(self):
        """Возвращает описание команды"""
        return "Удалить заметку"

    def execute(self):
        """Запускает метод удаления заметки"""
        self.console.remove_note()

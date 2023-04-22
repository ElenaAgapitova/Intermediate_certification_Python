"""Модуль класса CommandExit"""
from .command_abstract import Command


class CommandExit(Command):
    """Класс CommandExit позволяет завершить работу программы."""

    def description(self):
        """Возвращает описание команды для выхода из приложения"""
        return "Завершить работу"

    def execute(self):
        """Вызывает метод, которые завершает работу программы"""
        self.console.finish()

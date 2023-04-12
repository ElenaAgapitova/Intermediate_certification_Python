""" Модуль, реализующий класс создания заметки и работы с ней. """
from datetime import datetime


class Note:
    """
        Класс для создания заметки.

        Атрибуты:
        __title (str): текст заголовка заметки.
        __text_note (str): текст заметки.
        __creation_data (str): дата/время создания заметки.
        __changes_data (str): дата/время последнего изменения заметки
        Методы:
        1. __init__: конструктор (метод) класса для создания заметки.
        1. get_title: возвращает заголовок заметки.
        2. get_creation_data: возвращает дату и время создания заметки.
        3. get_changes_data: возвращает дату и время последнего изменения заметки.
        4. get_text_note: возвращает текст-содержание заметки.
        5. change: изменение заметки.
    """

    def __init__(self, title, creation_data, text_note, changes_data=''):
        self.__title = title
        self.__text_note = text_note
        self.__creation_data = creation_data
        self.__changes_data = changes_data

    def get_title(self):
        """
        Возвращает содержание заголовка заметки.
        :return: заголовок заметки.
        """
        return self.__title

    def get_creation_data(self):
        """
        Возвращает дату и время создания заметки.
        :return: дата и время создания заметки.
        """
        return self.__creation_data

    def get_changes_data(self):
        """
        Возвращает дату и время последнего изменения заметки.
        :return: дата и время последнего изменения заметки.
        """
        return self.__changes_data

    def get_text_note(self):
        """
        Возвращает текст-содержание заметки.
        :return: текст-содержание заметки.
        """
        return self.__text_note

    def change(self, title: str, new_text: str):
        """
        Редактирование заголовка, текста и даты/время изменения заметки.
        Пользователь может изменить либо заголовок заметки, либо содержание заметки,
        либо и то и другое. Дата и время редактирования устанавливаются текущие.
        :param title: текст заголовка.
        :param new_text: текст заметки.
        """
        if title:
            self.__title = title
        if new_text:
            self.__text_note = new_text
        self.__changes_data = datetime.today().strftime('%d.%m.%Y %H:%M')

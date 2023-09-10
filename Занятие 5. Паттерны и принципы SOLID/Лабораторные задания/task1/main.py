"""Модуль приложения для подсчета, хранения и отображения проектов организации"""
from abc import abstractmethod


class ProjectManagement:
    """Базовый класс управления проектами"""
    @abstractmethod
    def check_project(self, project):
        pass

    @abstractmethod
    def add_project(self, project):
        pass

    @abstractmethod
    def update_project(self, project):
        pass

    @abstractmethod
    def get_project(self, project_id):
        pass

    @abstractmethod
    def quantity_project(self, project, project_type):
        pass


class QueryManagement:
    """Базовый класс управления заявками"""
    @abstractmethod
    def set_query(self, query):
        pass

    @abstractmethod
    def get_query(self, query_id):
        pass


class IdCounter:
    """ Генератор значений id """
    def __init__(self, id_data):
        """
        :param id_data: Инициализируется id
        """
        self.id_data = id_data

    def current_id(self, id_):
        """ Проверяет текущий id """
        # реализация для проверки текущего id_
        pass

    def get_new_id(self):
        """ Возвращает новый id """
        # реализация для получения нового id_
        pass


class Project:
    """Класс проекта"""
    _counter = IdCounter()

    def __init__(self, project_id, project_type, name, price):
        """
        Создаем базовый проект организации
        :param project_id: Идентификационный номер проекта.
        :param project_type: Тип проекта.
        :param name: Наименование проекта.
        :param price: Стоимость проекта.
        """
        self.project_id = self._counter.current_id(project_id)
        self.project_type = project_type
        self.name = name
        self.price = price

    def _project_id_get(self):
        """Выводит идентификационный номер проекта."""
        return self._project_id

    def _project_id_set(self):
        """Устанавливает идентификационный номер проекта."""
        self._project_id = self._counter.get_new_id()


class Query:
    """Класс заявок"""
    _counter = IdCounter()

    def __init__(self, query_id, project_id, quantity):
        """
        Создаем базовую заявку
        :param query_id: Идентификационный номер заявки.
        :param project_id: Идентификационный номер проекта.
        :quantity: Количество проектов.
        """
        self.query_id = self._counter.current_id(query_id)
        self.project_id = project_id
        self.quantity = quantity

    def _query_id_get(self):
        """Выводит идентификационный номер заявки."""
        return self._query_id

    def _query_id_set(self):
        """Устанавливает идентификационный номер заявки."""
        self._query_id = self._counter.get_new_id()


class ProjectRepository:
    """Класс репозитория проектов"""
    def check_project(self, project):
        # реализация для проверки проекта на соответствие определенным требованиям
        pass

    def add_project(self, project):
        # реализация для добавления проекта в репозиторий
        pass

    def update_project(self, project):
        # реализация для обновления проекта в репозитории
        pass

    def get_project(self, project_id):
        # реализация для извлечения проекта из репозитория
        pass

    def quantity_project(self, project, project_type):
        # реализация для подсчета количества проектов (общее и по видам), размещенных в репозитории
        pass


class QueryRepository:
    """Класс репозитория заявок"""
    def set_query(self, query):
        # реализация для размещения заявки в репозитории
        pass

    def get_query(self, query_id):
        # реализация для извлечения заявки из репозитория
        pass


class ProjectStorage(ProjectManagement, QueryManagement):
    """Класс хранилища проектов организации"""
    def __init__(self, project_repository, query_repository):
        self.project_repository = project_repository
        self.query_repository = query_repository

    def check_project(self, project):
        self.project_repository.cheсk_project(project)

    def add_project(self, project):
        self.project_repository.add_project(project)

    def update_project(self, project):
        self.project_repository.update_project(project)

    def get_project(self, project_id):
        return self.project_repository.get_project(project_id)

    def quantity_project(self, project, project_type):
        return self.project_repository.quantity_project(project, project_type)

    def set_query(self, query):
        self.query_repository.place_query(query)

    def get_query(self, query_id):
        return self.query_repository.get_query(query_id)


# Добавляем новые классы User и UserRepository и управление пользователями в класс ProjectStorage
class User:
    """Базовый класс пользователей"""
    _counter = IdCounter()

    def __init__(self, username, password):
        """
        Инициализируются атрибуты пользователя
        :param username: Имя пользователя
        :param password: Пароль пользователя
        """
        self.user_id = self._counter.get_new_id()
        self.username = self.check_username(username)
        self.__password = password

    def check_username(self, username):
        """ Проверяет имя пользователя """
        # реализация для проверки имени пользователя
        pass
        self.username = username

    def get_username(self):
        # реализация для извлечения имени пользователя
        pass


class UserRepository:
    """Класс репозитория пользователей"""
    def add_user(self, user):
        # реализация для добавления пользователя в репозиторий
        pass

    def update_user(self, user):
        # реализация для обновления пользователя в репозитории
        pass

    def get_user(self, user_id):
        # реализация для извлечения пользователя из репозитория
        pass


class ProjectStorageUsers(ProjectStorage):
    """Класс хранилища проектов организации с возможностью управления пользователями"""
    def __init__(self, project_repository, query_repository, user_repository):
        super().__init__(project_repository, query_repository)
        self.user_repository = user_repository

    def add_user(self, user):
        self.user_repository.add_user(user)

    def update_user(self, user):
        self.user_repository.update_user(user)

    def get_user(self, user_id):
        return self.user_repository.get_user(user_id)


if __name__ == "__main__":
    pass

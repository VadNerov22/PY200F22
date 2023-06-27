import unittest

from task import Node


class TestCase(unittest.TestCase):
    def test_init_node_without_next(self):
        """Проверить следующий узел после инициализации с аргументом next_ по умолчанию"""
        self.assertIsNone(next)

    def test_init_node_with_next(self):
        """Проверить следующий узел после инициализации с переданным аргументом next_"""
        self.assertIsNotNone(next)

    def test_repr_node_without_next(self):
        """Проверить метод __repr__, для случая когда нет следующего узла."""
        self.assertEqual(f"Node({self.value}, {None})", self.__repr__())

    @unittest.skip
    def test_repr_node_with_next(self):
        """Проверить метод __repr__, для случая когда установлен следующий узел."""
        ...

    def test_str(self):
        some_value = 5
        node = Node(some_value)

        # TODO проверить строковое представление

    def test_is_valid(self):
        ...  # TODO проверить метод is_valid при корректных узлах

        # TODO с помощью менеджера контакста и метода assertRaises проверить корректность вызываемой ошибки

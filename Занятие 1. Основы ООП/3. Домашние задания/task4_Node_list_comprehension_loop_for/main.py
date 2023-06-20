from typing import Any, Optional


class Node:
    """ Класс, который описывает узел связного списка. """

    def __init__(self, value: Any, next_: Optional["Node"] = None):
        """
        Создаем новый узел для односвязного списка
        :param value: Любое значение, которое помещено в узел
        :param next_: следующий узел, если он есть
        """
        self.value = value
        self.next_ = next_

    def __repr__(self) -> str:
        return f"Node({self.value}, {self.next_})"


if __name__ == "__main__":
    list_nodes = [Node(val) for val in range(10)]
    print(list_nodes)

    for i, el in enumerate(list_nodes):
        print(list_nodes[i].value)
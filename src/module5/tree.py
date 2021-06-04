from module5.node import Node


class BinaryTree:

    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self.__insert(value, self.root)

    def insert_range(self, *values):
        for value in values:
            self.insert(value)

    def __insert(self, value, current_node):
        if not current_node:
            return Node(value)

        if current_node.value > value:
            current_node.left = self.__insert(value, current_node.left)
        elif current_node.value < value:
            current_node.right = self.__insert(value, current_node.right)

        return current_node
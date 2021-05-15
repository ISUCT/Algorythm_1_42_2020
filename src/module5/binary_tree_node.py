class BinaryTreeNode:

    def __init__(self, value):
        self.__value = value
        self.__left = None
        self.__right = None

    @property
    def value(self):
        return self.__value

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, left):
        self.__left = left

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, right):
        self.__right = right

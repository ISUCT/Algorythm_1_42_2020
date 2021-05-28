class Node:
    __height = 0

    def __init__(self, data):
        self.data = data
        self.l = None
        self.r = None

    @property
    def height(self):
        return self.__height + 1

    def add(self, value, depht):
        if self.data == value:
            return
        if value < self.data:
            if self.l:
                self.l.add(value, depht+1)
            else:
                if Node.__height < depht:
                    Node.__height = depht
                self.l = Node(value)
        else:
            if self.r:
                self.r.add(value, depht+1)
            else:
                if Node.__height < depht:
                    Node.__height = depht
                self.r = Node(value)

    def find_forks(self):
        if self.l:
            self.l.find_forks()
        if not(self.l and self.r) and not(not self.l and not self.r):
            print(self.data)
        if self.r:
            self.r.find_forks()

def building_tree(elem):
    root = Node(elem[0])
    for i in range(1, len(elem)):
        root.add(elem[i], 1)
    return root

def main():
    elem = list(map(int, input().split()))
    elem.pop(-1)
    tree = building_tree(elem)
    tree.find_forks()

main()
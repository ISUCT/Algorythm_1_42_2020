from module5.tree import BinaryTree


def print_node_with_single_child(node):
    if node.left:
        print_node_with_single_child(node.left)

    if (bool(node.right) + bool(node.left)) == 1:
        print(node.value)

    if node.right:
        print_node_with_single_child(node.right)


def get_input_data():
    return list(map(int, input().split()))


def main():
    '''
    <<< 7 3 2 1 9 5 4 6 8 0
    >>> main()
    2
    9
    '''
    tree = BinaryTree()

    items = get_input_data()
    items.pop()

    tree.insert_range(*items)

    print_node_with_single_child(tree.root)


if __name__ == '__main__':
    main()

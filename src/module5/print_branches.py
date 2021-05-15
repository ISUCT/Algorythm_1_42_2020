from binary_tree import BinaryTree


def print_node_with_single_child(node):
    count = bool(node.left) + bool(node.right)

    if count == 2:
        print_node_with_single_child(node.left)
        print_node_with_single_child(node.right)
        return

    if count == 1:
        print(node.value)


def main():
    tree = BinaryTree()

    tree.insert_range()

    print_node_with_single_child(tree.root)


if __name__ == '__main__':
    main()

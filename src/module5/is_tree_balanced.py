from module5.tree import BinaryTree

def height(node):
    if not node:
        return 0

    return max(height(node.left), height(node.right)) + 1

def is_tree_balanced(node):
    return (not node) or (height(node.left) == height(node.right) \
        or height(node.left) + 1 == height(node.right) \
        or height(node.left) == height(node.right) + 1) \
        and is_tree_balanced(node.left) and is_tree_balanced(node.right)


def get_input_data():
    return list(map(int, input().split()))


def main():
    '''
    <<< 7 3 2 1 9 5 4 6 8 0
    >>> main()
    YES
    '''
    tree = BinaryTree()

    items = get_input_data()
    items.pop()

    tree.insert_range(*items)

    print("YES" if is_tree_balanced(tree.root) else "NO")


if __name__ == '__main__':
    main()
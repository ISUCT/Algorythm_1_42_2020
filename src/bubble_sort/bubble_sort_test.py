import unittest
from bubble_sort import bubble_sort, bubble_sort_shuffles


class TestBubbleSort(unittest.TestCase):

    def test_bubble_sort(self):
        array = [5, 3, 65, 2, 6, 4, 100]
        expected = [2, 3, 4, 5, 6, 65, 100]

        result = bubble_sort(array)

        self.assertEqual(result, expected)

    def test_bubble_sort_shuffles(self):
        array = [1, 2, 3, 4, 5]
        expected = 0

        result = bubble_sort_shuffles(array)

        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()

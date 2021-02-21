import unittest
from unittest.mock import patch
from io import StringIO

from recursive_sorts_0 import merge_sort


class TestBubbleSort(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def test_recursive_sorts_0(self, stdout):
        array = [5, 4, 3, 2, 1]
        expected = '\n'.join([
            '1 2 4 5',
            '4 5 1 2',
            '3 5 1 3',
            '1 5 1 5'
        ])

        merge_sort(array, 0, len(array) - 1)

        result = stdout.getvalue().strip()
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()

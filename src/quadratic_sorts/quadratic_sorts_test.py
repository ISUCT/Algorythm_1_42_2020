import unittest
from unittest.mock import patch
from io import StringIO

from quadratic_sorts_0 import bubble_sort
from quadratic_sorts_1 import sort_by_cost_and_id


class TestBubbleSort(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def test_quadratic_sorts_0(self, stdout):
        array = [1, 2, 3, 4, 5]
        expected = '0'

        bubble_sort(array)

        result = stdout.getvalue().strip()
        self.assertEqual(result, expected)

    @patch('sys.stdout', new_callable=StringIO)
    def test_quadratic_sorts_1(self, stdout):
        items = [
            [20, 80],
            [30, 90],
            [25, 90]
        ]

        expected = '\n'.join([
            '25 90',
            '30 90',
            '20 80'
        ])

        sort_by_cost_and_id(items)

        result = stdout.getvalue().strip()
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()

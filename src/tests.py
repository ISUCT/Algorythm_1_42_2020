import unittest
import pogtest

from quadratic_sorts import quadratic_sorts_0
from quadratic_sorts import quadratic_sorts_1

from recursive_sorts import recursive_sorts_0
from recursive_sorts import recursive_sorts_1


def load_tests(loader, tests, ignore):
    modules = [
        quadratic_sorts_0,
        quadratic_sorts_1,

        recursive_sorts_0,
        recursive_sorts_1,
    ]

    for module in modules:
        tests.addTests(pogtest.DocTestSuite(module))

    return tests


if __name__ == '__main__':
    unittest.main()

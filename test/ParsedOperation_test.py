import unittest
from pprint import pprint

from engine.ParsedOperation import ParsedOperation


class ConstructorTest(unittest.TestCase):
    def test_something(self):
        date = "2020-01-01"
        case = ParsedOperation(description="test case", execDate=date, orderDate=date, amount=1.0, account="1")
        pprint(case)
        self.assertEqual(case.amount, 1.0)


if __name__ == '__main__':
    unittest.main()

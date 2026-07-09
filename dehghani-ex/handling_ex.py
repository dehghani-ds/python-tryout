def divide(a, b):
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        print('division by zero')
    return result
num1,num2 = None, None
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
except ValueError:
    print("input isn't a number")
else:
    print("Result:", divide(num1, num2))
finally:
    print("app ended successfully ;)")

import unittest

class TestError(unittest.TestCase):

    def test_division_by_zero(self):
        first_number = 1
        second_number = 0
        n = divide(first_number, second_number)
        self.assertEqual(n, None)


if __name__ == '__main__':
    unittest.main()
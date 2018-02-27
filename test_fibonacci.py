import unittest

from fibonacci import fibonacci, FibonacciError


class TestFibonacci(unittest.TestCase):
    def test_not_integer(self):
        with self.assertRaises(FibonacciError):
            fibonacci(1.5)

        with self.assertRaises(FibonacciError):
            fibonacci('abc')

        with self.assertRaises(FibonacciError):
            fibonacci(None)

    def test_negative(self):
        with self.assertRaises(FibonacciError):
            fibonacci(-1)

    def test_base_cases(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)

    def test_low_values(self):
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(3), 2)
        self.assertEqual(fibonacci(4), 3)
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(6), 8)

    def test_high_values(self):
        self.assertEqual(fibonacci(30), 832040)
        self.assertEqual(fibonacci(40), 102334155)
        self.assertEqual(fibonacci(50), 12586269025)
        self.assertEqual(fibonacci(100), 354224848179261915075L)
        self.assertEqual(fibonacci(1000), 43466557686937456435688527675040625802564660517371780402481729089536555417949051890403879840079255169295922593080322634775209689623239873322471161642996440906533187938298969649928516003704476137795166849228875L)


if __name__ == '__main__':
    unittest.main()

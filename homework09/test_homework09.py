import unittest
from homeworks import multiplication_table, sum_of_numbers, arithmetic_mean


class TestMultiplicationTable(unittest.TestCase):
    def test_multiplication_table_below_25(self):
        """TC01: Перевірки де результат > 25"""
        actual = multiplication_table(2)
        expected = [
            (2, 1, 2), (2, 2, 4), (2, 3, 6), (2, 4, 8),
            (2, 5, 10), (2, 6, 12), (2, 7, 14), (2, 8, 16),
            (2, 9, 18), (2, 10, 20)
        ]
        self.assertEqual(actual, expected)

    def test_multiplication_table_exceeds_25(self):
        """TC02: Перевірка того чи функція прериває свою роботу якщо результат > 25"""
        actual = multiplication_table(6)
        expected = [(6, 1, 6), (6, 2, 12), (6, 3, 18), (6, 4, 24)]
        self.assertEqual(actual, expected)

    def test_multiplication_table_zero(self):
        """TC03: Перевірка для числа для числа 0"""
        actual = multiplication_table(0)
        expected = [
            (0, 1, 0), (0, 2, 0), (0, 3, 0), (0, 4, 0),
            (0, 5, 0), (0, 6, 0), (0, 7, 0), (0, 8, 0),
            (0, 9, 0), (0, 10, 0)
        ]
        self.assertEqual(actual, expected)

    def test_multiplication_table_edge_case(self):
        """TC04: Перевірка граничного значення, результат == 25"""
        actual = multiplication_table(5)
        expected = [(5, 1, 5), (5, 2, 10), (5, 3, 15), (5, 4, 20), (5, 5, 25)]
        self.assertEqual(actual, expected)

    def test_multiplication_table_non_numeric(self):
        """TC05: Перевірка для нечислового значення"""
        with self.assertRaises(TypeError):
            multiplication_table("a")
        with self.assertRaises(TypeError):
            multiplication_table(None)

class TestSumOfNumbers(unittest.TestCase):

    def test_sum_of_two_positive_integers(self):
        """TC01: Перевірка з позитивними числами"""
        actual = sum_of_numbers(3, 5)
        self.assertEqual(actual, 8)

    def test_sum_of_two_negative_integers(self):
        """TC02: Перевірка з двома негативними числами"""
        actual = sum_of_numbers(-4, -6)
        self.assertEqual(actual, -10)

    def test_sum_positive_and_negative_integer(self):
        """TC03: Перевірка з одним негативним числом"""
        actual = sum_of_numbers(8, -5)
        self.assertEqual(actual, 3)

    def test_sum_of_two_floats(self):
        """TC04: Перевірка з float"""
        actual = sum_of_numbers(3.5, 2.4)
        self.assertEqual(actual, 5.9)

    def test_sum_integer_and_float(self):
        """TC05: Перевірка з float та цілим"""
        actual = sum_of_numbers(4, 2.5)
        self.assertEqual(actual, 6.5)

    def test_sum_with_zero(self):
        """TC06: Перевірка з нулем"""
        actual = sum_of_numbers(0, 5)
        self.assertEqual(actual, 5)

    def test_sum_with_string_first(self):
        """TC07: Перевірка зі строкою"""
        with self.assertRaises(TypeError):
            sum_of_numbers("string", 5)

    def test_sum_large_numbers(self):
        """TC08: Перевірка з великими числами"""
        actual = sum_of_numbers(10**18, 10**18)
        self.assertEqual(actual, 2 * 10**18)

class TestArithmeticMean(unittest.TestCase):

    def test_with_positive_numbers(self):
        """TC_001: Перевірка з позитивними числами"""
        actual = arithmetic_mean(1, 2, 3, 4, 5)
        self.assertEqual(actual, 3)

    def test_with_positive_and_negative_numbers(self):
        """TC_002: Перевірка з позитивними та негативними числами"""
        actual = arithmetic_mean(1, -2, 3, -4, 5)
        self.assertEqual(actual, 0.6)

    def test_single_number(self):
        """TC_003: Перевірка з одним числом"""
        actual = arithmetic_mean(5)
        self.assertEqual(actual, 5)

    def test_floats(self):
        """TC_004: Перевірка з float"""
        actual = arithmetic_mean(1.5, 2.5, 3.5)
        self.assertEqual(actual, 2.5)

    def test_string_input(self):
        """TC_005: Провірка зі строками"""
        with self.assertRaises(TypeError):
            arithmetic_mean("a", "b", "c")

    def test_mixed_types(self):
        """TC_006: Перевірка змішаних даних"""
        with self.assertRaises(TypeError):
            arithmetic_mean(1, 2, "3")

    def test_large_input(self):
        """TC_007: Перевірка з великою кількістю чисел"""
        actual = arithmetic_mean(*range(1000000))
        self.assertEqual(actual, 499999.5)

if __name__ == '__main__':
    unittest.main()

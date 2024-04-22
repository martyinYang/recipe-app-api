from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    
    def test_add_numbers(self):
        res = calc.add(2, 2)
        self.assertEqual(res, 4)


    def test_subtract_numbers(self):
        res = calc.subtract(15, 10)

        self.assertEqual(res, 5)
        
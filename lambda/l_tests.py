import l_exercises as le
import unittest

class LambdaTests(unittest.TestCase):
    def test_make_square(self):
        l = le.make_square()
        self.assertEqual(l(2), 4)
        self.assertEqual(l(12), 144)


    def test_make_upper(self):
        l = le.make_upper()
        self.assertEqual(l('ahoj'), "AHOJ")


    def test_make_power(self):
        power = le.make_power()
        self.assertEqual(power(3, 3), 27)
        self.assertEqual(power(2, 10), 1024)


    def test_make_power2(self):
        cube = le.make_power2(3)
        self.assertEqual(cube(3), 27)

        deka = le.make_power2(10)
        self.assertEqual(deka(2), 1024)


    def test_call_name(self):
        l = le.call_name()
        self.assertEqual(l('ahoj', 'upper'), 'AHOJ')


if __name__ == '__main__':
    unittest.main()
import unittest
from moje_kalkulacka import soucet, rozdil, nasobeni, podil


class TestKalkulacka(unittest.TestCase):

    def test_soucet(self):
        self.assertEqual(soucet(5, 2), 7)
        self.assertEqual(soucet(-7, 4), -3)
        self.assertAlmostEqual(soucet(0.1, 0.2), 0.3, places=4)

    def test_rozdil(self):
        self.assertEqual(rozdil(4, 2), 2)
        self.assertEqual(rozdil(-5, 4), -9)

    def test_nasobeni(self):
        self.assertEqual(nasobeni(4, 6), 24)
        self.assertEqual(nasobeni(-5, 4), -20)

    def test_podil(self):
        self.assertEqual(podil(8, 4), 2)
        self.assertEqual(podil(-8, 4), -2)

    def test_podil_nulou(self):
        with self.assertRaises(ZeroDivisionError):
            podil(5, 0)


if __name__ == "__main__":
    unittest.main()

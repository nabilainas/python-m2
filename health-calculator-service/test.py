import unittest
from health_utils import calculate_bmi, calculate_bmr

class TestHealthUtils(unittest.TestCase):
    def test_calculate_bmi(self):
        weight = 70
        height = 1.75
        self.assertEqual(calculate_bmi(weight, height), {"bmi": 22.86})

    def test_calculate_bmr(self):
        weight = 70
        height = 1.75
        age = 18
        gender = "male"
        self.assertEqual(calculate_bmr(weight, height, age, gender), {"bmr": 932.36})

if __name__ == '__main__':
    unittest.main()
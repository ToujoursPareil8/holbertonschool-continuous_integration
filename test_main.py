import unittest

class TestApplication(unittest.TestCase):
    def test_addition(self):
        # True, test success
        self.assertEqual(1 + 1, 2)

    def test_deliberate_failure(self):
        # False. meant to fail here
        self.assertEqual(2 + 2, 5)

if __name__ == '__main__':
    unittest.main()
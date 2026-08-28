import unittest
from app import app


class TestApplication(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_hello_default_greeting(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Default Welcome Message", response.data)


if __name__ == '__main__':
    unittest.main()

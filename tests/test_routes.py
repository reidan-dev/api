import unittest

from app import create_app


class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.testing = True
        self.client = self.app.test_client()

    def test_home(self):
        response = self.client.get("/api")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Welcome to the Flask API!", response.data)

    def test_get_data(self):
        response = self.client.get("/api/data")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"key": "value"})


if __name__ == "__main__":
    unittest.main()

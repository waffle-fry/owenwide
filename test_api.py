from api import app
import unittest


class TestAPI(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.context = app.app_context()
        self.context.push()

    def tearDown(self):
        self.context.pop()

    def test_health(self):
        with self.app as client:
            response = client.get('/health')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json, {'status': 'ok'})

    def test_customers(self):
        with self.app as client:
            response = client.get('/customers')
            self.assertEqual(response.status_code, 200)
            self.assertIsInstance(response.json, list)
            self.assertGreater(len(response.json), 0)

    def test_account_balances(self):
        with self.app as client:
            response = client.get('/account_balances')
            self.assertEqual(response.status_code, 200)
            self.assertIsInstance(response.json, dict)
            self.assertGreater(len(response.json), 0)

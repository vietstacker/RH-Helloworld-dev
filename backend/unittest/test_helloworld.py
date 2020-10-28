from app import app as flask_app

import unittest


class HelloWorldUnittest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        # creates a test client
        self.flask_app = flask_app.test_client()
        # propagate the exceptions to the test client
        self.flask_app.testing = True

    def tearDown(self):
        pass

    def test_status_code(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.flask_app.get('/api/hello')

        # assert the status code of the response
        self.assertEqual(result.status_code, 200)

    def test_return_data(self):
        result = self.flask_app.get('/api/hello')
        print(result.data)
        # assert the status code of the response
        self.assertEqual(result.data, b'Hello from hello-world-backend (1)')
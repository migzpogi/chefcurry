import unittest
import responses
from boba import app


class TestBobaApp(unittest.TestCase):

    def test_sum(self):
        self.assertTrue(app.sum(1, 2), 3)

    @responses.activate
    def test_foobar(self):
        """
        See https://stackoverflow.com/questions/9559963/unit-testing-a-python-app-that-uses-the-requests-library
        :return:
        """
        responses.add(**{
            'method': responses.GET,
            'url': 'https://www.google.com',
            'body': '{"error": "reason"}',
            'status': 500,
            'content_type': 'application/json',
            'adding_headers': {'X-Foo': 'Bar'}
        })

        self.assertEqual(app.get_foobar(), 500)


if __name__ == '__main__':
    unittest.main()

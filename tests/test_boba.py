import unittest
from boba import app


class TestBobaApp(unittest.TestCase):

    def test_sum(self):
        self.assertTrue(app.sum(1, 2), 3)


if __name__ == '__main__':
    unittest.main()
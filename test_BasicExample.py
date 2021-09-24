import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(False,False)
    def test_something11(self):
        self.assertEqual(True,False)


if __name__ == '__main__':
    unittest.main()



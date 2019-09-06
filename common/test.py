import unittest

class InequalityTest(unittest.TestCase):

    def testEqual(self):
        self.assertEqual(1, 2)
        print("1111")

    def testNotEqual(self):
        self.assertEqual(2, 2)


if __name__ == '__main__':
    unittest.main()
import test
import unittest

class TestTest(unittest.TestCase):

    def test_u1_lower(self):
        self.assertFalse(test.u1(90,89,90))
    def test_u1_higher(self):
        self.assertTrue(test.u1(91,92,93))
    def test_u2_1(self):
        self.assertEqual(test.u2(10,10),1)
    def test_u2_2(self):
        self.assertEqual(test.u2(20,10),2)

if __name__ == '__main__':
    unittest.main()
import unittest

class SimpleTest(unittest.TestCase):

    def test(self):
        res = 120
        self.assertEqual(res, 120)

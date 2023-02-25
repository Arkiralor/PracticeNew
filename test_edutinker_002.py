import unittest

def mul_two(a:int, b:int):
    return a*b

class TestCases(unittest.TestCase):

    def test_mul_two(self, c:int=5, d:int=6):
        '''
        Test mul_two() above
        '''
        res = mul_two(c, d)
        actual_res = c*d
        self.assertEqual(res, actual_res)

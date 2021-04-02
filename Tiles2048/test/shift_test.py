'''
Created on 2 Apr 2021

@author: Vance
'''
import unittest
from test.test__xxsubinterpreters import expect_channel_closed
import Tiles2048.shift as shift

class Test(unittest.TestCase):

    def test010_001_Validating_parms(self):
        parms = {"grid": "0000222244448888", "score":0, "direction":"abc", "integrity": "00000"}
        expected = {"status": "error: invalid direction"}
        actual = shift._check_parms(parms)
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
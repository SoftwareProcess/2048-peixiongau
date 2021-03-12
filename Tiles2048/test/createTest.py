import unittest
import Tiles2048.create as create
from test.test__xxsubinterpreters import expect_channel_closed

class CreateTest(unittest.TestCase):

#  The following is included only for illustrative purposes.  It tests nothing
#  useful.  Please delete and replace with your own test code.
    def test_create_HappyPathTest010(self):
        userParms = {'op': 'create', 'size': '4'}
        actualResult = create._create(userParms)
        self.assertIsNotNone(actualResult)
        
    #0001
    #def test001_010(self):
    #    userParms = {'op': 'create'}
    #    expect = {"grid":0, "score":0, "integrity": 0, "status": 0}
    #    actual = create._create(userParms)
    #    self.assertDictEqual(expect, actual)
    
    #002
    #def test005_010(self):
    #    actual = create._generateGrid()
    #    self.assertIsNotNone(actual)
    
    #def test005_020(self):
    #    expect = b'0'
    #    actual = create._generateIntegrity('0002000200000000', 40)
    #    self.assertEqual(actual, expect)
        
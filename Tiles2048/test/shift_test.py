'''
Created on 2 Apr 2021

@author: Vance
'''
import unittest
from test.test__xxsubinterpreters import expect_channel_closed
import Tiles2048.shift as shift

class Test(unittest.TestCase):

    def test010_001_Validating_parms(self):
        parms = {"grid": "0000222244448888", "score":'0', "direction":"abc", "integrity": "00000"}
        expected = {"status": "error: invalid direction"}
        actual = shift._check_parms(parms)
        self.assertEqual(actual, expected)

    def test010_002_validating_parms(self):
        parms = {"grid": "000022224444", "score":'0', "direction":"up", "integrity": "00000"}
        expected = {"status": "error: invalid grid"}
        actual = shift._check_parms(parms)
        self.assertEqual(actual, expected)
    
    def test010_003_validating_parms(self):
        parms = {"score":0, "direction":"abc", "integrity": "00000"}
        expected = {"status": "error: missing grid"}
        actual = shift._check_parms(parms)
        self.assertEqual(actual, expected)
    def test010_004_validating_parms(self):
        parms = {"grid": "0000222244448888", "score":'0', "direction":"up", "integrity": "00000"}
        expected = {"status": "error: bad integrity value"}
        actual = shift._check_parms(parms)
        self.assertEqual(actual, expected)
    
    def test010_005_validating_parms(self):
        parms = {"grid": "0000222244448888", "score":'99', "direction":"abc", "integrity": "00000"}
        expected = {"status": "error: invalid score"}
        actual = shift._check_parms(parms)
        self.assertEqual(actual, expected)
        
    def test010_006_validating_parms(self):
        parms = {"grid": "16161616222244448888", "score":'0', "direction":"abc", "integrity": "00000"}
        expected = {"status": "error: no shift possible"}
        actual = shift._check_parms(parms)
        self.assertEqual(actual, expected)
        
        
    def test020_001_happy_path(self):
        parms = {"grid": "002200440088161688", "score":'0', "direction":"down", 
                 "integrity": '675E0CECD8BE05E63B50BAB79D808607EBAE51367A8F8DF7F28EA595A79F4232\
CB7564DB2265528FC83764CB59ED88500EC33CCA41E4E6B91CEAB984EDC5F085'}
        expected = 'ok'
        actual = shift._shift(parms)[3]
        self.assertEqual(actual, expected)    
    
    
    def test_500_001_check_missing(self):
        parms = {"grid": '000000'}
        expected = "error: missing score"
        actual = shift._check_missing(parms)
        self.assertEqual(actual, expected)
    
    def test500_002_check_grid(self):
        parms = {"grid": "2222222244448888", "score" : '0', "direction":"abcd", "integrity": "00000"}
        expected = 'error: no shift possible'
        actual = shift._check_grid(parms['grid'])[0]
        self.assertEqual(actual, expected)
    def test500_003_check_grid(self):
        parms = {"grid": "2222222244448880", "score" : '0', "direction":"abcd", "integrity": "00000"}
        expected = 'passed'
        actual = shift._check_grid(parms['grid'])[0]
        self.assertEqual(actual, expected)
        
    def test500_004_check_score(self):
        parms = {"grid": "2222222244448880", "score" : '99', "direction":'down', "integrity": "00000"}
        expected = 'error: invalid score'
        actual = shift._check_score(parms['score'])
        self.assertEqual(actual, expected)
        
        
    '''
    def test500_005_operatings(self):
        grid = '0022002200220022'
        dir = 'right'
        expected = "0004000400040004"
        gridNew = shift._check_grid(grid)[1]
        actual = shift._operate(gridNew, dir)
        self.assertEqual(actual, expected)   
    def test500_006_operatings(self):
        grid = '204420442088821616'
        dir = 'right'
        expected = "002800280021608232"
        gridNew = shift._check_grid(grid)[1]
        actual = shift._operate(gridNew, dir)
        self.assertEqual(actual, expected)   
        
    def test500_007_operatings(self):
        grid = '204420442088821616'
        dir = 'left'
        expected = '280028002160082320'
        gridNew = shift._check_grid(grid)[1]
        actual = shift._operate(gridNew, dir)
        self.assertEqual(actual, expected)   
    
    def test500_008_operatings(self):
        grid = '4000400000080008'
        dir = 'down'
        expected = "00000000000080016"
        gridNew = shift._check_grid(grid)[1]
        actual = shift._operate(gridNew, dir)
        self.assertEqual(actual, expected) 
        
    def test500_009_operatings(self):
        grid = '4000400000080008'
        dir = 'up'
        expected = "80016000000000000"
        gridNew = shift._check_grid(grid)[1]
        actual = shift._operate(gridNew, dir)
        self.assertEqual(actual, expected)  
    '''
    def test500_010_gentiles(self):
        grid = ['2', '2','2', '2','2', '2','2', '2','2', '2','2', '2','2', '2','2', '2']
        expected = 'lose'
        actual = shift._gen_tiles(grid)[2]
        self.assertEqual(expected, actual)
    
    def test500_011_gentiles(self):
        grid = ['2', '2','2', '2','2', '2','2', '2','2', '2','2', '2','2', '2','2', '2048']
        expected = 'win'
        actual = shift._gen_tiles(grid)[2]
        self.assertEqual(expected, actual)
        
        

    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
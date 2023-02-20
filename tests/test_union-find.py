import unittest
from algorithms.unionfind.count_islands import (
    num_islands
    
)
    
class TestUnionAndNumIslands(unittest.TestCase):
    
    def test_union_and_num_islands(self):
        positions = [[0,0], [0,1], [1,2], [2,1]]
        expected = [1, 1, 2, 3]
        self.assertEqual(num_islands(positions), expected)
        
        positions = [[0,0], [0,1], [1,2], [2,1], [1,1]]
        expected = [1, 1, 2, 3, 2]
        self.assertEqual(num_islands(positions), expected)
        
        positions = [[0,0], [0,1], [1,2], [2,1], [1,1], [1,0]]
        expected = [1, 1, 2, 3, 2, 1]
        self.assertEqual(num_islands(positions), expected)

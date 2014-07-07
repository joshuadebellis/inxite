# -*- coding: utf-8 -*-
"""
Created on Mon Jul  7 16:50:04 2014

@author: josh
"""

from scanner import TextScanner

import unittest

class TestFileTypes(unittest.TestCase):
    def setUp(self):
        self.endnumber = TextScanner("numberatend.txt")
        self.galaxysong = TextScanner("galaxysong.txt")
        self.empty = TextScanner("emptylist.txt")
        
    
    def test_numberword_at_list_end(self):
        self.assertEqual(self.endnumber.wordsum(), 900000002)
        
    def test_galaxysong(self):
        self.assertEqual(self.galaxysong.wordsum(), 100213189920)
        
    def test_empty_file(self):
        self.assertEqual(self.empty.wordsum(), 0)
        
        
if __name__ == '__main__':
    unittest.main()    
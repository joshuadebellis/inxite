# -*- coding: utf-8 -*-
"""
Created on Mon Jun 30 17:10:36 2014

@author: josh
"""

from textscanner import textscanner


lyrics = raw_input("Enter the name of the file to be scanned: ")



song = textscanner(lyrics)
print song.textscanner.wordsum()

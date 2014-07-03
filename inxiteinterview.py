# -*- coding: utf-8 -*-
"""
Created on Mon Jun 30 17:10:36 2014

@author: josh
"""



from scanner import TextScanner
 
prompt = raw_input("Enter the name of the file to be scanned: ")
 
song = TextScanner(prompt)
wordsum = song.wordsum()
print("The sum of the number words in this song is " + str(wordsum))



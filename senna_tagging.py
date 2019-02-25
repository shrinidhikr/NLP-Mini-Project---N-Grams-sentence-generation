#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 20:22:08 2018

@author: shrinidhikr
"""

from os.path import expanduser
home = expanduser("~")
from nltk.tag.senna import SennaTagger
st = SennaTagger(home+'/senna')
with open("test.txt") as file:
    data = file.read().replace("\n","")
    data = data.split(".")
x = " "
text = "The quick brown fox jumps over the lazy dog"
for line in data:
    #print(line)
    print(st.tag(line.split()))
#! /home/gary/.asdf/shims/python
''' This is my path to python, you should update this with the output of which python on your system '''

import re

def getip(line):
    p = re.compile(r"\b((?:\d{1,3}\.){3}\d{1,3})")
    m = p.findall(line)
    if(m):
        return m
    return None

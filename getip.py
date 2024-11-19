#! /home/gary/.asdf/shims/python
''' This is my path to python, you should update this with the output of which python on your system '''

import re

def getip(line):
    p = re.compile(r"\b((?:\d{1,3}\.){3}\d{1,3})")
    m = p.findall(line)
    if(m):
        return m
    return None

'''
    Detect if we are being called as a script and print out all the ips
    allows us to do
    cat sample_ips.txt | ./getips.py | sort -u > found_ips.txt
'''
if __name__ == "__main__":
    import sys
    for line in sys.stdin:
        result = getip(line)
        if(result):
            for ip in result:
                print(ip)
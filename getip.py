#! /home/gary/.asdf/shims/python
''' This is my path to python, you should update this with the output of which python on your system
    This allows running the program without needing to specify the interperater like so
    ./getip.py
    Note: getip.py must be marked exacutable for this to work at which point you can remove the extension
    and just run ./getip and if you put it in a path were you system looks for executables like /usr/bin
    then you can just type getip

    This comment is pydoc which allws us to get documentation by typing:
    python -m pydoc getip
    or start up a docementation server by typing
    python -m pydoc -p 1234
'''

import re


def getip(line: str) -> list:
    """
    Extracts and returns IP addresses from a given string.

    Parameters:
        line (str): The input string within which to find IP addresses.

    Returns:
        list: A list of extracted IP addresses as strings. If no IP addresses are found, returns an empty list.
    """

    # Regular expression pattern to match IP addresses
    p = re.compile(r'(?:^|\s|\[|\||\'|\,|\")((?:\d{1,3}\.){3}\d{1,3})\.?(?:$|\s|\]|\||\'|\,|\")')

    # Find all occurrences of IP addresses in the input string
    m = p.findall(line)

    if m:
        return m

    return None





'''
    Detect if we are being called as a script and print out all the ips
    so we can do:
    cat sample_ips.txt | ./getips.py | sort -u > found_ips.txt
'''
if __name__ == "__main__":
    import sys
    for line in sys.stdin:
        result = getip(line)
        if(result):
            for ip in result:
                print(ip)
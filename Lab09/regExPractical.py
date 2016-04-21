#! /usr/bin/env python3.4

import os
import glob
import re
import sys

def getAddress(sentence):
    pattern = re.compile(r"([\dA-Fa-f]{2})([-:]{1})([\dA-Fa-f]{2})([-:]{1})([\dA-Fa-f]{2})([-:]{1})([\dA-Fa-f]{2})([-:]{1})([\dA-Fa-f]{2})([-:]{1})([\dA-Fa-f]{2})")
    search_val = re.search(pattern, sentence)
    string = ""
    if search_val is None:
        return None

    else:
        string += str(search_val.group(0))

    return string

def getSwitches(commandline):
    pattern = re.compile(r"([+\\])[\s]*(\S*)[\s]*")
    match = re.findall(pattern, commandline)
    print(match)

def getElements(fullAddress):
    pattern = re.compile(r"(http://|https://)([a-zA-Z0-9.]+)/([a-zA-Z0-9]+)/([a-zA-Z0-9]+)[\s]*$")
    match = re.match(pattern, fullAddress)
    if(match is not None):
        if match.group(2) is not None and match.group(3) is not None and match.group(4) is not None:
            ret_tuple = (match.group(2),match.group(3),match.group(4))
        else:
            return None
    else:
        return None

    return ret_tuple



if __name__ == "__main__" :
    getAddress("The card was at 58-1c-0a-6e-39-4d, but it was removed.")
    getSwitches("myscript.bash +v \i 2 +p /local/bin/somefolder")
    url = "https://www.paypal.com/Customer1Area/Pay2"
    print(getElements(url))
#! /usr/bin/envpython3.4
#
#$Author: ee364a09 $
#$Date: 2016-02-17 00:42:47 -0500 (Wed, 17 Feb 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364a09/Prelab06/email.py $
#$Revision: 88307 $

import os
import glob
import re

def email():
    repl = "ecn."
    pattern = r"([\w.-]+)@(purdue.edu)(\s+)(\d*)\.(\d*)"
    with open("Part2.in",'r') as input:
        for line in input:
            match = re.match(pattern, line)
            #print(match)
            if match is not None:

                newstr = match.group(1) + "@ecn."+match.group(2) + match.group(3) + match.group(4) + "." + match.group(5) + "/100"
                print(newstr)
    return 0

if __name__ == "__main__" :
    email()



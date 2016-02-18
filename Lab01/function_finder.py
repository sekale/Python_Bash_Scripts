#! /usr/bin/envpython3.4
#
#$Author: ee364a09 $
#$Date: 2016-02-17 02:32:29 -0500 (Wed, 17 Feb 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364a09/Prelab06/function_finder.py $
#$Revision: 88309 $

import os
import glob
import re
import sys

def function_finder(filename):
    try:
        open(filename,"r")

    except IOError:
        print("Error: Could not read %s"%(filename))
        return 1

    #pattern = r"[def]\s+([a-zA-Z]{1})([\w]*|[-]*)\s+[(]{1}([\w]*)[)]{1}[:]{1}"
    pattern = r"def\s+(([a-zA-Z])(\w|-|_)+)\((.*)\)"
    #print(pattern)
    with open(filename) as input:
        for line in input:
            match = re.match(pattern,line)
            list_val = []
            if match is not None:
                str = match.group(4)
                list_val = str.split(',')
                count = 0
                for i in list_val:
                    list_val[count] = i.strip()
                    count += 1
                #print(list_val)
                count=0
                print(match.group(1))
                for i in list_val:
                    print('Arg%d: %s' %(count + 1,list_val[count]))
                    count+=1




    return 0

def main():
    #function_finder()
    nargs = len(sys.argv)
    if(nargs != 2):
        print("Usage: function_finder.py [python_file_name]")

    else:
        filename = sys.argv[1]
        function_finder(filename)

if __name__ == "__main__" :
    main()




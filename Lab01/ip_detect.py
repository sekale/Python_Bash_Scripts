#! /usr/bin/envpython3.4
#
#$Author: ee364a09 $
#$Date: 2016-02-17 01:23:40 -0500 (Wed, 17 Feb 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364a09/Prelab06/ip_detect.py $
#$Revision: 88308 $

import os
import glob
import re

def ipdetect():
    pattern = r"0{0,2}(\d+)\.0{0,2}(\d+)\.0{0,2}(\d+)\.0{0,2}(\d+):(\w+)"
    with open("addys.in") as input:
        for line in input:
            match = re.match(pattern,line)
            flag_ip = 0
            flag_port = 0
            if match is not None:
                for i in range(1,5):
                    if(int(match.group(i)) > 255):
                        flag_ip = 1

                for i in match.group(5):
                    #print(i)
                    if not (i >= "0" and i <= "9"):
                        #print("here")
                        flag_port = 1

                if flag_port != 1:
                    if not (int(match.group(5)) >=1 and int(match.group(5)) <= 32767):
                        flag_port = 1

                #print(match.group(5))


                if (flag_port == 0 and flag_ip == 0 and int(match.group(5)) <= 1024):
                    strval = "Valid (root privileges required)"

                elif (flag_port == 0 and flag_ip == 0 and int(match.group(5)) > 1024):
                    strval = "Valid"

                elif (flag_ip == 1):
                    strval = "Invalid IP Address"

                elif (flag_port == 1):
                    strval = "Invalid Port Number"
                #print(line)
                finalstr = line + '- ' + strval
                finalstr = finalstr.replace("\n"," ")
                print(finalstr)
    return 0

if __name__ == "__main__" :
    ipdetect()





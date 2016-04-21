#!/usr/bin/env python3.4

import os
import sys
import re
import string

def idIsAcceptable(ver_id):
    for i in ver_id:
        if i not in string.ascii_letters and i not in string.digits and (i!='_'):
            return False
    return True

def processSingle(ver_assignment):
    pattern = r"\.(.*?)\((.*?)\)\s*$"

    match = re.match(pattern,ver_assignment)
    if match is not None:
        if match.group(1) is not None and match.group(2) is not None:
            if(idIsAcceptable(match.group(1)) and idIsAcceptable(match.group(2))):
                retTuple = ( match.group(1), match.group(2) )
                return retTuple
            else:
                raise ValueError(ver_assignment)
        else:
            raise ValueError(ver_assignment)

    else:
        raise ValueError(ver_assignment)

def processLine(ver_line):
    pattern = r"\s*(\d*\w*_*)\s*(\d*\w*_*)\s*\((.*)\)"
    valid = 0
    valid1 = 0
    valid2 = 0
    valid3 = 1
    list_val = []
    match = re.match(pattern, ver_line)


    if match is not None:

        if(match.group(1) is not None):
            if match.group(1) == "":
                raise ValueError
            if(idIsAcceptable(match.group(1))):
                valid1 = 1
            else:
                raise ValueError(match.group(1))

        if(match.group(2) is not None):
            if match.group(2) == "":
                raise ValueError
            if(idIsAcceptable(match.group(2))):
                valid2 = 1
            else:
                raise ValueError(match.group(2))

        if match.group(3) is not None:
            assignments = match.group(3).split(',')
            for assignment in assignments:
                assignment = assignment.strip()
                assignmentValid = processSingle( assignment )
                if not assignmentValid:
                    valid3 = 0
                    raise ValueError
                else:
                    list_val.append(assignmentValid)
                tuple_list_val = tuple(list_val)

        if(valid1 == 1 and valid2 == 1 and valid3 == 1):
            ret_tuple = (match.group(1),match.group(2),tuple_list_val)
            print(ret_tuple)
            return ret_tuple

        else:
            raise ValueError(ver_line)
    else:
        raise ValueError










if __name__ == "__main__":
    assignment = "DFFSR Q_int1_reg ( .D(serial_in), .CLK(clk), .R(1), .S(n5), .Q(Q_int1) )"
    assi = "BAD(.A(n32),.B(n5),.C(n3),.D(n6),.Y(n25))"
    print(processLine(assignment))

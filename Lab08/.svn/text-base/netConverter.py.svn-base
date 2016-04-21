#!/usr/bin/env python3.4

import sys
import os
import string
import HardwareTasks

def verilog2vhdl(ver_line):
    try:
        value = HardwareTasks.processLine(ver_line)

    except ValueError:
        return "Error: Bad Line."

    string = ""
    list_value = []
    for i in value:
        list_value.append(i)

    string1 = list_value[1]
    string2 = ": "
    string3 = list_value[0]
    string4 = " PORT MAP"
    string5 = "("

    string = string1 + string2+ string3+ string4+ string5
    string6 = ""
    for i in value[2]:
        for item in i:
            string6 += item
            string6 += "=>"
        string6 = string6[0:-1]
        string6 = string6[0:-1]
        string6 +=", "
    string6 = string6[0:-1]
    string6 = string6[0:-1]

        #print(i)

    string6 += ");"
    string += string6
    #print(string)

    return string

def convertNetlist(sourceFile, targetFile):
    vhdl_item = []
    with open(sourceFile) as fptr1:
        value = fptr1.readlines()
        for item in value:
            new_item = item[0:-1]
            vh_item = verilog2vhdl(new_item)
            print(vh_item)
            vhdl_item.append(vh_item)


    fptr1.close()

    f = open(targetFile, 'w')
    string_val = ""
    for item in vhdl_item:
        string_val += item
        string_val += "\n"

    string_val = string_val[0:-1]

    f.write(string_val)

    f.close()






    #with open(targetFile) as fptr2:









if __name__ == "__main__":
    #verilog2vhdl("DFFSR Q_int1_reg ( .D(serial_in), .CLK(clk), .R(1), .S(n5), .Q(Q_int1) )")
    convertNetlist("verilog_test.v","vhdl_test.vhdl")
    #"Q_int1_reg: DFFSR PORT MAP(D=>serial_in, CLK=>clk, R=>1, S=>n5, Q=>Q_int1);"




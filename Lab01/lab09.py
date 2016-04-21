#! /usr/bin/env python3.4
__author__ = 'ee364h05'


import sys
import os
import string
import re
import collections


def outputTwoLines():
    outFilename = "finalGrades.xml"
    OutFile = open( outFilename, 'w' )
    filename = "rawGrades.xml"
    with open( filename, 'r' ) as inputFile:
        content = inputFile.readlines()
    for line in content[:2]:
        writeLine = line
        OutFile.write( writeLine )

#   Gets the entire file as a string
def getEntireFile():
	filename = "rawGrades.xml"
	LongString = ""
	with open( filename, 'r' ) as inputFile:
		content = inputFile.readlines()
	LongString = LongString.join(content)
	#print( LongString )

	return LongString

#   Gets details for every student
def getDetails():

    outFilename = "finalGrades.xml"
    OutFile = open( outFilename, 'a' )
    entireFile = getEntireFile();

    match = re.findall( r"<?(\w{3})>(\w* \w+):(.*)</?(.*)>", entireFile )

    #   Prints out first two lines from xml file
    lines = entireFile.split("\n")

    outputTwoLines()

    if match:
        #   New Student
        for element in match:
            #   element 0 :     ID
            #   element 1 :     Name
            #   element 2 :     Courses and grades
            #print( element )
            id = element[0]
            name = element[1]
            allCourses = element[2]
            closingId = element[3]
            #print( id + " : " + closingId)

            #   Check if line is valid
            if id == closingId:
                #   Output student header < name id >
                writeLine = "   <student name=\"" + name + "\" id=\"" + id + "\">\n"
                OutFile.write( writeLine )

                #   Regex for courses and grades
                allCourseList = re.findall( r"\[?(\w*):(\w*)\]?", allCourses )
                if allCourseList:
                    #   Check for retaken courses                                       ~~~~!!~~~~
                    allCourses = {}

                    #   Gets a list of all courses and grades for each student
                    for element in allCourseList:
                        #   element 0 :     Course Number
                        #   element 1 :     Grade
                        #print( element[0] + " : " + element[1] )
                        courseNum = element[0]
                        scoreTemp = element[1]

                        #   Put courses into dictionary
                        allCourses[ courseNum ] = scoreTemp


                        #   Write to file
                        #writeLine = "      <ECE" + courseNum + " score=\"" + score + "\" grade=\"" + grade + "\"/>\n"
                        #OutFile.write( writeLine )

                        pass
                    #   Sort the courses
                    allKeys = allCourses.keys()
                    keylist = []

                    for key in allKeys:
                        keylist.append( key )
                    keylist.sort()
                    #print( keylist)
                    for key in keylist:
                        courseNumber = key
                        score = allCourses[ key ]
                        #   Calculate grade
                        if int(score) < 60:
                            grade = "F"
                        elif int(score) < 70:
                            grade = "D"
                        elif int(score) < 80:
                            grade = "C"
                        elif int(score) < 90:
                            grade = "B"
                        else:
                            grade = "A"

                        writeLine = "      <ECE" + courseNumber + " score=\"" + score + "\" grade=\"" + grade + "\"/>\n"
                        OutFile.write( writeLine )
                OutFile.write("   </student>\n")

    OutFile.write("</students>")

def main():
    getDetails()

if __name__ == "__main__" :
    main()


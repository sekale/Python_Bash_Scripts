#! /usr/bin/env python3.4
#
#$Author: ee364a09 $
#$Date: 2016-03-01 12:32:29 -0500 (Tue, 01 Mar 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364a09/Lab06/applyRegEx.py $
#$Revision: 89150 $

import os
import glob
import re
import sys

def getRejectedUsers():
    pattern = re.compile(r"(([A-Za-z]+)(,?)([\s]{1,2})((\w)+))")
    pattern2 = re.compile(r"([\w.-]+@[\w.-]+)")
    pattern3 = re.compile(r"([\d]){10}")
    pattern4 = re.compile(r"([\d]{3})(-)([\d]{3})(-)([\d]{4})")
    pattern5 = re.compile(r"\(([\d]{3})\) ([\d]{3})(-)([\d]{4})")
    pattern6 = re.compile(r"((\w+)$|(\w+ \w+)$)")

    list_rejected = []
    with open("SiteRegistration.txt","r") as input:
        for line in input:
            match = re.match(pattern, line)

            match2 = re.search(pattern2, line)
            match3 = re.search(pattern3, line)
            match4 = re.search(pattern4, line)
            match5 = re.search(pattern5, line)
            match6 = re.search(pattern6, line)

            if match is not None:
                #print(match.group(0))
                #print (match.groups())
                #print(match.group(1))
                #print(match.group(2))
                #print(match.group(3))
                #print(match.group(4))
                #print(match.group(5))
                if(match.group(3) != ''):
                    str = match.group(5).strip() + ' ' + match.group(2).strip()
                    #print(str)
                else:
                    #print(match.group(4))
                    str = match.group(1).strip() + ' ' + match.group(4).strip()

            if match is not None and match2 is None and match3 is None and match4 is None and match5 is None and match6 is None:
                #print(match.group(1))
                if(str[-1]==' '):
                    str = str[0:-1]
                list_rejected.append(str)

    #for i in list_rejected:
     #   print(i)
    return sorted(list_rejected)

def getUsersWithEmails():
    pattern = re.compile(r"(([A-Za-z]+)(,?)([\s]{1,2})((\w)+))")
    pattern2 = re.compile(r"([\w.-]+@[\w.-]+)")
    dict_users = {}
    with open("SiteRegistration.txt","r") as input:
        for line in input:
            match = re.match(pattern, line)

            match2 = re.search(pattern2, line)
            #match3 = re.search(pattern3, line)
            #match4 = re.search(pattern4, line)
            #match5 = re.search(pattern5, line)
            #match6 = re.search(pattern6, line)

            if match is not None:
                #print(match.group(0))
                #print (match.groups())
                #print(match.group(1))
                #print(match.group(2))
                #print(match.group(3))
                #print(match.group(4))
                #print(match.group(5))
                if(match.group(3) != ''):
                    str = match.group(5).strip() + ' ' + match.group(2).strip()
                    #print(str)
                else:
                    #print(match.group(4))
                    str = match.group(1).strip() + ' ' + match.group(4).strip()

            if match is not None and match2 is not None:
                #print(match.group(1))
                if(str[-1]==' '):
                    str = str[0:-1]
                dict_users[str] = match2.group(0)

    return dict_users


def getUsersWithPhones():
    pattern = re.compile(r"(([A-Za-z]+)(,?)([\s]{1,2})((\w)+))")
    #pattern2 = re.compile(r"([\w.-]+@[\w.-]+)")
    pattern3 = re.compile(r"([\d]){10}")
    pattern4 = re.compile(r"([\d]{3})(-)([\d]{3})(-)([\d]{4})")
    pattern5 = re.compile(r"\(([\d]{3})\) ([\d]{3})(-)([\d]{4})")
    dict_users = {}
    with open("SiteRegistration.txt","r") as input:
        for line in input:
            match = re.match(pattern, line)

            #match2 = re.search(pattern2, line)
            match3 = re.search(pattern3, line)
            match4 = re.search(pattern4, line)
            match5 = re.search(pattern5, line)
            #match6 = re.search(pattern6, line)

            if match is not None:
                #print(match)
                #print(match.group(0))
                #print (match.groups())
                #print(match.group(1))
                #print(match.group(2))
                #print(match.group(3))
                #print(match.group(4))
                #print(match.group(5))
                if(match.group(3) != ''):
                    str = match.group(5).strip() + ' ' + match.group(2).strip()
                    #print(str)
                else:
                    #print(match.group(4))
                    str = match.group(1).strip() + ' ' + match.group(4).strip()

            if match is not None:
                #print(match.group(1))

                if(str[-1]==' '):
                    str = str[0:-1]
                if match3 is not None:
                    #print("here")
                    #print("3rd group user: " ,match3.group(0))

                    #print(match3.group(0))
                    count = 0
                    string = '('
                    for i in match3.group(0):
                        if(count <= 2):
                            string += i
                            count = count + 1
                        elif count > 2 and count <= 3:
                            string += ') '
                            string += i
                            count = count + 1
                        elif count > 3 and count <= 5:
                            string += i
                            count = count + 1
                        elif count > 5 and count <= 6:
                            string += '-'
                            string += i
                            count = count + 1
                        elif count >6:
                            string += i
                            count = count+1

                    dict_users[str] = string
                    #print(string)
                    #print(match3.group(2))
                elif match4 is not None:
                    #print("here")
                    #print(match4.group(0))
                    #print(match4.group(0))
                    string1 = match4.group(0)
                    string1 = string1.replace("-","")
                    #print(string1)

                    count = 0
                    string = '('
                    for i in string1:
                        if(count <= 2):
                            string += i
                            count = count + 1
                        elif count > 2 and count <= 3:
                            string += ') '
                            string += i
                            count = count + 1
                        elif count > 3 and count <= 5:
                            string += i
                            count = count + 1
                        elif count > 5 and count <= 6:
                            string += '-'
                            string += i
                            count = count + 1
                        elif count >6:
                            string += i
                            count = count+1


                    #print(string)
                    dict_users[str] = string
                elif match5 is not None:
                    #print("here")
                    #print(match5.group(0))
                    dict_users[str] = match5.group(0)

    #for i in dict_users:
     #   print("%s:"%i,dict_users[i])

    return dict_users

def getUsersWithStates():
    pattern = re.compile(r"(([A-Za-z]+)(,?)([\s]{1,2})((\w)+))")
    #pattern2 = re.compile(r"([\w.-]+@[\w.-]+)")
    pattern3 = re.compile(r"([\d]){10}")
    pattern4 = re.compile(r"([\d]{3})(-)([\d]{3})(-)([\d]{4})")
    pattern5 = re.compile(r"\(([\d]{3})\) ([\d]{3})(-)([\d]{4})")
    pattern6 = re.compile(r"((\w+)$|(\w+ \w+)$)")
    dict_users = {}
    with open("SiteRegistration.txt","r") as input:
        for line in input:
            match = re.match(pattern, line)

            #match2 = re.search(pattern2, line)
           # match3 = re.search(pattern3, line)
            #match4 = re.search(pattern4, line)
            #match5 = re.search(pattern5, line)
            match6 = re.search(pattern6, line)

            if match is not None:
                #print(match)
                #print(match.group(0))
                #print (match.groups())
                #print(match.group(1))
                #print(match.group(2))
                #print(match.group(3))
                #print(match.group(4))
                #print(match.group(5))
                if(match.group(3) != ''):
                    str = match.group(5).strip() + ' ' + match.group(2).strip()
                    #print(str)
                else:
                    #print(match.group(4))
                    str = match.group(1).strip() + ' ' + match.group(4).strip()

            if match is not None:
                #print(match.group(1))

                if(str[-1]==' '):
                    str = str[0:-1]
                if match6 is not None:
                    dict_users[str] = match6.group(0)

    return dict_users

def getUsersWithoutEmails():
    list_rejected = getRejectedUsers()
    list_users = []
    pattern = re.compile(r"(([A-Za-z]+)(,?)([\s]{1,2})((\w)+))")
    pattern2 = re.compile(r"([\w.-]+@[\w.-]+)")
    #dict_users = {}
    with open("SiteRegistration.txt","r") as input:
        for line in input:
            match = re.match(pattern, line)

            match2 = re.search(pattern2, line)
            #match3 = re.search(pattern3, line)
            #match4 = re.search(pattern4, line)
            #match5 = re.search(pattern5, line)
            #match6 = re.search(pattern6, line)

            if match is not None:
                #print(match.group(0))
                #print (match.groups())
                #print(match.group(1))
                #print(match.group(2))
                #print(match.group(3))
                #print(match.group(4))
                #print(match.group(5))
                if(match.group(3) != ''):
                    str = match.group(5).strip() + ' ' + match.group(2).strip()
                    #print(str)
                else:
                    #print(match.group(4))
                    str = match.group(1).strip() + ' ' + match.group(4).strip()

            if match is not None and match2 is None:
                #print(match.group(1))
                if(str[-1]==' '):
                    str = str[0:-1]
                if str not in list_rejected:
                    list_users.append(str)

    return sorted(list_users)

def getUsersWithoutStates():
    list_rejected = getRejectedUsers()
    list_users = []
    pattern = re.compile(r"(([A-Za-z]+)(,?)([\s]{1,2})((\w)+))")
    pattern2 = re.compile(r"([\w.-]+@[\w.-]+)")
    pattern3 = re.compile(r"([\d]){10}")
    pattern4 = re.compile(r"([\d]{3})(-)([\d]{3})(-)([\d]{4})")
    pattern5 = re.compile(r"\(([\d]{3})\) ([\d]{3})(-)([\d]{4})")
    pattern6 = re.compile(r"((\w+)$|(\w+ \w+)$)")
    with open("SiteRegistration.txt","r") as input:
        for line in input:
            match = re.match(pattern, line)

            match2 = re.search(pattern2, line)
            match3 = re.search(pattern3, line)
            match4 = re.search(pattern4, line)
            match5 = re.search(pattern5, line)
            match6 = re.search(pattern6, line)

            if match is not None:
                #print(match.group(0))
                #print (match.groups())
                #print(match.group(1))
                print(match.group(2))
                print(match.group(3))
                print(match.group(4))
                print(match.group(5))
                if(match.group(3) != ''):
                    str = match.group(5).strip() + ' ' + match.group(2).strip()
                    #print(str)
                else:
                    #print(match.group(4))
                    str = match.group(1).strip() + ' ' + match.group(4).strip()

            if match is not None and match6 is None:
                if match2 is not None or match3 is not None or match4 is not None or match5 is not None:
                #print(match.group(1))
                    if(str[-1]==' '):
                        str = str[0:-1]
                    if str not in list_rejected:
                        list_users.append(str)

    return sorted(list_users)

def getUsersWithoutPhones():
    dict_user_with_phones = getUsersWithPhones()

    list_rejected = getRejectedUsers()

    list_users = []

    pattern = re.compile(r"(([A-Za-z]+)(,?)([\s]{1,2})((\w)+))")
    pattern2 = re.compile(r"([\w.-]+@[\w.-]+)")
    pattern3 = re.compile(r"([\d]){10}")
    pattern4 = re.compile(r"([\d]{3})(-)([\d]{3})(-)([\d]{4})")
    pattern5 = re.compile(r"\(([\d]{3})\) ([\d]{3})(-)([\d]{4})")
    pattern6 = re.compile(r"((\w+)$|(\w+ \w+)$)")
    with open("SiteRegistration.txt","r") as input:
        for line in input:
            match = re.match(pattern, line)

            match2 = re.search(pattern2, line)
            match3 = re.search(pattern3, line)
            match4 = re.search(pattern4, line)
            match5 = re.search(pattern5, line)
            match6 = re.search(pattern6, line)

            if match is not None:
                #print(match.group(0))
                #print (match.groups())
                #print(match.group(1))
                #print(match.group(2))
                #print(match.group(3))
                #print(match.group(4))
                #print(match.group(5))
                if(match.group(3) != ''):
                    str = match.group(5).strip() + ' ' + match.group(2).strip()
                    #print(str)
                else:
                    #print(match.group(4))
                    str = match.group(1).strip() + ' ' + match.group(4).strip()

            if match is not None and match3 is None and match4 is None and match5 is None:
                if match2 is not None or match6 is not None:
                #print(match.group(1))
                    if(str[-1]==' '):
                        str = str[0:-1]
                    if str not in list_rejected:
                        list_users.append(str)

    return sorted(list_users)

def getUsersWithCompleteInfo():
    pattern = re.compile(r"(([A-Za-z]+)(,?)([\s]{1,2})((\w)+))")
    pattern2 = re.compile(r"([\w.-]+@[\w.-]+)")
    pattern3 = re.compile(r"([\d]){10}")
    pattern4 = re.compile(r"([\d]{3})(-)([\d]{3})(-)([\d]{4})")
    pattern5 = re.compile(r"\(([\d]{3})\) ([\d]{3})(-)([\d]{4})")
    pattern6 = re.compile(r"((\w+)$|(\w+ \w+)$)")
    dict_users = {}
    with open("SiteRegistration.txt","r") as input:
        for line in input:
            match = re.match(pattern, line)

            match2 = re.search(pattern2, line)
            match3 = re.search(pattern3, line)
            match4 = re.search(pattern4, line)
            match5 = re.search(pattern5, line)
            match6 = re.search(pattern6, line)

            if match is not None:
                #print(match)
                #print(match.group(0))
                #print (match.groups())
                #print(match.group(1))
                #print(match.group(2))
                #print(match.group(3))
                #print(match.group(4))
                #print(match.group(5))
                if(match.group(3) != ''):
                    str = match.group(5).strip() + ' ' + match.group(2).strip()
                    #print(str)
                else:
                    #print(match.group(4))
                    str = match.group(1).strip() + ' ' + match.group(4).strip()

            if match is not None and match2 is not None and match6 is not None:
                #print(match.group(1))

                if(str[-1]==' '):
                    str = str[0:-1]
                if match3 is not None:
                    #print("here")
                    #print("3rd group user: " ,match3.group(0))

                    #print(match3.group(0))
                    count = 0
                    string = '('
                    for i in match3.group(0):
                        if(count <= 2):
                            string += i
                            count = count + 1
                        elif count > 2 and count <= 3:
                            string += ') '
                            string += i
                            count = count + 1
                        elif count > 3 and count <= 5:
                            string += i
                            count = count + 1
                        elif count > 5 and count <= 6:
                            string += '-'
                            string += i
                            count = count + 1
                        elif count >6:
                            string += i
                            count = count+1


                    #print(string)
                    #print(match3.group(2))
                elif match4 is not None:
                    #print("here")
                    #print(match4.group(0))
                    #print(match4.group(0))
                    string1 = match4.group(0)
                    string1 = string1.replace("-","")
                    #print(string1)

                    count = 0
                    string = '('
                    for i in string1:
                        if(count <= 2):
                            string += i
                            count = count + 1
                        elif count > 2 and count <= 3:
                            string += ') '
                            string += i
                            count = count + 1
                        elif count > 3 and count <= 5:
                            string += i
                            count = count + 1
                        elif count > 5 and count <= 6:
                            string += '-'
                            string += i
                            count = count + 1
                        elif count >6:
                            string += i
                            count = count+1


                    #print(string)

                elif match5 is not None:
                    #print("here")
                    #print(match5.group(0))
                    string = match5.group(0)

            if match3 is not None or match4 is not None or match5 is not None:
                if match2 is not None and match6 is not None:
                    #print(match2.groups(0))
                    #print(match6.groups(0))
                    dict_users[str] = (match2.group(0),string,match6.group(0))


    #for i in dict_users:
     #   print("%s:"%i,dict_users[i])

    return dict_users


myscript.bash +v \i 2 +p /local/bin/somefolder

















if __name__ == "__main__" :
    getUsersWithPhones()

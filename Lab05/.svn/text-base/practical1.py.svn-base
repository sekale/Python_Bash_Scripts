import os
import sys
import glob
import string

def rowSumIsValid(mat):
    length = len(mat[0])
    print(len(mat[0]))
    list = []
    sum = 0
    prevsum = 0
    for i in range(0,length):
        sum = 0
        for j in range(0,length):
            sum = sum + mat[i][j]

        if sum not in list:
            list.append(sum)

    if len(list) == 1:
        return True

    else:
        return False


    return True

def columnSumIsValid(mat):
    length = len(mat[0])
    print(len(mat[0]))
    list = []
    sum = 0
    prevsum = 0
    for i in range(0,length):
        sum = 0
        for j in range(0,length):
            sum = sum + mat[j][i]

        if sum not in list:
            list.append(sum)

    if len(list) == 1:
        return True

    else:
        return False


    return True

def magicSquareIsValid(filePath):

    list = []
    name = filePath.split('.')
    #print(name)
    length_temp = name[0][13]
    length = int(length_temp)
    #print(length)
    for i in range(0,length):
        list.append([])

    #print(list)


    with open(filePath) as input:

        value = input.readlines()
        count = 0
        for i in range(0,length):

            value_new = value[i].split()
            for j in range(0,length):
                #print(int(value_new[i]))
                #print(count)
                #print(j)
                list[count].append(int(value_new[j]))
            count += 1

    if rowSumIsValid(list)== False:
        return False

    if columnSumIsValid(list) == False:
        return False

    return True

def getTotalCost(itemSet):
    dict = {}
    list = []
    list1 = []
    filenames = glob.glob("Stores/*")

    #b = [int(i[0]) for i in a]
    for tuple in itemSet:
        list.append(tuple[0])
    for tuple in itemSet:
        list1.append(tuple[1])

    #print(list)
    for file in filenames:
        with open(file) as fptr:
            store_name_temp = file.split('.')
            print(store_name_temp)
            store_name_temp_1 = store_name_temp[0].spilt('/')
            print(store_name_temp_1[1])
            store_name = store_name_temp_1[1].strip
            print(store_name)
            value = fptr.readlines()
            for line in value[3:]:
                value_line = line.split(',')
                cpu_name = value_line[0].strip()
                cpu_cost = value_line[0].strip()
                count = 0
                for j in list:
                    if(cpu_name == j):
                        total_cost = cpu_cost * list1[count]
                        dict[store_name] = total_cost
                    count = count+1

    #print(dict)
    return dict















if __name__ == "__main__" :

    square4 = [[16, 2, 3, 13],
           [5, 11, 10, 1],
           [9, 7, 6, 12],
           [4, 14, 15, 8]]

    square6 = [[35, 1, 6, 26, 19, 24],
           [3, 25, 7, 21, 23, 32],
           [31, 9, 2, 22, 27, 20],
           [8, 28, 33, 17, 10, 15],
           [30, 5, 34, 12, 14, 16],
           [4, 36, 29, 13, 18, 11]]
    #rowSumIsValid(square6)
    #filePath = "Squares/magic6.txt"
    #magicSquareIsValid(filePath)

    #itemSet = {('Intel i7-4960HQ', 9), ('Intel i7-6700HQ', 7), ('Intel i7-6970HQ', 3)}
    #getTotalCost(itemSet)
    cpuSet = {'Intel i7-6970HQ', 'Intel i7-6700TE', 'Intel i7-4860HQ', 'Intel i7-4870HQ', 'Intel i7-6700K'}
    getBestPrices(cpuSet)

import glob
import sys
import filecmp
import os

def getWordFrequency():
    ListFile = getFileName()
    word_dict = {}
    for I in ListFile:
        with open(I) as fp:
            Content = fp.readlines()
            fileContent = Content[0].split()
            for J in fileContent:
                if J not in word_dict:
                    word_dict[J] = 1
                else:
                    word_dict[J] += 1
    return word_dict



def getDuplicates():
    ListFile = getFileName()
    group_dict = {}
    names_read = []
    for name in ListFile:
        if name not in names_read:
            group = checkDuplicate(name, ListFile)
            names_read.append(group)
            length = len(group)
            if length > 1:
                group_key = group[0]
                group_path = "files/%s.txt"%(group_key)
                num_words = getWordCount(group_path)
                group_tuple = (num_words, group)
                group_dict[group_key] = group_tuple
    return group_dict

def getPurchaseReport():
    ItemCost_dict = {}
    PurchaseReport_dict = {}
    FileList = glob.glob('purchases/*')
    with open(FileList[0]) as fp:
        Content = fp.readlines()
        for I in range(2, len(Content)):
            ContentFile = Content[I].split()
            Cost = ContentFile[1].split('$')
            ItemCost_dict[ContentFile[0]] = float(Cost[1])
    for J in range(1, len(FileList)):
        index = FileList[J].find("0")
        key = int(FileList[J][(index + 1):(index + 3)])
        with open(FileList[J]) as fp:
            Content = fp.readlines()
            for K in range(2, len(Content)):
                ContentFile = Content[K].split()
                if key not in PurchaseReport_dict:
                    PurchaseReport_dict[key] = 0
                    PurchaseReport_dict[key] += ItemCost_dict[ContentFile[0]] * int(ContentFile[1])
                    PurchaseReport_dict[key] = round(PurchaseReport_dict[key], 2)
                else:
                    PurchaseReport_dict[key] += ItemCost_dict[ContentFile[0]] * int(ContentFile[1])
                    PurchaseReport_dict[key] = round(PurchaseReport_dict[key], 2)
    return PurchaseReport_dict

def getTotalSold():
    FileList = glob.glob('purchases/*')
    TotalSold_dict = {}
    for I in range(1, len(FileList)):
        with open(FileList[I]) as fp:
            Content = fp.readlines()
            for J in range(2, len(Content)):
                ContentFile = Content[J].split()
                if ContentFile[0] not in TotalSold_dict:
                    TotalSold_dict[ContentFile[0]] = 0
                    TotalSold_dict[ContentFile[0]] += int(ContentFile[1])
                else:
                    TotalSold_dict[ContentFile[0]] += int(ContentFile[1])
    return TotalSold_dict

def getFileName():
    FileList = glob.glob('files/*')
    return FileList

def checkDuplicate(name, ListFile):
    nameoffile = name[6:9]
    group = [nameoffile]
    for I in ListFile:
        if name != I:
            if filecmp.cmp(name, I):
                nameoffile = I[6:9]
                group.append(nameoffile)
    list.sort(group)
    return group

def getWordCount(groupKeyPath):
    word_count = 0
    new_str = ""
    new_wordlist = []
    word_dict = {}
    with open(groupKeyPath) as fp:
        string = fp.read()
        for I in string:
            if (ord(I) >= ord('a') and ord(I) <= ord('z')) or (ord(I) >= ord('A') and ord('Z')) or ord(I) == ord(' '):
                new_str += I
    new_wordlist = new_str.split()
    for J in new_wordlist:
        word_dict[J] = 1
    for key in word_dict:
        word_count += 1

    return word_count

if __name__ == "__main__" :
    getTotalSold()
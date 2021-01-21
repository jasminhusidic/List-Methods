"""
Author: Jasmin Husidic
File: listMethods.py
Description: Functions for list methods.
"""

def myCount(myList,item):
    count = 0
    for word in myList:
        if word == item:
            count += 1
    return count


def myIndex(myList,item):
    count = 0
    for word in myList:
        if word != item:
            count += 1
        elif word == item:
            return count
    if count == len(myList):
        return -1

def contains(myList,item):
    for word in myList:
        if word == item:
            return True
    return False
               
         
def myInsert(myList,index,item):
    if index < 0:
        return myList
    else:
        newList = myList[0:index]+[item]+myList[index:]
        return newList
    

def myReverse(myList):
    output = []
    length = len(myList)
    for index in range(length):
        word = myList[length - index - 1]
        output = output + [word]
    return output

# Sidonia Stanton
# Nov 5 2024
# HW 6: Tool Belt


def countEvens(aList):
    counter = 0
    for i in aList:
        if i % 2 == 0:
            counter += 1
    return counter



def countLarger(numArray, x):
    numCounter = 0
    for i in numArray:
        if i > x:
            numCounter += 1
    return numCounter




def isPalindrome(aString):
    aString = aString.lower()
    for i in range(len(aString)):
        oneBack = (aString[len(aString)-1-i])
        forward = (aString[i]) # i is an index of list
        if oneBack != forward:
            return False
    return True    

# Sidonia Stanton
# Nov 5 2024
# HW 6: Tool Belt


def countEvens(aList):
    counter = 0
    for i in aList:
        if i % 2 == 0:
            counter += 1
    return counter

x = countEvens([2,5,7, 8,10])
print(x)
print(countEvens([10,5,20]))


numArray = []
x = ()
listSize = len(numArray)
def countLarger(numArray):
    numCounter = 0
    for i in numArray:
        if i > x:
            numCounter += 1
    return numCounter

x = 4 
numArray = [2, 6, 34, 60]
numLarger = countLarger(numArray)
print(numLarger)



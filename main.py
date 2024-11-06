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


def fibGenerator(raySize):
    if raySize < 2:
        return []
    twoNumbers = [0,1]
    for i in range (raySize-2):
        fibNum = twoNumbers[i] + twoNumbers[i+1]
        twoNumbers.append(fibNum)
    return twoNumbers

    

def main():
    print(countEvens([4,6,1,3,9,10]))
    print(countEvens([4,6,100,0,9,10]))
    print(countLarger([1,100,80,20],20))
    print(countLarger([1,5,4,80,20],20))
    print(isPalindrome("Racecar"))
    print(isPalindrome("HelloWorld"))
    print(fibGenerator(1))
    print(fibGenerator(10))
    print(fibGenerator(15))

main()
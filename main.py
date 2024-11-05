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
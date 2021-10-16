"""
Your job is to write a function which increments a string, to create a new string.

If the string already ends with a number, the number should be incremented by 1.
If the string does not end with a number. the number 1 should be appended to the new string.
Examples:

foo -> foo1

foobar23 -> foobar24

foo0042 -> foo0043

foo9 -> foo10

foo099 -> foo100

Attention: If the number has leading zeros the amount of digits should be considered.
"""


strng = "foobar00"

def increment_string(strng):
    numberOfZeros = 0
    tempNumber = 0
    tempString = ""
    zeros = ""

    for x in strng:
        if x.isdigit():
            if int(x) == 0:
                numberOfZeros += 1
            else:
                tempNumber = str(tempNumber) + x
        else:
            tempString += x
        pass
    
    # increment number
    tempNumber = int(tempNumber) + 1

    # create zero string
    for y in range(numberOfZeros):
        zeros += str(0)
    
    # form new string
    strng = tempString + zeros + str(tempNumber) 

    return strng

print(increment_string(strng))
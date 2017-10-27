#
# Input 3 Numbers and print the average of the numbers
#

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
firstNum = input("Please enter first number: ")
if is_number(firstNum):
    firstNum = float(firstNum)
else:
    print("First number is not a number")
    
secNum = input("Please enter second number: ")
if is_number(secNum):
    secNum = float(secNum)
else:
    print("Second number is not a number")
    
thirdNum = input("Please enter third number: ")
if is_number(thirdNum):
    thirdNum = float(thirdNum)
else:
    print("Third number is not a number")

if is_number(firstNum) and is_number(secNum) and is_number(thirdNum):
    avg = (firstNum + secNum + thirdNum)/ 3
    print("The average of", firstNum,",", secNum, "and", thirdNum, "is", avg)
else:
    print("One or all of the inputs where not a number, end of program!")



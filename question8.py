# Q8. Write a function that handles the ValueError exception that may be raised when trying to convert a string to an integer. The function should prompt the user to enter a new string until a valid integer is entered.
#
# Input: '3'
# Output: 3
#
# Input: 'abc'
# Output: ValueError exception handled, new input prompted.

runcode=True
while(runcode):
    input_number=input("enter a number")
    try:
        print(type(input_number))
        number=int(input_number)
        runcode=False
        print(number)
        print(type(number))
    except:
        input_number=input("enter a number")
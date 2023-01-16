
# Q7. Write a function that takes a list of numbers and returns the sum of the numbers that are divisible by 3 or 5. The function should use a generator expression to accomplish this.
#
# Input: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Output: 33
#
# Input: [0, 15, 30, 45, 60, 75, 90, 105]
# Output: 330

def generate_sum(listdata):
    sum=0
    for number in listdata:
        if(number%3==0 or number%5==0):
            sum=sum+number
    yield sum

#list_data=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,7]
list_data=[0, 15, 30, 45, 60, 75, 90, 105]
for value in generate_sum(list_data):
    print(value)
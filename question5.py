
# Q5. Write a function or lambda function (preferably) that takes a list of strings and returns a new list with all strings sorted in descending order of length.
#
# Input: ["dog", "cat", "bird"]
# Output: ['bird', 'cat', 'dog']
#
# Input: ["python", "java", "c++"]
# Output: ["python", "java", "c++"]


myList = ["python", "java", "c++"]

myList.sort(key=lambda myStr: len(myStr), reverse=True)
print(myList)
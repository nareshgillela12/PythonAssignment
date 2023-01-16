
# Q1. Write a program that reads in all the lines of the file (take any random or article from wikipedia), and then create a dictionary, where the key is the line number and value is another dictionary. This another dictionary should contain length of the words as keys, and the number of words having same length as values.
#
# Example, first line in the file: "The quick brown fox jumps over the lazy dog"
#
# output - {
#     1: {
#         3: 4  # This is comment for explaination. There are four words having 3 chars - the, fox, the, dog
#         5: 3  # This is comment for explaination. There are 3 words having 5 chars - quick, brown, jumps
#         4: 2  # This is comment for explaination. There are 2 words having 4 chars - over, lazy
#     }
# }



lines = open("textdata.txt").read().splitlines()
linenumber=0
main_dict={}

for line in lines:
    loopdict={}
    linenumber=linenumber+1
    wordslength=[len(word) for word in line.split(" ")]
    set_length=set()
    for length in wordslength:
        set_length.add(length)
    #print(set_length)
    for slength in set_length:
        wordscount = 0
        for word in line.split(" "):
            #wordscount=1
            if(slength==len(word)):
                wordscount=wordscount+1
            #loopdict[slength].append(wordscount)
            loopdict.update({slength:wordscount})
        main_dict.update({linenumber:loopdict})
print(main_dict)









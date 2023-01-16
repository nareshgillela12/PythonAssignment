# Q6.Write a function that reads in a CSV file and returns a list of dictionaries, where each dictionary represents
# a row in the CSV file with the keys being the column names and the values being the cell values.
# Example
# Input: CSV file containing the following data:
# id, name, age
# 1, Alice, 20
# 2, Bob, 25
# 3, Charlie, 30
# Output: [{'id': '1', 'name': 'Alice', 'age': '20'},
#          {'id': '2', 'name': 'Bob', 'age': '25'},
#          {'id': '3', 'name': 'Charlie', 'age': '30'}]


# added csv file testdata.csv in soltion.

import csv

content = []
csvReader = csv.DictReader(open("testdata.csv"))
for row in csvReader:
    # print(row)
    content.append(row)

print(content)
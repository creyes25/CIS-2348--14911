# Carolina Reyes
# 1563200

# Write a program that first reads in the name of
# an input file and then reads the file using the csv.reader() method.
# The file contains a list of words separated by commas.
# Your program should output the words and their frequencies
# (the number of times each word appears in the file) without any duplicates.


# import statement will import csv
import csv

# allows the user to input the file they want the program to read
Name_file = input()

# added a dictionary so that it can store the elements from file
frequency = {}

# open() allows you to open the file the user inputted and also reads it
with open(Name_file, 'r') as input_file:
    reader = csv.reader(input_file)

# reads the names in the output and counts the number of times that name appears
    for line in reader:
        for name in line:

            if name not in frequency.keys():
                frequency[name] = 1

            else:
                frequency[name] = frequency[name] + 1
# prints the amount of times the name appears
for amount in frequency.keys():
    print(amount, str(frequency[amount]))

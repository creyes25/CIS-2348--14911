
# Carolina Reyes
# 1563200
# Write a program that reads a list of words. Then, the program outputs those words and their frequencies.

# user inputs words
user_input = input()
# the inputs are separated
list_words = user_input.split()

# created an empty list
words = []

# for loop will add the frequency number of each word in the words list
for items in list_words:
    words.append(list_words.count(items))

    # for loop get the position of the frequencies and is assigned to freq
    # to be able to display it line by line
    for pos in words:
        freq = '{}'.format(pos)
    print(items, freq)  # prints both the word and frequency number

# Carolina Reyes
# 1563200

# A palindrome is a word or a phrase that is the same when read both forward and backward.
# Examples are: "bob," "sees," or "never odd or even" (ignoring spaces).
# Write a program whose input is a word or phrase, and that outputs whether the input is a palindrome.

# split will separate the words and remove the white spaces
phrase = input()
remove = phrase.split()
joining = ''.join(remove)  # join will join all the words together with no whitespaces
backwards = joining[::-1]  # [::-1] will display the words backwards

# if else statement will display if it is a palindrome or not
if joining == backwards:
    print(phrase, 'is a palindrome')
else:
    print(phrase, 'is not a palindrome')

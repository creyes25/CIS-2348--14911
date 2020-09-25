
# Carolina Reyes
# 1563200

# assign variable to necessary information
user_pass = input()
password = ''
append = 'q*s'

# create an else if loop for characters that we want to change
for pass_1 in user_pass:
    if pass_1 == 'i':
        pass_1 = '!'
        password += pass_1

    elif pass_1 == 'a':
        pass_1 = '@'
        password += pass_1

    elif pass_1 == 'm':
        pass_1 = 'M'
        password += pass_1

    elif pass_1 == 'B':
        pass_1 = '8'
        password += pass_1

    elif pass_1 == 'o':
        pass_1 = '.'
        password += pass_1
# else statement will print all the characters that were not change plus the character that were
    else:
        password += pass_1

# it is going to print the new updated password plus the append that needs to be added at end of password
print(password+append)

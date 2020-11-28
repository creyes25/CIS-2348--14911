

# Carolina Reyes
# 1563200

# The given program reads a list of single-word first names and ages
# (ending with -1), and outputs that list with the age incremented.
# The program fails and throws an exception if the second input on a line
# is a string rather than an integer.
# At At FIXME in the code, add try and except blocks to catch the ValueError exception and output 0 for the age.


# Split input into 2 parts: name and age
parts = input().split()
name = parts[0]

# while statement to end program when input is -1
while name != '-1':
    # increase age by 1
    # except: adds a Value error the second part of the input is not an integer
    try:
        age = int(parts[1]) + 1
    except ValueError:
        age = 0
    print('{} {}'.format(name, age))

    # Get next line
    parts = input().split()
    name = parts[0]

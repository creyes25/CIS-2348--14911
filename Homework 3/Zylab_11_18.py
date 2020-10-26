
# Carolina Reyes
# 1563200

# Write a program that gets a list of integers from input, and outputs
# non-negative integers in ascending order (lowest to highest).

# user inputs all the numbers
user_input = input()
user_list = user_input.split()

# creates a list
nums = []

# turns the numbers from str to integers
for numbers in user_list:
    nums.append(int(numbers))
    for num in nums:
        if num < 0: # will grab all the negative number and delete them
            nums.remove(num)
    nums.sort()  # it will then sort the list in order

print(str(nums)[1:-1].replace(',', ''), end=' ')

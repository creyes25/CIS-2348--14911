
# Carolina Reyes
# 1563200

# Write the function selection_sort_descend_trace() that takes an integer list
# and sorts the list into descending order. The function should use nested loops and
# output the list after each iteration of the outer loop,
# thus outputting the list N-1 times (where N is the size).
#
# Complete __main__ to read in a list of integers, and then call selection_sort_descend_trace() to sort the list.


# function for selection sort
# will find the highest number and move it to the front
def selection_sort_descend_trace(numbers):
    for i in range(len(numbers) - 1):
        large = i
        for j in range(i + 1, len(numbers)):
            if numbers[j] > numbers[large]:
                large = j

        temp = numbers[i]
        numbers[i] = numbers[large]
        numbers[large] = temp

        # prints each iteration
        for num1 in numbers:
            print(num1, end=' ')
        print()

    return numbers


if __name__ == "__main__":
    numbers = input().split()  # creates a list
    numbers = [int(i) for i in numbers]  # convert string into integer
    selection_sort_descend_trace(numbers)  # call the function

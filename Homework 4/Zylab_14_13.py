
# Carolina Reyes
# 1563200

# Given code that reads user IDs (until -1), complete the quicksort() and
# partition() functions to sort the IDs in ascending order using
# the Quicksort algorithm. Increment the global variable num_calls
# in quicksort() to keep track of how many times quicksort() is called.
# The given code outputs num_calls followed by the sorted IDs


# Global variable
num_calls = 0


# function that partition the list in half until it sorts the list
def partition(user_ids, i, k):
    #  Picks the middle element as the pivot
    midpoint = i + (k - i) // 2
    pivot = user_ids[midpoint]

    #  Initialize variables
    done = False
    c = i
    h = k
    # while statements whether the
    while not done:
        #  Increment c while names[c] < pivot
        while user_ids[c] < pivot:
            c = c + 1
        #  Decrement h while pivot < names[h]
        while pivot < user_ids[h]:
            h = h - 1

        if c >= h:
            done = True
        else:
            """  Swap numbers[c] and numbers[h],

                     update c and h """
            temp = user_ids[c]
            user_ids[c] = user_ids[h]
            user_ids[h] = temp
            c = c + 1
            h = h - 1
    return h


# function that sorts the partitions.
# will sort high and low partitions
def quicksort(user_ids, i, k):
    global num_calls  # calls in the global variable
    num_calls += 1  # counts how many times the quicksort gets called
    if i >= k:
        return

    j = partition(user_ids, i, k)

    quicksort(user_ids, i, j)
    quicksort(user_ids, j + 1, k)
    return


if __name__ == "__main__":
    # allows user to input
    user_ids = []
    user_id = input()
    # while statement if the user inputs -1 will stop asking to input and will add to list
    while user_id != "-1":
        user_ids.append(user_id)
        user_id = input()

    # calls the quick sort function
    quicksort(user_ids, 0, len(user_ids) - 1)

    # Print number of calls to quicksort
    print(num_calls)

    # Prints the sorted list
    for user_id in user_ids:
        print(user_id)


# Carolina Reyes
# 1563200

# Write a program with total change amount as an integer input that outputs the change using the fewest coins,
# one coin type per line. The coin types are dollars, quarters, dimes, nickels, and pennies. Use singular and
# plural coin names as appropriate, like 1 penny vs. 2 pennies.
# our program must define and call the following function. The function exact_change() should return num_dollars,
# num_quarters, num_dimes, num_nickels, and num_pennies.
# def exact_change(user_total)


# added a function to the all the calculations
def exact_change(user_total):
    # added an if-else statement that if the input is less than 0 than it would be no change if is false
    # then it will calculate the cents
    if user_total <= 0:
        print('no change')
    else:
        dollar1 = user_total // 100
        quarter = (user_total % 100) // 25
        dime = (user_total % 100 % 25) // 10
        nickel = (user_total % 100 % 25 % 10) // 5
        pennies = (user_total % 100 % 25 % 10 % 5)
    # added a nested while loop with if statements so that the appropriate name comes out if its is more than one
    while user_total > 0:
        if dollar1 == 1:
            print(dollar1, "dollar")
        elif dollar1 == 0:
            pass
        else:
            print(dollar1, "dollars")
        if quarter == 1:
            print(quarter, 'quarter')
        elif quarter == 0:
            pass
        else:
            print(quarter, 'quarters')
        if dime == 1:
            print(dime, "dime")
        elif dime == 0:
            pass
        else:
            print(dime, 'dimes')
        if nickel == 1:
            print(nickel, "nickel")
        elif nickel == 0:
            pass
        else:
            print(nickel, 'nickels')
        if pennies == 1:
            print(pennies, "penny")
        elif pennies == 0:
            pass
        else:
            print(pennies, 'pennies')
        break  # break the loop
    return dollar1, quarter, dime, nickel, pennies  # allows all the results to exit the function


# Calls the function
if __name__ == '__main__':
    exact_change(int(input()))

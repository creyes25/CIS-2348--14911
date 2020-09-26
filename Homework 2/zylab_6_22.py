
# Carolina Reyes
# 1563200

# 6.22 CIS 2348 LAB: Brute force equation solver
# Numerous engineering and scientific applications require finding solutions to a set of equations.
# Ex: 8x + 7y = 38 and 3x - 5y = -1 have a solution x = 3, y = 2.
# Given integer coefficients of two linear equations with variables x and y,
# use brute force to find an integer solution for x and y in the range -10 to 10.


# allows the user to input the numbers for the equation
x_1 = int(input(''))
y_1 = int(input(''))
total_1 = int(input())
x_2 = int(input(''))
y_2 = int(input(''))
total_2 = int(input(''))

# variable is defined to be able to out a no solution if there is none
final_solution = ''

# for loop is being used to assign a variable to range
# while loop statement will help determine if the x and y has a solution and final_solution equal to solution
for x in range(-10, 11):
    for y in range(-10, 11):
        while ((x_1 * x) + (y_1 * y)) == total_1 and ((x_2 * x) + (y_2 * y)) == total_2:
            print(x, y)
            final_solution = 'solution'
            break  # breaks the while loop so it wont create a infinite loop

# if statement that if there is no solution that is what it will print 
if final_solution != 'solution':
    print('No solution')





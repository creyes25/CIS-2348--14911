
# Carolina Reyes
# 1563200


import math  # imports math functions

# set to where the user inputs the height and width
wall_height = int(input('Enter wall height (feet):\n'))
wall_width = int(input('Enter wall width (feet):\n'))

# calculates the square feet by multiplying the height and width
wall_area = wall_height * wall_width
print('Wall area:', wall_area, 'square feet')

# calculates the paint needed with a floating point of 2
paint_needed = (wall_area / 350)
print('Paint needed:', '{:.2f}'.format(paint_needed), 'gallons')

cans_needed = math.ceil(wall_area / 350)
print('Cans needed:', cans_needed, 'can(s)\n')

# dictionary for al the colors and their corresponding prices
colors = {'red': '$35', 'blue': '$75', 'green': '$23'}

# user inputs a color of paint
choose_color = input("Choose a color to paint the wall:\n")

# it prints the color chosen and the price of that paint color
print('Cost of purchasing', choose_color, 'paint:', colors[choose_color])


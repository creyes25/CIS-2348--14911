
# Carolina Reyes
# 1563200

import math
wall_height = int(input('Enter wall height (feet):\n'))
wall_width = int(input('Enter wall width (feet):\n'))
gallon = 350

wall_area = wall_height * wall_width
print('Wall area:', wall_area, 'square feet')

paint_needed = (wall_area / gallon)
print('Paint needed:', '{:.2f}'.format(paint_needed), 'gallons')

cans_needed = math.ceil(wall_area / 350)
print('Cans needed:', cans_needed, 'can(s)\n')

colors = {'red': '$35', 'blue': '$75', 'green': '$23'}

choose_color = input("Choose a color to paint the wall:\n")
print('Cost of purchasing', choose_color, 'paint:', colors[choose_color])


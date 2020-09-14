
# Carolina Reyes
# 1563200

lemon_juice = float(input('Enter amount of lemon juice (in cups):\n'))
water = float(input('Enter amount of water (in cups):\n'))
agave_nectar = float(input('Enter amount of agave nectar (in cups):\n'))
servings = float(input('How many servings does this make?\n'))

print('\nLemonade ingredients - yields ' '{:.2f}'.format(servings), 'servings')

print('{:.2f}'.format(lemon_juice), 'cup(s) lemon juice')
print('{:.2f}'.format(water), 'cup(s) water')
print('{:.2f}'.format(agave_nectar), 'cup(s) agave nectar\n')

serving_1 = float(input('How many servings would you like to make?\n'))

print('\nLemonade ingredients - yields ''{:.2f}'.format(serving_1), 'servings')
print('{:.2f}'.format((lemon_juice * serving_1) / servings), 'cup(s) lemon juice')
print('{:.2f}'.format((water * serving_1) / servings), 'cup(s) water')
print('{:.2f}'.format((agave_nectar * serving_1) / servings), 'cup(s) agave nectar')


print('\nLemonade ingredients - yields ''{:.2f}'.format(serving_1), 'servings')
print('{:.2f}'.format((lemon_juice * (serving_1 / servings))/16), 'gallon(s) lemon juice')
print('{:.2f}'.format((water * (serving_1 / servings))/16), 'gallon(s) water')
print('{:.2f}'.format((agave_nectar * (serving_1 / servings))/16), 'gallon(s) agave nectar')

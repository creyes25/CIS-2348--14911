
# Carolina Reyes
# 1563200

# prints the tittle and sub tittle
print('Birthday Calculator')
print('Current day')

# user inputs the current date
current_month = int(input('Month: '))
current_day = int(input('Day: '))
current_year = int(input('Year: '))

# user inputs their birthdate
print('Birthday')
b_day_month = int(input('Month: '))
b_day_day = int(input('Day: '))
b_day_year = int(input('Year: '))

# calculates the age
age = (current_year - b_day_year) - ((current_month, current_day) < (b_day_month, b_day_day))

# prints the age
print('You are', age, 'years old.')

# determines if it is their birthday
if current_month == b_day_month and current_day == b_day_day:
    print('Happy Birthday!')


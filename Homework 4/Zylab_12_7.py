
# Carolina Reyes
# 1563200

# Write a program that calculates an adult's fat-burning heart rate, which is 70% of 220 minus the person's age.
# Complete fat_burning_heart_rate() to calculate the fat burning heart rate.
# The adult's age must be between the ages of 18 and 75 inclusive. If the age entered is not in this range,
# raise a ValueError exception in get_age() with the message "Invalid age."
# Handle the exception in __main__ and print the ValueError message along with "Could not calculate heart rate info."


# function calculates the heart rate
def fat_burning_heart_rate(age):
    burning = (220 - age) * .70
    return burning


# user inputs age
# if-else statement requiring the age to be between 18 and 75
# if age in not in between 18 and 75 then use raise Value Error
def get_age():
    age = int(input())
    if 18 < age < 75:
        return age
    else:
        raise ValueError('Invalid age.')


if __name__ == '__main__':

    try:
        range_age = get_age()  # calls function
        heart_rate = fat_burning_heart_rate(range_age)  # calls function
        # Displays sentence
        print('Fat burning heart rate for a {} year-old: {} bpm'.format(range_age, heart_rate))

        # if age is not between 18 and 75 this will display
    except ValueError as excpt:
        print(excpt)
        print('Could not calculate heart rate info.')
        print()

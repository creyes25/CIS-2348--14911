# Carolina Reyes
# 1563200

# create an empty dictionary, empty list
soccer_rating = {}
sort_list = []
players = 1


# function to output the roster in order
def Output_roster():
    print('ROSTER')
    for index in sort_list:
        print('Jersey number: {}, Rating: {}'.format(index, soccer_rating[index]))
    return


# allows user to input number and rating with in the range
for players in range(1, 6):
    jersey_number = int(input("Enter player {}'s jersey number:\n".format(players)))
    if jersey_number < 0 or jersey_number > 99:
        print('Invalid')
        jersey_number = int(input("Enter player {}'s jersey number:\n".format(players)))

    rating = int(input("Enter player {}'s rating:\n".format(players)))
    print()
    if rating < 0 or rating > 9:
        print('Invalid')
        rating = int(input("Enter player {}'s rating:\n".format(players)))

    soccer_rating[jersey_number] = rating  # adds the inputs in the dictionary
# for loop to get hte keys from the dictionary and put it in a list
for keys in soccer_rating.keys():
    sort_list.append(keys)
    sort_list.sort()  # sorts the jersey numbers in order

# Calls the roster function
Output_roster()


# function to add players
def add_player():
    new_number = int(input('Enter a jersey number:'))

    new_rating = int(input('Enter a new rating for player'))
    if (new_number < 0 or new_number > 99) and (new_rating < 0 or new_rating > 9):
        soccer_rating.update({new_number: new_rating})


# function to remove player
def remove():
    print()


# function to update
def update():
    print()


def Output_players():
    print()


# displays the menu so user can choose a option from the menu
menu = ('\nMENU\n'
        'a - Add player\n'
        'd - Remove player\n'
        'u - Update player rating\n'
        'r - Output players above a rating\n'
        'o - Output roster\n'
        'q - Quit\n')

choose = ' '
# while loop statements that prints the menu
# if statements, so that functions can be called when a certain choice is inputted
while choose != 'q':
    print(menu)
    choose = str(input('Choose an option:\n'))
    if choose == 'a':
        add_player()

    elif choose == 'd':
        remove()

    elif choose == 'u':
        update()

    elif choose == 'r':
        Output_players()

    elif choose == 'o':
        Output_roster()
    elif choose == 'q':
        break

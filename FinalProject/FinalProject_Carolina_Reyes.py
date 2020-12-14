
# Carolina Reyes
# 1563200

# import csv will allow the code to read and write csv files.
import csv
# import datetime allows dates to be imported and is easier to compare the dates
from datetime import datetime

items = {}  # an initial dictionary to append all the information from the files that re being read
ManufacturersList = []  # adds information from the manufacturing name file
PriceList = []  # adds information from the prices file
ServiceDate_list = []  # adds information from the Service Date file

# with open('', 'r') opens the csv files and reads them and then for loop too add it to the corresponding list
# it then closes the file
with open('ManufacturerList.csv', 'r') as rfile:
    reader1 = csv.reader(rfile)
    for row in reader1:
        ManufacturersList.append(row)

    rfile.close()

with open('PriceList.csv', 'r') as rfile2:
    reader1 = csv.reader(rfile2)
    for row in reader1:
        PriceList.append(row)

    rfile2.close()

with open('ServiceDatesList.csv', 'r') as rfile3:
    reader1 = csv.reader(rfile3)
    for row in reader1:
        ServiceDate_list.append(row)

    rfile3.close()

    # It grabs all the lists and adds them to the items dictionary
    for line in ManufacturersList:
        item_id = line[0]  # first index of the list is the ID number
        items[
            item_id] = {}  # creates a new dictionary to be able to add all items with the same ID into this dictionary
        manufact_name = line[1]
        item_type = line[2]
        damaged = line[3]
        items[item_id] = {}
        items[item_id]['manufacturer_name'] = manufact_name.strip()  # adds a title to the values of manufacturers
        items[item_id]['item_type'] = item_type.strip()  # adds a title to the values of item type -
        items[item_id]['damaged'] = damaged  # adds a title to the values of items that are damaged
    for line1 in PriceList:
        item_id = line1[0]
        price = line1[1]
        items[item_id]['price'] = int(price)  # makes the prices into integers
    for line2 in ServiceDate_list:
        item_id = line2[0]
        service_date = line2[1]
        items[item_id]['service_date'] = service_date  # adds a title to the values of their service dates

    # creates a new file and writes in the file
    # grabs the information from the dictionary and place all the items in order
    with open('FullInventory.csv', 'w') as wfile:
        # sorts the manufacturing names in order
        keys = sorted(items.keys(), key=lambda x: items[x]['manufacturer_name'])
        # grabs all the keys and values from the dictionary to be able to write it into the file
        for item in keys:
            id = item
            manufact_name = items[item]['manufacturer_name']
            item_type = items[item]['item_type']
            damaged = items[item]['damaged']
            price = items[item]['price']
            service_date = items[item]['service_date']
            wfile.write('{},{},{},{},{},{}\n'.format(id, manufact_name, item_type, price, service_date, damaged))

    # creates a new file and writes in the file
    # grabs the information from the dictionary and place all the items in order
    with open('PastServiceDateInventory.csv', 'w') as wfile2:
        # sorts by service dates (from oldest to recent)
        keys = sorted(items.keys(), key=lambda x: datetime.strptime(items[x]['service_date'], "%m/%d/%Y").date())
        # grabs all the keys and values from the dictionary to be able to write it into the file
        for item in keys:
            id = item
            manufact_name = items[item]['manufacturer_name']
            item_type = items[item]['item_type']
            price = items[item]['price']
            damaged = items[item]['damaged']
            service_date = items[item]['service_date']
            today = datetime.now().date()  # grabs the current date
            date = datetime.strptime(service_date,
                                     "%m/%d/%Y").date()  # grabs the service dates from each item and formats it
            expired = date < today  # checks if service date is expired
            if expired:
                wfile2.write('{},{},{},{},{},{}\n'.format(id, manufact_name, item_type, price, service_date, damaged))

    # creates a new file and writes in the file
    # grabs the information from the dictionary and place all the items in order
    with open('DamagedInventory.csv', 'w') as wfile3:
        # gets sorted by price and uses the reverse=True to make the list go from highest price to lowest
        keys = sorted(items.keys(), key=lambda x: items[x]['price'], reverse=True)
        # grabs all the keys and values from the dictionary to be able to write it into the file
        for item in keys:
            id = item
            manufact_name = items[item]['manufacturer_name']
            item_type = items[item]['item_type']
            price = items[item]['price']
            service_date = items[item]['service_date']
            damaged = items[item]['damaged']
            if damaged:
                wfile3.write('{},{},{},{},{}\n'.format(id, manufact_name, item_type, price, service_date))

    # creates a new file and writes in the file
    # grabs the information from the dictionary and place all the items in order
    I_types = []  # creating a list to put all the item type in one list
    for item in items:
        item_type = items[item]['item_type']
        if item_type not in I_types:
            I_types.append(item_type)  # adds the item type that is on the list to the I_types list
    # for loop that goes through eat item type in the list
    for type in I_types:
        keys = sorted(items.keys())
        with open(type.capitalize() + 'Inventory.csv',
                  'w') as typeinventory:  # open files and names it by each item type
            for item in keys:
                id = item
                manufact_name = items[item]['manufacturer_name']
                price = items[item]['price']
                service_date = items[item]['service_date']
                damaged = items[item]['damaged']
                item_type = items[item]['item_type']
                if type == item_type:
                    typeinventory.write('{},{},{},{},{}\n'.format(id, manufact_name, price, service_date, damaged))

type_item = I_types  # uses existing list to look through all the item types that are in the inventory
manuf_name = []  # create a new list to append only the manufacturers names that are in the inventory
final_list = []  # initial list that appends the words that the user inputs, but only if they are in the inventory
list = []  # initial list that appends the items that are in the final_list and extra information from the dictionary
consider = {}  # initial dictionary to append items to be able to find prices that are close to the item that wasn't
# in the inventory

# for loop to append all the manufacturers name in the manuf_name list
for item in items:
    name = items[item]['manufacturer_name']
    if name not in manuf_name:
        manuf_name.append(name)

# allows user to input
input_user = input('Enter Manufacturer and Inventory Type or q to quit: ')
user = input_user.split()  # splits the input into seperate words and adds them into a list


# a while loop to start the query
while input_user != 'q':

    if input_user == 'q':
        break
    else:
        # goes trough the input words and if they are in both manufacturer
        # and type list then it will get appened to the final_list
        for name in user:
            for type in user:
                if name in manuf_name and type in type_item:
                    man = name
                    i_type = type
                    final_list.append(man)
                    final_list.append(i_type)

    # if the input was not then that means that the final_list is empty meaning that the input is not in the inventory
    if name and type not in final_list:
        print('No such item in inventory')
    else:
        # wiil display the user item in order by price
        keys = sorted(items.keys(), key=lambda x: items[x]['price'], reverse=True)
        for item in keys:
            if items[item]['item_type'] == i_type:  # looks in the dictionary that the item is in the inventory
                is_damaged = items[item]['damaged']  # checks if that item is damaged
                if items[item]['manufacturer_name'] == man:  # looks in the dictionary that the name is in the inventory
                    if is_damaged:  # if the item is damaged then it tells user is damaged and prints another altenative
                        print('This item is damaged')
                        consider[item] = items[item]
                        # ps. I'm having issues here. It displays the item that was inputted even if it is damaged
                        # it basically doesn't show a similar item than from the damaged item
                        for item_consider in consider:
                            ID_item = item_consider
                            name_man = consider[item_consider]['manufacturer_name']
                            type_I = consider[item_consider]['item_type']
                            i_price = consider[item_consider]['price']

                        print('You may, also, consider: {}, {}, {}, {}\n'.format(ID_item, name_man, type_I, i_price))
                        break

                    else:
                        list.append((item, items[item]))  # if the item is not damaged the it appends it into a list

        # it displays the item that was inputted with all of its information
        if list:
            item = list[0]
            ID = item[0]
            man_name = item[1]['manufacturer_name']
            t_item = item[1]['item_type']
            i_price = item[1]['price']
            print('Your item is: {}, {}, {}, {}\n'.format(ID, man_name, t_item, i_price))

    # user continues to input item manufacturer to check information until they input q to quit the loop
    input_user = input('Enter Manufacturer and Inventory Type or q to quit: ')
    user = input_user.split()
    list.clear()

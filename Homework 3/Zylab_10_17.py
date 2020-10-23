
# Carolina Reyes
# 1563200

# (1) Build the ItemToPurchase class with the following specifications:
#
# Attributes (3 pts)
# item_name (string)
# item_price (float)
# item_quantity (int)
# Default constructor (1 pt)
# Initializes item's name = "none", item's price = 0, item's quantity = 0
# Method
# print_item_cost()

# (2) In the main section of your code, prompt the user for two items
# and create two objects of the ItemToPurchase class. (2 pts)

# (3) Add the costs of the two items together and output the total cost. (2 pts)

# creates a class
class ItemToPurchase:
    # initializes the constructors
    def __init__(self, item_name='none', item_price=0, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    # creates a class method to make the calculation of of the total price
    # displays the information

    def print_item_cost(self):
        cost = self.item_price * self.item_quantity
        print('{} {} @ ${} = ${}'.format(self.item_name, self.item_quantity, self.item_price, cost))


if __name__ == '__main__':
    # call the class function and user inputs all the information for Item 1
    item_1 = ItemToPurchase()
    print('Item 1')
    item_1.item_name = input('Enter the item name:\n')
    item_1.item_price = int(input('Enter the item price:\n'))
    item_1.item_quantity = int(input('Enter the item quantity:\n'))

    # call the class function and user inputs all the information for Item 2
    item_2 = ItemToPurchase()
    print('\nItem 2')
    item_2.item_name = input('Enter the item name:\n')
    item_2.item_price = int(input('Enter the item price:\n'))
    item_2.item_quantity = int(input('Enter the item quantity:\n'))
    print()

    # Function adds all the prices together
    Total = (item_1.item_quantity * item_1.item_price) + (item_2.item_quantity * item_2.item_price)

    # prints the Total cost
    print('TOTAL COST')
    item_1.print_item_cost()
    item_2.print_item_cost()
    print()

    print('Total: ${}'.format(Total))

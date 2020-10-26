# Carolina Reyes
# 1563200

# creates a class
class ItemToPurchase:
    # constructor
    def __init__(self, item_name='none', item_price=0, item_quantity=0, item_description='none'):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    # prints the the item name, quantity and total price
    def print_item_cost(self):
        cost = self.item_price * self.item_quantity
        print('{} {} @ ${} = ${}'.format(self.item_name, self.item_quantity, self.item_price, cost))

    # prints description
    def print_item_description(self):
        print('{}: {}, %d oz.'.format(self.item_name, self.item_description, self.item_quantity))


# new class
class ShoppingCart:
    # constructor
    def __init__(self, customer_name='none', current_date='January 1, 2016', cart_items=None):
        if cart_items is None:
            cart_items = []
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = cart_items

    # method to add items to the cart
    def add_item(self):
        print('ADD ITEM TO CART')

        item_name = str(input('Enter the item name:'))
        print()
        item_description = str(input('Enter the item description:'))
        print()
        item_price = int(input('Enter the item price:'))
        print()
        item_quantity = int(input('Enter the item quantity:'))
        print()

        self.cart_items.append(ItemToPurchase(item_name, item_price, item_quantity, item_description))

    # method to remove items to the cart
    def remove_item(self):
        global flag
        print('REMOVE ITEM FROM CART')

        item_to_remove = str(input('Enter name of item to remove:'))
        print()
        n = 0

        for name_item in self.cart_items:

            if name_item.item_name == item_to_remove:
                del self.cart_items[n]
                flag = True
                break

            else:
                flag = False
            n += 1

        # if the item is not found
        if not flag:
            print('Item not found in cart. Nothing removed.')

    # method to modify items to the cart
    def modify_item(self):
        global flags
        print('CHANGE ITEM QUANTITY')

        name_of_item = str(input('Enter the item name:'))
        print()

        for name_item in self.cart_items:

            if name_item.item_name == name_of_item:
                quantity = int(input('Enter the new quantity:'))
                print()
                name_item.item_quantity = quantity
                flags = True
                break

            else:
                flags = False

        if not flags:
            print('Item not found in cart. Nothing modified.')
        print()

    # method to get number of items in the cart
    def get_num_items_in_cart(self):
        number_items = 0
        for name_item in self.cart_items:
            number_items += name_item.item_quantity

        return number_items

    # gets the cost of everything that is in the cart
    def get_cost_of_cart(self):
        total_cost = 0

        for name_item in self.cart_items:
            cost = (name_item.item_quantity * name_item.item_price)
            total_cost += cost

        return total_cost

    # prints the total amount from everything in the cart
    def print_total(self):
        total_cost = self.get_cost_of_cart()
        if total_cost == 0:
            print('SHOPPING CART IS EMPTY')
        else:
            self.output_cart()

    # method to print description
    def print_descriptions(self):
        print('OUTPUT ITEMS\' DESCRIPTIONS')
        print('{}\'s Shopping Cart - {}'.format(self.customer_name, self.current_date), end='\n')
        print('\nItem Descriptions')

        for name_item in self.cart_items:
            print('{}: {}'.format(name_item.item_name, name_item.item_description))

    # method displays everything that is in cart
    def output_cart(self):
        print('OUTPUT SHOPPING CART')
        print('{}\'s Shopping Cart - {}'.format(self.customer_name, self.current_date))
        print('Number of Items:', self.get_num_items_in_cart())
        print()
        total_c = 0
        for name_item in self.cart_items:
            print('{} {} @ ${} = ${}'.format(name_item.item_name, name_item.item_quantity,
                                             name_item.item_price, (name_item.item_quantity * name_item.item_price)))
            total_c += (name_item.item_quantity * name_item.item_price)

        if len(self.cart_items) == 0:
            print('SHOPPING CART IS EMPTY')
        print()

        print('Total: ${}'.format(total_c))


# prints the menu
def print_menu(customer_Cart):
    menu = ('\nMENU\n'
            'a - Add item to cart\n'
            'r - Remove item from cart\n'
            'c - Change item quantity\n'
            'i - Output items\' descriptions\n'
            'o - Output shopping cart\n'
            'q - Quit\n')

    choose = ''
# allows the user to choose anything from the menu until they quit it
    while choose != 'q':
        print(menu)

        choose = input('Choose an option:')
        print()

        while (choose != 'a' and choose != 'o' and choose != 'i' and choose != 'r'
               and choose != 'c' and choose != 'q'):
            choose = input('Choose an option:')
            print()

        if choose == 'a':
            customer_Cart.add_item()

        if choose == 'o':
            customer_Cart.output_cart()

        if choose == 'i':
            customer_Cart.print_descriptions()

        if choose == 'r':
            customer_Cart.remove_item()
        if choose == 'c':
            customer_Cart.modify_item()

# prints all the information needed

def main():
    customer_name = str(input('Enter customer\'s name:'))
    print()

    current_date = str(input('Enter today\'s date:'))
    print('\n')

    print('Customer name:', customer_name, end='\n')
    print('Today\'s date:', current_date, end='\n')

    Cart_new = ShoppingCart(customer_name, current_date)

    print_menu(Cart_new)


# Calls the main()
if __name__ == '__main__':
    main()

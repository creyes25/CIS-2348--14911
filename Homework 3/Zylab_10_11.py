# Carolina Reyes
# 1563200

# Complete the FoodItem class by adding a constructor to initialize a food item. T
# he constructor should initialize the name to "None" and all other instance attributes to 0.0 by default.
# If the constructor is called with a food name, grams of fat, grams of carbohydrates,
# and grams of protein, the constructor should assign each instance attribute with the appropriate parameter value.
#
# The given program accepts as input a food item name, fat, carbs,
# and protein and the number of servings. The program creates a food item
# using the constructor parameters' default values and a food item using the input values. T
# he program outputs the nutritional information and calories per serving for both food items.

# Initiates a class to have all definitions organized
class FoodItem:
    # default argument
    def __init__(self, name='None', fat=0.0, carbs=0.0, protein=0.0):  # initializes the parameters
        self.name = name
        self.fat = fat
        self.carbs = carbs
        self.protein = protein

    # calculate the calories
    def get_calories(self, num_servings):
        # Calorie formula
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * num_servings
        return calories

    # prints all the information of name, fat, carbs, protein
    def print_info(self):
        print('Nutritional information per serving of {}:'.format(self.name))
        print('   Fat: {:.2f} g'.format(self.fat))
        print('   Carbohydrates: {:.2f} g'.format(self.carbs))
        print('   Protein: {:.2f} g'.format(self.protein))


if __name__ == '__main__':
    item1 = FoodItem()   # calls the class

# user inputs all the necessary information
    name_item = input()
    fat_amount = float(input())
    carbs_amount = float(input())
    protein_amount = float(input())
    item2 = FoodItem(name_item, fat_amount, carbs_amount, protein_amount)

    num_servings = float(input())

# prints the print_info and the calculation of calories 
    item1.print_info()
    print('Number of calories for {:.2f} serving(s): {:.2f}'.format(num_servings, item1.get_calories(num_servings)))
    print()
    item2.print_info()
    print('Number of calories for {:.2f} serving(s): {:.2f}'.format(num_servings, item2.get_calories(num_servings)))

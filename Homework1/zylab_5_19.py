
# Carolina Reyes
# 1563200

# assigned variables to the prices
oil_change = '$35'
tire_rotation = '$19'
car_wash = '$7'
car_wax = '$12'

# dictionary was made to list all the prices for each service
services = {'Oil change': 35, 'Tire rotation': 19, 'Car wash': 7, 'Car wax': 12, '-': 0}

# prints the services and prices
print("Davy's auto shop services")
print('Oil change -- $35')
print('Tire rotation -- $19')
print('Car wash -- $7')
print('Car wax -- $12\n')

# tells the user to input first service and second service
first_service = input('Select first service:\n')
second_service = input('Select second service:\n')

print("\nDavy's auto shop invoice\n")

# used if-else if-else statements for the selection of services
if first_service == 'Oil change':
    print('Service 1: Oil change,', oil_change)
elif first_service == 'Tire rotation':
    print('Service 1: Tire rotation,', tire_rotation)
elif first_service == 'Car wash':
    print('Service 1: Car wash,', car_wash)
elif first_service == 'Car wax':
    print('Service 1: Car wax:', car_wax)
else:
    print('Service 1: No service')


if second_service == 'Oil change':
    print('Service 2: Oil change,', oil_change)
elif second_service == 'Tire rotation':
    print('Service 2: Tire rotation,', tire_rotation)
elif second_service == 'Car wash':
    print('Service 2: Car wash,', car_wash)
elif second_service == 'Car wax':
    print('Service 2: Car wax,', car_wax)
else:
    print('Service 2: No service')

# calculates the sum of both services
total = services[first_service] + services[second_service]

# prints the total
print('\nTotal: $', total, sep="")




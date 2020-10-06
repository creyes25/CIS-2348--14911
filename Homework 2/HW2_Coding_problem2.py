
# Carolina Reyes
# 1563200

dates_inputs = open(input(), 'r')
dates_outputs = open('parsedDates.txt', 'w')

Listings = ['January', 'February', 'March', 'April', 'May', 'June',
            'July', 'August', 'September', 'October', 'November', 'December']

for inputs in dates_inputs:
    if inputs == '-1':
        break

    lists = inputs.split()
    if len(lists) >= 3:
        month = lists[0]
        day = lists[1]
        year = lists[2]
        d, comma = day.split(',')


dates_inputs.close()
dates_outputs.close()
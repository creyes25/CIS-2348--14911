
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

    for months in range(12):
        if inputs.find(Listings[months]) >=0:
            month_number = str(months + 1)
            day = day[:- 1]
            output_list = month_number + "/" + day + "/" + year
            dates_outputs.write(output_list)
            dates_outputs.write("\n")
            
dates_inputs.close()
dates_outputs.close()

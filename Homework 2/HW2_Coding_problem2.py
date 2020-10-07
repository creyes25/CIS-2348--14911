
# Carolina Reyes
# 1563200

# open the file the user inputs and reads it
# opens a new file where the output will be written
dates_inputs = open(input(), 'r')
dates_outputs = open('parsedDates.txt', 'w')

# a array so that the Months can be identified later on
Listings = ['January', 'February', 'March', 'April', 'May', 'June',
            'July', 'August', 'September', 'October', 'November', 'December']

# if -1 appears in a any file it will stop it
for inputs in dates_inputs:
    if inputs == '-1':
        break

# it will split the inputs from the file and arrange them in order
    lists = inputs.split()
    if len(lists) >= 3:
        month = lists[0]
        day = lists[1]
        year = lists[2]

# gets all the data and formats it to mm/dd/yyyy
    for months in range(12):
        if inputs.find(Listings[months]) >= 0:
            month_number = str(months + 1)
            day = day[:- 1]
            output_list = month_number + "/" + day + "/" + year
            dates_outputs.write(output_list)  # writes the new format into the new file
            dates_outputs.write("\n")         # adds a new line after ever output

# closes both files
dates_inputs.close()
dates_outputs.close()



# Carolina Reyes
# 1563200

import csv
from datetime import datetime

items = {}
ManufacturersList = []
PriceList = []
ServiceDate_list = []

with open('ManufacturerList.csv', 'r') as file:
    reader1 = csv.reader(file)
    for row in reader1:
        ManufacturersList.append(row)

with open('PriceList.csv', 'r') as file2:
    reader1 = csv.reader(file2)
    for row in reader1:
        PriceList.append(row)

with open('ServiceDatesList.csv', 'r') as file3:
    reader1 = csv.reader(file3)
    for row in reader1:
        ServiceDate_list.append(row)

    for line in ManufacturersList:
        item_id = line[0]
        items[item_id] = {}
        manufact_name = line[1]
        item_type = line[2]
        damaged = line[3]
        items[item_id] = {}
        items[item_id]['manufacturer_name'] = manufact_name.strip()
        items[item_id]['item_type'] = item_type.strip()
        items[item_id]['damaged'] = damaged
    for line1 in PriceList:
        item_id = line1[0]
        price = line1[1]
        items[item_id]['price'] = price
    for line2 in ServiceDate_list:
        item_id = line2[0]
        service_date = line2[1]
        items[item_id]['service_date'] = service_date

    with open('FullInventory.csv', 'w') as file:
        keys = sorted(items.keys(), key=lambda x: items[x]['manufacturer_name'])
        keys.sort()
        for item in keys:
            id = item
            manufact_name = items[item]['manufacturer_name']
            item_type = items[item]['item_type']
            damaged = items[item]['damaged']
            price = items[item]['price']
            service_date = items[item]['service_date']
            file.write('{},{},{},{},{},{}\n'.format(id, manufact_name, item_type, price, service_date, damaged))

    with open('PastServiceDateInventory.csv', 'w') as file:
        keys = sorted(items.keys(), key=lambda x: datetime.strptime(items[x]['service_date'], "%m/%d/%Y").date())
        for item in keys:
            id = item
            manufact_name = items[item]['manufacturer_name']
            item_type = items[item]['item_type']
            price = items[item]['price']
            damaged = items[item]['damaged']
            service_date = items[item]['service_date']
            today = datetime.now().date()
            date = datetime.strptime(service_date, "%m/%d/%Y").date()
            expired = date < today
            if expired:
                file.write('{},{},{},{},{},{}\n'.format(id, manufact_name, item_type, price, service_date, damaged))

    with open('DamagedInventory.csv', 'w') as file:
        keys = sorted(items.keys(), key=lambda x: items[x]['price'])
        for item in keys:
            id = item
            manufact_name = items[item]['manufacturer_name']
            item_type = items[item]['item_type']
            price = items[item]['price']
            service_date = items[item]['service_date']
            damaged = items[item]['damaged']
            if damaged:
                file.write('{},{},{},{},{}\n'.format(id, manufact_name, item_type, price, service_date))

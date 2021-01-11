import csv
with open("main.csv", "r") as f:
    reader = csv.reader(f,delimiter=',')
    i=0
    for row in reader:
        i+=1
        if "USA" in row[-1] or i == 1:
            with open('filteredCountry.csv', 'a+', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(row)

group= list()
with open("filteredCountry.csv", "r") as f:
    reader = csv.reader(f,delimiter=',')
    i=0
    for row in reader:
        i+=1
        group.append(row[0])
    group = list(dict.fromkeys(group))
    # print(group[1])

for grp_i, grp in enumerate(group):
        # print(grp)
    if grp=="SKU":
            continue
    price = list()
    with open("filteredCountry.csv", "r") as f:
        reader = csv.reader(f,delimiter=',')
        for index,row in enumerate(reader):
            if index==0:
                continue
            if row[0]=="SKU":
                continue
            if int(grp) == int(row[0]) :
                row[5]=row[5].replace(",","")
                row[5]=row[5].replace("?","")
                row[5]=row[5].replace("$","")
                price.append(row[5])
    # print(price)
    with open('lowestPrice.csv', 'a+', newline='') as file:
        writer = csv.writer(file)
        if grp_i==1:
                writer.writerow(["SKU","FIRST_MINIMUM_PRICE","SECOND_MINIMUM_PRICE"])
        if len(price) == 1:
            price[0] = f"${price[0]}"
            writer.writerow([grp,price[0],price[-1]])
        else:
            price[0] = f"${price[0]}"
            price[1] = f"${price[1]}"
            writer.writerow([grp,price[0],price[1]])
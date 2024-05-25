import csv
with open("budget_data.csv", 'r') as pybank:
    csvreader = csv.reader(pybank, delimiter=',')
    header = next(csvreader)
    print(header)
    for i in range(4):
        print(next(csvreader))
    print("----")
    
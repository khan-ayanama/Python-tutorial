from csv import reader

with open('file1.csv', 'r') as f:
    csv_reader = reader(f)
    next(csv_reader)
    for row in csv_reader:
        print(row)

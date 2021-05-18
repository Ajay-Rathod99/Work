from csv import DictReader

with open('csv_file.csv') as f:
    csv_reader = DictReader(f)

    for rows in csv_reader:
        print(rows['name'])
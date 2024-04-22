# import csv
#
# with open('resource/eggs.csv') as csv_file:
#     csvreader = csv.reader(csv_file)
#     for row in csvreader:
#         print(row)
#
#
# with open('resource/new_csv.csv', 'w') as csv_file:
#     csvwriter = csv.writer(csv_file, delimiter=';')
#     csvwriter.writerow(['Anna', 'Bob', 'Charlie'])
#     csvwriter.writerow(['Alex', 'Sita', 'Zara'])
#
# with open('resource/new_csv.csv') as csv_file:
#     csvreader = csv.reader(csv_file)
#     for row in csvreader:
#         print(row)


import csv

# Чтение данных из CSV файла
with open('resource/eggs.csv') as csv_file:
    csvreader = csv.reader(csv_file)
    for row in csvreader:
        if row:  # Проверка на непустую строку
            print(row)

# Запись данных в CSV файл
with open('resource/new_csv.csv', 'w') as csv_file:
    csvwriter = csv.writer(csv_file, delimiter=';')
    csvwriter.writerow(['Anna', 'Bob', 'Charlie'])
    csvwriter.writerow(['Alex', 'Sita', 'Zara'])

# Чтение данных из нового CSV файла
with open('resource/new_csv.csv') as csv_file:
    csvreader = csv.reader(csv_file)
    for row in csvreader:
        if row:  # Проверка на непустую строку
            print(row)

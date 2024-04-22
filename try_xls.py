import xlrd

# Открываем файл XLS
book = xlrd.open_workbook('resource/file_example_XLS_10.xls')

print(f'Количество листов: {book.nsheets}')
print(f'Имена листов: {book.sheet_names()}')
sheet = book.sheet_by_index(0)
print(f'Количество колонок: {sheet.ncols}')
print(f'Количество строк: {sheet.nrows}')
print(f'Пересечение строки и столбца {sheet.cell_value(rowx=3, colx=1)}')
for rx in range(sheet.nrows):
    print(sheet.row(rx))

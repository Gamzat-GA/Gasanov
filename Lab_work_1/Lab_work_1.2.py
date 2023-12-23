disk_capacity_Mb = 1.44
lists = 100
strings = 50
simbols_in_string = 25
symbol_capacity_b = 4

# Объем диска в байтах
disk_capacity_b = disk_capacity_Mb * 1024 ** 2

# Объем одной книги
book_capacity = symbol_capacity_b * simbols_in_string * strings * lists

# Количество книг, помешающихся на диске
books_quantity = int(disk_capacity_b/book_capacity)

# TODO Найдите количество книг, которое можно разместить на дискете

print("Количество книг, помещающихся на дискету:", books_quantity)

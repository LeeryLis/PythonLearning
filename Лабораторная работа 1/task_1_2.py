# Информационный объем дискеты в байтах
diskette_size_bytes = 1.44 * 1024 * 1024

# Параметры книги
pages_per_book = 100
lines_per_page = 50
characters_per_line = 25
bytes_per_character = 4

# Размер одной книги в байтах
book_size_bytes = pages_per_book * lines_per_page * characters_per_line * bytes_per_character

# Количество книг, которые могут поместиться на дискете
num_books = int(diskette_size_bytes // book_size_bytes)

print("Количество книг, помещающихся на дискету:", num_books)

# Выведите все строки данного входного файла в обратном порядке.
# Для этого считайте список всех строк при помощи метода readlines().
#
# Последняя строка входного файла заканчивается символом '\n'.
#
# Ссылка на входной файл: https://stepik.org/media/attachments/lesson/258918/input.txt

data = open('input4.txt', 'r')
s = data.readlines()
s.reverse()
print(''.join(s).strip('\n'))

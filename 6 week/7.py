# Выведите в обратном порядке содержимое всего файла полностью.
# Для этого считайте файл целиком при помощи метода read().
#
# Ссылка на входной файл: https://stepik.org/media/attachments/lesson/258921/input.txt

data = open('input7.txt', 'r')
u = data.read()
print(u[::-1])

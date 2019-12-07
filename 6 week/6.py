# В качестве ответа введите все строки наибольшей длины из входного файла, не меняя их порядок.
#
# В данной задаче удобно считать список строк входного файла целиком при помощи метода readlines().
#
# Ссылка на входной файл: https://stepik.org/media/attachments/lesson/258920/input.txt

with open('input6.txt') as file:
    text = file.readlines()

maxlen = max(len(line) for line in text)
print(*filter(lambda line: len(line) == maxlen, text))

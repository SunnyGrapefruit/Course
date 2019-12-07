# Дан файл. Определите сколько в нем букв (латинского алфавита), слов, строк.
# Выведите три найденных числа в формате, приведенном в примере.
# Словом считается последовательность больших и маленьких латинских букв (для проверки того, состоит ли строка только из латинских букв удобно пользоваться методом isalpha()).
# Все остальные символы считаются разделителями слов.
#
# Ссылка на входной файл: https://stepik.org/media/attachments/lesson/258919/input.txt

letters = words = lines = 0  # counters
inword = False
with open('input5.txt', 'r') as f:
    for line in f:
        for char in line:
            if char.isalpha():
                letters += 1
                if not inword:
                    inword = True
                    words += 1
            else:
                inword = False

        lines += 1

print('Input file contains:')
print(letters, 'letters')
print(words, 'words')
print(lines, 'lines')

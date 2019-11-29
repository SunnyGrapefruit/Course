# Дан текст на языке племени Мумба-Юмба.
# Выведите все слова, встречающиеся в тексте, разделяя их пробелом.
# Слова должны быть отсортированы по убыванию их количества появления в тексте, а при одинаковой частоте появления — в алфавитном порядке.
#
# Подсказка.
# После того, как вы создадите словарь всех слов, вам захочется отсортировать его по частоте встречаемости слова.
# Желаемого можно добиться, если создать список, элементами которого будут кортежи из двух элементов: частота встречаемости слова и само слово.
# Например, [(2, 'hi'), (1, 'what'), (3, 'is')].
# Тогда стандартная сортировка будет сортировать список кортежей, при этом кортежи сравниваются по первому элементу, а если они равны — то по второму.
# Это почти то, что требуется в задаче, а чтобы сделать то что нужно — вспомните про параметр key в сортировке.
#
# В этой задачи нужно сдать только ответ для входного файла.
# Ссылка на входной файл https://stepik.org/media/attachments/lesson/258916/input.txt

data = open('input.txt', 'r')
words = {}
for line in data:
    new = line.split()
    for i in range(len(new)):
        if new[i] not in words:
            words[new[i]] = 1
        else:
            words[new[i]] += 1

spisok = []
for key, value in words.items():
    aKey = key
    aValue = value
    c = (aKey, aValue)
    spisok.append(c)

pairs = [(-pair[1], pair[0]) for pair in spisok]
wor = [pair[1] for pair in sorted(pairs)]
print('\n'.join(wor))

f = open('output.txt', 'w')
for i in wor:
    f.write(i + '\n')

# print(s)
    # f.write('{}:{}\n'.format(key, value))

# print(sorted(regions.items(), key=lambda x: x[1])[-1][0], sorted(proffs.items(), key=lambda x: x[1])[-1][0], sep=' ')

from collections import Counter



# data = open('input.txt', 'r')
# for line in data:
#     words = line.split()
#     for i in range(len(words)):
#         if words[i] not in words:



# for _ in range(int(input())):
#     words.extend(input().split())

# counter = Counter(words)
# pairs = [(-pair[1], pair[0]) for pair in counter.most_common()]
# words = [pair[1] for pair in sorted(pairs)]
# print('\n'.join(words))




# spisok = []
#
# for key, value in words.items():
#     aKey = key
#     aValue = value
#     c = (aKey, aValue)
#     spisok.append(c)
#     s0 = sorted(spisok)
#     s1 = sorted(s0, key=lambda x: x[1], reverse=True)
#     for ke, val in s1:
#         f.write('{}:{}\n'.format(ke, val))


# def makey(x):
#     return x[1]
#
#
# fin = open('input.txt', 'r', encoding='utf8')
# spisok = []
# counter = {}
# for line in fin:
#     a = list(line.split())
#     # print(a)
#     for i in a:
#         if i not in counter:
#             counter[i] = 1
#         else:
#             counter[i] += 1
# # print(counter)
# fin.close()
#
#
#
# list_d = sorted(counter.items(), key=lambda x: x[1], reverse=True)
# d = sorted(list_d)
# # print(d)
# # print(list_d)
#
# with open('output.txt', 'w') as out:
#     for i in d:
#         x = i[0]
#         out.write(x + '\n')

# with open('output.txt', 'w') as out:
#     for key, value in d.items():
#         out.write('{}:{}\n'.format(key, value))

        # aKey = key
        # aValue = value
        # c = (aKey, aValue)
        # spisok.append(c)
        # s0 = sorted(spisok)
        # s1 = sorted(s0, key=makey, reverse=True)
        # for i in s1:
        #     x = i[0]
        #     # out.write('{}:{}\n'.format(key,value))
        #     out.write(x + '\n')


# f = open('output.txt', 'w')
# for i in counter.items():
#     f.write(i[0])

# f = open('output.txt', 'w')
#
# for key, value in counter.items():
#     aKey = key
#     aValue = value
#     c = (aKey, aValue)
#     spisok.append(c)
#     s0 = sorted(spisok)
#     s1 = sorted(s0, key=makey, reverse=True)
#     for i in s1:
#         x = i[0]
#         f.write(x + '\n')


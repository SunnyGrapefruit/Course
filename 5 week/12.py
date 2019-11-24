# Дана строка.
# Выведите слово, которое в этой строке встречается чаще всего.
# Если таких слов несколько, выведите то, которое меньше в лексикографическом (алфавитном) порядке.

d = {}
for word in input().split():
    d[word] = d.get(word, 0) + 1

max_count = max(d.values())
most_frequent = [k for k, v in d.items() if v == max_count]
print(min(most_frequent))
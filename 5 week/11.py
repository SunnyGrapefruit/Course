# На вход подается строка.
# Словом считается последовательность непробельных символов идущих подряд, слова разделены одним или большим числом пробелов или символами конца строки.
# Для каждого слова из этого текста подсчитайте, сколько раз оно встречалось в этом тексте ранее.

d = {}
for word in input().split():
    d[word] = d.get(word, 0) + 1
    print(d[word] - 1, end=' ')

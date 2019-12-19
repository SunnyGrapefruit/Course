# Файл https://stepik.org/media/attachments/lesson/209719/2.html содержит статью с Википедии про язык Python.
# В этой статье есть теги code, которыми выделяются конструкции на языке Python.
# Вам нужно найти все строки, содержащиеся между тегами <code> и </code> и найти те строки, которые встречаются чаще всего и вывести их в алфавитном порядке, разделяя пробелами.
#
# Например, если исходный текст страницы выглядел бы так:

from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

s, d = [], []

resp = urlopen('https://stepik.org/media/attachments/lesson/209719/2.html')
html = resp.read().decode('utf8')
soup = BeautifulSoup(html, 'html.parser')
for link in soup.find_all('code'):
    t = link.text
    s.append(t)

f = (max(s.count(i) for i in s))

for i in s:
    if s.count(i) == f:
        d.append(i)

print(*sorted(set(d)))
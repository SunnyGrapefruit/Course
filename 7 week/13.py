# В этой задаче достаточно вам необходимо найти все внутренние ссылки, которые есть в обеих статьях: https://stepik.org/media/attachments/lesson/258943/Moscow.html и https://stepik.org/media/attachments/lesson/258944/New-York.html и вывести их в алфавитном порядке по одной в строке.
#
# Обратите внимание, что если ссылка встречается в статье несколько раз, то учитывать ее нужно лишь однажды.

from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup


def url_count(url):
    u = []
    resp = urlopen(url)
    html = resp.read().decode('utf8')
    soup = BeautifulSoup(html, 'html.parser')
    for link in soup.find_all('a'):
        if link.has_attr('href'):
            s = link.get('href')
            if s.startswith('/w') and ':' not in s and not s.startswith('#'):
                u.append(s)
    return u


data = open('output13.txt', 'w', encoding='utf8')

url1 = url_count('https://stepik.org/media/attachments/lesson/258943/Moscow.html')
url2 = url_count('https://stepik.org/media/attachments/lesson/258944/New-York.html')

s = list(set(url1) & set(url2))
s.sort()

for i in s:
    print(i, file=data)

data.close()
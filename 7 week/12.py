# В этой задаче достаточно вам необходимо посчитать количество внутренних ссылок, которые есть в обеих статьях: https://stepik.org/media/attachments/lesson/258943/Moscow.html и https://stepik.org/media/attachments/lesson/258944/New-York.html
#
# Обратите внимание, что если ссылка встречается в статье несколько раз, то учитывать ее нужно лишь однажды, т.е. необходимо найти количество различных страниц википедии, на которых есть ссылка как из первой, так и из второй статьи.

from urllib.request import urlopen
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


url1 = 'https://stepik.org/media/attachments/lesson/258943/Moscow.html'
url2 = 'https://stepik.org/media/attachments/lesson/258944/New-York.html'

i = url_count(url1)
o = url_count(url2)

s = list(set(i) & set(o))
print(len(s))
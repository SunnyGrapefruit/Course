# В этой задаче достаточно обернуть в функцию то, что делает предыдущая и вызвать подсчет числа внутренних ссылок для двух статей: https://stepik.org/media/attachments/lesson/258943/Moscow.html и https://stepik.org/media/attachments/lesson/258944/New-York.html
#
# В качестве ответа на задачу введите два числа через пробел.

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
    return len(u)

url1 = 'https://stepik.org/media/attachments/lesson/258943/Moscow.html'
url2 = 'https://stepik.org/media/attachments/lesson/258944/New-York.html'

print(url_count(url1), url_count(url2))
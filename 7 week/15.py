# В файле https://stepik.org/media/attachments/lesson/209723/4.html находится одна таблица.
# Просуммируйте все числа в ней.
# Теперь мы добавили разных тегов для изменения стиля отображения.
# Для доступа к ячейкам используйте возможности BeautifulSoup.

from urllib.request import urlopen
from bs4 import BeautifulSoup

g = 0

resp = urlopen('https://stepik.org/media/attachments/lesson/209723/4.html')
html = resp.read().decode('utf8')
soup = BeautifulSoup(html, 'html.parser')
for number in soup.find_all('td'):
    s = int(number.text)
    g += s

print(g)
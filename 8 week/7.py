# Вася решил открыть АЗС (заправку).
# Чтобы оценить уровень конкуренции он хочет изучить количество заправок в интересующем его районе.
# Вася скачал интересующий его кусок карты OSM https://stepik.org/media/attachments/lesson/245681/map2.osm и хочет посчитать, сколько на нём отмечено точечных объектов (node), являющихся заправкой.
# В качестве ответа вам необходимо вывести одно число - количество АЗС.
#
# Заправка в OSM обозначается парой ключ-значение amenity=fuel.
# Эта пара находится среди тегов tag внутри node.

from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

resp = urlopen('https://stepik.org/media/attachments/lesson/245681/map2.osm')
xml = resp.read().decode('utf8')
soup = BeautifulSoup(xml, 'xml')

cnt_n = 0

for node in soup.find_all('node'):
    for tag in node('tag'):
        if tag['k'] == 'amenity' and tag['v'] == 'fuel':
            cnt_n += 1
print(cnt_n)
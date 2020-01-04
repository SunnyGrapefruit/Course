# В OpenStreetMap XML встречаются теги way, которые соответствуют некоторым линиям и многоугольникам на карте.
# Way состоит из списка нодов (точек), которые задаются тегами nd вложенными в тег way.
# Для доступного по ссылке https://stepik.org/media/attachments/lesson/245681/map2.osm определите id того way, который содержит в себе наибольшее количество нодов.
# Если таких несколько - выведите тот id, который встречается в файле раньше.

from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

resp = urlopen('https://stepik.org/media/attachments/lesson/245681/map2.osm')
xml = resp.read().decode('utf8')
soup = BeautifulSoup(xml, 'xml')

k, l = [], []
for way in soup.find_all('way'):
    k.append(way['id'])
    l.append(len(way('nd')))

m = max(l)
d = dict(zip(k, l))

for key, value in d.items():
    if value == m:
        print(key)
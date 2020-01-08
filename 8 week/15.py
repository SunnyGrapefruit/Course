# Вам дана область карты https://stepik.org/media/attachments/lesson/266078/mapcity.osm
#
# Пройдите по всем way в этой области, выделите среди них замкнутые (те, у которых совпадает ссылка на первый и последний node), среди всех замкнутых выделите те, у которых установлен tag с ключом building и произвольным значением.
#
# Запомните id для way и список кортежей, содержащих координаты (широту и долготу) всех node, входящих в этот way.
#
# Вам предложена функция, которая определяет нечто похожее на площадь замкнутой ломаной.

import math
from urllib.request import urlopen
from bs4 import BeautifulSoup


def getsqr(coordlist):
    baselat = coordlist[0][0]
    baselon = coordlist[0][1]
    degreelen = 111300
    newcoord = []
    for now in coordlist:
        newcoord.append(((now[0] - baselat) * degreelen, (now[1] - baselon) * degreelen * math.sin(baselat)))
    sqr = 0
    for i in range(len(newcoord) - 1):
        sqr += newcoord[i][0] * newcoord[i + 1][1] - newcoord[i + 1][0] * newcoord[i][1]
    sqr += newcoord[-1][0] * newcoord[0][1] - newcoord[0][0] * newcoord[-1][1]
    return abs(sqr)


resp = urlopen('https://stepik.org/media/attachments/lesson/266078/mapcity.osm')
xml = resp.read().decode('utf8')
soup = BeautifulSoup(xml, 'xml')

d, nodes, max_sq = {}, {}, {}

for node in soup.find_all('node'):
    lat = float(node['lat'])
    lon = float(node['lon'])
    id_node = int(node['id'])
    nodes[id_node] = (lat, lon)

for way in soup.find_all('way'):
    way_id = way['id']
    for tag in way('tag'):
        if tag['k'] == 'building':
            d[way_id] = []
            for nd in way('nd'):
                ref = float(nd['ref'])
                d[way_id].append(ref)

for i in d:
    asd = []
    for j in d[i]:
        if j in nodes.keys():
            asd.append(nodes[j])
    max_sq[i] = getsqr(asd)

max_value = max(max_sq.values())
max_keys = [k for k, v in max_sq.items() if v == max_value]

print(*max_keys, max_value)

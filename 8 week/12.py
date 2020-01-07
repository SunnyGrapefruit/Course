# Вам дана область карты https://stepik.org/media/attachments/lesson/266078/mapcity.osm
#
# Пройдите по всем way в этой области, выделите среди них замкнутые (те, у которых совпадает ссылка на первый и последний node), среди всех замкнутых выделите те, у которых установлен tag с ключом building и произвольным значением.
#
# Для каждого подходящего под условия way выведите его id по одному в строке.
#
# Если вы все делаете правильно, то ваш ответ должен начинаться со строк#
# 28889642
# 28911067

from urllib.request import urlopen
from bs4 import BeautifulSoup

resp = urlopen('https://stepik.org/media/attachments/lesson/266078/mapcity.osm')
xml = resp.read().decode('utf8')
soup = BeautifulSoup(xml, 'xml')

for way in soup.find_all('way'):
    for tag in way('tag'):
        if tag['k'] == 'building':
            print(way['id'])
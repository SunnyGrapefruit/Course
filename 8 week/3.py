# Сейчас вам нужно установить библиотеку lxml для обработки xml с помощью BeatifulSoup.
# Чтобы проверить, что всё установилось хорошо, необходимо запусить код, представленный ниже и сдать в качестве ответа то, что он выводит.

from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

resp = urlopen('https://stepik.org/media/attachments/lesson/245681/map2.osm')
xml = resp.read().decode('utf8')
soup = BeautifulSoup(xml, 'xml')
cnt = 0
for way in soup.find_all('way'):
    cnt += 1
print(cnt)
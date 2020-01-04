# Вася, открывший заправку в прошлой задаче, разорился.
# Конкуренция оказалась слишком большой.
# Вася предполагает, что это произошло от того, что теги заправки могут быть не только на точке, но и на каком-то контуре.
# Определите, сколько заправок на самом деле (не только обозначенных node, но и way) есть на фрагменте карты https://stepik.org/media/attachments/lesson/245681/map2.osm



from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

resp = urlopen('https://stepik.org/media/attachments/lesson/245681/map2.osm')
xml = resp.read().decode('utf8')
soup = BeautifulSoup(xml, 'xml')

def fuel(data):
    cnt = 0
    for way in soup.find_all(data):
        for tag in way('tag'):
            if tag['k'] == 'amenity' and tag['v'] == 'fuel':
                cnt += 1
    return cnt

print(fuel('node') + fuel('way'))
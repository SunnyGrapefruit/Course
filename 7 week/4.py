# Вам нужно научиться пользоваться функцией urlopen модуля urllib.requests
#
# Откройте файл https://stepik.org/media/attachments/lesson/209717/1.html с помощью скрипта на питоне, примените функцию urlopen, затем примените метод read, а затем метод decode со строкой параметром utf-8. Напечатайте что получилось и сдайте в качестве ответа.
#

from urllib.request import urlopen
resp = urlopen('https://stepik.org/media/attachments/lesson/209717/1.html')
html = resp.read().decode('utf8')


data = open('output4.html', 'w', encoding='utf8')
print(html, file=data)
data.close()
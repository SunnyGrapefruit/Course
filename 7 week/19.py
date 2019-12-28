# В файле https://stepik.org/media/attachments/lesson/258944/New-York.html есть несколько таблиц, у которых атрибут class равен wikitable collapsible collapsed.
#
# Вам необходимо найти вторую (при нумерации с единицы) такую таблицу и преобразовать ее в csv-таблицу.
# В csv-таблице ячейки должны разделяться запятой, а строки не должны окружаться кавычками.
#
# Например, для таблицы:
#
# <table>
# <tr><td>a</td><td>b</td></tr>
# <tr><td colspan=2>c</td></tr>
# </table>
# ответ должен выглядеть так:
#
# a,b
# c
# Обратите внимание, что в таблице может встречаться тег <tbody>, на который мы можем просто не обращать внимания.
# Также там могут встречаться теги <th> (ячейка-заголовок), которые следует интерпретировать так же как теги <td>.
# Для поиска нескольких тегов удобно пользоваться методом find_all, которому в качестве параметра передается список строк с нужными названиями тегов.
#
# Чтобы получить содержимое тега td (то что записано от открывающего до закрывающего тега), достаточно написать td.text.
# Лучше удалить все пробельные символы в полученной строке с помощью метода strip().a


# https://stackoverflow.com/questions/38917958/convert-html-into-csv

from urllib.request import urlopen
from bs4 import BeautifulSoup

resp = urlopen('https://stepik.org/media/attachments/lesson/258944/New-York.html')
html = resp.read().decode('utf8')
soup = BeautifulSoup(html, 'html.parser')


table = soup.find_all('table', attrs={'class':'wikitable collapsible collapsed'})[0]

rows = table.findAll("tr")

for row in rows:
    csv_row = []
    for cell in row.findAll(["td", "th"]):
        csv_row.append(cell.get_text().strip())
    print(','.join(map(str, csv_row)))
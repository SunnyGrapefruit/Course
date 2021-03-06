# В этой задаче вам необходимо научиться генерировать html-код на питоне и сдать на проверку html-файл, в котором будет таблица размером 10 на 10, которая должна содержать таблицу умножения для чисел от 1 до 10.
# При открытии вашего файла в браузере это должно выглядеть примерно так:
# Ваш файл должен начинаться с тегов <html> и <body> и заканчиваться </body> и </html>.
#
# Для создания таблицы можно пользоваться тегами <table> (создание таблицы), <tr> (создание строки в таблице) и <td> (создание отдельной ячейки).
# Все открытые теги нужно закрыть, причем сделать это нужно в правильном порядке.

data = open('output2.html', 'w', encoding='utf8')
print('<html>', '<body>', '<table>', file=data, sep='\n')
for i in range(1, 11):
    print('<tr>', file=data)
    for j in range(1, 11):
        print('<td>', i * j, '</td>', file=data)
    print('</tr>', file=data)
print('</table>', '</body>', '</html>', file=data, sep='\n')
data.close()
# Вася составил таблицу с ценами на продукты в разных магазинах.
# В первой строке таблицы (кроме первой ячейки) записаны названия продуктов.
# Во всех строках, начиная со второй, записана информация о ценах в магазине.
# В первой ячейки написано название магазина, а в ячейках, начиная со второй - цена на товар, название которого записано в первой строке соответствующего столбца.
#
# Таблица задана как csv-файл, разделителем ячеек выступает точка с запятой, а строковые константы не окружаются кавычками.
#
# Вася очень хочет поесть, но денег у него мало.
# Поэтому помогите ему определить цену самого дешевого продукта. В качестве ответа введите одно число.
#
# Ссылка на csv-файл: https://stepik.org/media/attachments/lesson/258925/input.csv

data = open('data/input10.csv', 'r')

a, n = [], []

for line in data:
    new = line.strip('\n').split(';')[1:]
    a.append(new)

for i in a[1:]:
    m = list(map(int, i))
    n.append(min(m))

print(min(n))
# Даны два списка чисел.
# Выведите все числа, которые входят как в первый, так и во второй список в порядке возрастания.

print(*sorted(set(input().split()) & set(input().split()), key=int))
# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N].
# Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai
# . Последняя строка содержит число X
# 5
# 1234 5
# 3 -> 1

N = int(input('Введите число: '))
numbers = [i for i in range(1, N)]
print(numbers)
a = int(input('Какое число надо найти? '))
print(numbers.count(a))

# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
lst = list(map(int, input("Введите числа через пробел:\n").split()))
lis_two = []
for i in lst:
    if i not in lis_two:
        lis_two.append(i)
print(f'Неповторяющиеся элементы исходной последовательности {lis_two}')        
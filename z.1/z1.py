# Вычислить число Пи c заданной точностью d
import math
x=str(math.pi)
n=input('Введите точность вывода числа π (0.001, 0,01): ')
n = n.replace('0.', '')
count=0

for i in n:
    count +=1

print(f'Число π -> {x[:count+2]}')

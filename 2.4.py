import math
n = int(input("Введите общую длину марафона (в километрах): "))
m = int(input("Введите сколько километров спортсмен пробегает за один день: "))
days = math.ceil(n / m)
print("Спортсмен добежит до финиша на {}-й день".format(days))
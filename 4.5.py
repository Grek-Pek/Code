number = int(input("Введите число: "))
sum_of_divisors = 0

for i in range(1, number + 1):
    if number % i == 0:
        sum_of_divisors += i

print("Сумма делителей числа", number, "составляет:", sum_of_divisors)

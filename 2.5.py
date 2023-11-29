number = input("Введите трёхзначное число: ")
first_digit = int(number[0])
second_digit = int(number[1])
third_digit = int(number[2])
sum_of_first_and_third = first_digit + third_digit
if sum_of_first_and_third % 8 != 0 and second_digit == 3:
    print("Подходит")
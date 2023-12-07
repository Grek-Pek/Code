numbers = []
while True:
    num = int(input())
    if abs(num) >= 1000:
        break
    numbers.append(num)
maximum = max(numbers)
numbers.remove(maximum)
second_maximum = max(numbers)

print(second_maximum)

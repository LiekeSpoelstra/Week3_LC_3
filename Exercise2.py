numbers = [3, 6, 9, 12, 15, 18, 21, 24]
count = 0
for number in numbers:
    if number % 2 == 0:
        count += number
print(count)

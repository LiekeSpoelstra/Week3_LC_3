numbers = [23, 5, 7, 8, 13, 37, 24]
total = 0
for number in numbers:
    if number % 2 == 1:
        total += number
    else:
        break
print(total)
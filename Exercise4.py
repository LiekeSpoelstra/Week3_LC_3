numbers = [12, 10, 32, 3, 66, 17, 42, 99, 20]
total = 0
product = 1
for number in numbers:
    print(number)
    print(number**2)

for number in numbers:
    total = total + number
print(total)

for number in numbers:
    product = product * number
print(product)

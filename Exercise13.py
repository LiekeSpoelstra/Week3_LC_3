n = 123456789
count = 0
while n > 0:
    digit = n % 2
    if digit == 0:
        count += 1
    n = n // 10
print(count)
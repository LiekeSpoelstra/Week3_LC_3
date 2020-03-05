n = 25
approximation = n/2
threshold = 0.001

while True:
    better = (approximation + n / approximation) / 2
    print(better)
    approximation = better
    if abs(approximation - better) < threshold:
        print("The best approximation is ", better)
        break
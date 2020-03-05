a = float(input("Enter the length of side A: "))
b = float(input("Enter the length of side B: "))
c = float(input("Enter the length of side C: "))
threshold = 0.000001
if abs(a**2 + b**2 - c**2) < threshold:
    print("True")   # True means it is a right angled triangle
elif abs(a**2 + c**2 - b**2) < threshold:
    print("True")
elif abs(b**2 + c**2 - a**2) < threshold:
    print("True")
else: print("False")
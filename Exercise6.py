names = ["Peter", "Hank", "Anna", "Sam", "Lieke", "Tom"]
count = 0
for name in names:
    if name != "Sam":
        count += 1
    else:
        break
print(count)

marks = [(83, "First"), (75, "First"), (74.9, "Upper Second"),
        (70, "Upper Second"), (69.9, "Second"), (65, "Second"),
        (60, "Second"), (59.9, "Third"), (55, "Third"), (50, "Third"),
        (49.9, "F1 Supp"), (45, "F1 Supp"), (44.9, "F2"), (40, "F2"),
        (39.9, "F3"), (2, "F3"), (0, "F3")]
for mark, grade in marks:
    print("A " + str(mark) + " equals a grade of: " + str(grade))

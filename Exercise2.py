starting_day = int(input("What day will you be leaving? "))
length_of_stay = int(input("How many nights will you be staying? "))
number_of_weeks = length_of_stay // 7   # length of stay in weeks
number_of_days = length_of_stay % 7     # remaining number of days
returning_day = starting_day + number_of_days
if returning_day == 3:
    print("You will return home on a Wednesday")
elif returning_day == 4:
    print("You will return home on a Thursday")
elif returning_day == 5:
    print("You will return home on a Friday")
elif returning_day == 6:
    print("You will return home on a Saturday")
elif returning_day == 7:
    print("You will return home on a Sunday")
elif returning_day == 8:
    print("You will return home on a Monday")
else:
    print("You will return home on a Tuesday")




# Write a program that outputs whether or not today is a weekday.
# weekdays as a tuple

import datetime

weekDays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
weekend = ("Saturday", "Sunday")

now = datetime.datetime.now()
weekday = now.weekday()
weekdaystring = weekDays[weekday]
weekendaystring = weekend [weekday]

if weekday < 5:
    print("Yes, unfortunately today is a weekday. {}".format(weekdaystring))
else:
    print("It is the weekend, yay! {}".format(weekendaystring))
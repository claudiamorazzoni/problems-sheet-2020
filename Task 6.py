# Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.
# You should create a function called sqrt that does this.

# Please enter a positive number: 14.5
# The square root of 14.5 is approx. 3.8.

import math
num = float(input("Please enter a positive number:  "))
sqrt = math.sqrt(num)

print("The square root of {} is approx. {}" .format(num, "%.1f" % sqrt))
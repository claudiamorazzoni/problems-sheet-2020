# Write a program that calculates somebody's Body Mass Index (BMI).
# The inputs are the person's height in centimetres and weight in kilograms.
# The output is their weight divided by their height in metres squared.

height = float(input("What is you height in centimetres?  "))
weight = float(input("What is your weight in kg?  "))

heightsquared = ((height * height)/100)
BMI = (weight/heightsquared)*100

print("Your BMI is",BMI,)
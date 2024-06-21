# EXPECTED OUTPUT:
# 7.38 miles is 11.88 kilometers
# 12.25 kilometers is 7.61 miles

kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61

print(miles, "miles is", round(miles_to_kilometers, 4), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 4), "miles")


# PAY attention that in the task
# EXPECTED RESULTS are
# y = -1.0
# y = 3.0
# y = -9.0

x = 0
x = float(x)
y = 3 * x**3 - 2 * x**2 + 3 * x - 1
print("y =", y)

x = 1
x = float(x)
y = 3 * x**3 - 2 * x**2 + 3 * x - 1
print("y =", y)

x = -1
x = float(x)
y = 3 * x**3 - 2 * x**2 + 3 * x - 1
print("y =", y)

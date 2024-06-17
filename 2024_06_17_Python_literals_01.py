

# You can write this number either like this: 11111111, or like this: 11_111_111.
# Note *Python 3.6 has introduced underscores in numeric literals, allowing for the placement of
# single underscores between digits and after base specifiers for improved readability.
# This feature is not available in older versions of Python.

print("Number like this: 11111111 is the same like this: 11_111_111.")
a=1_100
b=20
c=a+b
print("So, the sum of ", a, "and", b, "is", c, end="\n")
print("Or if the number is float type, the sum is", float(c))
print("Let's try on your own!")
float_number_1 = None
float_number_2 = None
float_number_1 = input("Please enter 'a' the first integer or float: ")
float_number_2 = input("Please enter 'b' the second integer or float: ")
try:
    value1 = (float(float_number_1))
    value2 = (float(float_number_2))
    print("The sum of the entered numbers 'a+b' is", value1 + value2)
except:
    print("Invalid input, please enter TWO NUMBERS!")


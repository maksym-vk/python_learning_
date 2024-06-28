

# 3.1.4 Operators
var = 0  # Assigning 0 to var
print(var == 0)

var = 1  # Assigning 1 to var
print(var == 0)


# 3.1.6   LAB   Variables ‒ Questions and answers
n = int(input("Please enter the number which will be checked if it's greater than or equal to 100: "))
print(n >= 100)

# n = int(input("Enter a number: ")) # solution
# print(n >= 100)

# IF - ELSE and IF - ELIF - ELSE

# 1.
# if the_weather_is_good:
#     if nice_restaurant_is_found:
#         have_lunch()
#     else:
#         eat_a_sandwich()
# else:
#     if tickets_are_available:
#         go_to_the_theater()
#     else:
#         go_shopping()

# 2.
#  if the_weather_is_good:
#     go_for_a_walk()
# elif tickets_are_available:
#     go_to_the_theater()
# elif table_is_available:
#     go_for_lunch()
# else:
#     play_chess_at_home()


# 3.1.8 Analyzing code samples


# Read two numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

# Choose the larger number
if number1 > number2:
    larger_number = number1
else:
    larger_number = number2

# Print the result
print("The larger number is:", larger_number)


# Improvement with two equal numbers
# Read two numbers
number1 = int(input("Enter the first integer number: "))
number2 = int(input("Enter the second integer number: "))

# Choose the larger number
if number1 > number2:
    larger_number = number1
    smaller_number = number2
    print("The larger number is:", larger_number)
    print("Number", larger_number, "is bigger than", smaller_number, sep=' ')
elif number1 < number2:
    larger_number = number2
    smaller_number = number1
    print("The larger number is:", larger_number)
    print("Number", larger_number, "is bigger than number", smaller_number, sep=' ')
else:
    print("Number", number1, "is equal number", number2, sep=' ')


# More complicated comparison
# Read three numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

# We temporarily assume that the first number
# is the largest one.
# We will verify this soon.
largest_number = number1

# We check if the second number is larger than the current largest_number
# and update the largest_number if needed.
if number2 > largest_number:
    largest_number = number2

# We check if the third number is larger than the current largest_number
# and update the largest_number if needed.
if number3 > largest_number:
    largest_number = number3

# Print the result
print("The largest number is:", largest_number)
#
# Why if and not elif
#
#     Independent Checks:
#         The checks for number2 and number3 being larger than largest_number are independent
#         of each other.
#         This means that after updating largest_number with number2, you still need to check
#         if number3 is larger than the updated largest_number.
#
#     Sequential Comparison:
#         Initially, largest_number is set to number1.
#         The first if statement checks if number2 is larger than largest_number
#         (which is number1 at this point). If true, largest_number is updated to number2.
#         The second if statement then checks if number3 is larger than the current
#         largest_number (which could be number1 or number2 depending on the first check).
#         If true, largest_number is updated to number3.
#
# Why Not elif
#
#     elif (else if) implies a mutually exclusive condition that is checked only if
#     the preceding if (or elif) condition is False.
#     If you used elif here, the second condition would only be checked if
#     the first condition (number2 > largest_number) is False. This would mean that
#     number3 is only compared to number1 and not to a potentially updated largest_number.
#
# Correct Logic with if
#
# Using if for both conditions ensures each number is compared independently
# to the current largest value, guaranteeing the correct largest number is identified.
#
# Thus, the correct approach is to use two if statements to ensure each number
# has the opportunity to be the largest number after each comparison.


# Alternative solution
# Read three numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

# Determine the largest number using nested if-else statements
if number1 >= number2:
    if number1 >= number3:
        largest_number = number1
    else:
        largest_number = number3
else:
    if number2 >= number3:
        largest_number = number2
    else:
        largest_number = number3

# Print the result
print("The largest number is:", largest_number)


# 3.1.10   LAB   Comparison operators and conditional execution
# SPATHIPHYLLUM program
word = input("Please enter the white sail plant: ")
if word == "Spathiphyllum":
    print("Yes - Spathiphyllum is the best plant ever!")
elif word == "spathiphyllum":
    print("No, I want a big Spathiphyllum!")
else:
    print("Spathiphyllum! Not", word, end="!") # print("Spathiphyllum! Not", name + "!")


# 3.1.11   LAB   Essentials of the if-else statement
# Tax calculator

tax_base = float(input("Please enter the citizen's income here: "))
if tax_base > 85528:
    tax = 14839,2 + (0,32*(tax_base - 85528))
    tax = round(tax, 0)
    print("Your tax is: ", tax)

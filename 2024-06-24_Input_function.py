

# It shows a very simple case of using the input() function.

print("Tell me anything...")
anything = input("Your text should be entered here: ->")  # <- Your text should be entered here
print("Hmm...", anything, "... Really?")


# Example of the type conversions.
anything = float(input("Enter a number: "))
something = anything ** 2.0
print(anything, "to the power of 2 is", something)

# Example of the type conversions.
anything = input("Enter a number: ")
try:
    anything = float(anything)
except:
    print("You entered an invalid input!")
else:
    something = float(anything) ** 2.0
    print(anything, "to the power of 2 is", something)  # power of 2 is square (**2)

# Pythagorean theorem or Pythagoras' theorem
leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
hypo = (leg_a**2 + leg_b**2) ** .5
print("Hypotenuse length is", hypo)


# This simple program shows the '+' sign in its second use:
fnam = input("May I have your first name, please? ")
lnam = input("May I have your last name, please? ")
print("Thank you.")
print("\nYour name is " + fnam + " " + lnam + ".")


# This simple program "draws" a rectangle, making use of an old operator (+) in a new role:
print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")


# 2.6.9   LAB   Simple input and output
a = float(input('Enter please a float value for variable "a" here: ')) # input a float value for variable a here
b = float(input('Enter please a float value for variable "b" here: ')) # input a float value for variable b here

print('the result of addition here', a+b, sep=' => ') # output the result of addition here
print('the result of subtraction here:', a*b) # output the result of subtraction here
print('the result of multiplication here:', a-b) # output the result of multiplication here
print('the result of division here:', a/b)# output the result of division here

print("\nThat's all, folks!")

# 2.6.9   LAB   Simple input and output(HINT solution)
a = float(input("Enter first value: "))
b = float(input("Enter second value: "))
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("\nThat's all, folks!")


# 2.6.10   LAB   Operators and expressions
# Your task is to complete the code in order to evaluate the following expression
# y = 1 / (1/ (1/ ((1/x)+x) +x)+x)


x = float(input("Enter value for x: "))
y_1 = 1 / ( 1 / (1 / ((1 / x) + x ) + x ) + x ) # first option
print('y_1 =', y_1)


x = float(input("Enter value for x: ")) # second option
var4 = x + 1/x
var3 = x + 1/var4
var2 = x + 1/var3
y = 1/var2
print("y =", y)


# 2.6.11   LAB   Operators and expressions – 2
# Your task is to prepare a simple code able to evaluate the end time of a period of time,
# given as a number of minutes (it could be arbitrarily large). The start time is given as
# a pair of hours (0..23) and minutes (0..59). The result has to be printed to the console.
# For example, if an event starts at 12:17 and lasts 59 minutes, it will end at 13:16.
# Don't worry about any imperfections in your code ‒ it's okay if it accepts an invalid time ‒
# the most important thing is that the code produces valid results for valid input data.
# Test your code carefully. Hint: using the % operator may be the key to success.

hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))
mins = mins + dura # find a total of all minutes
hour = hour + mins // 60 # find a number of hours hidden in minutes and update the hour
mins = mins % 60 # correct minutes to fall in the (0..59) range
hour = hour % 24 # correct hours to fall in the (0..23) range
print(hour, ":", mins, sep='')


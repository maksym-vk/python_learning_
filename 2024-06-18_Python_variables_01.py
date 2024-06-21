# Take a look at the list of words that play a very special role in every Python program.
#
# ['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del',
# 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is',
# 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
#
# They are called keywords or (more precisely) reserved keywords.
# They are reserved because you mustn't use them as names: neither for your variables,
# nor functions, nor any other named entities you want to create.

var = "3.8.5"
print("Python version: " + var) # the same as
#print("Python version:", var)

# Pythagorean theorem or Pythagoras' theorem
a = (input("Please enter the first side of the triangle (cathet):"))
b = (input("Please enter the second side of the triangle (cathet):"))
try:
    a = float(a)
    b = float(b)
    if a <= 0 or b <= 0:
        print("You entered invalid number!")
    else:
        c = (float(a) ** 2 + float(b) ** 2) ** 0.5 # We use ** instead of a square root.
        print("The Hypotenuse is: ", c)
except:
    print("The entered input is invalid!")


john = 10
mary = 5
adam = 2
total_apples = john + mary + adam
print("John", "Mary", "Adam", sep=',')
print(john, mary, adam, sep=',')
print(total_apples, "is a total number of apples that John, Mary and Adam have.")
avg_apples = total_apples / 3
print("Average number of apples:", avg_apples)
int_avg_apples = total_apples // 3
print("Average integer number of apples:", int_avg_apples)


a = 6
b = 3
a /= 2 * b # this means a = a / (2 * b) because first we should complete the operators to the right of the "="
print(a)

a = 6
b = 3
a = a / 2 * b # this might be written as a /= 2 then a *= b
print(a)




print("Hello Python!")


# If you'd like to quickly comment or uncomment multiple lines of code, select the line(s)
# you wish to modify and use the following keyboard shortcut:
# CTRL + / (Windows) or
# CMD + / (Mac OS).
# It's a very useful trick, isn't it? Now experiment with the code in the editor.


# Take a look at the list of words that play a very special role in every Python program.
#
# ['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del',
# 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is',
# 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
#
# They are called keywords or (more precisely) reserved keywords.
# They are reserved because you mustn't use them as names: neither for your variables,
# nor functions, nor any other named entities you want to create.

print(1 == True)

for i in range(5):
    print('I in range(5): ', i)
for i in range(1, 10):
    print('I in range(1, 10): ', i)
for i in range(0, 1, 10):
    print('I in range(0, 1, 10): ', i)

list(range(0, 10, 3))

a = True or False
print('True or False: ', True or False)
print('True and False: ', True and False)
print('False and True: ', False and True)
print('False or True: ', False or True)
print('True or not False: ', True or not False)
print('False or not True: ', False or not True)
print('a == True :', a == True)
print('a != True :', a != True)

print('not True or not False: ', not True or not False)
print('not False or not True: ', not False or not True)
print('not True and not False: ', not True and not False)
print('not False and not True: ', not False and not True)

print('_____')
print('True or not False: ', True or not False)
print('False or not True: ', False or not True)
print('True and not False: ', True and not False)
print('False and not True: ', False and not True)

print(0 and 10)    # 0
print(0 or 10)

d = not 2 == 2
print('d: ', d)
print('not d: ', not d)

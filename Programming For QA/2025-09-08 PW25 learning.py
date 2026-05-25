# 5.36, 5.37 (Функції, Будова функції)
def result(total, correct):
    if 0.8 <= correct/total <= 1:
        status = True
    else:
        status = False
    return status

a = int(input("Enter the number of questions: "))
b = int(input("Enter the number of correct answers: "))
x = result(a, b)
print(x)

ans_passed = "Passed"
ans_failed = "Failed"

if x == True:
    print(ans_passed)
else:
    print(ans_failed)


num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))
def select_function(a, b):
    if a >= 0:
        return a
    else:
        return b

x = select_function(num_1, num_2)

print(x)


input("Please hit enter to continue.")
def greeting(name="username"): #the default ARGUMENT of the function is added
    message = "Nice to see you, "+name+"!"
    return message
#name = input("Enter the username: ")
text = greeting()
print(text)


'''

count(x) -
islower()
replace (a, b)
split(x)
title()

'''

string = "StaffManagement - це внутрішня система управління персоналом департаменту розвитку ПЗ."
y = string.count('i')
print(y)

model = "F 150"
print(len(model))

name = "pavlo the first"
print(name.capitalize())


car = ['Audi', 2019, 2.5, 'blue', True]
car.append('sedan')
print(car)
print(len(car))
print(car[5])


car = ['Audi', 2019, 2.5, 'blue', True]
car.insert(0, 'Sale')
print(car)
print(car[0])
car.pop(0)
print(car)


cars = ['BMW', 'Ford', 'Audi', 'VW', 'Skoda', 'Volvo']
name = 'Joahn'
print('Sorted is below:')
print(sorted(cars))
print(sorted(name))
print('Reversed sorted is below:')
print(sorted(cars, reverse=True))
print(sorted(name, reverse=True))


cars.sort()
print(".sort:", cars)
cars.sort(reverse=True)
print(".sort reverse:", cars)

#Here will be the mistake: '''AttributeError: 'str' object has no attribute 'sort' '''
#name = "Josephine"
#name.sort()
#print(name)


a = [1, 2, 3, 4, 5]
print(sum(a) / len(a))


brands = ["Audi", "Ford", "Nissan"]
brands.insert(1, "BMW")
brands.append("Toyota")

print(brands[3])


mustang = ('Ford', 3.5, 2020, True)
for i in mustang:
    print(i)


car = ["Audi", "blue"]
params = (180, 25, 75)

brand, color = car
height, age, weight = params

print(brand, color)
print(height, age, weight)


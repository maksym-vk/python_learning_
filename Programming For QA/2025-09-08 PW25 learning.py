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


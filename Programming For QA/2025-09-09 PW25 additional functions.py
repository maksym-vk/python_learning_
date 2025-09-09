'''
Типи параметрів (по порядку):
- positional-only parameters (/)
- positional-or-keyword parameters
- var-positional parameters (*args)
- keyword parameters (*)
- var-keyword parameters (**kwargs)

Типи аргументів:
- positional arguments
- keyword arguments
'''

def function(x, /, a, b, *, y):
    print(x, y)
    print(a, b)
function(2, a=3, b=4, y=5)


def add_numbers(numbers):
    result = 0
    for n in numbers:
        result += n
    return result


numbers = [1, 2, 3]

print(add_numbers(numbers))


def add_numbers(*args): # те саме що й def add_numbers(*numbers):
    result = 0
    for n in args: # те саме що й for n in numbers:
        result += n # result = result + n
    return result


print(add_numbers(1, 2, 25, 100))


def show_data(**kwargs):
    for key, value in kwargs.items():
        print(key, "це", value)
show_data(brand="AUDI", model="Q7", year=2022, color="red", insurance=True)


car_dictionary = {
    "brand" : "Ford"
    "model" : "Mustang"
    "year" : "1965"
    "color" : "yellow"
}


def function_our(p, /, p_k, *args, k, **kwargs):
    pass


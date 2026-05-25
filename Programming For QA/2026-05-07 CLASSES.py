from pyclbr import Class

#CLASSES (practics + lecture "Python 3rd lecture")

class Car:
    def __init__(self, brand, model, color, year, owner):
        self.brand = brand
        self.model = model
        self.color = color
        self.year = year
        self.owner = owner
    def horn(self):
        print("B-e-e-e-e-e-p!")
auto_1 = Car("VW", "Golf IV", "Grey metallic", "2000", "Maksym")
print(f"Car model and owner: {auto_1.model}, {auto_1.owner}") # alternate print("Car model and owner: ", auto_1.model, auto_1.owner, sep=", ")

auto_1.horn()

my_auto_2 = Car("Skoda", "Scala", "White", "2019", "Maksym K.")

print(f"Car brand, model, year and owner: {my_auto_2.brand}, {my_auto_2.model}, {my_auto_2.year}, {my_auto_2.owner}")
my_auto_2.horn()

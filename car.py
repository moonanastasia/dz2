class Car:
    brands = "None"
    cars = 0

    def __init__(self, brand, drive=False, wheels=False, motor=False, doors=False):
        Car.cars += 1
        self.brand = brand
        self.drive = drive
        self.wheels = wheels
        self.motor = motor
        self.doors = doors



    def drivee(self):
        if self.drive:
            print(f"{self.brand} can go!")
        else:
            print(f"{self.brand} can't go!")

    def wheelss(self):
        if self.wheels:
            print(f"{self.brand} there are wheels!")
        else:
            print(f"{self.brand} no wheels!")

    def motorr(self):
        if self.motor:
            print(f"{self.brand} there is a motor!")
        else:
            print(f"{self.brand} No motor!")

    def doorss(self):
        if self.doors:
            print(f"{self.brand} there are four doors!")
        else:
            print(f"{self.brand} there are two doors!")


Ferrari = Car("Ferrari F8 Tributo", drive=True, wheels=True, motor=True, doors=False)
BMW = Car("bmw x5", drive=True, wheels=True, motor=True, doors=True)
Mercedesbenz = Car("mercedes-benz s-class", drive=True, wheels=True, motor=True, doors=True)
Audi = Car("audi a6", drive=True, wheels=True, motor=True, doors=True)
Tesla = Car("Tesla x", drive=True, wheels=True, motor=False, doors=True)

print(Ferrari.brand, Ferrari.drivee(), Ferrari.wheelss(), Ferrari.motorr(), Ferrari.doorss())
print(BMW.brand, BMW.drivee(), BMW.wheelss(), BMW.motorr(), BMW.doorss())
print(Mercedesbenz.brand, Mercedesbenz.drivee(), Mercedesbenz.wheelss(), Mercedesbenz.motorr(), Mercedesbenz.doorss())
print(Audi.brand, Audi.drivee(), Audi.wheelss(), Audi.motorr(), Audi.doorss())
print(Tesla.brand, Tesla.drivee(), Tesla.wheelss(), Tesla.motorr(), Tesla.doorss())

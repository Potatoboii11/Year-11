class Car:
    def __init__(self,company, model, year, price = None, colour = None, horsepower = 400, fuel_capacity = 50, sale = True, wheels = 4, doors = 4): #Initialising with default variables for average car
        self.company = company #Initialising all variables
        self.model = model
        self.year = year
        self.price = price
        self.colour = colour
        self.horsepower = horsepower
        self.fuel_capacity = fuel_capacity
        self.sale = sale
        self.wheels = wheels
        self.doors = doors
    
    def __str__(self):
        if self.sale == True: #printing sale or not for sale for sale status
            self.sale = 'For sale'
        else:
            self.sale = 'Not for sale'
        car = 'Company: ' + str(self.company) + '\nModel: ' + str(self.model) + '\nYear: ' + str(self.year) + '\nPrice: $' + str(self.price) + '\nSale Status: ' + str(self.sale) + '\nColour: ' + str(self.colour) + '\nHorsepower: ' + str(self.horsepower) + '\nFuel Capacity: ' + str(self.fuel_capacity) + 'L\n' #printing everything
        return car

c1 = Car('Ferrari', 'SF90 Stradale', 2019, 2000000, horsepower= 500, fuel_capacity = 60, doors = 2) #Ferrari status
c2 = Car('Lamborghini', 'Aventador S Auto AWD MY18', 2022, 999990, 'Red', 769, sale = False, doors = 2) #Lamborghini status
c3 = Car('Ford', 'Mustang', 2025, 99500, 'yellow and black', doors = 2) #Ford Mustang Status

cars = [c1,c2,c3] #creating a list to print with loop
for car in cars: #printing using a loop
    print(car)
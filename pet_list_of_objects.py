class Pet:
    def __init__(self, name, category, age = 0, ccard = 'unknown', vaccinated = False): #Default values for no inputs to avid errors
        self.name = name
        self.category = category
        self.age = age
        self.ccard = ccard
        self.vaccinated = vaccinated
    
    def __str__(self): 
        payment = 'Your pet has no registered payment details'
        if self.ccard != 'unknown': #Checks if there is any payment information
            payment = 'Your pet has registered payment details' #Changes the print statement if there is payment information
        my_status = 'Name: ' + self.name + '\nCategory: ' + self.category + '\nAge: ' + str(self.age) + '\n' + payment + '\nVaccinated Status: ' + str(self.vaccinated) #stores everything here to return in one go
        return my_status

p1 = Pet("Bonnie", "Cat") #Creating a pet, the rest of the variables have default values so they do not have to be added
p2 = Pet('Clyde','Dog',7)
p3 = Pet(category = 'Rabbit', name = 'Ruby', age = 13) #This way the variables can be set in any order, so you do not have to set each one when most of it is still default

pets = [p1, p2, p3] #creating a list with all pets to print later

p4 = Pet('Dom','Hamster',8)

pets.append(p4) #Task 1: adding a pet to the list

for pet in pets: #printing every item in the list 'pets'
    if pet.vaccinated == False: #Changing the vaccination status variable in pet to True
        print('Pet is being vaccinated...')
        pet.vaccinated = True 
    print(pet) 

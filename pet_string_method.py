class Pet:
    def __init__(self, name, category, age = 0, ccard = 'unknown', vaccinated = False):
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

p1 = Pet("Bonnie", "Cat",)

print(p1)
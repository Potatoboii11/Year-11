class Pet:
    def __init__(self, name, category, age = 0, account_balance = 0): #Setting defualt values for attributes
        self.name = name #Initialising all attributes
        self.category = category
        self.age = age
        self.ccard = 'unknown'
        self.vaccinated = False
        self.account_balance = account_balance

    
    def have_birthday(self): #Function to increase the age of the pet by 1
        self.age += 1 #Adds 1 to age

    def vaccinate(self): #Vaccinates the pet
        if self.vaccinated == False: #Checks whether pet is vaccinated and then vaccinates them
            print('Vaccinating')
            self.vaccinated == True
        else:
            print("Already vaccinated")
    
    def clear_balance(self): #Sets balance to 0
        self.account_balance = 0
        print("Account balance clearedwww")
    
    def human_age(self): #Changes the pets age into human age
        if self.category.lower() == 'dog': #Checks whether pet is dog, cat or neither
            self.age *= 7 #Multiplies by 7 for dogs
        elif self.category.lower() == 'cat':
            self.age *= 6 #Multiplies by 6 for cats

    def __str__(self): #Printing everything
        pet = 'Name: ' + str(self.name) + '\nCategory: ' + str(self.category) + '\nAge: ' + str(self.age) + '\nAccount_balance: ' + str(self.account_balance)
        return pet

p1 = Pet(name = 'Bonnie', category = 'cat', age = 10, account_balance = 20)
print(p1)

#Calling functions
p1.have_birthday() 
p1.clear_balance()
p1.human_age()
print(p1)

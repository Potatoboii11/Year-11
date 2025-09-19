class Pet:
    def __init__(self, name, category, breed = None, age = 0): #Setting default values for attributes
        self._name = name #Initialising attributes
        self.__category = category #Make private
        self.__breed = breed #Make private
        self.age = age
        self.__ccard = 'unknown'
        self.vaccinated = False
        self.weight = 0

    def have_birthday(self): 
        self.age += 1 #Increase age by one
    
    def get_weight(self):
        return self.weight
    
    def set_weight(self, new_weight): #Setting a new value for weight
        if type(new_weight) == int or type(new_weight) == float: #Checks to see if the variable is a number
            if new_weight > 0: #checks to see if the weight is positive
                self.weight = new_weight
            else:
                print("Weight must be positive")
        else:
            print("Weight must be a number")

    def __str__(self): #Printing function
        payment_status = 'unregistered' 
        if len(self.__ccard) == 19:  
            payment_status = 'registered'

        my_status = 'Name: ' + self._name +'\nCategory: ' + self.__category + '\nAge: ' + str(self.age) +'\nPayment status: ' + payment_status + '\nVaccinated: '+ str(self.vaccinated)
        return my_status

p1 = Pet(name = 'Bonnie', category = 'Cat', age = 10)

p1.set_weight(5) #calling set_weight function to set a new weight for p1.weight
print('Bonnies weight:',p1.weight) #printing the new variable for weight

print(p1)
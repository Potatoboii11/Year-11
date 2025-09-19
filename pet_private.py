class Pet:
    def __init__(self, name, category, breed = None, age = 0): #Setting default values for attributes
        self._name = name #Initialising attributes
        self.__category = category #Make private
        self.__breed = breed #Make private
        self.age = age
        self.__ccard = 'unknown'
        self.vaccinated = False

    def have_birthday(self): 
        self.age += 1 #Increase age by one

    def __str__(self): #Printing function
        payment_status = 'unregistered' 
        if len(self.__ccard) == 19:  
            payment_status = 'registered'

        my_status = 'Name: ' + self._name +'\nCategory: ' + self.__category + '\nAge: ' + str(self.age) +'\nPayment status: ' + payment_status + '\nVaccinated: '+ str(self.vaccinated)
        return my_status

p1 = Pet(name = 'Bonnie', category = 'Cat', age = 10)
print(p1)


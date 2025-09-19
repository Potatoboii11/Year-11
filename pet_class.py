class Pet: #The class Pet
    def __init__(self, name, category, age, vaccinated, ccard, billing_address): #Initialise the class, with variables
        self.name = name #Defines variables as themself
        self.category = category
        self.age = age
        self.vaccinated = vaccinated
        self.ccard = ccard
        self.billing_address = billing_address
        self.account_balance = 0 #Account Balance is preset to 0
        self.owner_name = 'unknown' #Account Balance is preset to unknown

p1 = Pet('Bonnie','cat',11, False, '3253 3542 3532 5353', 'Penrith') #Call Pet class to input Bonnie
print(f"{p1.name}'s vacination status is {p1.vaccinated}") #print the vaccinated status
p2 = Pet('Foxy','dog', 8, False, '3253 3542 3532 5353', 'Sydney' ) #Call Pet class to input Foxy
print(f"{p2.name}'s vacination status is {p2.vaccinated}") #print the vaccinated status

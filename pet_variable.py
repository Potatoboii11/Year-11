name = 'Bonnie'
animal_category = 'Cat'
age = 4
vaccinated = True
ccard = '3423 2326 7543 1234'
billing_address = '17 Park Drive, The Shire 2695'
owner_name = 'Alex Ngyuen'
account_balance = 129.95

age += 1 #Adds 1 to age
billing_address = '17 Park Street, The Shire 2695' #Replaces the variable with new string
vaccinated = False #Updates vaccinated status
ccard = input("Update credit card number: ") #Allows the user to update their credit card number.
name = 'Alex Jones' #Updates users name
account_balance -= 25 #Subtracts $25 from users balance.

print(age, billing_address, vaccinated, ccard, name, account_balance)
name = 'Bonnie'
animal_category = 'Cat'
age = 3
vaccinated = False
ccard = '3423 2326 7543 1234'
billing_address = '17 Park Drive, The Shire 2695'
owner_name = 'Alex Ngyuen'
account_balance = 129.95

def help():
  print('Welcome to the Pet Data Management System')
  print("Every vet's best friend")

def increase_age():
  global age
  age = age + 1

def verify_credit_card(card_num):
  if len(card_num) == 19:
    if len(card_num.split()) == 4:
      return True
  return False


help()
increase_age()
print(age)

valid = verify_credit_card('1234 4334 1001 0000')

user_card = input("Enter your credit card number to check for validity: ")
user_valid = verify_credit_card(user_card)
if user_valid == True:
  account_balance -= 39

def vaccinate(vaccinated):
    if vaccinated == False:
        print("Vaccinating")
        print("Vaccinated")
        return True
    else:
       print("You are already vaccinated")

vaccinated = vaccinate(vaccinated)
vaccinate(vaccinated)




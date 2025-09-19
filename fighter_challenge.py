import random, time 

class Fighter:
    def __init__(self,name, starting_health, weapon, shield):
        self.name = name
        self.health = starting_health #Protected value
        self.weapon = weapon
        self.shield = shield
  
    def report(self):
        print(self.name+':'+ ' Health: '+ str(round(self.health, 1))) #Rounds when printing to make it easier to read

    def is_dead(self): #Method to check if it is dead
        if self.health <= 0:
            return True
        else:
            return False

    def random_attack(self):
        attack_power = random.randint(int(self.weapon/2), int(self.weapon*2))
        print('Attack power:', attack_power)
        return attack_power 
    
    def skill_attack(self):
        attack_power = random.randint(int(self.weapon/2), int(self.weapon*2))
        target = random.randint(2,6) #Randomised time amount to press space
        print('Hit enter in exactly',target,'seconds')
        tic = time.time() #Get start time 
        input()
        toc = time.time() #Get end time
        time_taken = toc - tic #Find how long user took inbetween times
        multiplier = 2.5 - abs(target-time_taken) #Make negative numbers positve, penalises user's multiplier for being off time
        if multiplier < 1.5: #Multiplier has to be within a certian range
            multiplier = 0.5 

        print('Attack power:', attack_power)
        print('Multiplier:', round(multiplier, 1))
        return attack_power * multiplier

    def defend(self,attack_power):
        damage = attack_power - self.shield
        if damage >  0:
            self.health -= damage
            print('Damage:', round(damage, 1)) 
        else:
            print('No damage')

class Mage(Fighter): #Parent class as attribute
    def __init__(self,name, starting_health, weapon, shield, magic): 
        super().__init__(name, starting_health, weapon, shield) #Inheritence
        self.magic = magic #New attribute
    
    def random_attack(self):
        attack_power = (random.randint(int(self.weapon/2), int(self.weapon*2))) + self.magic #Add magic power to attack power
        print('Attack power:', self.attack_power)
        return self.attack_power
    
class Ninja(Fighter):
    def __init__(self, name, starting_health, weapon, shield, dodge_chance):
        super().__init__(name, starting_health, weapon, shield)
        self.dodge_chance = dodge_chance
    
    def defend(self,attack_power):
        dodge = random.randint(0,100)
        if dodge < self.dodge_chance:
            damage = 0
            print('Dodged')
        else:
            damage = attack_power - self.shield
        if damage >  0:
            self.health -= damage
            print('Damage:', round(damage, 1)) 
        else:
            print('No damage')

print("1: Fighter: \nHealth: 100 \nWeapon: 60 \nShield: 20")
print("2. Mage: \nHealth: 80 \nWeapon: 20 \nShield: 60 \nMagic: 40")
print("3. Ninja: \nHealth: 80 \nWeapon: 50 \nShield: 15 \nDodge Chance: 50%" )

name = input("Enter your name: ")
fighter_class = int(input("Enter the number of the class you would like to be: ")) #input which class they want to be in int
if fighter_class == 1:
    you = Fighter(name,100,60,20)
elif fighter_class == 2:
    you = Mage(name,80,30,60,60)
else:
    you = Ninja(name,80,50,15,50)

opp_class = int(input("Enter the number of the class you would like your opponent to be: ")) #input which class they want they're opponent to be in int
if opp_class == 1:
    opp = Fighter('Berserker Fighter',100,60,20)
elif opp_class == 2:
    opp = Mage('Great Mage',80,30,60,60)
else:
    opp = Ninja('Ninja',80,50,15,50)

you.report()
opp.report()

while opp.is_dead() == False and you.is_dead() == False: #Checks if either one has died yet
    time.sleep(1) #Delay for 1 second before conutinuing
    print('')
    opp.defend(you.skill_attack()) #Subtract damage from health
    print('You attacked', opp.name) #PLayer goes first
    print('')
    if opp.is_dead(): #Checks if troll is still alive
        print(opp.name,'has been defeated')
        you.report()
        opp.report()
        break
    time.sleep(1)
    print(opp.name,'attacked you . . .')
    you.defend(opp.random_attack()) #Troll attacks player if still alive
    print('')
    you.report()
    opp.report()
    if you.is_dead():
        print('You have lost')
        break
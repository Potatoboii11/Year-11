import random, time 

class Fighter:
    def __init__(self,name, starting_health, weapon, shield):
        self.name = name
        self.__health = starting_health #Protected value
        self.weapon = weapon
        self.shield = shield
  
    def report(self):
        print(self.name+':'+ ' Health: '+ str(round(self.__health, 1))) #Rounds when printing to make it easier to read

    def is_dead(self): #Method to check if it is dead
        if self.__health <= 0:
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
        print('Hit enter is exactly',target,'seconds')
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
            self.__health -= damage
            print('Damage:', round(damage, 1)) 
        else:
            print('No damage')

class Wizard(Fighter): #Parent class as attribute
    def __init__(self,name, starting_health, weapon, shield, magic): 
        super().__init__(name, starting_health, weapon, shield) #Inheritence
        self.magic = magic #New attribute
    
    def random_attack(self):
        attack_power = random.randint(int(self.weapon/2), int(self.weapon*2)) + self.magic #Add magic power to attack power
        print('Attack power:', attack_power)
        return attack_power

you = Fighter('You',100,60,20)
wiz = Wizard('The greatest Wzard',150,30,20,50)

you.report()
wiz.report()

while wiz.is_dead() == False and you.is_dead() == False: #Checks if either one has died yet
    time.sleep(1) #Delay for 1 second before conutinuing
    print('')
    wiz.defend(you.skill_attack()) #Subtract damage from health
    print('You attacked', wiz.name) #PLayer goes first
    print('')
    if wiz.is_dead() == False: #Checks if troll is still alive
        time.sleep(1)
        print(wiz.name,'attacked you . . .')
        you.defend(wiz.random_attack()) #Troll attacks player if still alive
    else:
        continue #Continues next loop which wil automatically end since troll is dead
    you.report()
    wiz.report()

print('')
you.report()
wiz.report()
if wiz.is_dead() == True: #Prints who won and how much health they both have remaining
    print(wiz.name,'has been defeated')
else:
    print('You have lost')

import random, time

class Fighter:
    def __init__(self, name, starting_health, weapon, shield):
        self.name = name
        self.health = starting_health
        self.weapon = weapon
        self.shield = shield

    def report(self): #This is no longer useful since I cannot directly change health so it will always print the same thing
        if self.health > 0:
            print(self.name + ':' + ' Health: ' + str(self.health))
        else:
            print(self.name + ':' + ' Health: 0')

    def random_attack(self): 
        attack_power = random.randint(int(self.weapon/2), self.weapon*2) #creates a range from which a random number is selected from the attack power
        print('Attack power:', attack_power)
        return attack_power
    
    def defend(self, attack_power): 
        damage = attack_power - self.shield #A random amount of the attack power will be reduced 
        if damage > 0: 
            self.health -= damage
            print('Damage:',damage)
        else: #If it is already dead then it will take skip this part
            print('No Damage')

you = Fighter('You',100,60,20) #Player 
troll = Fighter('Troll', 200,30,10) #Enemy

you.report()
troll.report()

while troll.health > 0 and you.health > 0: #Checks if either one has died yet
    time.sleep(1) #Delay for 1 second before conutinuing
    print('')
    print('You attacked the troll') #PLayer goes first
    troll.defend(you.random_attack()) #Subtract damage from health
    print('')
    if troll.health > 0: #Checks if troll is still alive
        print('The troll attacked you')
        you.defend(troll.random_attack())
    else:
        continue #Continues next loop which wil automatically end since troll is dead
    you.report()
    troll.report()

print('')
you.report()
troll.report()
if troll.health <= 0: #Prints who won and how much health they both have remaining
    print('The troll has been defeated')
else:
    print('You have lost')

import random

class Fighter:
    def __init__(self, name, starting_health, weapon, shield):
        self.name = name
        self.__health = starting_health #Make attribute private
        self.weapon = weapon
        self.shield = shield

    def get_health(self): #To access private attributes
        return self.__health

    def report(self): #This is no longer useful since I cannot directly change health so it will always print the same thing
        print(self.name + ':' + ' Health: ' + str(self.__health))

    def random_attack(self): 
        attack_power = random.randint(int(self.weapon/2), self.weapon*2) #creates a range from which a random number is selected from the attack power
        print('Attack power:', attack_power)
        return attack_power
    
you = Fighter('You',100,60,20) #Player 
troll = Fighter('Troll', 200,30,10) #Enemy

you_health = you.get_health() #Get health for the characters
troll_health = troll.get_health()

print('You: Health:',you_health) 
print('Troll: Health:',troll_health)

while troll_health > 0 and you_health > 0: #Checks if either one has died yet
    print('You attacked the troll') #PLayer goes first
    troll_health -= you.random_attack() #Subtract damage from health
    if troll_health > 0: #Checks if troll is still alive
        print('The troll attacked you')
        you_health -= troll.random_attack() 
    else:
        continue #Continues next loop which wil automatically end since troll is dead
    print('')
    if troll_health > 0 and you_health > 0: #Only prints if both are alive to avoid printing negative health
        print('You: Health:', you_health)
        print('Troll: Health:', troll_health)

print('')
if troll_health <= 0: #Prints who won and how much health they both have remaining
    print('You: Health:',you_health)
    print('Troll: Health: 0')
    print('The troll has been defeated')
else:
    print('You: Health: 0')
    print('Troll: Health:',troll_health)
    print('You have lost')
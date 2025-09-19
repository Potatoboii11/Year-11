import random, time 

class Fighter:
    def __init__(self,name, starting_health, weapon, shield):
        self.name = name
        self.__health = starting_health #Private attribute
        self.weapon = weapon
        self.shield = shield

    def report(self):
        print(self.name+':'+ ' Health: '+ str(self.__health))

    def is_dead(self):
        if self.__health <= 0:
            return True
        else:
            return False

    def random_attack(self):
        attack_power = random.randint(int(self.weapon/2), int(self.weapon*2)) #int because sometimes it is float, and randint only takes integers
        print('Attack power:', attack_power)
        return attack_power

    def defend(self,attack_power):
        damage = attack_power - self.shield
        if damage >  0:
            self.__health -= damage
            print('Damage:', damage)
        else:
            print('No damage')



you = Fighter('You',100,60,20)
troll = Fighter('Troll',200,30,10)

while troll.is_dead() == False and you.is_dead() == False: #Checks if either one has died yet
    time.sleep(1) #Delay for 1 second before conutinuing
    print('')
    print('You attacked the troll') #PLayer goes first
    troll.defend(you.random_attack()) #Subtract damage from health
    print('')
    if troll.is_dead() == False: #Checks if troll is still alive
        print('The troll attacked you')
        you.defend(troll.random_attack()) #Troll attacks player if still alive
    else:
        continue #Continues next loop which wil automatically end since troll is dead
    you.report()
    troll.report()

print('')
you.report()
troll.report()
if troll.is_dead() == True: #Prints who won and how much health they both have remaining
    print('The troll has been defeated')
else:
    print('You have lost')
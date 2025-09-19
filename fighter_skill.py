import random, time 

class Fighter:
    def __init__(self,name, starting_health, weapon, shield):
        self.name = name
        self.__health = starting_health
        self.weapon = weapon
        self.shield = shield
  
    def report(self):
        print(self.name+':'+ ' Health: '+ str(round(self.__health, 1))) #Rounds when printing to make it easier to read

    def is_dead(self):
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


you = Fighter('You',100,60,20)
troll = Fighter('Troll',300,30,10)

you.report()
troll.report()

while troll.is_dead() == False and you.is_dead() == False: #Checks if either one has died yet
    time.sleep(1) #Delay for 1 second before conutinuing
    print('')
    troll.defend(you.skill_attack()) #Subtract damage from health
    print('You attacked the troll') #PLayer goes first
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
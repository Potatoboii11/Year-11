import random #Too get random number
max = 1000 #Max value in range
min = 0 #Min value in range
num = random.randint(min,max) #Random number
guesses = 0 #Guess counter
while guesses < 10: #Keeps going until turns up. It is <10 since counter goes up after while loop, meaning on the tenth turn, guess counter will me 9
    guess = int(input(f"Guess a number from {min}-{max}: ")) #Ask for a guess
    if min < guess <= max: #Makes sure guess is in between range
        guesses += 1 #Add a guess
        print('Guess:',guesses) 
        if guess == num: #Checks if guess was correct, too high or too low
            print('Congradulations you have won!!!, in',guesses,'guesses')
        elif guess > num:
            print('Lower')
        else:
            print('Higher')
    else:
        print('Not in the range, try again')
if guess != num: 
    print("You lost, you didn't guess it in 10 tries")
print("The number was",num)
import random #Too get random number
max = 1000 #Max value in range
min = 0 #Min value in range
num = random.randint(min,max) #Random number
guesses = 0
while guesses < 10:
    guess = int(input("Guess a number from 1-1000: "))
    if min < guess <= max:
        guesses += 1
        print('Guess:',guesses)
        if guess == num:
            print('Congradulations you have won!!!, in',guesses,'guesses')
        elif guess > num:
            print('Lower')
        else:
            print('Higher')
    else:
        print('Not in the range, try again')
if guesses == 11:
    print("You lost, you didn't guess it in 10 tries")
print("The number was",num)
#Number guessing game
import random #import random module to generate random numbers
secretNumber = random.randint(1,10) #random number between 1 to 10
print("Welcome to Number Guessing Game!")

guess=0
while guess != secretNumber: #loop until guess is equal to secretNumber
    guess = int(input("Enter your guess (1 to 10): ")) #take input from user and convert to integer
    if guess < secretNumber: #if guess is less than secretNumber    
        print("Too low! Try again.")
    elif guess > secretNumber: #if guess is greater than secretNumber   
        print("Too high! Try again.")
    else: #if guess is equal to secretNumber    
        print("Congratulations! You guessed it right.")
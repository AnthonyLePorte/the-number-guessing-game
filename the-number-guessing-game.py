import random

def start_game():
    print("Welcome to The Number Guessing Game!")
    number = random.randint(1, 10)
    high_score = 10
    attempts = 0
    print("The highscore is {} attempts.".format(high_score))
    while attempts <= 100:
        try:
            guess = int(input("Please guess a number from 1-10:  "))
            if guess == number:
                print("You got it! Congratulations you have won!")
                attempts += 1
                if attempts < high_score:
                    high_score = attempts 
                print("It took you {} attempt(s). Game over.".format(attempts))
                print("The highscore is {} attempts.".format(high_score))
                attempts = 0
                answer = (input("Would you like to play again? (yes/no):  ")).lower()
                if answer == "yes":
                    continue
                elif answer == "no":
                    print("Thanks for playing, goodbye!")
                    break
                else: 
                    print("Sorry but that is not a valid choice. Restarting game.")
                    start_game()
            elif guess > int(10):
                print("Your guess was outside of the guessing range. Try again.")
            elif guess < int(1):
                print("Your guess was outside of the guessing range. Try again.")
            elif guess < number:
                print("Your guess was too low. Try again.")
                attempts += 1
                print("You are at {} attempt(s)".format(attempts))
            elif guess > number:
                print("Your guess was too high. Try again.")
                attempts += 1
                print("You are at {} attempt(s)".format(attempts))
        except ValueError:
            print("Sorry but that is not a valid choice. Try again.")        
start_game()
        

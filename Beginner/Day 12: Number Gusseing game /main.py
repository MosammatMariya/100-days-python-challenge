import random
import logo

EASY_LIVES = 10
HARD_LIVES = 5



def difficulty():
    level = input("Choose a difficulty level. Type 'easy' or 'hard': ").lower()
    if level == 'easy':
        print("You have 10 atttempts remain to guess the number.")
        return EASY_LIVES

    else:
        print(" You have 5 atttempts remain to guess the number.")
        return HARD_LIVES

def compare(guess,n,turns):
    while guess != n:
        if guess < n:
            print("Your guess is too low")
            return turns-1
        elif guess > n:
            print("Your guess is too high")
            return turns-1
        else :
            print("You guessed it")


def play():
    print(logo.logo)
    print("Welcome to Number Guessing Game")
    print("I am thinking of a number between 1 and 100")

    n = random.randint(1, 100)
    turns = difficulty()
    guess = int(input("Enter a guess: "))

    guess = 0
    while guess != n:
        print(f"You have {turns} turns left.")
        guess = int(input("Make a guess : "))
        turns = compare(guess,n,turns)
        if turns == 0:
            print("You have no turns left.")
            print(f"The guessed number is {n}")
            return
        elif guess != n:
            print("Guess again!")



play()

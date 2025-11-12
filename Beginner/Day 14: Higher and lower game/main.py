import random
from art import logo,vs
from random_data import data

def random_data():
    return random.choice(data)


def place(account):
    name = account['name']
    description = account['description']
    country = account['country']
    return f'{name},a {description} from {country}'

def compare(guess,account1, account2):
    if account1 > account2:
        return guess == "a"
    else:
        return guess == "b"

def play():
    print(logo)
    score=0
    game_continue=True
    account_1 = random_data()
    account_2 = random_data()

    while  game_continue:
      account_1 = account_2
      account_2 = random_data()

      while account_1 == account_2:
          account_2 = random_data()

      print(f"Compare A: {place(account_1)}.")
      print(vs)
      print(f"Against B: {place(account_2)}.")

      guess = input("'A' or 'B'. Guess who has more follower: ").lower()
      account1_follower= account_1['follower_count']
      account2_follower= account_2['follower_count']
      find_correct = compare(guess, account1_follower, account2_follower)

      print(logo)
      if find_correct:
        score+=1
        print(f"You got it! You got {score} points.")
      else:
        game_continue=False
        print(f"Sorry, that's wrong.Your score is {score}.")


play()

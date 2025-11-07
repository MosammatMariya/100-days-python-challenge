import random
import logo

print(logo.logo)

def deal():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):

    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

#
def compare(your_score, computer_score):
    if your_score > 21 and computer_score > 21:
        return "More than 21. You lose"
    if your_score == computer_score:
        return "Draw "
    elif computer_score == 0:
        return "Lose, opponent has  won"
    elif your_score == 0:
        return "Win "
    elif your_score > 21:
        return "More than 21. You lose "
    elif computer_score > 21:
        return "Opponent went over 21. You win "
    elif your_score > computer_score:
        return "You win "
    else:
        return "You lose "

def play():
    your_cards = []
    computer_cards = []
    game_over = False

    for char in range(2):
        your_cards.append(deal())
        computer_cards.append(deal())

    while not game_over:
        your_score = calculate_score(your_cards)
        computer_score = calculate_score(computer_cards)
        print(f"     Your cards: {your_cards}, current score: {your_score}")
        print(f"     Computer's first card: {computer_cards[0]}")

        if your_score == 0 or computer_score == 0 or your_score > 21:
            game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                your_cards.append(deal())
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {your_cards}, final score: {your_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(your_score, computer_score))

game = input("Do you want to play a game of Blackjack? Type 'y' for Yes or 'n' for No: ") 
if game == "y":
    play()
